# Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기
"""
지금까지 간단하게 'Hello, world!'를 출력하는 함수와 두 수를 더하는 함수를 만들어보았습니다. 파이썬에서는 함수를 좀 더 편리하게 사용할 수 있도록 다양한 기능을 제공합니다.
이번에는 함수에서 위치 인수, 키워드 인수를 사용하는 방법과 리스트, 딕셔너리 언패킹(unpacking)을 활용하는 방법을 알아보겠습니다.
"""




## 30.1 위치 인수와 리스트 언패킹 사용하기
""" 함수에 인수를 순서대로 넣는 방식을 위치 인수(positional argument)라고 합니다. 즉, 인수의 위치가 정해져 있습니다. """
print(10, 20, 30)           # 10, 20, 30을 위치 인수라고 한다. / 출력 : 10 20 30




### 30.1.1  위치 인수를 사용하는 함수를 만들고 호출하기
"""
숫자 세 개를 각 줄에 출력하는 함수를 만들어보겠습니다.
"""
def print_numbers(a, b, c) :
    print(a)
    print(b)
    print(c)

print_numbers(10, 20, 30)
"""
(1) def print_numbers(a, b, c) :
    - print_numbers라는 함수를 정의합니다. 이 함수는 세 개의 매개변수 a, b, c를 입력받습니다.

(2) print(a), print(b), print(c)
    - 매개변수 a, b, c의 값을 출력합니다.

(3) print_numbers(10, 20, 30)
    - print_numbers 함수를 호출하면서 10, 20, 30을 인수로 전달합니다.
"""




### 30.1.2  언패킹 사용하기
"""
# 이렇게 인수를 순서대로 넣을 때는 리스트나 튜플을 사용할 수도 있습니다. 다음과 같이 리스트 또는 튜플 앞에 *(애스터리스크)를 붙여서 함수에 넣어주면 됩니다.

# 함수(*리스트)
# 함수(*튜플)
# """
def print_numbers(a, b, c) :
    print(a)
    print(b)
    print(c)

x = [10, 20, 30]
print_numbers(*x)
"""
(1) def print_numbers(a, b, c) :
    - print_numbers라는 함수를 정의합니다. 이 함수는 세 개의 매개변수 a, b, c를 입력받습니다.

(2) print(a), print(b), print(c)
    - 매개변수 a, b, c의 값을 출력합니다.

(3) x = [10, 20, 30]
    - 10, 20, 30을 요소로 가지는 리스트 x를 생성합니다.

(4) print_numbers(10, 20, 30)
    - 함수를 호출하면서 리스트 x의 요소 10, 20, 30을 각각 함수 print_numbers의 인수 a, b, c로 전달합니다.
"""


""" 리스트 변수 대신 리스트 앞에 바로 *를 붙여도 동작은 같습니다. """
def print_numbers(a, b, c) :
    print(a)
    print(b)
    print(c)

print_numbers(*[10, 20, 30])
"""
(1) def print_numbers(a, b, c) :
    - print_numbers라는 함수를 정의합니다. 이 함수는 세 개의 매개변수 a, b, c를 입력받습니다.

(2) print(a), print(b), print(c)
    - 매개변수 a, b, c의 값을 출력합니다.

(3) print_numbers(10, 20, 30)
    - 리스트 [10, 20, 30]의 요소를 각각 언패킹하여 함수 print_numbers의 인수 a, b, c에 전달합니다.
"""
"""
리스트 x를 넣고 *만 붙였는데도 숫자가 각 줄에 출력되었습니다. 
즉, 리스트(튜플) 앞에 *를 붙이면 언패킹(unpacking)이 되어서 print_numbers(10, 20, 30)과 똑같은 동작이 됩니다. 말 그대로 리스트의 포장을 푼다는 뜻입니다.

단, 이때 함수의 매개변수 개수와 리스트의 요소 개수는 같아야 합니다.(개수가 틀리면 error 발생)
"""




### 30.1.3  가변 인수 함수 만들기
"""
그럼 위치 인수와 리스트 언패킹은 어디에 사용할까요? 이 기능들은 인수의 개수가 정해지지 않은 가변 인수(variable argument)에 사용합니다.
즉, 같은 함수에 인수 한 개를 넣을 수도 있고, 열 개를 넣을 수도 있습니다. 또는, 인수를 넣지 않을 수도 있습니다.
다음과 같이 가변 인수 함수는 매개변수 앞에 *를 붙여서 만듭니다.

def 함수이름(*매개변수):
    코드
"""

