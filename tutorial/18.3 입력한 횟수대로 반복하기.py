## 18.3 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요 : '))
i = 0
while True :        # 무한 루프
    print(i)
    i += 1
    if i == count : # i가 입력받은 값과 같을 때
        break       # 반복문을 끝냄
"""
input으로 입력 값을 받아서 count 변수에 저장했습니다(이때 반드시 int를 사용하여 input에서 나온 문자열을 정수로 변환해줍니다).
그다음에 i에는 0을 할당하고, while에 True를 지정하여 무한 루프로 만듭니다.
반복문 안에서는 i의 값을 출력하고, 변화식에서는 i를 1씩 증가시킵니다. 그리고 i가 count의 값과 같으면 break를 실행합니다.
"""

### 18.3.1  입력한 숫자까지 홀수 출력하기
count = int(input('반복할 횟수를 입력하세요 : '))
for i in range(count + 1) :     # 0부터 증가하면서 count까지 반복(count + 1)
    if i % 2 == 0:              # i를 2로 나누었을 때 나머지가 0이면 짝수  
        continue                # 아래 코드를 실행하지 않고 건너뜀
    print(i)
