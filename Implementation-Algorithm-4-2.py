'''

<이것이 취업을 위한 코딩 테스트다 with 파이썬>

구현 - 시각 (113p)

'''

'''

[문제]

정수 N이 입력된다.
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하라.

'''

'''

[아이디어]

1초씩 늘려가면서 시간을 문자열로 변환해 '3' in 문자열을 이용해 점검하자.

'''

'''

[디버그]

Real time: 0.135 s
User time: 0.076 s
Sys. time: 0.026 s
CPU share: 74.96 %
Exit code: 0

'''

from sys import stdin

count = 0 ### 경우의 수
hour = 0
minute = 0
second = 0

N = int(stdin.readline())

while True :
    
    if hour == N and minute == 59 and second == 59 : ### N시 59분 59초가 되면 종료
        break
    
    if second == 60 :
        minute += 1
        second = 0
    
    if minute == 60 :
        hour += 1
        minute = 0
        
    if '3' in str(hour) or '3' in str(minute) or '3' in str(second) : ### 3이 적어도 하나 포함되는 경우
        count += 1
    
    second += 1
    
print(count)
