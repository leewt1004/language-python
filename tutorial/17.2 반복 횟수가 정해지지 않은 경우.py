## 17.2 반복 횟수가 정해지지 않은 경우
"""
while 반복문은 반복 횟수가 정해지지 않았을 때 주로 사용합니다.
난수를 생성해서 숫자에 따라 반복을 끝내 보겠습니다. 
난수(random number)란 특정 주기로 반복되지 않으며 규칙 없이 무작위로 나열되는 숫자를 뜻합니다.
현실에서 쉽게 접할 수 있는 난수가 바로 주사위를 굴려서 나온 숫자입니다.

파이썬에서 난수를 생성하려면 random 모듈이 필요합니다. 모듈은 다음과 같이 import 키워드를 사용하여 가져올 수 있습니다.

import 모듈
"""

import random # random 모듈을 가져옴
print(random.random())

"""
숫자를 좀 더 알아보기 쉽도록 정수를 생성하는 random 모듈의 randint 함수를 사용해보겠습니다. 
다음과 같이 randint 함수는 난수를 생성할 범위를 지정하며, 범위에 지정한 숫자도 난수에 포함됩니다.

random.randint(a, b)
"""
import random
print(random.randint(1, 6))

""" 이제 이 함수를 while 반복문에 사용해보겠습니다. """
import random # random 모듈을 가져옴

i = 0
while i != 3 : # 3이 아닐 때 계속 반복
    i = random.randint(1, 6) # randint를 사용하여 1과 6 사이의 난수를 생성
    print(i)

"""  while 반복문은 반복 횟수가 정해져 있지 않을 때 유용합니다. """


#### 참고 : random.choice
"""
random.choice 함수를 사용하면 시퀀스 객체에서 요소를 무작위로 선택할 수 있습니다.
random.choice 함수는 시퀀스 객체를 받으므로 리스트뿐만 아니라 튜플, range, 문자열 등을 넣어도 됩니다.
"""
import random

dice = [1, 2, 3, 4, 5, 6]
print(random.choice(dice))
