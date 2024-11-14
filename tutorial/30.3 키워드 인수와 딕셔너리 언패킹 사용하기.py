## 30.3 키워드 인수와 딕셔너리 언패킹 사용하기
"""
지금까지 함수를 호출할 때 키워드 인수로 직접 값을 넣었습니다. 이번에는 딕셔너리를 사용해서 키워드 인수로 값을 넣는 딕셔너리 언패킹을 사용해보겠습니다.
다음과 같이 딕셔너리 앞에 **(애스터리스크 두 개)를 붙여서 함수에 넣어줍니다.

함수(**딕셔너리)
"""
def personal_info(name, age, address) :
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

x = {'name' : '홍길동', 'age' : 30, 'address' : '서울시 용산구 이촌동'}     # 딕셔너리의 키워드(키)는 반드시 문자열 형태라야 함
personal_info(**x)
# 이름 : 홍길동
# 나이 : 30
# 주소 : 서울시 용산구 이촌동
"""
----- 코드 흐름 및 설명 -----

(1) def personal_info(name, age, address) :
    - 함수를 정의하고 name, age, addrss라는 세 개의 파라미터 입력 값을 받습니다.

(2) print('이름 : ', name), ('나이 : ', age), ('주소 : ', address)
    - 입력받는 name, age, address 결과를 출력합니다.

(3) x = {'name' : '홍길동', 'age' : 30, 'address' : '서울시 용산구 이촌동'}
    - x라는 딕셔너리를 생성합니다. 이 딕셔너리에는 키(name, age, address)와 그에 대응하는 값들이 저장되어 있습니다.

(4) personal_info(**x)
    - 함수를 호출하면서 x 딕셔너리를 언패킹하여 키-값 쌍을 각각의 파라미터에 전달합니다.
    - **x는 딕셔너리 x의 키를 파라미터 이름과 맞춰 name, age, address에 각각의 값을 전달합니다.

(5) 설명
    **x처럼 딕셔너리를 언패킹하면 딕셔너리의 값들이 함수의 인수로 들어갑니다.
    즉, personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동') 또는 personal_info('홍길동', 30, '서울시 용산구 이촌동')과 똑같은 동작이 됩니다.
    딕셔너리 언패킹을 사용할 때는 함수의 매개변수 이름과 딕셔너리의 키 이름이 같아야 합니다. 또한, 매개변수 개수와 딕셔너리 키의 개수도 같아야 합니다.
    만약 이름과 개수가 다르면 함수를 호출할 수 없으며 error가 발생합니다.
"""
""" 딕셔너리 변수 대신 딕셔너리 앞에 바로 **를 붙여도 동작은 같습니다. """
personal_info(**{'name' : '홍길동', 'age' : 30, 'address' : '서울시 용산구 이촌동'})




### 30.3.1  **를 두 번 사용하는 이유
"""
딕셔너리는 **처럼 *를 두 번 사용할까요? 왜냐하면 딕셔너리는 키-값 쌍 형태로 값이 저장되어 있기 때문입니다.
*를 한 번만 사용해서 함수를 호출해봅니다.
"""

""" *(애스터리스크)를 한 번만 사용해서 함수를 호출해봅니다. """
def personal_info(name, age, address) :
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

x = {'name' : '홍길동', 'age' : 30, 'address' : '서울시 용산구 이촌동'}     # 딕셔너리의 키워드(키)는 반드시 문자열 형태라야 함
personal_info(*x)
# 이름 :  name
# 나이 :  age
# 주소 :  address
"""
----- 코드 흐름 및 설명 -----

(1) def personal_info(name, age, address) :
    - 함수를 정의하고 name, age, addrss라는 세 개의 파라미터 입력 값을 받습니다.

(2) print('이름 : ', name), ('나이 : ', age), ('주소 : ', address)
    - 입력받는 name, age, address 결과를 출력합니다.

(3) x = {'name' : '홍길동', 'age' : 30, 'address' : '서울시 용산구 이촌동'}
    - x라는 딕셔너리를 생성합니다. 이 딕셔너리에는 키(name, age, address)와 그에 대응하는 값들이 저장되어 있습니다.

(4) personal_info(*x)
    - 여기서 *x는 딕셔너리 x의 키들('name', 'age', 'address')만 가져와서 언패킹합니다.

(5) 설명
    *x를 넣으면 x의 키가 출력됩니다. 즉, 딕셔너리를 한 번 언패킹하면 키를 사용한다는 뜻이 됩니다. 따라서 **처럼 딕셔너리를 두 번 언패킹하여 값을 사용하도록 만들어야 합니다.
"""




