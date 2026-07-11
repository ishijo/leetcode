class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i:[] for i in range(numCourses)}
        for course,p_course in prerequisites:
            prereqs[course].append(p_course)
        
        def cycle(course,visit):
            if course in visit:
                return True
            visit.add(course)
            for c in prereqs[course]:
                if cycle(c,visit):
                    return True
            prereqs[course] = []
            visit.remove(course)
            return False

        visit = set()
        for course in range(numCourses):
            if cycle(course,visit):
                return False
        return True
            

'''
visit - 0 1
0: [1]
1: [0]
'''