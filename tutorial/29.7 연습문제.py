## 29.3 연습문제
"""
몫과 나머지를 구하는 함수 만들기

다음 소스 코드를 완성하여 x를 y로 나누었을 때의 몫과 나머지를 출력되게 만드세요.

x = 10
y = 3

____________________
____________________

quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))

- 실행 결과 -
몫 : 3, 나머지 : 1
"""

def remainder(a, b) : 
    c = a % b
    return c

def quotient(a, b) :
    c = a // b                              # 몫을 정수로 계산
    d = remainder(a, b)
    print(f'몫 : {c}, 나머지 : {d}')        # 한 줄로 출력

x = 10
y = 3

quotient(x,y)
"""
--- 직접 수행한 코드 ---

remainder 함수
(1) def remainder(a, b):
    - remainder라는 함수를 정의합니다. 이 함수는 두 개의 매개변수 a와 b를 입력받습니다. remainder 함수의 역할은 두 숫자의 나머지를 계산하여 반환하는 것입니다.

(2) c = a % b
    - % 연산자를 사용하여 a를 b로 나눈 나머지를 계산합니다.

(3) return c
    - c의 값을 remainder 함수 호출한 곳으로 반환


quotient 함수
(1) def quotient(a, b):
    - quotient라는 또 다른 함수를 정의합니다. 이 함수도 두 개의 매개변수 a와 b를 입력받습니다. quotient 함수는 두 숫자의 몫을 계산하고, 나머지를 출력하는 역할을 합니다.

(2) c = a // b
    - // 연산자를 사용하여 a를 b로 나눈 정수 몫을 계산합니다.
        · /(일반 나눗셈) : 항상 실수(float) 결과를 반환합니다.
        · //(몫 나눗셈) : 정수 몫을 반환합니다(소수점 이하 버림)

(3) d = remainder(a, b)
    - quotient 함수 내부에서 remainder(a, b) 함수를 호출하여 나머지 값을 계산합니다.

(4) print(f'몫 : {c}, 나머지 : {d}')
    - print 함수로 문자열을 출력합니다. f 문자열 포매팅을 사용하여 c와 d 값을 포함한 메시지를 한 줄로 출력합니다.

    
변수 및 함수 호출
(1) x = 10
    - 변수 x에 10을 저장합니다. 이 값은 나중에 quotient 함수에 전달할 첫 번째 값입니다.

(2) y = 3
    - 변수 y에 3을 저장합니다. 이 값은 quotient 함수에 전달할 두 번째 값입니다.

(3) quotient(x, y)
    - quotient 함수를 호출하면서 x와 y를 인수로 전달합니다. 여기서 a = 10과 b = 3으로 설정하여 quotient 함수가 실행됩니다.
    - quotient 함수는 c = a // b로 몫을 계산하고, d = remainder(a, b)로 나머지를 계산한 후 print로 몫 : 3, 나머지 : 1을 출력합니다.
"""




x = 10
y = 3

def get_quotient_remainder(a, b):
    return a // b, a % b

quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))
"""
--- 정답 코드 ---

변수 선언
(1) x = 10
    - 변수 x에 숫자 10을 저장합니다. 이 값은 함수에 전달할 첫 번째 값입니다.

(2) y = 3
    - 변수 y에 숫자 3을 저장합니다. 이 값은 함수에 전달할 두 번째 값입니다.


함수 선언
(1) def get_quotient_remainder(a, b):
        return a // b, a % b
    - get_quotient_remainder라는 함수를 정의합니다. 이 함수는 두 개의 매개변수 a와 b를 입력받습니다. 이 함수의 역할은 두 숫자의 몫과 나머지를 동시에 계산하여 반환하는 것입니다.
    - return 키워드를 사용해 두 값을 동시에 반환합니다. a // b는 a를 b로 나눈 정수 몫을 계산하고, a % b는 나머지를 계산합니다.


함수 호출
(1) quotient, remainder = get_quotient_remainder(x, y)
    - get_quotient_remainder(x, y) 함수를 호출합니다. 이때 x와 y는 각각 10과 3으로 전달되어 a와 b가 됩니다. 함수가 반환한 두 값 (3, 1)을 각각 quotient와 remainder에 저장합니다.


몫과 나머지 출력
(1) print('몫: {0}, 나머지: {1}'.format(quotient, remainder))
    - print 함수로 몫과 나머지를 출력합니다.
    - .format() 메서드를 사용하여 quotient와 remainder의 값을 {0}과 {1} 자리에 넣습니다.
    - quotient = 3이고 remainder = 1이므로 최종적으로 몫: 3, 나머지: 1이 출력됩니다.
"""




"""
--- 답지와 직접 수행한 코드의 차이점 ---

함수 개수와 반환 방식
(1) 답지 코드
    - get_quotient_remainder라는 하나의 함수에서 몫과 나머지를 동시에 계산하여 두 개의 값을 동시에 반환합니다. 이렇게 하면 함수 호출 한 번으로 두 결과를 얻을 수 있습니다.
(2) 수행 코드
    - quotient와 remainder라는 두 개의 함수를 사용합니다. quotient 함수는 몫을 계산하고, remainder 함수는 나머지를 계산합니다. 
    - 또한 quotient 함수 내부에서 remainder 함수를 호출하고, 결과를 print로 출력합니다. 함수가 값을 반환하기보다는 print로 화면에 표시하는 구조입니다.


출력 위치와 방식
(1) 답지 코드
    - 함수 자체는 몫과 나머지를 계산하여 반환만 하고, 호출한 곳에서 그 값을 print로 출력합니다. 함수와 출력이 분리되어 있어 함수가 순수하게 계산만 수행합니다.
(2) 수행 코드
    - quotient 함수가 몫과 나머지를 직접 print하여 출력하는 방식입니다. 이 경우 함수가 호출될 때마다 항상 출력이 이루어지며, 다른 곳에서 호출 시 출력 조정이 어렵습니다.


유연성과 재사용성
(1) 답지 코드
    - 함수가 두 값을 반환하므로, 반환된 값을 다양한 방식으로 활용할 수 있습니다. 예를 들어, 출력하지 않고 다른 계산에 활용하거나, 필요할 때만 출력할 수 있어 유연성이 높습니다.
(2) 수행 코드
    - quotient 함수는 내부에서 무조건 print로 결과를 출력하므로, 다른 용도로 반환 값을 재사용하거나 수정하기 어려운 구조입니다.


함수 호출 횟수
(1) 답지 코드
    - 함수를 한 번만 호출하여 동시에 몫과 나머지를 얻기 때문에 코드가 간결하고 효율적입니다.
(2) 수행 코드
    - quotient 함수가 내부에서 remainder 함수를 호출하므로, 두 함수 호출이 필요합니다. 이는 구조적으로 약간 더 복잡합니다.


요약
(1) 답지 코드
    - 하나의 함수로 두 값을 반환하여 함수 호출 한 번으로 필요한 결과를 얻습니다. 출력은 함수 외부에서 조정할 수 있어 유연하고 재사용성이 높습니다.
(2) 수행 코드
    - 두 함수로 나누어 각각 몫과 나머지를 계산하며, print를 사용해 함수 내부에서 결과를 직접 출력하므로 재사용성이 떨어지고 출력 조정이 어렵습니다.
"""
