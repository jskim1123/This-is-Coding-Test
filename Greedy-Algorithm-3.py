'''

<이것이 취업을 위한 코딩 테스트다 with 파이썬>

그리디 알고리즘 - 숫자 카드 게임 (96p)

'''

'''

[문제]

숫자가 쓰인 카드들이 N x M 형태로 놓여 있다.
하나의 행을 선택해 숫자가 가장 작은 카드를 뽑는다는 룰을 적용했을 때,
뽑을 수 있는 가장 큰 숫자의 카드를 출력하라.

'''

'''

[아이디어]

각 행의 최솟값 중에서 최댓값을 구한다.

'''

import sys

minCardList = [] ### 카드의 각 행에서 숫자가 가장 작은 카드들의 리스트

N, M = map(int, sys.stdin.readline().strip().split(" ")) ### N은 행, M은 열

for _ in range (N) : ### 카드의 행을 입력받으며 각 행의 최솟값을 minCardList에 추가
    minCardList.append(min(list(map(int, sys.stdin.readline().strip().split(" ")))))

print(max(minCardList)) ### minCardList의 최댓값 출력

