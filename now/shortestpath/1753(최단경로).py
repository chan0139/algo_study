
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
v,e = map(int, input().split())

start = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))


dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])