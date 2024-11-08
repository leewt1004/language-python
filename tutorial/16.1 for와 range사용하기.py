# Unit 16. for 반복문으로 Hello, world! 100번 출력하기
"""
대부분의 프로그래밍 언어에서는 반복되는 작업을 간단하게 처리하기 위해 반복문이라는 기능을 제공해줍니다.
반복문은 반복 횟수, 반복 및 정지 조건을 자유자재로 제어할 수 있습니다.
"""


## 16.1 for와 range사용하기
"""
for 반복문은 range에 반복할 횟수를 지정하고 앞에 in과 변수를 입력합니다.
그리고 끝에 :(콜론)을 붙인 뒤 다음 줄에 반복할 코드를 넣습니다.

for 변수 in range(횟수) :
    반복할 코드
"""
for i in range(100) :
    print('Hello, world!')
"""
for 반복문은 range에서 in으로 숫자를 하나하나 꺼내서 반복하는 방식입니다. 그리고 for는 숫자를 꺼낼 때마다 코드를 실행합니다.
range(100)과 같이 지정하면 0부터 99까지 숫자 100개를 생성합니다. 그리고 for는 in으로 숫자를 하나씩 꺼내서 변수 i에 저장하고, print를 실행합니다. 
즉, range(100)에서 숫자를 100번 꺼내면서 print를 실행하므로 'Hello, world!'가 100번 출력되는 것이죠.
이처럼 for 반복문은 반복 횟수가 정해져 있을 때 주로 사용합니다.
for 변수 in range(횟수) → 반복할 코드로 순환하는 것을 루프(loop)라고 부릅니다.
"""


### 16.1.1 반복문에서 변수의 변화 알아보기
for i in range(100) :
    print('Hello, world!', i)


#### 참고 : 반복문의 변수 i
""" 변수 i를 루프 인덱스라고 부르며 index의 첫 머리글자를 따서 i를 주로 사용합니다. """
