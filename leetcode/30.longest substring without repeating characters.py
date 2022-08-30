class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        result = []
        for i in s:
            if i not in stack:
                stack.append(i)
            else:
                result.append(len(stack))
                pos = stack.index(i)
                stack = stack[pos + 1:]
                stack.append(i)
        result.append(len(stack))

        return max(result)