## 8.2 논리 연산자 사용하기

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

#### 참고 : 정수, 실수, 문자열을 불로 만들기
"""
정수, 실수, 문자열을 불로 만들 때는 bool을 사용하면 됩니다. 
이때 정수 1은 True, 0은 False입니다. 만약 문자열의 내용이 'False'라도 불로 만들면 True입니다. 
문자열의 내용 자체는 판단하지 않으며 값이 있으면 True입니다. 즉, 정수 0, 실수 0.0이외의 모든 숫자는 True입니다. 그리고 빈 문자열 '', ""를 제외한 모든 문자열은 True입니다.
"""
bool(1)
True
bool(0)
False
bool(1.5)
True
bool('False')
True

#### 참고 : 단락 평가
"""
논리 연산에서 중요한 부분이 단락 평가(short-circuit evalution)입니다. 
단락 평가는 첫 번째 값만으로 결과가 확실할 때 두 번째 값은 확인(평가)하지 않는 방법을 말합니다. 
"""

"""
and 연산자는 두 값이 모두 참이라야 참이므로 첫 번째 값이 거짓이면 두 번째 값은 확인하지 않고 바로 거짓으로 결정합니다.
"""
print(False and True) # False
print(False and False) # False

"""
or 연산자는 두 값 중 하나만 참이라도 참이므로 첫 번째 값이 참이면 두 번째 값은 확인하지 않고 바로 참으로 결정합니다.
"""
print(True or True) # True
print(True or False) # True

"""
논리 연산자는 이 단락 평가에 따라 반환하는 값이 결정됩니다. 
True, False를 논리 연산자로 확인하면 True, False가 나왔는데, True and 'Python'의 결과는 무엇이 나올까요?
"""
True and 'Python'
'Python'
"""
문자열 'Python'도 불로 따지면 True라서 True and True가 되어 True가 나올 것 같지만 'Python'이 나왔습니다. 
왜냐하면 파이썬에서 논리 연산자는 마지막으로 단락 평가를 실시한 값을 그대로 반환하기 때문입니다. 
따라서 논리 연산자는 무조건 불을 반환하지 않습니다.
"""

"""
마지막으로 단락 평가를 실시한 값이 불이면 불을 반환하게 됩니다.
"""
'Python' and True
True
'Python' and False
False
"""
and 연산자 앞에 False나 False로 치는 값이 와서 첫 번째 값 만으로 결과가 결정나는 경우에는 첫 번째 값이 반환됩니다.
"""
False and 'Python'
False
0 and 'Python'    # 0은 False이므로 and 연산자는 두 번째 값을 평가하지 않음
0

"""
or 연산자도 마찬가지로 마지막으로 단락 평가를 실시한 값이 반환됩니다.
or 연산자에서 첫 번째 값만으로 결과가 결정되므로 첫 번째 값이 반환됩니다.
"""
True or 'Python'
True
'Python' or True
'Python'
"""
두 번째 값까지 판단해야 한다면 두 번째 값이 반환됩니다.
"""
False or 'Python'
'Python'
0 or False
False
