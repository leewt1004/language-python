# Unit 25. 딕셔너리 응용하기
"""
딕셔너리의 키-값 쌍을 조작하는 메서드와 정보를 조회하는 메서드를 사용해보겠습니다.
그리고 for 반복문을 사용하여 키와 값에 접근하는 방법, 딕셔너리 표현식, 중첩 딕셔너리도 함께 대해 알아보겠습니다.
"""


## 25.1 딕셔너리 조작하기
""" 딕셔너리를 조작하는 메서드와 정보를 얻는 메서드부터 알아보겠습니다. 파이썬에서 제공하는 딕셔너리 메서드는 여러 가지가 있지만 여기서는 자주 쓰는 메서드를 설명하겠습니다. """


### 25.1.1  딕셔너리에 키-값 쌍 추가하기
"""
딕셔너리의 중요한 기능 중 하나가 바로 키-값 쌍 추가입니다. 다음과 같이 딕셔너리에 키-값 쌍을 추가하는 메서드는 2가지가 있습니다.

setdefault: 키-값 쌍 추가
update: 키의 값 수정, 키가 없으면 키-값 쌍 추가
"""


# 25.1.2  딕셔너리에 키와 기본값 저장하기
"""
setdefault(키)는 딕셔너리에 키-값 쌍을 추가합니다. setdefault에 키만 지정하면 값에 None을 저장합니다. 
다음은 키 'e'를 추가하고 값에 None을 저장합니다.
"""
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x)                # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None}

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e', None)
print(x)                # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None}


### 25.1.3  딕셔너리에서 키의 값 수정하기

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""
키-값 쌍을 추가했으면 값을 수정하고 싶을 수도 있겠죠? 이때는 update 메서드를 사용합니다.
이름 그대로 딕셔너리에서 키의 값을 수정합니다. 예를 들어 딕셔너리가 x = {'a': 10}이라면 x.update(a=90)과 같이 키에서 작은따옴표 또는 큰따옴표를 빼고 키 이름과 값을 지정합니다.

update(키=값)
"""
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a = 90)
print(x)                # {'a': 90, 'b': 20, 'c': 30, 'd': 40}
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
""" 딕셔너리에 키가 없으면 키-값 쌍을 추가합니다. 딕셔너리 x에는 키 'e'가 없으므로 x.update(e=50)을 실행하면 'e': 50을 추가합니다. """
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(e=50)
print(x)                # {'a': 90, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
""" update는 키-값 쌍 여러 개를 콤마로 구분해서 넣어주면 값을 한꺼번에 수정할 수 있습니다. 이때도 키가 있으면 해당 키의 값을 수정하고 없으면 키-값 쌍을 추가합니다. """
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=900, f=60)
print(x)                # {'a': 900, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
""" update(키=값)은 키가 문자열일 때만 사용할 수 있습니다. 만약 키가 숫자일 경우에는 update(딕셔너리)처럼 딕셔너리를 넣어서 값을 수정할 수 있습니다. """
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
print(y)                # {1: 'ONE', 2: 'two', 3: 'THREE'}
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
""" 
리스트와 튜플을 이용하는 방법도 있습니다. update(리스트), update(튜플)은 리스트와 튜플로 값을 수정합니다.
여기서 리스트는 [[키1, 값1], [키2, 값2]] 형식으로 키와 값을 리스트로 만들고 이 리스트를 다시 리스트 안에 넣어서 키-값 쌍을 나열해줍니다(튜플도 같은 형식).
"""
y = {1: 'ONE', 2: 'two', 3: 'THREE'}
y.update([[2, 'TWO'], [4, 'FOUR']])
print(y)                # {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR'}
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
""" 특히 update(반복가능한객체)는 키-값 쌍으로 된 반복 가능한 객체로 값을 수정합니다. 즉, 다음과 같이 키 리스트와 값 리스트를 묶은 zip 객체로 값을 수정할 수 있습니다. """
y = {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR'}
y.update(zip([1, 2], ['one', 'two']))       # zip() 함수는 두 개의 리스트 [1, 2]와 ['one', 'two']를 (키, 값) 쌍으로 묶어주는 역할을 합니다.
print(y)                # {1: 'one', 2: 'two', 3: 'THREE', 4: 'FOUR'}
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""


#### 참고 : setdefault와 update의 차이
""" setdefault는 키-값 쌍 추가만 할 수 있고, 이미 들어있는 키의 값은 수정할 수 없습니다. 하지만 update는 키-값 쌍 추가와 값 수정이 모두 가능합니다. """
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('a', 90)
print(x)            # 'a'의 값은 바뀌지 않습니다.


### 25.1.4  딕셔너리에서 키-값 쌍 삭제하기
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""
딕셔너리에서 특정 키-값 쌍을 삭제한 뒤 삭제한 값을 반환합니다.

pop(키)
"""
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
print(x)                # {'b': 20, 'c': 30, 'd': 40}
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""
기본값을 지정하면 딕셔너리에 키가 있을 때는 해당 키-값 쌍을 삭제한 뒤 삭제한 값을 반환하지만 키가 없을 때는 기본값만 반환합니다.

