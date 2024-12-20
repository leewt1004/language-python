## 10.2 튜플 사용하기
"""
튜플은 리스트처럼 요소를 일렬로 저장하지만, 안에 저장된 요소를 변경, 추가, 삭제를 할 수 없습니다. 
간단하게 읽기 전용 리스트라고 할 수 있습니다.
변수에 값을 저장할 때 ( )(괄호)로 묶어주면 튜플이 되며 각 값은 ,(콤마)로 구분해줍니다. 
또는, 괄호로 묶지 않고 값만 콤마로 구분해도 튜플이 됩니다.
튜플 = (값, 값, 값)
튜플 = 값, 값, 값
"""
a = (38, 21, 53, 62, 19)
a
a = 38, 21, 53, 62, 19
a

"""
튜플도 리스트처럼 여러 자료형을 섞어서 저장해도 됩니다.
"""
person = ('james', 17, 175.3, True)
person

"""
그런데 저장된 요소를 변경, 추가, 삭제할 수도 없는 튜플을 왜 만들어 놓았을까요? 이유는 간단합니다. 
파이썬 프로그래밍에서 튜플을 사용하는 쪽이 더 유리한 경우도 있기 때문입니다. 보통 튜플은 요소가 절대 변경되지 않고 유지되어야 할 때 사용합니다.
튜플을 만든 상태에서 요소를 변경하게 되면 에러가 발생하게 됩니다. 따라서 요소를 실수로 변경하는 상황을 방지할 수 있습니다.
반면 요소를 자주 변경해야 할 때는 리스트를 사용합니다. 
보통 실무에서는 요소를 변경하는 경우가 많기 때문에 튜플보다 리스트를 더 자주 사용하는 편입니다.
"""

### 10.2.1 요소가 한 개 들어있는 튜플 만들기
"""
요소가 한 개인 튜플을 만들 때는 ( )(괄호) 안에 값 한 개를 넣고 ,(콤마)를 붙입니다. 
또는, 괄호로 묶지 않고 값 한 개에 ,를 붙여도 됩니다.
튜플 = (값, )
튜플 = 값,
튜플은 요소를 변경, 추가, 삭제할 수도 없는데 값 한 개짜리 튜플은 왜 필요할까요? 
함수(클래스)를 사용하다 보면 값이 아닌 튜플을 넣어야 할 경우가 생깁니다. 
이때 값은 한 개지만 튜플을 넣어야 할 때 (값, )과 같은 형식을 사용해야 합니다. 
실무에서는 가끔 이 문법을 사용하게 되는데, 그냥 튜플 형태를 유지하기 위한 문법이라고 생각하면 됩니다.
"""
(38, )
38,

### 10.2.2  range를 사용하여 튜플 만들기
"""
tuple 안에 range를 넣으면 튜플이 생성됩니다.
튜플 = tuple(range(횟수))
"""
a = tuple(range(10))
a

"""
range에 시작하는 숫자와 끝나는 숫자를 지정해서 튜플을 만들 수도 있습니다.
튜플 = tuple(range(시작, 끝))
"""
b = tuple(range(5, 12))
b

"""
range에 증가폭을 지정하는 방법도 가능합니다.
튜플 = tuple(range(시작, 끝, 증가폭))
"""
c = tuple(range(-4, 10, 2))
c

### 10.2.3  튜플을 리스트로 만들고 리스트를 튜플로 만들기
"""
튜플과 리스트는 요소를 변경, 추가, 삭제할 수 있는지 없는지만 다를 뿐 기능과 형태는 같습니다. 
따라서 튜플을 리스트로 만들거나 리스트를 튜플로 만들 수도 있습니다.
"""
a = [1, 2, 3]
tuple(a) # tuple 안에 리스트를 넣으면 새 튜플이 생깁니다. / 결과값 : (1, 2, 3)

b = (4, 5, 6)
list(b) # list 안에 튜플을 넣으면 새 리스트가 생성됩니다. / 결과값 : [4, 5, 6]

"""
리스트를 생성할 때는 [ ](대괄호)를 사용하고, 튜플을 생성할 때는 ( )(괄호)를 사용한다는 점이 중요합니다. 
특히, 튜플은 안에 저장된 요소를 변경, 추가, 삭제할 수 없으므로 요소가 그대로 유지되어야 할 때 사용한다는 점도 기억해두세요.
"""

#### 참고 : list와 tuple 안에 문자열을 넣으면?
"""
문자 리스트, 문자 튜플이 생성됩니다.
"""
list('Hello') # 결과값 : ['H', 'e', 'l', 'l', 'o']
tuple('Hello') # 결과값 : ('H', 'e', 'l', 'l', 'o')

#### 참고 :  리스트와 튜플로 변수 만들기
"""
리스트와 튜플을 사용하면 변수 여러 개를 한 번에 만들 수 있습니다. 
이때 변수의 개수와 리스트(튜플)의 요소 개수는 같아야 합니다.
"""
a, b, c = [1, 2, 3]
print(a, b, c)
d, e, f = (4, 5, 6)
print(d, e, f)

"""
리스트와 튜플 변수로도 변수 여러 개를 만들 수 있습니다. 
리스트와 튜플의 요소를 변수 여러 개에 할당하는 것을 리스트 언패킹(list unpacking), 튜플 언패킹(tuple unpacking)이라고 합니다.
"""
x = [1, 2, 3]
a, b, c = x
print(a, b, c)
y = (4, 5, 6)
d, e, f = y
print(d, e, f)

"""
input().split()은 리스트를 반환합니다. 그래서 리스트 언패킹 형식으로 입력 값을 변수 여러 개에 저장할 수 있었습니다.
input().split()은 사용자가 입력한 문자열을 공백을 기준으로 나누어 리스트(list) 형태로 반환하는 기능입니다. 
input()은 입력을 문자열로 받으며, 그 문자열에 split()을 적용하면 공백을 기준으로 분리된 값들이 리스트로 저장됩니다. 
이 리스트의 각 요소는 기본적으로 문자열입니다.
"""
input().split()
# 입력값 : 10 20
['10', '20']

x = input().split()
# 입력값 : 10 20
a, b = x         # a, b = input().split()과 같음
print(a, b)
# 결과값 : 10 20

"""
리스트 패킹(list packing)과 튜플 패킹(tuple packing)은 변수에 리스트 또는 튜플을 할당하는 과정을 뜻합니다.
"""
a = [1, 2, 3]    # 리스트 패킹
b = (1, 2, 3)    # 튜플 패킹
c = 1, 2, 3      # 튜플 패킹