"""
숫자 여러 개를 받고, 숫자를 각 줄에 출력하는 함수를 만들어보겠습니다. 다음과 같이 함수를 만들 때 괄호 안에 *args와 같이 매개변수 앞에 *를 붙입니다.
그리고 함수 안에서는 for로 args를 반복하면서 print로 값을 출력합니다.
매개변수 이름은 원하는 대로 지어도 되지만 관례적으로 arguments를 줄여서 args로 사용합니다. 특히 이 args는 튜플이라서 for로 반복할 수 있습니다.
그럼 print_numbers 함수에 숫자를 넣어서 호출해봅니다. 숫자를 한 개 넣으면 한 개 출력되고, 네 개 넣으면 네 개가 출력됩니다. 즉, 넣은 숫자 개수만큼 출력됩니다.
"""
def print_numbers(*args) :
    for arg in args :
        print(arg)
print_numbers(10)
print_numbers(10, 20, 30, 40)
"""
(1) def print_numbers(a, b, c) :
    - print_numbers라는 함수를 정의합니다. *args는 여러 개의 인수를 튜플 형태로 받을 수 있도록 합니다.

(2)  for arg in args:
        print(arg)
    - for 루프를 사용하여 args 튜플의 각 요소(arg)를 반복하며 출력합니다.
    - 함수에서 *를 사용하여 (*변수이름)처럼 쓰면 변수 이름에 상관없이 전달된 여러 인수들이 무조건 튜플 형태로 묶여서 함수 내에서 사용됩니다.

(3) print_numbers(10)
    - print_numbers(10)을 호출하여 10을 인수로 전달합니다. args는 (10,)이 되고, 10이 출력됩니다.

(3) print_numbers(10, 20, 30, 40)
    - print_numbers(10, 20, 30, 40)을 호출하여 10, 20, 30, 40을 인수로 전달합니다. args는 (10, 20, 30, 40)이 되고, 각 숫자가 한 줄씩 출력됩니다.
"""


""" 함수에 인수 여러 개를 직접 넣어도 되고, 리스트(튜플) 언패킹을 사용해도 됩니다. 다음과 같이 숫자가 들어있는 리스트를 만들고 앞에 *를 붙여서 넣어봅니다. """
def print_numbers(*args) :
    for arg in args :
        print(arg)

x = [10]
print_numbers(*x)

y = [10, 20, 30, 40]
print_numbers(*y)
"""
(1) def print_numbers(a, b, c) :
    - print_numbers라는 함수를 정의합니다. *args는 여러 개의 인수를 튜플 형태로 받을 수 있도록 합니다.

(2)  for arg in args:
        print(arg)
    - for 루프를 사용하여 args 튜플의 각 요소(arg)를 반복하며 출력합니다.

(3) x = [10]
    print_numbers(*x)
    - x라는 리스트에 10이라는 값 하나를 담습니다. 즉, x는 [10]이라는 리스트가 됩니다.
    - *x는 리스트 x의 요소를 언패킹하여 함수에 전달합니다. 여기서는 x에 [10]이라는 하나의 값만 있기 때문에, print_numbers(10)과 동일한 호출이 됩니다.
    - 함수 내에서 args는 (10,)이라는 튜플이 되고, 반복문이 10을 출력하게 됩니다.

(3) y = [10, 20, 30, 40]
    print_numbers(*y)
    - y라는 리스트에 값 10, 20, 30, 40이 차례로 들어 있습니다. 즉, y는 [10, 20, 30, 40]이라는 리스트가 됩니다.
    - *y는 리스트 y의 요소를 언패킹하여 함수에 전달합니다. 여기서는 y에 네 개의 값이 있으므로, print_numbers(10, 20, 30, 40)과 동일한 호출이 됩니다.
    - 함수 내에서 args는 (10, 20, 30, 40)이라는 튜플이 되고, 반복문이 10, 20, 30, 40을 각각 출력하게 됩니다.

(4) 설명
    *x와 *y는 각각 리스트 x와 y의 요소들을 개별 인수로 분리하여 함수에 전달합니다.
    print_numbers 함수는 전달된 인수들을 튜플 형태로 묶어서 받기 때문에, args는 각각 (10,)과 (10, 20, 30, 40)이라는 튜플로 저장됩니다.
    이처럼 함수를 만들 때 def print_numbers(*args):와 같이 매개변수에 *를 붙여주면 가변 인수 함수를 만들 수 있습니다.
    그리고 이런 함수를 호출할 때는 인수를 각각 넣거나, 리스트(튜플) 언패킹을 사용하면 됩니다.
"""




