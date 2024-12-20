## 30.2 키워드 인수 사용하기
"""
지금까지 함수에 인수를 넣을 때 값이나 변수를 그대로 넣었습니다. 그러다 보니 각각의 인수가 무슨 용도인지 알기가 어려웠습니다. 보통은 함수의 사용 방법을 익힐 때 인수의 순서와 용도를 함께 외웁니다.
예를 들어 개인 정보를 출력하는 함수를 만들어보겠습니다.
"""
def personal_info(name, age, address) :
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

personal_info('홍길동', 30, '서울시 용산구 이촌동')
# 이름 : 홍길동
# 나이 : 30
# 주소 : 서울시 용산구 이촌동
"""
(1) def personal_info(name, age, address):
    - 함수를 정의하고 name, age, addrss라는 세 개의 파라미터 입력 값을 받습니다.

(2) print('이름 : ', name), ('나이 : ', age), ('주소 : ', address)
    - 입력받는 name, age, address 결과를 출력합니다.

(3) personal_info('홍길동', 30, '서울시 용산구 이촌동')
    - 함수를 호출하면서 각각의 인수를 전달합니다.

(4) 설명
    만약 인수의 순서가 달라지면 잘못된 결과가 출력됩니다.
    인수의 순서와 용도를 모두 기억해야 해서 불편합니다.
"""


""" 
파이썬에서는 인수의 순서와 용도를 매번 기억하지 않도록 키워드 인수(keyword argument)라는 기능을 제공합니다.
키워드 인수는 말 그대로 인수에 이름(키워드)을 붙이는 기능인데 키워드=값 형식으로 사용합니다.
그럼 personal_info 함수를 키워드 인수 방식으로 호출해보겠습니다.

함수(키워드=값)
"""
def personal_info(name, age, address) :
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

personal_info(name='홍길동', address='서울시 용산구 이촌동', age=30, )
# 이름 : 홍길동
# 나이 : 30
# 주소 : 서울시 용산구 이촌동
"""
(1) def personal_info(name, age, address) :
    - 함수를 정의하고 name, age, addrss라는 세 개의 파라미터 입력 값을 받습니다.

(2) print('이름 : ', name), ('나이 : ', age), ('주소 : ', address)
    - 입력받는 name, age, address 결과를 출력합니다.

(3) personal_info(name='홍길동', address='서울시 용산구 이촌동', age=30, )
    - 함수를 호출하면서 키워드 인수를 사용합니다.
    - 키워드 인수를 사용했기 때문에 인수 순서를 바꿔도 파라미터에 맞게 값이 전달됩니다.

(4) 설명
    키워드 인수를 사용하니 함수를 호출할 때 인수의 용도가 명확하게 보입니다. 특히 키워드 인수를 사용하면 인수의 순서를 맞추지 않아도 키워드에 해당하는 값이 들어갑니다.
personal_info 함수는 이름, 나이, 주소 순으로 인수를 넣어야 하지만, 키워드 인수를 사용해서 순서를 지키지 않고 값을 넣었습니다.

참고로 print 함수에서 사용했던 sep, end도 키워드 인수입니다.
"""
