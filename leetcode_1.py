class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preNum = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in preNum:
                return [preNum[diff], i]
            preNum[n] = i

        return
