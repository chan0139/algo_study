import sys

n = int(sys.stdin.readline())
words = []
for i in range(n):
    temp = input()
    if temp not in words:
        words.append(temp)

words = sorted(words, key=lambda x:(len(x),x))

for i in words:
    print(i)