### 30.3.2  키워드 인수를 사용하는 가변 인수 함수 만들기
"""
이번에는 키워드 인수를 사용하는 가변 인수 함수를 만들어보겠습니다. 다음과 같이 키워드 인수를 사용하는 가변 인수 함수는 매개변수 앞에 **를 붙여서 만듭니다.
이제 값 여러 개를 받아서 매개변수 이름과 값을 각 줄에 출력하는 함수를 만들어보겠습니다.
함수를 만들 때 괄호 안에 **kwargs와 같이 매개변수 앞에 **를 붙입니다. 함수 안에서는 for로 kwargs.items()를 반복하면서 print로 값을 출력합니다.
매개변수 이름은 원하는 대로 지어도 되지만 관례적으로 keyword arguments를 줄여서 kwargs로 사용합니다. 특히 이 kwargs는 딕셔너리라서 for로 반복할 수 있습니다.
personal_info 함수에 키워드와 값을 넣어서 실행해봅니다. 값을 한 개 넣어도 되고, 세 개 넣어도 됩니다.

def 함수이름(**매개변수):
    코드
"""
def personal_info(**kwargs) :
    for kw, arg in kwargs.items() :
        print(kw, ': ', arg, sep='')

personal_info(name='홍길동')        # 출력 : name: 홍길동
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
# name: 홍길동
# age: 30
# address: 서울시 용산구 이촌동
"""
----- 코드 흐름 및 설명 -----

(1) def personal_info(**kwargs) :
    - 함수를 정의합니다. 이 함수는 여러 개의 키워드 인수를 받아서 kwargs라는 딕셔너리로 저장합니다.(키-값 쌍을 모두 포함)

(2) for kw, arg in kwargs.items() :
    - for 반복문을 사용하여 kwargs 딕셔너리의 키와 값을 순회합니다. kw는 키, arg는 해당 키에 대한 값을 나타냅니다.

(3) print(kw, ': ', arg, sep='')
    - 현재 키(kw)와 값(arg)을 출력합니다. sep=''는 출력 시 각 요소 사이에 공백 없이 연결해 표시합니다.

(4) personal_info(name='홍길동')
    - 함수를 호출하여 키워드 인수를 출력합니다.

(5) personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
    - 함수를 호출하여 세 개의 키워드를 출력합니다.

이렇게 인수를 직접 넣어도 되고, 딕셔너리 언패킹을 사용해도 됩니다.
"""


""" 다음과 같이 딕셔너리를 만들고 앞에 **를 붙여서 넣어봅니다. """
def personal_info(**kwargs) :
    for kw, arg in kwargs.items() :
        print(kw, ': ', arg, sep='')

x = {'name' : '홍길동'}
y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)      # 출력 : name: 홍길동
personal_info(**y)
# name: 홍길동
# age: 30
# address: 서울시 용산구 이촌동
"""
----- 코드 흐름 및 설명 -----

(1) def personal_info(**kwargs) :
    - 함수를 정의합니다. 이 함수는 여러 개의 키워드 인수를 받아서 kwargs라는 딕셔너리로 저장합니다.(키-값 쌍을 모두 포함)

(2) for kw, arg in kwargs.items() :
    - for 반복문을 사용하여 kwargs 딕셔너리의 키와 값을 순회합니다. kw는 키, arg는 해당 키에 대한 값을 나타냅니다.

(3) print(kw, ': ', arg, sep='')
    - 현재 키(kw)와 값(arg)을 출력합니다. sep=''는 출력 시 각 요소 사이에 공백 없이 연결해 표시합니다.

(4) x = {'name' : '홍길동'}
    y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
    - x, y라는 딕셔너리를 생산합니다. 각각에 키와 값(키-값)이 저장되어 있습니다.

(5) **personal_info(x)
    **personal_info(y)
    - 함수를 호출하면서 x, y딕셔너리를 언패킹하여 각각의 인수를 전달하고 출력합니다.

(6) 해설
    딕셔너리에 들어있는 값이 그대로 출력되었습니다. 
    즉, 딕셔너리 x는 {'name': '홍길동'}이므로 personal_info(**x)로 호출하면 personal_info(name='홍길동')과 같고, 
    딕셔너리 y는 {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}이므로 personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')과 같습니다.
    
    이처럼 함수를 만들 때 def personal_info(**kwargs):와 같이 매개변수에 **를 붙여주면 키워드 인수를 사용하는 가변 인수 함수를 만들 수 있습니다. 
    그리고 이런 함수를 호출할 때는 키워드와 인수를 각각 넣거나 딕셔너리 언패킹을 사용하면 됩니다.
"""


