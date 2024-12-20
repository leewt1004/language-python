## 20.4 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기
"""
논리 연산자 and를 사용하지 않고 3과 5의 공배수를 검사하려면 어떻게 해야 할 까요? 
3 * 5 = 15는 3과 5의 최소공배수이므로 15로 나눴을 때 나머지가 0인 값들은 3과 5의 공배수입니다.
"""
for i in range(1, 101):      # 1부터 100까지 100번 반복
    if i % 15 == 0:          # 15의 배수(3과 5의 공배수)일 때
        print('FizzBuzz')    # FizzBuzz 출력
    elif i % 3 == 0:         # 3의 배수일 때
        print('Fizz')        # Fizz 출력
    elif i % 5 == 0:         # 5의 배수일 때
        print('Buzz')        # Buzz 출력
    else:
        print(i)             # 아무것도 해당되지 않을 때 숫자 출력

""" 실무에서는 if i % 15 == 0: 보다는 i % 3 == 0 and i % 5 == 0처럼 의미를 명확하게 드러내는 것이 좋습니다. """
