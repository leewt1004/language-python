## 22.6 리스트에 map 사용하기
"""
map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니다(map은 원본 리스트를 변경하지 않고 새 리스트를 생성합니다).

list(map(함수, 리스트))
tuple(map(함수, 튜플))
"""
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)) :
    a[i] = int(a[i])
print(a)

""" 매번 for 반복문으로 반복하면서 요소를 변환하려니 조금 번거롭습니다. 이때는 map을 사용하면 편리합니다. """
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

"""
사실 map에는 리스트뿐만 아니라 모든 반복 가능한 객체를 넣을 수 있습니다.
이번에는 range를 사용해서 숫자를 만든 뒤 숫자를 문자열로 변환해보겠습니다.
"""
a = list(map(str, range(10)))
print(a)


### 22.6.1  input().split()과 map
""" input().split()을 사용한 뒤에 변수 한 개에 저장해보면 리스트인지 확인할 수 있습니다. """
a = input().split()
print(a)        # 10 20을 입력하면 ['10', '20']처럼 문자열 두 개가 들어있는 리스트가 만들어집니다.

""" map을 사용해서 정수로 변환해봅니다. """
a = map(int, input().split())
print(list(a))

""" 이 리스트 [10, 20]을 변수 두 개에 저장하면 지금까지 사용한 a, b = map(int, input().split())와 같은 동작이 됩니다. """
a, b = map(int, input().split())
print(a)
print(b)

""" , b = map(int, input().split())을 풀어서 쓰면 다음과 같은 코드가 됩니다. """
x = input().split()     # input().split()의 결과는 문자열 리스트
m = map(int, x)         # 리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = m                # 맵 객체는 변수 여러 개에 저장할 수 있음
print(a)
print(b)


"""
파이썬은 여러 가지 함수와 객체를 조합해서 결과를 만들어냅니다.
파이썬을 처음 접할 때는 이해하기가 쉽지 않은 부분이니 이런 것도 있구나 하고 넘어가도 됩니다.
"""
