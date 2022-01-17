import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, e = map(int, input().split())

sum = 0
graph =[[] for _ in range(n+1)]


for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v_1, v_2 = map(int, input().split())

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

first = dijkstra(1)
second = dijkstra(v_1)
third = dijkstra(v_2)
sum = min(first[v_1] + second[v_2] + third[n], first[v_2] + third[v_1] + second[n])

if sum >= INF:
    print(-1)
else:
    print(sum)



