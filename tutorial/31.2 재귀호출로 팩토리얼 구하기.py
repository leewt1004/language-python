## 31.2 재귀호출로 팩토리얼 구하기
"""
이번에는 재귀호출을 사용하여 팩토리얼을 구현해보겠습니다. 팩토리얼은 1부터 n까지 양의 정수를 차례대로 곱한 값이며 !(느낌표) 기호로 표기합니다.
예를 들어 5!은 5 * 4 * 3 * 2 * 1이며 결과는 120입니다.
"""
def factorial(n) :
    if n == 1 :                 # n이 1일 때
        return 1                # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n-1)   # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함

print(factorial(5))
"""
----- 코드 흐름 및 설명 -----

(1) def factorial(n) :
    - 함수를 정의하고 n이라는 파라미터를 입력받음

(2) if n == 1 :
        return 1
    - n == 1인 경우, 함수는 1을 반환하고 종료
    - 재귀 함수의 반환값은 항상 *** 바로 직전의 호출된 함수로 반환 *** ---> 재귀 호출을 멈추고 반환값을 거슬러 올라가기 시작

(3) return n * factorial(n-1)
    - n이 1이 아닌 경우 재귀 호출 실행
    - 현재 숫자 n과 factorial(n-1)의 값을 곱한 결과를 반환(n이 1이 될 때까지)
    - 반환값은 바로 직전 호출로 전달되며 최종 계산이 이루어짐

(4) print(factorial(5))
    - 함수를 호출하여 계산된 결과를 출력(재귀 함수는 스택구조이므로 거꾸로 출력)

(5) 실행 흐름
    - factorial(5) → factorial(4) → factorial(3) → factorial(2) → factorial(1)

(6) 반환 값
    - factorial(1) → 1
    - factorial(2) → 2 * 1 = 2
    - factorial(3) → 3 * 2 = 6
    - factorial(4) → 4 * 6 = 24
    - factorial(5) → 5 * 24 = 120

설명
    먼저 factorial 함수를 만들 때 매개변수 n을 지정해줍니다.
    팩토리얼은 1부터 n까지의 곱을 구하는 문제인데 여기서는 n부터 역순으로 1씩 감소하면서 재귀호출을 하고 n이 1이 되었을 때 재귀호출을 중단합니다.

    factorial 함수의 핵심은 반환값 부분입니다.
    계산 결과가 즉시 구해지는 것이 아니라 재귀호출로 n - 1을 계속 전달하다가 
    n이 1일 때 비로소 1을 반환하면서 n과 곱하고 다시 결괏값을 반환합니다. 
    그 뒤 n과 반환된 결괏값을 곱하여 다시 반환하는 과정을 반복합니다.

    factorial(5)를 호출해서 n이 1이 될 때까지 재귀호출을 합니다.
    이제 if n == 1:을 만나서 factorial 함수가 1을 반환합니다.
    그 뒤 1과 2를 곱해서 2를 반환하고, 3과 2를 곱해서 6을 반환하고, 4와 6을 곱해서 24를 반환하고, 5와 24를 곱해서 120을 반환하게 됩니다.
"""




"""
지금까지 함수의 재귀호출에 대해 배웠습니다. 재귀호출로 'Hello, world!'를 출력하는 부분은 크게 어렵지 않았지만 팩토리얼을 구할 때는 반환값과 매개변수로 계산하는 부분이 좀 어려웠습니다.
초보자들은 재귀호출 함수를 읽을 수 있을 정도만 되어도 제대로 공부한 것입니다.
알고리즘을 재귀호출로 만드는 일은 많은 공부와 연습이 필요합니다.
따라서 하루 아침에 습득할 수 있는 내용이 아니므로 당장 이해가 되지 않는다고 해서 걱정할 필요는 없습니다.
"""
