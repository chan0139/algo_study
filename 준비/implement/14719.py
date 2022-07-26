h,w = map(int, input().split())
block = list(map(int, input().split()))

rain = 0
for i in range(1,len(block)-1):
    left = max(block[:i])
    right = max(block[i+1:])
    if left <= block[i] or right <= block[i]:
        continue
    if left <= right:
        rain += left - block[i]
    if left > right:
        rain += right - block[i]

print(rain)

