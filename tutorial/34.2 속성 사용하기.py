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
    - Person 클래스 정의

(2)  def __init__(self) :
    - 
"""
