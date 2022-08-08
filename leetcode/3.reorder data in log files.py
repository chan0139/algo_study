class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for i in logs:
            temp = i.split(' ')
            if temp[1].isalpha():
                letters.append(i)
            else:
                digits.append(i)

        letters.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))

        result = letters + digits
        return result