""" 보통 **kwargs를 사용한 가변 인수 함수는 다음과 같이 함수 안에서 특정 키가 있는지 확인한 뒤 해당 기능을 만듭니다. """
def personal_info(**kwargs) :
    if 'name' in kwargs : 
        print('이름 : ', kwargs['name'])
    if 'age' in kwargs : 
        print('나이 : ', kwargs['age'])
    if 'address' in kwargs : 
        print('주소 : ', kwargs['address'])

personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
"""
----- 코드 흐름 및 설명 -----

(1) def personal_info(**kwargs) :
    - 함수를 정의합니다. 이 함수는 여러 개의 키워드 인수를 바당서 kwargs라는 딕셔너리에 저장합니다.

(2) if 'name' in kwargs : 
        print('이름 : ', kwargs['name'])
    if 'age' in kwargs : 
        print('나이 : ', kwargs['age'])
    if 'address' in kwargs : 
        print('주소 : ', kwargs['address'])
    - kwargs 딕셔너리에 'name', 'age', 'address' 키가 있는지 확인합니다. 만약 있다면, 각각의 값을 가져와서 다음 줄의 print 문을 실행합니다.
    - 반복문의 가변인수를 출력합니다.

(3) personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
    - 함수를 호출하면서 세 개의 키워드 인수를 전달합니다.
    - 조건문이 True가 되어 인수를 순서대로 출력합니다.
"""




#### 참고 : 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기
"""
고정 인수와 가변 인수(키워드 인수)를 함께 사용할 때는 다음과 같이 고정 매개변수를 먼저 지정하고, 그 다음 매개변수에 **를 붙여주면 됩니다. 
**kwargs가 고정 매개변수보다 앞쪽에 오면 안 됩니다. 매개변수 순서에서 **kwargs는 반드시 가장 뒤쪽에 와야 합니다.
"""
def personal_info(name, **kwargs) :
    print(name)
    print(kwargs)

personal_info('홍길동')
personal_info('홍길동', age=30, address='서울시 용산구 이촌동')
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})




#### 참고 : 위치 인수와 키워드 인수를 함께 사용하기
"""
함수에서 위치 인수를 받는 *args와 키워드 인수를 받는 **kwargs를 함께 사용할 수도 있습니다.
대표적인 함수가 print인데 print는 출력할 값을 위치 인수로 넣고 sep, end 등을 키워드 인수로 넣습니다. 
"""
def custon_print(*args, **kwargs) :
    print(*args, **kwargs)

custon_print(1, 2, 3, sep=':', end='')
"""
----- 코드 흐름 및 설명

(1) def custon_print(*args, **kwargs) :
    - 함수를 정의합니다. 이 함수는 위치 인수를 받을 수 있는 *args와 키워드 인수를 받을 수 있는 **kwargs를 사용합니다.

(2) print(*args, **kwargs)
    - print 함수에 *args와 **kwargs를 전달합니다.
    - *args는 위치 인수들을 언패킹하여 print 함수에 전달하고, **kwargs는 키워드 인수들을 언패킹하여 전달합니다.

(3) custon_print(1, 2, 3, sep=':', end='')
    - *args는 1, 2, 3을 튜플 형태 (1, 2, 3)로 받습니다.
    - **kwargs는 키워드 인수 sep=':'와 end=''를 딕셔너리 형태 {'sep': ':', 'end': ''}로 받습니다.

(4) 참고
    딕셔너리 자체는 항상 :로 키와 값을 구분합니다.
    함수에서 사용하는 키워드 인수는 =로 키와 값을 구분하며, 이 키워드 인수들은 함수 내부에서 **kwargs로 모일 때 딕셔너리로 변환됩니다.    
"""


"""
**kwargs가 *args보다 앞쪽에 오면 안 됩니다. 매개변수 순서에서 **kwargs는 반드시 가장 뒤쪽에 와야 합니다.
특히 고정 매개변수와 *args, **kwargs를 함께 사용한다면 def custom_print(a, b, *args, **kwargs):처럼 매개변수는 고정 매개변수, *args, **kwargs 순으로 지정해야 합니다.
"""
