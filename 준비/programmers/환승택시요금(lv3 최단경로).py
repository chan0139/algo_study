def solution(n, s, a, b, fares):
    print(n)
    INF = int(1e9)
    dist = [[INF]*(n+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        dist[i][i] = 0
        
    for fare in fares:
        src, end, fee = fare[0], fare[1], fare[2]
        if dist[src][end] > fee:
            dist[src][end] = fee
        if dist[end][src] > fee:
            dist[end][src] = fee
#     print(dist)
#     print('---------------------------------')
    answer = dist[s][a] + dist[s][b] #각자 갈 경우 비용
#     print(answer)
    
    #플로이드 와샬
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
#     s = 4
#     a = 6
#     b = 2

    for k in range(1, n+1): # k까지 같이 타고감
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])
        
    
    return answer