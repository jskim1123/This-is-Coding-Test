'''

<이것이 취업을 위한 코딩 테스트다 with 파이썬>

그리디 알고리즘 - 큰 수의 법칙 (92p)

'''

'''

[문제]

첫째 줄에 N, M, K가 주어진다. 
N개의 자연수가 있을 때, 한 인덱스의 숫자를 최대 K번까지 포함해 M번을 더하여 가장 큰 수를 만든다.
이때, 동일한 숫자라도 인덱스가 다를 경우 다른 숫자로 간주한다.

'''

'''

[아이디어]

가장 큰 수가 K번, 그 다음으로 큰 수가 1번 등장하는 수열 S가 반복된다.
S의 길이는 K + 1이므로, M을 K + 1으로 나눈 몫에 K를 곱하면 가장 큰 수의 개수를 알 수 있다.
이때, M이 K + 1으로 나누어 떨어지지 않는 경우를 고려해 M % (K + 1)을 더한다.

'''

import sys

firstPlusNum = 0 ### 가장 큰 수의 개수
sum = 0 ### 수의 합

N, M, K = map(int, sys.stdin.readline().strip().split(" "))
numList = list(map(int, sys.stdin.readline().strip().split(" ")))

firstNum = max(numList) ### 가장 큰 수
numList.remove(firstNum)
secondNum = max(numList) ### 두번째로 큰 수

firstPlusNum = (M // (K + 1)) * K + (M % (K + 1)) ### 가장 큰 수의 개수 구하기
sum = firstPlusNum * firstNum + (M - firstPlusNum) * secondNum

print(sum)