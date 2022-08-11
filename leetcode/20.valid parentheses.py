class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(', '{', '[']
        for i in s:
            if i in opens:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()

                if ord(temp) < 50 and ord(temp) != ord(i)-1:
                    return False
                if ord(temp) > 50 and ord(temp) != ord(i)-2:
                    return False
        if len(stack) != 0:
            return False

        return True

