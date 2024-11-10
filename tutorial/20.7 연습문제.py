## 20.7 연습문제
"""
2과 11의 배수, 공배수 처리하기
다음 소스 코드를 완성하여 1부터 100까지의 숫자를 출력하면서 
2의 배수일 때는 'Fizz', 11의 배수일 때는 'Buzz', 2과 11의 공배수일 때는 'FizzBuzz'가 출력되게 만드세요.

for i in range(1, 101):
    if (1)____________________ :
        print('FizzBuzz')
    elif (2)_______________ :
        print('Fizz')
    elif (2)_______________ :
        print('Buzz')
    else:
        print(i)

- 실행 결과 -
1
Fizz
3
... (생략)
FizzBuzz
89
Fizz
91
Fizz
93
Fizz
95
Fizz
97
Fizz
Buzz
Fizz
"""

""" 풀이식 1번 and 연산자 사용"""
for i in range(1, 101) :
    if i % 2 == 0 and i % 11 ==0 :
        print('FizzBuzz')
    elif i % 2 == 0 :
        print('Fizz')
    elif i % 11 == 0 :
        print('Buzz')
    else :
        print(i)

""" 풀이식 2번 논리 연산자 미사용 """
for i in range(1, 101) :
    if i % 22 == 0:
        print('FizzBuzz')
    elif i % 2 == 0 :
        print('Fizz')
    elif i % 11 == 0 :
        print('Buzz')
    else :
        print(i)

""" 풀이식 3번 코드 단축 """
for i in range(1, 101) :
    print('Fizz' * (i % 2 ==0) + 'Buzz' * (i % 11 == 0) or i)
