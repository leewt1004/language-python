## 34.2 속성 사용하기
"""
지금까지 클래스에서 메서드를 만들고 호출해보았습니다. 이번에는 클래스에서 속성을 만들고 사용해보겠습니다. 속성(attribute)을 만들 때는 __init__ 메서드 안에서 self.속성에 값을 할당합니다.

class 클래스이름:
    def __init__(self):
        self.속성 = 값
"""
class Person:
    def __init__(self) :
        self.hello = '안녕하세요'   # 속성 정의 및 값 할당

    def greeting(self) :
        print(self.hello)   # self.hello 속성 값 출력

james = Person()    # 클래스 Person의 인스턴스(객체) james 생성
print(james.greeting()) # greeting 메서드 호출
"""
----- 코드 흐름 및 설명 -----

(1) class Person:
    - Person 클래스 정의합니다.
    - Person은 객체를 만들기 위한 설계도로 보면 됩니다.

(2)  def __init__(self) :
        self.hello = '안녕하세요'
    - 새로운 객체를 만들 때 자동으로 실행되는 특별한 함수입니다.
    - 초기화 함수라고도 하며, 객체가 생성될 때 필요한 데이터를 설정하는 역할을 합니다.
    - __init__ 함수는 hello라는 속성(특징 같은 것)을 만들고, 그 값으로 '안녕하세요'를 저장합니다.
    - ⭐ self는 항상 메서드를 호출한 객체를 가리키기 때문에, 두 경우 모두 james를 가리킵니다.
        · self는 "지금 만들어지고 있는 객체 자신"을 가리킵니다. 예를 들어, james = Person()을 하면 self는 james가 됩니다.
    - ⭐ 속성이란 객체 내부에 저장된 데이터 이며, 속성은 클래스 안에서 "self.속성명 = 값"과 같은 방식으로 정의되고, 각각의 객체마다 독립적으로 관리됩니다.
        · self.hello에서 hello가 속성입니다.
        · hello는 객체가 가지고 있는 속성이고, 그 값은 "안녕하세요" 입니다.
        · 이 속성은 james라는 객체에 속해 있습니다.

⭐(3) def greeting(self) :
        print(self.hello) 
    - greeting이라는 이름의 함수(메서드)를 만듭니다. 이 함수는 "객체가 가진 데이터를 출력하는 기능"을 합니다.
    - self는 지금 이 함수를 쓰는 객체를 뜻합니다. 예를 들어, james.greeting()을 호출하면, self는 james가 됩니다.
    - self.hello에서의 self는 이 함수를 호출한 객체입니다. 여기서는 james가 호출했으니, self.hello는 james.hello를 뜻합니다.
    - james 객체의 hello 속성에 저장된 값을 꺼냅니다. 그 값은 '안녕하세요'입니다.
    - print()로 '안녕하세요'를 화면에 보여줍니다.
    - 이 함수는 객체가 가진 "hello" 데이터를 꺼내서 보여주는 역할을 합니다.
        · 만약 james.greeting()을 호출하면 james가 가지고 있는 hello 속성 값을 꺼내서, 그 값을 화면에 출력하는 겁니다.
    
(4) james = Person()
    - Person 클래스를 호출해 새로운 객체를 생성합니다. 이 과정에서 __init__ 함수가 자동 실행되어 james 객체에 hello 속성이 생기고 값은 '안녕하세요'가 됩니다.

(5) print(james.greeting())
    - james.greeting() 호출
        · james 객체가 greeting 메서드를 실행합니다.
        · 메서드 내부에서 print(self.hello)가 실행되어 '안녕하세요'를 출력합니다.
    - print
        · greeting() 메서드는 아무 값을 반환하지 않으므로 None을 반환합니다.

(6) ⭐ 왜 메서드마다 self를 써야 할까?
    - __init__에서의 self
        · 객체 james가 생성될 때, __init__ 메서드가 자동으로 호출됩니다.
        · 이때 self는 "지금 생성되고 있는 객체", 즉 james를 가리킵니다.
        · 그래서 self.hello = '안녕하세요'로 james라는 객체에 hello라는 속성을 저장합니다.

    - greeting에서 self
        · james.greeting()을 호출하면, Python은 자동으로 greeting(self)를 실행합니다.
        · 여기서 self는 "지금 이 메서드를 호출한 객체", 즉 james를 가리킵니다.
        · 그래서 print(self.hello)는 james.hello 값을 출력합니다.

    - 독립적인 메서드가 각자 self를 받아야 한다
        · Python에서는 각 메서드가 호출될 때마다 self를 통해 호출한 객체를 전달받아야 합니다.
        · __init__과 greeting은 서로 다른 메서드이기 때문에, 객체와의 연결을 각각 명확히 해야 합니다.

    - 비유로 쉽게 설명
        · james라는 사람이 있습니다.
        · __init__은 james에게 "이름표"를 붙이는 작업입니다.(여기서 self는 이름표를 붙이는 대상을 명확히 알려주는 역할을 합니다.)
        · greeting은 james가 자신의 이름표를 읽는 작업입니다.(여기서도 self는 **"지금 이름표를 읽는 사람이 james야!"**라고 알려줍니다.)

(7) ⭐ 왜 두 개의 메서드(__init__, greeting)를 사용할까?
    - __init__
        · 이 메서드는 객체를 만들 때 자동으로 실행됩니다.
        · 객체가 태어나자마자 해야 할 일을 처리하는 겁니다.
        · james라는 객체가 만들어질 때 "내 이름은 안녕하세요 야!" 하고 이름표를 붙이는 것처럼, 데이터를 미리 준비하는 역할입니다.
        · james = Person() # "나는 james라는 이름을 가진 사람이야!" / 이름표를 붙임
    - greeting
        · 이 메서드는 이미 만들어진 데이터(hello)를 사용하는 역할입니다.
        · 준비된 이름표를 보고, "내 이름은 안녕하세요 야!" 라고 말하는 역할이라고 생각하면 됩니다.
        · james.greeting() # "내 이름은 '안녕하세요' 야!" / 이름표를 보고 자기 소개를 함
    - 두개의 메서드를 쓰는 이유
        · __init__ : 태어날 때 이름표를 붙이기
        · greeting : 이름표를 읽고 말하기
        · 이렇게 나누면 태어날 때 한 번만 해야할일(__init__)과 언제든 반복해서 할 수 있는 일(greeting)을 따로 관리할 수 있습니다.
        · 즉, 클래스에서 두 개의 메서드를 사용한 이유는 "역할을 분리"하고 "확장성"을 높이기 위함입니다.
"""




