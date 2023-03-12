'''

<이것이 취업을 위한 코딩 테스트다 with 파이썬>

구현 - 왕실의 나이트 (115p)

'''

'''

[문제]

8 X 8 좌표 평면이 있다.
행은 1부터 8까지로 표현하고, 열은 a부터 h까지로 표현한다. (가장 왼쪽 위는 a1, 가장 오른쪽 아래는 h8)
좌표 평면상에서 나이트의 위치가 주어질 때, 다음 두 이동을 통해 나이트가 도달할 수 있는 좌표의 개수를 출력하자.

이동 1) 수평으로 두 칸 이동한 후 수직으로 한 칸 이동
이동 2) 수직으로 두 칸 이동한 후 수평으로 한 칸 이동

단, 나이트는 좌표 평면을 벗어날 수 없다.

'''

'''

[아이디어]

방향 벡터를 설정한 뒤, 하나씩 꺼내 시작 좌표에 더해서 좌표 평면을 벗어나는지 확인한다.

'''

'''

[디버그]

Real time: 0.144 s
User time: 0.037 s
Sys. time: 0.032 s
CPU share: 48.41 %
Exit code: 0

'''

from sys import stdin

### 경우의 수
count = 0

### 방향 벡터
rowVector = [1, -1, 1, -1, 2, 2, -2, -2]
colVector = [2, 2, -2, -2, 1, -1, 1, -1]

currentCol, currentRow = map(str, list(stdin.readline().strip()))

currentCol = ord(currentCol) ### 이동이 용이하도록 아스키 코드로 변환
currentRow = int(currentRow)

for row, col in zip(rowVector, colVector) :
    
    nextRow = currentRow + row
    nextCol = currentCol + col
    
    if 1 <= nextRow and nextRow <= 8 and ord('a') <= nextCol and nextCol <= ord('h') : ### 좌표 평면을 벗어나지 않음
        count += 1
        
print(count)
