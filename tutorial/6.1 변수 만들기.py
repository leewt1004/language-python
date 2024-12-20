# Unit 6. 변수와 입력 사용하기

## 6.1 변수 만들기
x = 10 
"""
변수이름 = 값 형식이죠. 이렇게 하면 변수가 생성되는 동시에 값이 할당(저장)됩니다.

변수 이름은 원하는 대로 지으면 되지만 다음과 같은 규칙을 지켜야 합니다.
- 영문 문자와 숫자를 사용할 수 있습니다.
- 대소문자를 구분합니다.
- 문자부터 시작해야 하며 숫자부터 시작하면 안 됩니다.
- _(밑줄 문자)로 시작할 수 있습니다.
- 특수 문자(+, -, *, /, $, @, &, % 등)는 사용할 수 없습니다.
- 파이썬의 키워드(if, for, while, and, or 등)는 사용할 수 없습니다.
"""
X = 10
y = 'Hello World'

### 6.1.1 변수의 자료형 알아내기
"""
파이썬에서는 변수의 자료형이 중요합니다. 
앞에서 type을 사용해서 10, 5.3과 같은 숫자의 자료형을 알아보았습니다. 
마찬가지로 type에 변수를 넣으면 변수(객체)의 자료형이 나옵니다.
"""
type(x)
type(y)

#### 참고 : = 기호
"""
프로그래밍 언어에서 =는 변수에 값을 할당(assignment)한다는 의미입니다. 수학의 등호와 같은 역할을 하는 연산자는 == 입니다.
"""

### 6.1.2 변수 여러 개를 한 번에 만들기
x, y, z = 10, 20, 30
# 변수 여러 개를 만들 때 값이 모두 같아도 된다면 다음과 같은 방식도 사용할 수 있습니다.
x = y = z = 10
# 두 변수의 값을 바꾸려면 어떻게 해야 할까요? 다음과 같이 변수를 할당할 때 서로 자리를 바꿔주면 됩니다. 
x, y = 10, 20
x, y = y, x

#### 참고 : 변수 삭제하기
"""
변수 삭제는 del을 사용합니다.
지금은 변수 삭제가 큰 의미가 없지만 나중에 리스트를 사용할 때 del이 유용하게 쓰입니다.
"""
x = 10
del x

#### 참고 : 빈 변수 만들기
"""
값이 들어있지 않은 빈 변수를 만들때는 None을 할당해주면 됩니다.
파이썬에서 None은 아무것도 없는 상태를 나타내는 자료형입니다.
보통 다른 언어에서는 널(null)이라고 표현합니다.
"""
x = None
print(x)
