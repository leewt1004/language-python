## 30.4 매개변수에 초깃값 지정하기
"""
지금까지 함수를 호출할 때 항상 인수를 넣어서 값을 전달했습니다. 그러면 인수를 생략할 수는 없을까요?
이때는 함수의 매개변수에 초깃값을 지정하면 됩니다. 초깃값은 다음과 같이 함수를 만들 때 매개변수=값 형식으로 지정합니다.
매개변수의 초깃값은 주로 사용하는 값이 있으면서 가끔 다른 값을 사용해야 할 때 활용합니다.
대표적인 예가 print 함수인데, print 함수의 sep는 초깃값이 ' '(공백)으로 지정되어 있어서 대부분 그대로 사용하고, 가끔 sep에 다른 값을 넣어서 사용합니다.

def 함수이름(매개변수=값):
    코드
"""

""" 이제 personal_info 함수에서 매개변수 address의 초깃값을 '비공개'로 지정해보겠습니다. """
def personal_info(name, age, address='비공개') :
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30)                                # address는 초깃값이 있으므로 personal_info는 addrss 부분을 비워두고 호출할 수 있음
personal_info('홍길동', 30, '서울시 용산구 이촌동')         # 매개변수에 초깃값이 지정되어 있더라도 값을 넣으면 해당 값이 전달됨




### 30.4.1  초깃값이 지정된 매개변수의 위치
"""
매개변수의 초깃값을 지정할 때 한 가지 주의할 점이 있습니다. 초깃값이 지정된 매개변수 다음에는 초깃값이 없는 매개변수가 올 수 없습니다.
personal_info 함수에서 address가 가장 마지막 매개변수였는데 이번에는 address를 두 번째 매개변수로 만들고, 그 다음에 초깃값을 지정하지 않은 age가 오도록 만들어보겠습니다.
"""
def personal_info(name, address='비공개', age) :        # address 초깃값을 두번째로 지정(error 발생)
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30, '서울시')                  
personal_info('홍길동', 30, '서울시 용산구 이촌동')
"""
함수를 만들어보면 문법 에러가 발생합니다. 왜냐하면 함수를 이렇게 만들어버리면 personal_info('홍길동', 30)으로 함수를 호출했을 때 30이 어디로 들어가야 할지 알 수가 없기 때문입니다.
address에 들어가려니 age 부분이 비어 버리죠. 잘못된 문법이므로 이렇게 만들면 안 됩니다.
즉, 다음과 같이 초깃값이 지정된 매개변수는 뒤쪽에 몰아주면 됩니다.
"""
def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info('홍길동', 30)     # 마지막 파라미터값만 초깃값을 설정했으므로 첫 번째, 두 번째 인수값만 와야 함

def personal_info(name, age=0, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info('홍길동')         # 두 번째, 세 번째 파라미터값만 초깃값을 설정했으므로 첫 번째 인수값만 와야 함

def personal_info(name='비공개', age=0, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info()                 # 모든 매개변수에 초깃값을 지정하면 personal_info()처럼 인수를 넣지 않고 호출할 수 있음




"""
지금까지 위치 인수, 키워드 인수, 매개변수의 초깃값 사용 방법을 알아보았습니다.
함수에서 *와 **를 붙이는 문법이 조금 생소할 수도 있습니다. 여기서는 *를 리스트에 사용하고, **를 딕셔너리에 사용한다는 점만 기억하면 됩니다.
"""