#### 참고 : 고정 인수와 가변 인수를 함께 사용하기
"""
고정 인수와 가변 인수를 함께 사용할 때는 다음과 같이 고정 매개변수를 먼저 지정하고, 그 다음 매개변수에 *를 붙여주면 됩니다.
단, 이때 def print_numbers(*args, a):처럼 *args가 고정 매개변수보다 앞쪽에 오면 안 됩니다. 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야 합니다.
"""
def print_numbers(a, *args) : 
    print(a)
    print(args)

print_numbers(1)
print_numbers(1, 10, 20)
print_numbers(*[10, 20, 30])
"""
고정 인수와 가변 인수는 함수에 값을 전달하는 두 가지 주요 방식입니다.

(1) 고정 인수 (Positional or Fixed Argument)
    - 고정 인수는 정해진 수의 인수만 받는 함수에서 사용하는 인수입니다. 함수의 매개변수 개수에 맞춰 정확히 그 수만큼 인수를 전달해야 합니다. 예를 들어, 함수가 a와 b 두 개의 매개변수를 갖고 있다면, 두 개의 인수를 전달해야 합니다.

def add(a, b):
    return a + b
add(10, 20)  # 여기서는 10과 20이라는 두 개의 고정 인수를 전달합니다.

    - add 함수는 매개변수 a와 b를 사용하므로, 이 함수를 호출할 때 항상 두 개의 인수를 전달해야 합니다.
    - 고정 인수는 함수가 받을 인수의 개수와 일치해야 하는 특징이 있습니다.


(2) 가변 인수 (Variable-length Argument)
    - 가변 인수는 정해지지 않은 수의 인수를 받을 수 있는 함수에서 사용하는 인수입니다. *args나 **kwargs를 사용하여 가변 인수를 받을 수 있습니다.

*args는 여러 개의 위치 인수를 튜플로 묶어서 받습니다.
**kwargs는 여러 개의 키워드 인수를 딕셔너리로 묶어서 받습니다.

def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(10, 20, 30)  # 여기서는 10, 20, 30이라는 세 개의 가변 인수를 전달합니다.
print_numbers(5)           # 가변 인수를 하나만 전달할 수도 있습니다.
print_numbers 함수는 가변 인수 *args를 사용하므로, 전달된 인수 개수와 상관없이 모든 값을 받아서 출력할 수 있습니다.

(4) 요약
    - 고정 인수: 함수가 받을 인수 개수가 정해져 있어, 그 개수만큼 정확히 전달해야 합니다.
    - 가변 인수: 함수가 받을 인수 개수가 정해져 있지 않으며, *args를 사용하면 여러 개의 위치 인수를, **kwargs를 사용하면 여러 개의 키워드 인수를 받을 수 있습니다.
    - 이렇게 고정 인수와 가변 인수를 활용하면, 함수가 다양한 상황에서 유연하게 작동하도록 만들 수 있습니다.
"""




##### 참고 : 함수(*args)
"""
함수에서 *를 사용하여 *args처럼 쓰면 변수 이름에 상관없이 전달된 여러 인수들이 무조건 튜플 형태로 묶여서 함수 내에서 사용됩니다.
*가 붙은 인수는 항상 튜플 형태로 묶인다는 특징을 가지고 있습니다.
변수 이름이 *args, *values, *anything 이든지 상관없이 *가 붙으면 전달된 인수들이 튜플러 저장되는 것입니다.

튜플로 저장되는 이유
안정성 : 튜플은 불변 자료형이기 때문에, 함수 내부에서 인수들이 변경되지 않도록 보장 합니다.
효율성 : 튜플은 리스트보다 메모리를 적게 사용하며 더 빠르게 처리됩니다. 불필요한 수정이 없으므로 튜플이 더 효율적입니다.

추가로 언패킹(unpacking)은 리스트, 튜플 같은 여러 값을 담고 있는 자료형을 하나씩 꺼내서 변수에 할당 하거나,
함수의 안수로 개별 값으로 전달하는 것을 말합니다.
*는 리스트나 튜플을 언패킹할 때 사용하고, **는 딕셔너리를 언패킹할 때 사용합니다.
"""
