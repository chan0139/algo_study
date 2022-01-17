import heapq

INF = int(1e9)

n,m = map(int, input().split())

start_node = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c  = map(int,input().split()) # a에서 b로 가능 비용 = c
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, temp = heapq.heappop(q)

        if distance[temp] < dist:
            continue
        for i in graph[temp]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start_node)

for i in range(1, n+1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])