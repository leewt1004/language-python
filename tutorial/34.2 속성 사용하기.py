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

⭐(2)  def __init__(self) :
        self.hello = '안녕하세요'
    - 새로운 객체를 만들 때 자동으로 실행되는 특별한 함수입니다.
    - 초기화 함수라고도 하며, 객체가 생성될 때 필요한 데이터를 설정하는 역할을 합니다.
    - __init__ 함수는 hello라는 속성(특징 같은 것)을 만들고, 그 값으로 '안녕하세요'를 저장합니다.
    - self는 항상 메서드를 호출한 객체를 가리키기 때문에, 두 경우 모두 james를 가리킵니다.
        · self는 "지금 만들어지고 있는 객체 자신"을 가리킵니다. 예를 들어, james = Person()을 하면 self는 james가 됩니다.
    
    - 속성이란 객체 내부에 저장된 데이터 이며, 속성은 클래스 안에서 "self.속성명 = 값"과 같은 방식으로 정의되고, 각각의 객체마다 독립적으로 관리됩니다.
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

⭐(6) 왜 메서드마다 self를 써야 할까?
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
"""




### 34.2.1  self의 의미
"""
그런데 도데체 self는 뭘까요? self는 인스턴스 자기 자신을 의미합니다. 
우리는 인스턴스가 생성될 때 self.hello = '안녕하세요.'처럼 자기 자신에 속성을 추가했습니다.
여기서 __init__의 매개변수 self에 들어가는 값은 Person()이라 할 수 있습니다.
그리고 self가 완성된 뒤 james에 할당됩니다. 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어옵니다.
그래서 greeting 메서드에서 print(self.hello)처럼 속성을 출력할 수 있었던 것입니다.
"""
