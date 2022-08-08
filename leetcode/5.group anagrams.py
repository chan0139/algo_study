
#dictionary 이용 -> 같은 key -> list 형태로 추가해서 묶기
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for i in strs:
            temp = ''.join(sorted(i))
            if temp not in result:
                result[temp] = [i]
            else:
                result[temp].append(i)

        return list(result.values())
