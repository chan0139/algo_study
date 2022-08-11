class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minimum = int(1e9)
        for i in prices:
            minimum = min(minimum, i)
            result = max(result, i - minimum)

        return result