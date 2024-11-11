# Unit 26. 세트 사용하기
""" 파이썬은 집합을 표현하는 세트(set)라는 자료형을 제공합니다. 집합을 영어로 하면 세트인데 수학에서 배우는 그 집합이 맞습니다. 따라서 세트는 합집합, 교집합, 차집합 등의 연산이 가능합니다. """

## 26.1 세트 만들기
"""
세트는 { }(중괄호) 안에 값을 저장하며 각 값은 ,(콤마)로 구분해줍니다.
세트는 요소의 순서가 정해져 있지 않습니다(unordered). 따라서 세트를 출력해보면 매번 요소의 순서가 다르게 나옵니다.

세트 = {값1, 값2, 값3}
"""
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)           # {'pineapple', 'orange', 'grape', 'strawberry', 'cherry'}

""" 세트에 들어가는 요소는 중복될 수 없습니다. """
fruits = {'orange', 'orange', 'cherry'}
print(fruits)           # {'cherry', 'orange'} / ornage를 두 개 넣어도 실제로는 한개만 출력

""" 세트는 리스트, 튜플, 딕셔너리와는 달리 [ ](대괄호)로 특정 요소만 출력할 수는 없습니다. """
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits[0])                    # error
print(fruits['strawberry'])         # error


### 26.1.1  세트에 특정 값이 있는지 확인하기
"""
그럼 세트에 특정 값이 있는지 확인하려며 어떻게 해야 할까요? 지금까지 리스트, 튜플, 딕셔너리에 사용했던 in 연산자를 사용하면 됩니다. 

값 in 세트
"""
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print('orange' in fruits)               # True
print('peach' in fruits)                # False

""" in 앞에 not을 붙이면 특정 값이 없는지 확인합니다. not in은 특정 값이 없으면 True, 있으면 False가 나옵니다. """
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print('peach' not in fruits)                # True
print('orange' not in fruits)               # False


### 26.1.2  set를 사용하여 세트 만들기
""" set를 사용하여 세트를 만들어보겠습니다.
set에는 반복 가능한 객체(iterable)를 넣습니다(반복 가능한 객체는 '?39.1 반복 가능한 객체 알아보기'에서 설명). 여기서는 간단하게 문자열과 range로 세트를 만들어보겠습니다.

set(반복가능한객체)
"""
a = set('apple')            # 유일한 문자만 세트로 만듦
print(a)                    # {'e', 'l', 'a', 'p'}

""" 숫자를 만들어내는 range를 사용 """
b = set(range(5))
print(b)                    # {0, 1, 2, 3, 4}


""" 빈 세트는 set에 아무것도 지정하지 않으면 됩니다. """
c = set()
print(c)                    # set()

""" 단, 세트가 { }를 사용한다고 해서 c = {}와 같이 만들면 빈 딕셔너리가 만들어지므로 주의해야 합니다. """
c = {}
print(type(c))              # type(객체) : <class 'dict'>
c = set()
print(type(c))              # type(객체) : <class 'set'>


#### 참고 : 한글 문자열을 세트로 만들기
""" set을 사용하여 한글 문자열을 세트로 만들면 다음과 같이 음절 단위로 세트가 만들어집니다. """
a = set('안녕하세요')
print(a)                    # {'녕', '요', '안', '세', '하'}


#### 참고 : 세트 안에 세트 넣기
""" 세트는 리스트, 딕셔너리와 달리 세트 안에 세트를 넣을 수 없습니다. """


#### 참고 : 프로즌 세트
""" 
파이썬은 내용을 변경할 수 없는 세트도 제공합니다.
이름 그대로 얼어 있는(frozen) 세트입니다. frozenset는 뒤에서 설명할 집합 연산과 메서드에서 요소를 추가하거나 삭제하는 연산, 메서드는 사용할 수 없습니다.
즉, 다음과 같이 frozenset의 요소를 변경하려고 하면 에러가 발생합니다.

프로즌세트 = frozenset(반복가능한객체)
"""
a = frozenset(range(10))
print(a)                    # frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

"""
요소를 변경할 수 없는 frozenset는 왜 사용할까요? frozenset는 세트 안에 세트를 넣고 싶을 때 사용합니다.
다음과 같이 frozenset는 frozenset를 중첩해서 넣을 수 있습니다. 단, frozenset만 넣을 수 있고, 일반 set는 넣을 수 없습니다.
"""
a = frozenset({frozenset({1, 2}), frozenset({3, 4})})
print(a)
