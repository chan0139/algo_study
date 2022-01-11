
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
A.sort()

def bisect(array, target, start, end):

    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return False

for i in B:
    if bisect(A, i, 0, len(A)-1):
        print(1)
    else:
        print(0)
