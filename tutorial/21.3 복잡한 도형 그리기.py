## 21.3 복잡한 도형 그리기
""" 이번에는 원을 그려보겠습니다. 터틀에서 원을 그릴 때는 circle을 사용합니다. """
import turtle as t

t.shape('turtle')
t.circle(120)       # 반지름이 120인 원을 그림

t.mainloop()


### 21.3.1  원을 반복해서 그리기
"""
for를 사용해서 원을 반복해서 그려보겠습니다.
speed는 거북이의 속도를 설정합니다. 속도는 다음과 같이 문자열 또는 숫자로 설정할 수 있습니다.
숫자는 0.5부터 10까지 설정할 수 있습니다. 

'fastest': 0
'fast': 10
'normal': 6
'slow': 3
'slowest': 1
"""
import turtle as t

n = 60                  # 원을 60번 그림
t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정

for i in range(n) :
    t.circle(120)       # 반지름이 120인 원을 그림
    t.right(360/n)      # 오른쪽으로 6도 회전

t.mainloop()


### 21.3.2  선으로 복잡한 무늬 그리기
""" 선을 이용해서 복잡한 무늬를 그려보겠습니다. """
import turtle as t
 
t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정

for i in range(300):    # 300번 반복(0~299)
    t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)         # 오른쪽으로 91도 회전

t.mainloop()


#### 참고 : 터틀 모양 설정하기
"""
터틀의 shape에는 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic' 등을 지정하여 여러 가지 터틀 모양을 사용할 수 있습니다.
특히, t.shape()와 같이 shape를 그대로 호출하면 현재 모양을 알아낼 수 있습니다.

import turtle as t
t.shape('arrow')    # 화살표 모양 사용
t.shape()           # 현재 모양 알아내기
'arrow'
"""
