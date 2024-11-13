## 29.3 연습문제
"""
몫과 나머지를 구하는 함수 만들기

다음 소스 코드를 완성하여 x를 y로 나누었을 때의 몫과 나머지를 출력되게 만드세요.

x = 10
y = 3

____________________
____________________

quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))

- 실행 결과 -
몫 : 3, 나머지 : 1
"""

def remainder(a, b) : 
    c = a % b
    return c

def quotient(a, b) :
    c = a // b                              # 몫을 정수로 계산
    d = remainder(a, b)
    print(f'몫 : {c}, 나머지 : {d}')        # 한 줄로 출력

x = 10
y = 3

quotient(x,y)