### 34.2.1  self의 의미
"""
그런데 도데체 self는 뭘까요? self는 인스턴스 자기 자신을 의미합니다. 
우리는 인스턴스가 생성될 때 self.hello = '안녕하세요.'처럼 자기 자신에 속성을 추가했습니다.
여기서 __init__의 매개변수 self에 들어가는 값은 Person()이라 할 수 있습니다.
그리고 self가 완성된 뒤 james에 할당됩니다. 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어옵니다.
그래서 greeting 메서드에서 print(self.hello)처럼 속성을 출력할 수 있었던 것입니다.
"""




### 34.2.2  인스턴스를 만들 때 값 받기
"""
이번에는 클래스로 인스턴스를 만들 때 값을 받는 방법을 알아보겠습니다. 다음과 같이 __init__ 메서드에서 self 다음에 값을 받을 매개변수를 지정합니다. 그리고 매개변수를 self.속성에 넣어줍니다.
그럼 Person 클래스로 인스턴스를 만들 때 이름, 나이, 주소를 받아보겠습니다.

class 클래스이름:
    def __init__(self, 매개변수1, 매개변수2):
        self.속성1 = 매개변수1
        self.속성2 = 매개변수2
"""
class Person :
    def __init__(self, name, age, address) :
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address
    def greeting(self) :
        print('{0}저는 {1}입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()    # 안녕하세요. 저는 마리아입니다.

print('이름 : ', maria.name)
print('나이 : ', maria.age)
print('주소 : ', maria.address)
"""
----- 코드 흐름 및 설명 -----

(1) class Person:
    - Person 클래스 정의합니다.
    - Person은 객체를 만들기 위한 설계도로 보면 됩니다.

(2) def __init__(self, name, age, address) :
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address
    - 객체가 생성될 때 자동으로 실행되며, 데이터 name, age, address, hello를 저장하고, 모든 객체는 기본적으로 hello = '안녕하세요' 라는 데이터를 가집니다.
    - name, age, addresssms __init__ 메서드로 값을 전달받기 위한 임시 변수라고 생각하면 됩니다. 이 변수들은 __init__ 메서드가 실행되는 동안만 사용됩니다.
    - 객체(maria)에서 전달받은 값(name, age, address)은 각각 self.name, self.age, self.address의 객체의 속성으로 저장됩니다.

(3) def greeting(self) :
        print('{0}저는 {1}입니다.'.format(self.hello, self.name))
    - 객체가 가진 데이터를 사용해서 인사말을 출력합니다.
    - {0} → self.hello / {1} → self.name
    - {0}, {1}은 리스트, 튜플, 문자열 등 모든 시퀀스 자료형의 인덱스가 0부터 시작하기 때문입니다.

(4) maria = Person('마리아', 20, '서울시 서초구 반포동')
    - maria라는 객체를 생성하면서 이름(마리아), 나이(20), 주소(서울시 서초구 반포동)를 __init__메서드를 통해 객체 안에 저장됩니다.
    - 객체에 저장된 결과는 maria.name = '마리아' / maria.age = 20 / maria.address = '서울시 서초구 반포동' 입니다.

(5) maria.greeting()
    - maria객체가 greeting()메서드를 실행합니다.

(6) print('이름 : ', maria.name)
    print('나이 : ', maria.age)
    print('주소 : ', maria.address)
    - maria 객체에 저장된 데이터를 각각 출력합니다.

(7) 해설
    __init__ 메서드를 보면 self 다음에 name, age, address를 지정했습니다. 그리고 메서드 안에서는 self.name = name처럼 매개변수를 그대로 self에 넣어서 속성으로 만들었습니다.
    greeting 메서드는 인사를 하고 이름을 출력하도록 수정했습니다. 물론 name 속성에 접근할 때는 self.name처럼 사용해야 합니다.
    이제 Person의 ( )(괄호) 안에 이름, 나이, 주소를 콤마로 구분해서 넣은 뒤에 변수에 할당합니다. 이렇게 하면 이름은 '마리아', 나이는 20, 주소는 '서울시 서초구 반포동'인 maria 인스턴스가 만들어집니다.
    maria 인스턴스의 greeting 메서드를 호출해보면 '안녕하세요. 저는 마리아입니다.'처럼 인삿말과 함께 이름도 출력됩니다.
    클래스 안에서 속성에 접근할 때는 self.속성 형식이었죠? 클래스 바깥에서 속성에 접근할 때는 인스턴스.속성 형식으로 접근합니다.
    다음과 같이 maria.name, maria.age, maria.address의 값을 출력해보면 Person으로 인스턴스를 만들 때 넣었던 값이 출력됩니다.
    이렇게 인스턴스를 통해 접근하는 속성을 인스턴스 속성이라 부릅니다.
    """




#### 참고 : 클래스의 위치 인수, 키워드 인수
"""
클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있습니다. 규칙은 함수와 같습니다.
위치 인수와 리스트 언패킹을 사용하려면 다음과 같이 *args를 사용하면 됩니다. 이때 매개변수에서 값을 가져오려면 args[0]처럼 사용해야 합니다.
"""
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아', 20, '서울시 서초구 반포동'])


""" 키워드 인수와 딕셔너리 언패킹을 사용하려면 다음과 같이 **kwargs를 사용하면 됩니다. 이때 매개변수에서 값을 가져오려면 kwargs['name']처럼 사용해야 합니다. """
class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})




