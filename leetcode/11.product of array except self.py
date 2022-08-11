
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        now = 1
        for i in range(len(nums)):
            left.append(now)
            now *= nums[i]
        now = 1
        for i in range(len(nums)-1, -1,-1):
            left[i] = left[i]*now
            now *= nums[i]
        return left