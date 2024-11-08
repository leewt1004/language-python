## 17.5 연습문제
"""
변수 두 개를 다르게 반복하기
다음 소스 코드를 완성하여 정수 2 5, 4 4, 8 3, 16 2, 32 1이 각 줄에 출력되게 만드세요.
while에 조건식은 두개 지정하고, 두 변수를 모두 변화시켜야 합니다.
i = 2
j = 5

(1)__________or__________        
    print(i, j)
    (2)_____
    (3)_____

- 실행 결과 -
2 5
4 4
8 3
16 2
32 1
"""

i = 2 # 변수 i에 2할당
j = 5 # 변수 j에 5할당

print(i, j) # 초깃값 출력

while i <= 32 or j >= 1 : # i가 32이하이거나 j가 1이상일 때 반복
    i *= 2 # 변화식 : i의 값을 2배로 만듬
    j -= 1 # 변화식 : j의 값을 1씩 감소
    print(i, j) # 각 반복에서 i와 j의 현재 값을 출력


"""
반복 과정 자세히 살펴보기
각 단계에서 i와 j의 값이 어떻게 변하고, while 조건이 어떻게 참인지 확인해 보겠습니다.

초기 출력: (2, 5)

첫 번째 반복:
i *= 2로 인해 i는 4가 됩니다.
j -= 1로 인해 j는 4가 됩니다.
print(i, j)는 (4, 4)를 출력합니다.

두 번째 반복:
i *= 2로 인해 i는 8이 됩니다.
j -= 1로 인해 j는 3이 됩니다.
print(i, j)는 (8, 3)을 출력합니다.

세 번째 반복:
i *= 2로 인해 i는 16이 됩니다.
j -= 1로 인해 j는 2가 됩니다.
print(i, j)는 (16, 2)를 출력합니다.

네 번째 반복:
i *= 2로 인해 i는 32가 됩니다.
j -= 1로 인해 j는 1이 됩니다.
print(i, j)는 (32, 1)을 출력합니다.

다섯 번째 반복:
i *= 2로 인해 i는 64가 됩니다.
j -= 1로 인해 j는 0이 됩니다.
print(i, j)는 (64, 0)을 출력합니다.

조건 확인 및 반복 종료:
i는 64, j는 0이 됩니다.
i <= 32는 거짓이 되고, j >= 1도 거짓이 됩니다.
두 조건이 모두 거짓이므로 while 반복이 종료됩니다.
"""
