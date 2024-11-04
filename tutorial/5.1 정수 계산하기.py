# Unit 5. 숫자 계산하기
""" note
숫자 = 정수(int), 실수(float),  복소수(xomplex)
"""

## 5.1 정수 계산하기

### 5.11 사칙연산
1 + 1
1 - 2
2 * 2
5 / 2
4 / 2 # 4/2 = 2.0 이렇게 파이썬 3은 나눗셈이 완전히 나누어 떨어져도 실수가 나옵니다

### 5.12 나눗셈 후 소수점 이하를 버리는 // 연산자
"""
//은 버림 나눗셈(floor division)이라고 부르며 나눗셈의 결과에서 소수점 이하는 버립니다.
"""
5 // 2 # 5 // 2 = 2.0
4 // 2.0 # 4 // 2.0 = 2

### 5.1.3 나눗셈 후 나머지를 구하는 % 연산자
5 % 2

### 5.1.4 거듭제곱을 구하는 ** 연산자
2 ** 10

### 5.1.5 값을 정수로 만들기
int(3.3)
int(5 / 2)
int('10')

### 5.1.6 객체의 자료형 알아내기
type(10)

#### 참고 : 몫과 나머지를 함께 구하기
divmod(5, 2)
"""
파이썬에서 값을 괄호로 묶은 형태를 튜플(tuple)이라고 하며 값 여러 개를 모아서 표현할 때 사용합니다. 튜플은 'Unit 10 리스트와 튜플 사용하기'에서 자세히 설명하겠습니다.

튜플은 변수 여러 개에 저장할 수 있는데 divmod의 결과가 튜플로 나오므로 몫과 나머지는 변수 두 개에 저장할 수 있습니다.
"""
quotient, remainder = divmod(5, 2)
print(quotient, remainder)
