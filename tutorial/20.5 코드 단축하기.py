## 20.5 코드 단축하기
""" 코드를 매우 단축하여 FizzBuzz 문제를 풀어보겠습니다. """
for i in range(1, 101) :
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i) # 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리

"""
'Fizz' * (i % 3 == 0)
문자열 곱셈을 이용하여 3의 배수일 때 'Fizz'를 출력합니다. 
i가 3의 배수이면 i % 3 == 0은 True이므로 'Fizz'가 출력되고, 3의 배수가 아니면 False이므로 'Fizz'가 출력되지 않습니다.

'Buzz' * (i % 5 == 0)
마찬가지로 'Buzz'도 문자열 곱셈을 이용하여 5의 배수일 때 출력합니다.

'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)
3과 5의 공배수일 때는 'FizzBuzz'를 출력해야 하는데 이때는 문자열 덧셈을 이용합니다.
즉, 3과 5의 공배수이면 'Fizz' * True + 'Buzz' * True가 되므로 'Fizz' + 'Buzz'로 'FizzBuzz'를 출력합니다.
만약 한 쪽이 만족하지 않으면 덧셈할 문자열이 없으므로 'Fizz'나 'Buzz'만 출력됩니다.

or i
3 또는 5의 배수가 아닐 때는 'Fizz' * False + 'Buzz' * False가 되고 결과는 빈 문자열 ''이 되는데, 이때는 or 연산자를 사용합니다. 
빈 문자열은 False로 취급하고, i는 항상 1 이상의 숫자이므로 or로 연산하면 i만 남게 되어 숫자가 그대로 출력됩니다.
"""

""" Fizz와 Buzz를 두번 씩 출력(1) """
for i in range(1, 101) :
    print('FizzFizz' * (i % 3 == 0) + 'BuzzBuzz' * (i % 5 == 0) or i)

""" Fizz와 Buzz를 두번 씩 출력(2) """
for i in range(1, 101) :
    print((('Fizz' * 2) * (i % 3 == 0)) + (('Buzz' * 2) * (i % 5 == 0)) or i)

""" 3과 5의 공배수일 때 FizzBuzzFizzBuzz 출력하기 """
for i in range(1, 101) :
    print((('FizzBuzz' * 2) * (i % 3 == 0 and i % 5 == 0)) or (('Fizz' * 2) * (i  %3 == 0)) + (('Buzz' * 2) * (i % 5 == 0)) or i)


"""
사실 FizzBuzz 문제는 프로그래밍 실력을 보는 것이 아니라 이해력을 보는 문제이기 때문입니다. 
프로그래밍 실력보다 중요한 것이 요구 사항에 대한 이해력이라는 점을 잊지 마세요.
"""
