from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counter = Counter(nums)
        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]
        for i in counter:
            result.append(i[0])
        return result