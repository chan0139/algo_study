class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0]*len(temperatures)
        stack = []
        for index,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i, t = stack.pop()
                days[i] = index - i
            stack.append((index, temp))
        return days