class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2):
            for number in nums:
                ans.append(number) 
        return ans