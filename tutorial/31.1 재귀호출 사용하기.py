# Unit 31. 함수에서 재귀호출 사용하기
"""
함수 안에서 함수 자기자신을 호출하는 방식을 재귀호출(recursive call)이라고 합니다.
재귀호출은 일반적인 상황에서는 잘 사용하지 않지만 알고리즘을 구현할 때 매우 유용합니다(구현은 만들다와 같은 뜻입니다).
보통 알고리즘에 따라서 반복문으로 구현한 코드보다 재귀호출로 구현한 코드가 좀 더 직관적이고 이해하기 쉬운 경우가 많습니다.
이번에는 재귀호출을 사용하는 방법과 주의점을 알아보겠습니다.
참고로 재귀호출은 코드가 간단한 편이지만 머릿속으로 생각을 많이 해야 됩니다. 그래서 초보자들은 한 번에 이해가 되지 않을 수도 있습니다.
"""




## 31.1 재귀호출 사용하기
""" 먼저 간단한 재귀호출 함수를 만들어보겠습니다. """
# def hello() :
#     print('Hello, world!')
#     hello()

# hello()
"""
hello 함수 안에서 다시 hello 함수를 호출하고 있습니다.
소스 코드를 실행해보면 'Hello, world!' 문자열이 계속 출력되다가 에러가 발생합니다.
왜냐하면 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000으로 정해져 있어서 그렇습니다.
즉, hello 함수가 자기자신을 계속 호출하다가 최대 재귀 깊이를 초과하면 RecursionError가 발생합니다.
"""




### 31.1.1  재귀호출에 종료 조건 만들기
""" 재귀호출을 사용하려면 반드시 다음과 같이 종료 조건을 만들어주어야 합니다. """
def hello(count) :
    if count == 0 :
        return
    print('Hello, world!', count)

    count -= 1
    hello(count)

hello(5)
"""
----- 코드 흐름 및 설명 -----

(1) def hello(count) :
    - hello라는 함수를 정의합니다. 이 함수는 count라는 매개변수를 받아들입니다.

(2) if count == 0 :
        return
    - count가 0인지 확인한 후 count가 0이라면 함수는 종료(return) 됩니다.
    - return 뒤에 아무 값도 없으므로 None을 반환하며 종료됩니다.

(3) print('Hello, world!', count)
    - count가 0이 아니면 'Hello, world!'와 현재 count 값을 출력합니다.

(4) count -= 1
    - count 값을 1 감소시킵니다.

(5) hello(count)
    - 현재 감소된 count 값을 인수로 전달하여 hello 함수를 다시 호출합니다. 이로 인해 재귀적으로 함수가 호출되면서 "Hello, world!"를 계속 출력하게 됩니다.

(6) hello(5)
    - 함수를 처음 호출할 때 count에 5를 전달하고, 0이 될 때까지 함수가 반복적으로 호출되며 5에서 0까지 감소하면서 총 5번 출력됩니다.

(7) 설명
    먼저 hello 함수의 반복 횟수를 계산하기 위해 매개변수 count를 지정합니다.
    그리고 count가 0이면 hello 함수를 호출하지 않고 끝냅니다.
    만약 0이 아니면 'Hello, world!'를 출력하고, count의 값을 1씩 감소시킨 뒤 hello 함수를 호출할 때 넣어줍니다.
"""
