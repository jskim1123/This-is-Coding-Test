'''

<이것이 취업을 위한 코딩 테스트다 with 파이썬>

구현 - 상하좌우 (110p)

'''

'''

[문제]

여행가 A는 1 x 1 크기의 정사각형 공간들로 이루어진 N x N 공간 위에 서있다.
가장 왼쪽 위 공간의 좌표를 (1, 1), 가장 오른쪽 아래 공간의 좌표를 (N, N)이라고 하자.
(1, 1)에서 시작해서 상(U), 하(D), 좌(L), 우(R) 방향으로 이동할 수 있다.
N x N 공간을 벗어나는 움직임을 무시할 때, 상하좌우 명령을 모두 마친 후 A가 서있는 최종 좌표를 구해보자.

'''

'''

[아이디어]

공간을 벗어나는 경우는 continue로 넘기자.

'''

from sys import stdin
from collections import deque

### 시작 좌표는 (1, 1)
currentRow = 1
currentCol = 1

### 상하좌우 순서의 방향 벡터
rowVector = [-1, 1, 0, 0]
colVector = [0, 0, -1, 1]

N = int(stdin.readline()) ### 공간의 크기를 나타내는 N 입력
directionDeque = deque(stdin.readline().strip().split(" ")) ### 여행가 A가 이동할 방향 명령어를 저장하는 덱

for direction in directionDeque :

    if direction == "U" and currentRow > 1 :
        idx = 0
    elif direction == "D" and currentRow < N :
        idx = 1
    elif direction == "L" and currentCol > 1 :
        idx = 2
    elif direction == "R" and currentCol < N :
        idx = 3
    else :
        continue
    
    currentRow += rowVector[idx]
    currentCol += colVector[idx]

print(currentRow, currentCol)

