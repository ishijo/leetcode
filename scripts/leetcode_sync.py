"""
Fetch LeetCode submission history and create backdated Git commits,
one per (problem, language) pair, dated at the first accepted submission.
"""

import os
import subprocess
import sys
import time
from pathlib import Path

import requests

SESSION = os.environ["LEETCODE_SESSION"]
CSRF = os.environ["LEETCODE_CSRF"]
FULL_IMPORT = os.environ.get("FULL_IMPORT", "false").lower() == "true"
GIT_NAME = os.environ["GIT_USER_NAME"]
GIT_EMAIL = os.environ["GIT_USER_EMAIL"]

BASE = "https://leetcode.com"
SUBMISSIONS_URL = f"{BASE}/api/submissions/"
PAGE_SIZE = 20
SLEEP_BETWEEN_PAGES = 1.2  # be polite to LeetCode

# LeetCode language slug -> file extension
LANG_EXT = {
    "python": "py", "python3": "py",
    "c": "c", "cpp": "cpp",
    "java": "java",
    "javascript": "js", "typescript": "ts",
    "csharp": "cs",
    "ruby": "rb",
    "swift": "swift",
    "golang": "go",
    "rust": "rs",
    "kotlin": "kt",
    "scala": "scala",
    "php": "php",
    "mysql": "sql", "mssql": "sql", "oraclesql": "sql",
    "bash": "sh",
    "dart": "dart",
    "elixir": "ex",
    "erlang": "erl",
    "racket": "rkt",
}


def make_session() -> requests.Session:
    s = requests.Session()
    s.cookies.set("LEETCODE_SESSION", SESSION, domain=".leetcode.com")
    s.cookies.set("csrftoken", CSRF, domain=".leetcode.com")
    s.headers.update({
        "Referer": "https://leetcode.com/",
        "x-csrftoken": CSRF,
        "User-Agent": "leetcode-sync/1.0 (+github-actions)",
    })
    return s


def fetch_all_submissions(session: requests.Session) -> list[dict]:
    """Paginate through /api/submissions/ until has_next is false."""
    out, offset = [], 0
    while True:
        r = session.get(
            SUBMISSIONS_URL,
            params={"offset": offset, "limit": PAGE_SIZE},
            timeout=30,
        )
        if r.status_code != 200 or "submissions_dump" not in r.text:
            print(f"::error::LeetCode returned status={r.status_code}. "
                  f"Your LEETCODE_SESSION cookie is probably expired.")
            print(r.text[:500])
            sys.exit(1)

        data = r.json()
        page = data.get("submissions_dump", [])
        if not page:
            break

        out.extend(page)
        print(f"  fetched {len(out)} so far (offset={offset})")

        if not data.get("has_next"):
            break
        offset += PAGE_SIZE
        time.sleep(SLEEP_BETWEEN_PAGES)
    return out


def first_accepted_by_problem_lang(subs: list[dict]) -> list[dict]:
    """Keep only the earliest accepted submission for each (slug, lang)."""
    best: dict[tuple[str, str], dict] = {}
    for s in subs:
        if s.get("status_display") != "Accepted":
            continue
        key = (s["title_slug"], s["lang"])
        if key not in best or s["timestamp"] < best[key]["timestamp"]:
            best[key] = s
    # oldest first, so git log reads chronologically
    return sorted(best.values(), key=lambda s: s["timestamp"])


def run(cmd: list[str], env: dict | None = None, check: bool = True):
    return subprocess.run(cmd, env=env, check=check,
                          capture_output=True, text=True)


def commit_submission(sub: dict) -> bool:
    """Write files and make a backdated commit. Returns True if a commit was made."""
    slug = sub["title_slug"]
    lang = sub["lang"]
    ext = LANG_EXT.get(lang, "txt")

    folder = Path("solutions") / slug
    folder.mkdir(parents=True, exist_ok=True)
    solution_path = folder / f"solution.{ext}"

    # Skip if we've already committed this exact code (idempotent re-runs)
    if solution_path.exists():
        if solution_path.read_text().strip() == sub["code"].strip():
            return False

    solution_path.write_text(sub["code"])

    readme = folder / "README.md"
    if not readme.exists():
        readme.write_text(
            f"# {sub['title']}\n\n"
            f"LeetCode: https://leetcode.com/problems/{slug}/\n"
        )

    # Format the timestamp as an ISO-8601 string in UTC
    ts = int(sub["timestamp"])
    iso = time.strftime("%Y-%m-%dT%H:%M:%S+0000", time.gmtime(ts))

    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = iso
    env["GIT_COMMITTER_DATE"] = iso
    env["GIT_AUTHOR_NAME"] = GIT_NAME
    env["GIT_AUTHOR_EMAIL"] = GIT_EMAIL
    env["GIT_COMMITTER_NAME"] = GIT_NAME
    env["GIT_COMMITTER_EMAIL"] = GIT_EMAIL

    run(["git", "add", str(folder)])

    # If nothing actually changed on disk, skip the commit
    if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode == 0:
        return False

    msg = f"Solve: {sub['title']} ({lang})"
    run(["git", "commit", "-m", msg], env=env)
    return True


def main():
    print(f"Full import: {FULL_IMPORT}")
    session = make_session()

    print("Fetching submissions from LeetCode...")
    all_subs = fetch_all_submissions(session)
    print(f"Total submissions fetched: {len(all_subs)}")

    picked = first_accepted_by_problem_lang(all_subs)
    print(f"Unique first-accepted (problem, language) pairs: {len(picked)}")

    committed = 0
    for sub in picked:
        date_str = time.strftime("%Y-%m-%d", time.gmtime(int(sub["timestamp"])))
        try:
            if commit_submission(sub):
                committed += 1
                print(f"  ✓ [{date_str}] {sub['title']} ({sub['lang']})")
        except subprocess.CalledProcessError as e:
            print(f"  ✗ Failed on {sub['title']}: {e.stderr}")

    print(f"\nDone. Backdated commits created this run: {committed}")


if __name__ == "__main__":
    main()
