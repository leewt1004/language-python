## 16.2 for와 range 응용하기
"""  range의 다양한 기능을 활용하여 for 반복문을 사용해보겠습니다. """


### 16.2.1 시작하는 숫자와 끝나는 숫자 지정하기
"""
range에 횟수만 지정하면 숫자가 0부터 시작하지만, 다음과 같이 시작하는 숫자와 끝나는 숫자를 지정해서 반복할 수도 있습니다.

for 변수 in range(시작, 끝):
"""
for i in range(5, 12) : # 5부터 11까지 반복
    print('Hello, world!', i)


### 16.2.2 증가폭 사용하기
"""
range는 증가폭을 지정해서 해당 값만큼 숫자를 증가시킬 수 있습니다.

for 변수 in range(시작, 끝, 증가폭):
"""
for i in range(0, 10, 2) : # 0부터 8까지 2씩 증가
    print('Hello, world!', i)


### 16.2.3 숫자를 감소시키기
""" 
range는 숫자가 증가하는 기본 값이 양수 1이기 때문에 
시작하는 숫자를 큰 숫자로 지정하고 끝나는 숫자를 작은 숫자로 지정해서 실행해봐도 아무것도 출력되지 않습니다.
range에 증가폭을 음수로 지정하면 숫자가 감소합니다.
"""
for i in range(0, 10, -1) : # 10에서 1까지 1씩 감소
    print('Hello, world!', i)

"""
증가폭을 음수로 지정하는 방법 말고도 reversed를 사용하면 숫자의 순서를 반대로 뒤집을 수 있습니다.
for 변수 in reversed(range(횟수))
for 변수 in reversed(range(시작, 끝))
for 변수 in reversed(range(시작, 끝, 증가폭))
"""
for i in reversed(range(10)) : # range에 reversed를 사용하여 숫자의 순서를 반대로 뒤집음
    print('Hello, world!', i) # 9 부터 0까지 10번 반복


#### 참고 : 반복문의 변수 i를 변경할 수 있을까?
""" for와 range로 반복하면서 변수 i를 변경하면 어떻게 될까요? """
for i in range(10) :  # 0부터 9까지 반복
    print(i, end = ' ') # i를 출력하고 줄바꿈 대신 공백을 추가
    i = 10 # i에 10을 할당하지만, 반복문에 영향을 주지 않음 0 1 2 3 4 5 6 7 8 9


### 16.2.4 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요 : '))

for i in range(count) : 
    print('Hello, world!', i)
"""
먼저 input으로 입력 값을 받아서 count 변수에 저장합니다(이때 반드시 int를 사용하여 input에서 나온 문자열을 정수로 변환해줍니다).
그리고 반복문에서는 for i in range(count):와 같이 range에 count를 넣어주면 입력받은 숫자만큼 반복됩니다.
"""
