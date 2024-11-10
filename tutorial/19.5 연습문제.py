## 19.5 연습문제
"""
역삼각형 모양으로 별 출력하기
다음 소스 코드를 완성하여 역삼각형 모양으로 별이 출력되게 만드세요.
for i in range(5):
    for j in range(5):
        ____________________________
        ...
        ____________________________
    print()

- 실행 결과 - 
*****
 ****
  ***
   **
    *
"""
""" 첫 번째 코드 """
for i in range(5) :
    for j in range(5) :
        if j >= i :
            print("*", end="")
        else :
            print(" ", end="")
    print()

""" 두 번째 코드"""
for i in range(5):
    for j in range(5):
        if j < i:
            print(" ", end="")
        else:
            print("*", end="")
    print()
