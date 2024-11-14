## 30.6 연습문제
"""
가장 높은 점수를 구하는 함수 만들기

다음 소스 코드를 완성하여 가장 높은 점수가 출력되게 만드세요.

korean, english, mathematics, science = 100, 86, 81, 91

_____________________________________________
...
_____________________________________________

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)

- 실행 결과 - 
높은 점수 : 100
높은 점수 : 91
"""

def get_max_score(*args) :
    return max(args)

korean, english, mathematics, science = 100, 86, 81, 91

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수 : ', max_score)

max_score = get_max_score(english, science)
print('높은 점수 : ', max_score)

"""
----- 코드 흐름 및 설명 -----

(1) def get_max_score(*args) :
    - 함수를 정의합니다. 이 함수는 여러 개의 위치 인수를 받을 수 있는 *args를 사용하여 입력받은 모든 점수를 튜플(args)로 저장합니다.

(2) return max(args)
    - max 함수는 args 튜플을 왼쪽부터 순차적으로 비교하고, 각 값을 비교하면서 현재까지 확인한 값 중 가장 큰 값을 추적합니다. 마지막 값까지 확인한 후, 가장 큰 값을 찾아 반환합니다.
    - args 튜플에서 max 함수를 사용하여 가장 큰 값을 반환합니다. 이로써 함수는 입력된 점수 중 최고 점수를 반환하게 됩니다.
    - max() 함수는 내장함수로 리스트, 튜플, 문자열, 또는 여러 인수 중에서 가장 큰 값을 쉽게 찾아주는 기능을 제공합니다.

(3) korean, english, mathematics, science = 100, 86, 81, 91
    - 각각의 변수에 점수를 할당합니다.

(4) max_score = get_max_score(korean, english, mathematics, science)
    print('높은 점수 : ', max_score)
    - 함수를 호출하면서 각각의 변수들을 위치 인수로 전달합니다. 함수는 가장 큰 값인 100을 반환하고 이 값을 max_score 변수에 저장합니다.
    - print() 함수는 변수의 값을 출력합니다.

(5) max_score = get_max_score(english, science)
    print('높은 점수 : ', max_score)
    - 함수를 호출하면서 2개의 변수를 위치 인수로 전달합니다. 함수는 가장 큰 값이 91을 반환하고 이 값을 max_score 변수에 저장합니다.
    - print() 함수는 변수의 값을 출력합니다.
"""
