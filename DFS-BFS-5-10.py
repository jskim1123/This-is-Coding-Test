from sys import stdin

def dfs(x, y) :
    if x <= -1 or x >= N or y <= -1 or y >= M :
        return False
    
    if graph[x][y] == 0 :
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

totalNum = 0
graph = []

N, M = map(int, stdin.readline().strip().split(" "))

for _ in range (N) :
    graph.append(list(map(int, stdin.readline().strip())))
    
print(graph)
    
for i in range (N) :
    for j in range (M) :
        if (dfs(i, j) == True) :
            totalNum += 1
            
print(totalNum)