pop(키, 기본값)
"""
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.pop('z', 0))            # 기본값으로 지정한 0을 반환
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
""" pop 대신 del로 특정 키-값 쌍을 삭제할 수도 있습니다. 이때는 [ ]에 키를 지정하여 del을 사용합니다. """
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']
print(x)
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""


### 25.1.5  딕셔너리에서 임의의 키-값 쌍 삭제하기
"""
딕셔너리에서 임의의 키-값 쌍을 삭제한 뒤 삭제한 키-값 쌍을 튜플로 반환합니다. 이 메서드는 파이썬 버전에 따라 동작이 달라지는데, 파이썬 3.6 이상에서는 마지막 키-값 쌍을 삭제하며 3.5 이하에서는 임의의 키-값 쌍을 삭제합니다.

poopitem()
"""
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()
('d',40)
print(x)                # {'a': 10, 'b': 20, 'c': 30}


### 25.1.6  딕셔너리의 모든 키-값 쌍을 삭제하기
"""
딕셔너리의 모든 키-값 쌍을 삭제합니다.

clear()
"""
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
print(x)                # {}


### 25.1.7  딕셔너리에서 키의 값을 가져오기
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""
딕셔너리에서 특정 키의 값을 가져옵니다.

get(키)
"""
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('a'))
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""
기본값을 지정하면 딕셔너리에 키가 있을 때는 해당 키의 값을 반환하지만 키가 없을 때는 기본값을 반환합니다.

get(키, 기본값)
"""
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('z',0))         # 기본값 0 반환
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""


### 25.1.8  딕셔너리에서 키-값 쌍을 모두 가져오기
"""
딕셔너리는 키와 값을 가져오는 다양한 메서드를 제공합니다.
이 메서드들은 보통 for 반복문과 조합해서 사용합니다.

items: 키-값 쌍을 모두 가져옴
keys: 키를 모두 가져옴
values: 값을 모두 가져옴
"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
""" items()는 딕셔너리의 키-값 쌍을 모두 가져옵니다. """
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items())                # dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
""" keys()는 키를 모두 가져옵니다. """
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.keys())             # dict_keys(['a', 'b', 'c', 'd'])
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
""" values()는 값을 모두 가져옵니다. """
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.values())           # dict_values([10, 20, 30, 40])
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""


### 25.1.9  리스트와 튜플로 딕셔너리 만들기
"""
이번에는 리스트(튜플)로 딕셔너리를 만들어보겠습니다.
먼저 keys = ['a', 'b', 'c', 'd']처럼 키가 들어있는 리스트를 준비합니다(튜플도 됩니다). 그리고 dict.fromkeys에 키가 들어있는 리스트를 넣으면 딕셔너리를 생성합니다.
"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""
키 리스트로 딕셔너리를 생성하며 값은 모두 None으로 저장합니다. 

dict.fromkeys(키리스트)
"""
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)                    # {'a': None, 'b': None, 'c': None, 'd': None}
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""
키 리스트와 값을 지정하면 해당 값이 키의 값으로 저장됩니다.

dict.fromkeys(키리스트, 값)
"""
keys = ['a', 'b', 'c', 'd']
y = dict.fromkeys(keys, 100)
print(y)                    # {'a': 100, 'b': 100, 'c': 100, 'd': 100}
"""------------------------------------------------------------------------------------------------------------------------------------------------------"""


#### 참고 : defaultdict 사용하기
"""
지금까지 사용한 딕셔너리(dict)는 없는 키에 접근했을 경우 에러가 발생합니다.
그러면 에러가 발생하지 않게 하려면 어떻게 해야 할까요? 이때는 defaultdict를 사용합니다.
defaultdict는 없는 키에 접근하더라도 에러가 발생하지 않으며 기본값을 반환합니다. defaultdict는 collections 모듈에 들어있으며 기본값 생성 함수를 넣습니다.

defaultdict(기본값생성함수)
"""
from collections import defaultdict         # collections 모듈에서 defaultdict를 가져옴
y = defaultdict(int)                        # int로 기본값 생성
print(y['z'])                               # 0

"""
defaultdict(int)처럼 int를 넣었는데 기본값이 왜 0인지 의문이 생길 수도 있습니다. int는 실수나 문자열을 정수로 변환하지만, int에 아무것도 넣지 않고 호출하면 0을 반환합니다.
defaultdict에는 특정 값을 반환하는 함수를 넣어주면 되는데, defaultdict(int)는 기본값 생성 함수로 int를 지정하여 0이 나오도록 만든 것입니다.
0이 아닌 다른 값을 기본값으로 설정하고 싶다면 다음과 같이 기본값 생성 함수를 만들어서 넣어주면 됩니다.
"""
from collections import defaultdict
z = defaultdict(lambda: 'python')
print(z['a'])                   # python
print(z[0])                     # python
