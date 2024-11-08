## 16.3 시퀀스 객체로 반복하기
""" for는 리스트, 튜플, 문자열 등 시퀀스 객체로 반복할 수 있습니다. """

""" 시퀀스객체 - 리스트 """
a = [10, 20, 30, 40, 50]
for i in a :
    print(i)

""" 시퀀스객체 - 튜플 """
fruits = ('apple', 'orange', 'grape')
for fruits in fruits : # for 반복문의 변수를 i 대신 fruit로 사용했습니다. for에서 변수 i는 다른 이름으로 만들어도 상관없습니다.
    print(fruits)

""" 시퀀스객체 - 문자열 """
for letter in 'Python' :
    print(letter, end = ' ')

""" 문자열 뒤집어서 출력 """
for letter in reversed('Python') :
    print(letter, end = ' ')

"""
for 반복문은 반복 개수가 정해져 있을 때 주로 사용합니다.
range의 다양한 사용 방법을 익혀 두기 바랍니다.
for 반복문은 range 이외에도 시퀀스 객체를 사용할 수 있다는 점이 중요합니다.
"""
