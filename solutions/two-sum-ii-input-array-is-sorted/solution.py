class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small, large = 0, len(numbers)-1
        while small<large:
            curr = numbers[small] + numbers[large]
            if curr>target:
                large -= 1
            elif curr< target:
                small += 1
            if curr==target:
                return [small+1,large+1]