### 참고 : 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기
"""
지금까지 클래스의 인스턴스 속성은 __init__ 메서드에서 추가한 뒤 사용했습니다.
하지만 클래스로 인스턴스를 만든 뒤에도 인스턴스.속성 = 값 형식으로 속성을 계속 추가할 수 있습니다.
다음 Person 클래스는 빈 클래스이지만 인스턴스를 만든 뒤 name 속성을 추가합니다.
"""
class Person:
    pass

maria = Person()        # 인스턴스 생성
maria.name = '마리아'   # 인스턴스를 만든 뒤 속성 추가
print(maria.name)


""" 이렇게 추가한 속성은 해당 인스턴스에만 생성됩니다. 따라서 클래스로 다른 인스턴스를 만들었을 때는 추가한 속성이 생성되지 않습니다. """
james = Person()
print(jame.name) # error 발생


"""
인스턴스는 생성한 뒤에 속성을 추가할 수 있으므로 __init__ 메서드가 아닌 다른 메서드에서도 속성을 추가할 수 있습니다. 단, 이때는 메서드를 호출해야 속성이 생성됩니다.
"""
class Person :
    def greeting(self) :
        self.hello = '안녕하세요'   # greeting 메서드에서 hello 속성 추가

maria = Person()
maria.hello     # 아직 hello 속성이 없음 / error 발생
maria.greeting()    # greeting 메서드를 호출해야
print(maria.hello)  # hello 속성이 생성됨


"""
인스턴스는 자유롭게 속성을 추가할 수 있지만 특정 속성만 허용하고 다른 속성은 제한하고 싶을 수도 있습니다.
이때는 클래스에서 __slots__에 허용할 속성 이름을 리스트로 넣어주면 됩니다. 특히 속성 이름은 반드시 문자열로 지정해줍니다.

__slots__ = ['속성이름1, '속성이름2']
"""
class Person() :
    __slots__ = ['name', 'age']     # name, age만 허용(다른 속성은 생성 제한)

maria = Person()
maria.name = '마리아'                   # 허용된 속성
maria.age = 20                          # 허용된 속성

maria.address = '서울시 서초구 반포동'  # 허용되지 않은 속성을 추가하면 error 발생
