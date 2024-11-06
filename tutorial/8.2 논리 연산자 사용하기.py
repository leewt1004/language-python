# 8.2 논리 연산자 사용하기

"""
a and b
and는 두 값이 모두 True라야 True입니다. 하나라도 False이면 False가 나옵니다.
"""
True and True
True and False
False and True
False and False

"""
a or b
or는 두 값 중 하나라도 True이면 True입니다. 두 값이 모두 False라야 False가 되죠.
"""
True or True
True or False
False or True
False or False # 두 값이 모두 False 이므로 False가 된다.

"""
not x
not은 논릿값을 뒤집습니다. 그래서 not True는 False가 되고, not False는 True가 됩니다.
"""
not True # False
not False # True

"""
and, or, not 논리 연산자가 식 하나에 들어있으면 not, and, or 순으로 판단합니다.
"""
not True and False or not False
"""
가장 먼저 not True와 not False를 판단하여 False and False or True가 됩니다.
"""
not True and False or not False
False and False or True
False or True
True
"""
이 식을 괄호로 표현하면 다음과 같은 모양이 됩니다.
"""
((not True) and False) or (not False)
True

### 8.2.1 논리 연산자와 비교 연산자를 함께 사용하기
10 == 10 and 10!= 5 # True and True
True

10 > 5 or 10 < 3 # True or Flase
True

not 10 > 5 # not True
False

not 1 is 1.0 # not False
True
"""
비교 연산자로 비교한 결과를 논리 연산자로 다시 판단했습니다. 
이때는 비교 연산자(is, is not, ==, !=, <, >, <=, >=)를 먼저 판단하고 논리 연산자(not, and, or)를 판단하게 됩니다
"""
