from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = list(jewels)
        counter = Counter(stones)

        answer = 0
        for i in jewel:
            answer += counter[i]
        return answer