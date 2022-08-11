class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        hap = 0
        for i in range(0, len(nums), 2):
            hap += min(nums[i], nums[i + 1])

        return hap
