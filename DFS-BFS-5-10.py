'''

<이것이 취업을 위한 코딩 테스트다 with 파이썬>

DFS/BFS - 음료수 얼려 먹기 (149p)

'''

'''

[문제]

N X M 크기의 얼음 틀이 주어진다.
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결된 것으로 간주한다.
이때 만들어지는 총 아이스크림의 개수를 구해보자.

'''

'''

[아이디어]

DFS를 이용한다.
각 노드의 방문 여부를 나타내는 visited는 따로 두지 않고, 좌표의 원소가 0인 경우 1로 변경하는 것으로 대신한다.

'''

'''

[디버그]

Real time: 0.141 s
User time: 0.038 s
Sys. time: 0.036 s
CPU share: 52.88 %
Exit code: 0

'''

from sys import stdin

def dfs(x, y) :
    if x <= -1 or x >= N or y <= -1 or y >= M : ### 얼음 틀을 벗어나는 경우
        return False
    
    if graph[x][y] == 0 : ### 방문하지 않은 경우, 구멍이 뚫려 있는 부분
        graph[x][y] = 1 ### 방문 표시
        
        ### 상, 하, 좌, 우 재귀 호출
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
        
for i in range (N) :
    for j in range (M) :
        if (dfs(i, j) == True) : ### 각 묶음에 대하여 가장 인덱스가 빠른 원소만 True가 되면서 총 개수를 구할 수 있음
            totalNum += 1
            
print(totalNum)
