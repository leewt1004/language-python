## 33.2 함수 안에서 함수 만들기
"""
이번에는 함수 안에서 함수를 만드는 방법을 알아보겠습니다. 다음과 같이 def로 함수를 만들고 그 안에서 다시 def로 함수를 만들면 됩니다.
간단하게 함수 안에서 문자열을 출력하는 함수를 만들고 호출해봅니다.

def 함수이름1():
    코드
    def 함수이름2():
        코드
"""
def print_hello():  # 외부 함수
    hello = 'Hello, world!'  # 외부 함수의 지역 변수

    def print_message():  # 내부 함수
        print(hello)  # 외부 함수의 지역 변수 'hello'를 출력

    print_message()  # 내부 함수 호출

print_hello()  # 외부 함수 호출
"""
----- 코드 흐름 및 설명 -----

(1) def print_hello():
        hello = 'Hello, world!'
    - 프로그램이 시작되면, 외부 함수 print_hello()가 호출됩니다. 이제 print_hello() 함수 안의 코드가 실행됩니다.
    - hello = 'Hello, world!'를 실행하여 지역 변수 hello를 선언합니다. hello는 print_hello() 함수 내부에서만 접근할 수 있는 변수입니다.

(2) def print_message():
        print(hello)
    - print_message()라는 내부 함수가 정의되나, 아직 실행되지 않았습니다.

(3) print_message()
    - print_message()가 호출됩니다. 호출 시, 내부 함수 print_message()가 실행됩니다
    - print(hello) 실행: 내부 함수가 외부 함수에서 정의된 hello 변수를 출력하며, 출력 내용은 'Hello, world!'입니다.

(4) print_hello()
    - 외부 함수를 호출합니다.
    - 내부 함수 실행이 끝나면, 외부 함수 print_hello()의 작업도 모두 종료됩니다.

(5) 설명
    함수 print_hello 안에서 다시 def로 함수 print_message를 만들었습니다. 그리고 print_hello 안에서 print_message()처럼 함수를 호출했습니다. 
    하지만 아직 함수를 정의만 한 상태이므로 아무것도 출력되지 않습니다.
    두 함수가 실제로 동작하려면 바깥쪽에 있는 print_hello를 호출해주어야 합니다. 즉, print_hello > print_message 순으로 실행됩니다.
"""




### 33.2.1  지역 변수의 범위
"""
지금까지 바깥쪽 함수의 지역 변수를 안쪽 함수에서 사용해봤습니다. 그럼 바깥쪽 함수의 지역 변수를 안쪽 함수에서 변경하면 어떻게 될까요?
다음과 같이 안쪽 함수 B에서 바깥쪽 함수 A의 지역 변수 x를 변경해봅니다.
실행을 해보면 20이 나와야 할 것 같은데 10이 나왔습니다. 
왜냐하면 겉으로 보기에는 바깥쪽 함수 A의 지역 변수 x를 변경하는 것 같지만, 실제로는 안쪽 함수 B에서 이름이 같은 지역 변수 x를 새로 만들게 됩니다. 
즉, 파이썬에서는 함수에서 변수를 만들면 항상 현재 함수의 지역 변수가 됩니다.

"""
def A():
    x = 10        # A의 지역 변수 x
    def B():
        x = 20    # x에 20 할당

    B()
    print(x)      # A의 지역 변수 x 출력

A()


"""
현재 함수의 바깥쪽에 있는 지역 변수의 값을 변경하려면 nonlocal 키워드를 사용해야 합니다. 다음과 같이 함수 안에서 nonlocal에 지역 변수의 이름을 지정해줍니다. 
이제 함수 B에서 함수 A의 지역 변수 x를 변경할 수 있습니다. 즉, nonlocal은 현재 함수의 지역 변수가 아니라는 뜻이며 바깥쪽 함수의 지역 변수를 사용합니다.

nonlocal 지역변수
"""
def A():
    x = 10        # A의 지역 변수 x
    def B():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20        # A의 지역 변수 x에 20 할당

    B()
    print(x)      # A의 지역 변수 x 출력

A()




### 33.2.3  nonlocal이 변수를 찾는 순서
"""
nonlocal은 현재 함수의 바깥쪽에 있는 지역 변수를 찾을 때 가장 가까운 함수부터 먼저 찾습니다. 이번에는 함수의 단계를 A, B, C로 만들었습니다.
"""
def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()

A()
"""
함수 C에서 nonlocal x를 사용하면 바깥쪽에 있는 함수 B의 지역 변수 x = 20을 사용하게 됩니다.
따라서 x = x + 30은 50이 나옵니다. 그리고 함수 C에서 nonlocal y를 사용하면 바깥쪽에 있는 함수의 지역 변수 y를 사용해야 하는데 함수 B에는 y가 없습니다.
이때는 한 단계 더 바깥으로 나가서 함수 A의 지역 변수 y를 사용하게 됩니다. 
즉, 가까운 함수부터 지역 변수를 찾고, 지역 변수가 없으면 계속 바깥쪽으로 나가서 찾습니다.

실무에서는 이렇게 여러 단계로 함수를 만들 일은 거의 없습니다. 그리고 함수마다 이름이 같은 변수를 사용하기 보다는 변수 이름을 다르게 짓는 것이 좋습니다.
"""




### 33.2.4  global로 전역 변수 사용하기
"""
특히, 함수가 몇 단계든 상관없이 global 키워드를 사용하면 무조건 전역 변수를 사용하게 됩니다.
함수 C에서 global x를 사용하면 전역 변수 x = 1을 사용하게 됩니다. 따라서 x = x + 30은 31이 나옵니다.
"""
x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x = x + 30
            print(x)
        C()
    B()

A()


"""
파이썬에서 global을 제공하지만 함수에서 값을 주고받을 때는 매개변수와 반환값을 사용하는 것이 좋습니다.
특히 전역 변수는 코드가 복잡해졌을 때 변수의 값을 어디서 바꾸는지 알기가 힘듭니다. 
따라서 전역 변수는 가급적이면 사용하지 않는 것을 권장합니다.
"""
