import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        letters = re.sub(r'[^\w]', ' ', paragraph).lower()
        temp = letters.split()
        print(temp)

        result = []
        for i in temp:
            if i not in banned:
                result.append(i)
        count = Counter(result)
        answer = ''.join(count.most_common()[0][0])
        return answer