n, c = map(int, input().split())
pos = []
for i in range(n):
    pos.append(int(input()))

pos.sort()
left = 1
right = pos[-1] - pos[0]
answer = 0
#mid -> 집 마다 거리 변수, count -> c만큼 설치가능한지 갯수 세는 변수
while left <= right:
    mid = (left+right) // 2
    count = 1
    cur = pos[0]
    for i in pos:
        if cur + mid <= i:
            count += 1
            cur = i
    if count >= c:
        left = mid + 1
        answer = mid
    if count < c:
        right = mid -1

print(answer)