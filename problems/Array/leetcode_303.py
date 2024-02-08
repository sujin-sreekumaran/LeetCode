class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixArr = []
        current = 0
        for n in nums:
            current += n
            self.prefixArr.append(current)
        

    def sumRange(self, left: int, right: int) -> int:
        rightSide = self.prefixArr[right]
        leftSide = self.prefixArr[left - 1] if left > 0 else 0
        return rightSide - leftSide

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)