def solution(info, edges):
    visited = [0] * len(info)
    global max_sheep
    max_sheep = -1
    def dfs(sheep, wolf):
        global max_sheep
        
        if wolf >= sheep:
            return
        else:
            max_sheep = max(sheep, max_sheep)
        
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = 0
    visited[0] = 1
    dfs(1, 0) 
    return max_sheep