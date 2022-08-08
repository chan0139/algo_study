from collections import deque

#list (my)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = []
        for i in s:
            if i.isalnum():
                sentence.append(i.lower())
        print(sentence)
        if len(sentence) == 0:
            return True
        for i in range(len(sentence)//2+1):
            print(sentence[i], sentence[-(i+1)])
            if sentence[i] != sentence[-(i+1)]:
                return False
        return True

#deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        queue = deque()

        for char in s:
            if char.isalnum():
                queue.append(char.lower())

        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False
        return True
#slicing
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '',s)

        return s == s[::-1]
