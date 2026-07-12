class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        res = [float("inf")]*(amount+1)
        res[0] = 0

        for amt in range(1,amount+1):
            for c in coins:
                if amt-c>=0:
                    res[amt] = min(res[amt],1 + res[amt-c])
        if res[amount]!=float("inf"):
            return res[amount]
        return -1




































        # counts = {coin:0 for coin in coins}
        # amt = amount
        # for i in range(len(coins)-1,-1,-1):
        #     while amt >= coins[i]:
        #         amt = amt - coins[i]
        #         counts[coins[i]] += 1
        # if amt == 0:
        #     return sum(counts.values())
        # return -1


        # counts = {coin:0 for coin in coins}
        # amt = amount
        # for i in range(len(coins)-1,-1,-1):
        #     while amt >= coins[i]:
        #         amt = amt - coins[i]
        #         counts[coins[i]] += 1
        # if amt == 0:
        #     return sum(counts.values())
        # return -1
            