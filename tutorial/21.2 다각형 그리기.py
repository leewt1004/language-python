## 21.2 다각형 그리기
""" 반복문을 사용해서 사각형을 그려보겠습니다. """
import turtle as t

t.shape('turtle')
for i in range(4) :         # 사각형이므로 4번 반복
    t.forward(100)
    t.right(90)

t.mainloop()


### 21.2.1  오각형 그리기
"""
그럼 오각형은 어떻게 그릴까요? 잠시 수학 시간에 배운 내용을 떠올려봅시다.
다각형에서 외각의 합은 항상 360도입니다.
그래서 사각형은 90도가 4개 들어있습니다( 90 * 4 = 360). 오각형은 360을 5로 나누면 외각을 구할 수 있습니다.
"""
import turtle as t

t.shape('turtle')
for i in range(5) :         # 오각형이므로 5번 반복
    t.forward(100)
    t.right(360 / 5)             # 360을 5로 나누어서 외각을 구함

t.mainloop()


### 21.2.2  다각형 그리기
""" 사용자가 숫자를 입력하면 해당 숫자에 해당하는 다각형을 그려보겠습니다. """
import turtle as t

n = int(input())            # 사용자의 입력을 받음
t.shape('turtle')
for i in range(n) :         # n번 반복
    t.forward(100)
    t.right(360 / n)        # 360을 n으로 나누어서 외각을 구함

t.mainloop()


### 21.2.3  다각형에 색칠하기
"""
다각형에 색을 칠해보겠습니다. 
여기서는 숫자 입력 과정은 생략하고 n에 6을 지정하여 육각형으로 만들겠습니다.
"""
import turtle as t
n = 6
t.shape('turtle')
t. color('red')         # 펜의 색을 빨간색으로 설정
t. begin_fill()         # 색칠할 영역 시작

for i in range(n) :     # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
t.end_fill()            # 색칠할 영역 끝

t.mainloop()


""" 공통된 부분을 일반화해서 원하는 결과를 얻어내는 과정이 프로그래밍이며 컴퓨테이셔널 씽킹입니다. """
