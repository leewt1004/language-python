## 14.3 if 조건문의 동작 방식 알아보기
""" 조건식이 아닌 값으로 if와 else의 코드를 동작시켜 보겠습니다. """
if True :
    print('참') # True는 참
else :
    print('거짓')

if False :
    print('참')
else :
    print('거짓') # False는 거짓

if None :
    print('참')
else :
    print('거짓') # None은 거짓 / 실제 코드를 작성할 때 변수에 들어있는 값이나 함수의 결과가 None인 경우가 많으므로 이 부분은 꼭 기억해두세요.


### 14.3.1 if 조건문에 숫자 지정하기
""" 숫자는 정수(2진수, 10진수, 16진수), 실수와 관계없이 0이면 거짓, 0이 아닌 수는 참입니다. """
if 0 :
    print('참')
else :
    print('거짓') # 0은 거짓

if 1 :
    print('참') # 1은 참
else :
    print('거짓')

if 0x1F : # 16진수
    print('참') # 0x1F는 참
else :
    print('거짓')

if 0b1000 : # 2진수
    print('참') # 0b1000은 참
else :
    print('거짓')

if 13.5 # 실수
    print('참') # 13.5는 참
else : 
    print('거짓')


### 14.3.2 if 조건문에 문자열 지정하기
""" 문자열은 내용이 있을 때 참, 빈 문자열은 거짓입니다. """
if 'hello' : # 문자열
    print('참') # 문자열은 참
else :
    print('거짓')

if '' : # 빈 문자열
    print('참') 
else :
    print('거짓') # 빈 문자열은 거짓

""" 값 자체가 있으면 if는 동작합니다. 반대로 0, None, ''은 False로 취급하므로 else가 동작합니다. """


#### 참고 : 0, None, 빈 문자열을 not으로 뒤집으면 ?
""" 0, None, 빈 문자열 ''을 not으로 뒤집으면 참(True)이 되므로 if를 동작시킬 수 있습니다. """
if not 0 :
    print('참') # not 0은 참

if not None :
    print('참') # not None은 참

if not '' : 
    print('참') # not 빈 문자열은 참


#### 참고 : True, False로 취급하는 것들
"""
None, False, 0인 숫자들: 0, 0.0, 0j, 
비어 있는 문자열, 리스트, 튜플, 딕셔너리, 세트: '', "", [], (), {}, set()
클래스 인스턴스의 __bool__(), __len__() 메서드가 0 또는 False를 반환할 때
앞에서 나열한 것들을 제외한 모든 요소들은 True로 취급합니다. 
"""
