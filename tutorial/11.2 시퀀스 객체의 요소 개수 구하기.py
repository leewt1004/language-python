## 11.2 시퀀스 객체의 요소 개수 구하기
"""
시퀀스 객체에는 요소가 여러 개 들어있죠? 이 요소의 개수(길이)를 구할 때는 len 함수를 사용합니다 
len(시퀀스객체)
"""


### 11.2.1 리스트와 튜플의 요소 개수 구하기
""" 리스트 """
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
len(a)

""" 튜플 """
b = (38, 76, 43, 62, 19)
len(b)


### 11.2.2 range의 숫자 생성 개수 구하기
""" range에 len 함수를 사용하면 숫자가 생성되는 개수를 구합니다. """
len(range(0, 10, 2)) # (0, 2, 4, 6, 8) 


### 11.2.3 문자열의 길이 구하기
"""
문자열의 길이(문자의 개수)를 구해보겠습니다. 문자열도 시퀀스 자료형이므로 len 함수를 사용하면 됩니다. 
문자열의 길이는 공백까지 포함합니다.
"""
hello = 'Hello, world!'
len(hello)

""" 한글 문자열의 길이도 len으로 구하면 됩니다. """
hello = '안녕하세요'
len(hello)
