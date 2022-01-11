n = int(input())

users = []

for i in range(n):
    a, b = input().split()
    a = int(a)
    users.append((a,b))

users = sorted(users, key=lambda x:x[0])
for member in users:
    print(member[0], member[1])