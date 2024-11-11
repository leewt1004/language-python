## 24.4 연습문제
"""
파일 경로에서 파일명만 가져오기
다음 소스 코드를 완성하여 파일 경로에서 파일명만 출력되게 만드세요.
단, 경로에서 폴더의 깊이가 달라지더라도 파일명만 출력할 수 있어야 합니다.

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
______________________________________
...
______________________________________

print(filename)

- 실행 결과 - 
python.exe
"""


"""
(1)

path.split('\\'): 경로를 역슬래시(\) 기준으로 나눕니다.
split('\\')는 path 문자열을 여러 부분으로 나눠서 리스트로 만듭니다.
결과: ['C:', 'Users', 'dojang', 'AppData', 'Local', 'Programs', 'Python', 'Python36-32', 'python.exe']

x[-1]: 리스트의 마지막 요소를 가져옵니다.
x[-1]은 리스트에서 마지막 요소인 'python.exe'를 가리킵니다.

print(filename): filename에 저장된 값인 'python.exe'을 출력합니다.
"""
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
filename = x[-1]
print(filename)


"""
(2)

path.split('\\'): 경로를 역슬래시(\) 기준으로 나눕니다.
결과: ['C:', 'Users', 'dojang', 'AppData', 'Local', 'Programs', 'Python', 'Python36-32', 'python.exe']

x.reverse(): 리스트를 뒤집어서 순서를 반대로 만듭니다.
결과: ['python.exe', 'Python36-32', 'Python', 'Programs', 'Local', 'AppData', 'dojang', 'Users', 'C:']

x[0]: 리스트의 첫 번째 요소를 가져옵니다.
리스트를 뒤집었기 때문에 x[0]은 'python.exe'가 됩니다.

print(filename): filename에 저장된 값인 'python.exe'를 출력합니다.
"""
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
x.reverse()
filename = x[0]
print(filename)


"""
(3)

path.rfind('\\'):
rfind('\\')는 문자열에서 오른쪽부터 \를 찾아, 가장 마지막에 있는 \의 인덱스를 반환합니다.
이 예제에서 가장 마지막 \의 위치는 인덱스 57입니다.

path.rfind('\\') + 1:
마지막 \ 바로 다음 위치에서 파일 이름이 시작되므로, 57 + 1 = 58을 사용합니다.
58은 문자열에서 파일 이름이 시작되는 인덱스입니다.

path[58:]:
인덱스 58부터 문자열의 끝까지 잘라냅니다.
path[58:]은 "python.exe"가 되며, 이 값이 filename에 저장됩니다.

출력 결과:
print(filename)은 최종적으로 **파일 이름인 'python.exe'**를 출력합니다.
"""
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
filename = path[path.rfind('\\') + 1:]
print(filename)

""" 파이썬에서는 문자열 안에서 **백슬래시(\) 두 개(\\)**는 항상 하나의 백슬래시(\)로 해석됩니다. 이는 파이썬뿐만 아니라 많은 프로그래밍 언어에서 사용하는 방식입니다. """


#### 참고 : raw 문자열 사용하기
"""
문자열 앞에 r 또는 R을 붙이면 raw 문자열이 됩니다. 이 raw 문자열은 이스케이프 시퀀스를 그대로 저장할 때 사용합니다. 
즉, 다음과 같이 \를 \\로 두 번 쓰지 않고 한 번만 써도 됩니다.
"""
print(r'C:\Users\dojang\AppData\Local\Programs\Python\Python36-32\python.exe')          # C:\Users\dojang\AppData\Local\Programs\Python\Python36-32\python.exe

"""
raw는 가공되지 않고 있는 그대로라는 뜻입니다. 따라서 이스케이프 시퀀스를 문자 그대로 표현합니다.
다음과 같이 raw 문자열에 제어 문자를 입력해보면 제어 문자가 동작하지 않는 것을 볼 수 있습니다.
"""
print(r'1\n2\n3\n')         # 1\n2\n3\n
