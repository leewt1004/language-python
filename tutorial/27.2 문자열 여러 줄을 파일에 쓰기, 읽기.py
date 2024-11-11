## 27.2 문자열 여러 줄을 파일에 쓰기, 읽기
""" 문자열 여러 줄을 파일에 쓰고 읽는 방법을 알아보겠습니다. """




### 27.2.1  반복문으로 문자열 여러 줄을 파일에 쓰기
"""
앞에서 문자열 한 줄을 파일에 썼는데 문자열 여러 줄은 어떻게 쓰면 될까요?
간단하게 반복문을 사용하면 됩니다.
"""
with open('hello.txt', 'w') as file :    # hello.txt 파일을 쓰기 모드(w)로 열기
    for i in range(3) :
        file.write('Hello, world! {0}\n'.format(i))
"""
(1) with open('hello.txt', 'w') as file :    # hello.txt 파일을 쓰기 모드(w)로 열기
    - with 다음에 open으로 파일을 열고 as 뒤에 파일 객체를 지정합니다.

(2) for i in range(3) :
        file.write('Hello, world! {0}\n'.format(i))
    - for 반복문 부분은 hello.txt 파일에 "Hello, world!"라는 문자열과 함께 반복 횟수 i를 3번 작성하는 역할을 합니다.
    - format(i)를 사용하여 {0} 위치에 i의 값을 삽입합니다. format은 문자열 메서드 입니다.(문자열 안에 값을 삽입하는 기능을 제공합니다.)

(3) 파일에 문자열 여러 줄을 저장할 때 주의할 부분은 개행 문자 부분입니다. 
    'Hello, world! {0}\n'와 같이 문자열 끝에 개행 문자 \n를 지정해주어야 줄바꿈이 됩니다.
    만약 \n을 붙이지 않으면 문자열이 모두 한 줄로 붙어서 저장되므로 주의해야 합니다.
"""




### 27.2.3  파일의 내용을 한 줄씩 리스트로 가져오기
"""
리스트에 들어있는 문자열을 파일에 써보겠습니다.

파일객체.writelines(문자열리스트)
"""
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

with open('hello.txt', 'w') as file :
    file.writelines(lines)
"""
(1) lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
    - 세 개의 문자열이 들어있는 리스트를 생성합니다. 파일에 각 줄이 끝날 때마다 줄을 바꾸도록 합니다.

(2) with open('hello.txt', 'w') as file :
        file.writelines(lines)
    - with 다음에 open으로 파일을 열고 as 뒤에 파일 객체를 지정합니다.
    - writelines() 메서드는 리스트 안의 문자열들을 한 번에 파일에 씁니다.

(3) writelines는 리스트에 들어있는 문자열을 파일에 씁니다. 
    특히 writelines를 사용할 때는 반드시 리스트의 각 문자열 끝에 개행 문자 \n을 붙여주어야 합니다.
    그렇지 않으면 문자열이 모두 한 줄로 붙어서 저장되므로 주의해야 합니다.
"""




### 27.2.4  파일의 내용을 한 줄씩 읽기
"""
앞에서 만든 hello.txt 파일의 내용을 한 줄씩 읽어보겠습니다. 
read는 파일의 내용을 읽어서 문자열로 가져오지만 readlines는 파일의 내용을 한 줄씩 리스트 형태로 가져옵니다.

변수 = 파일객체.readlines()
"""
with open('hello.txt', 'r') as file :    # hello.txt 파일을 읽기 모드(r)로 열기
    line = None    # 변수 line을 None으로 초기화
    while line != '':       # 파일의 끝이 아닐 때까지 반복
        line = file.readline()      # 파일에서 한 줄을 읽어오기
        print(line.strip('\n'))     # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
"""
(1) with open('hello.txt', 'r') as file :    # hello.txt 파일을 읽기 모드(r)로 열기
    - with 다음에 open으로 파일을 열고 as 뒤에 파일 객체를 지정합니다.

(2) line = None
    - 변수 line은 while로 반복하기 전에 None으로 초기화해줍니다. 

(3) while line != '':
    - line이 빈 문자열('')이 될 때까지 반복합니다. 파일 끝에 도달하면 readline()은 빈 문자열을 반환하므로 반복이 종료됩니다.

(4) line = file.readline()
    - 파일에서 한 줄을 읽어 line 변수에 저장합니다.

(5) print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
    - 읽어온 줄의 끝에 있는 \n을 제거한 후 출력합니다. strip()은 문자열 메서드 입니다.(기본적으로 공백을 제거하며, 제거할 문자를 괄호 안에 지정할 수 있습니다.)

(6) 설명
    readline으로 파일을 읽을 때는 while 반복문을 활용해야 합니다. 왜냐하면 파일에 문자열이 몇 줄이나 있는지 모르기 때문입니다. 
    while은 특정 조건이 만족할 때 계속 반복하므로 파일의 크기에 상관없이 문자열을 읽어올 수 있습니다.

    readline은 더 이상 읽을 줄이 없을 때는 빈 문자열을 반환하는데, while에는 이런 특성을 이용하여 조건식을 만들어줍니다.
    즉, line != ''와 같이 빈 문자열이 아닐 때 계속 반복하도록 만듭니다. 
    그리고 반복문 안에서는 line = file.readline()과 같이 문자열 한 줄을 읽어서 변수 line에 저장해주면 됩니다.

    특히 변수 line은 while로 반복하기 전에 None으로 초기화해줍니다.
    만약 변수 line을 만들지 않고 while을 실행하면 없는 변수와 빈 문자열 ''을 비교하게 되므로 에러가 발생합니다.
    또는, line을 None이 아닌 ''로 초기화하면 처음부터 line != ''는 거짓이 되므로 반복을 하지 않고 코드가 그냥 끝나버립니다.
    while을 사용할 때는 이 부분을 주의해주세요.
    ex) line = None    # 변수 line을 None으로 초기화
        while line != '':
        
    문자열을 출력할 때는 print(line.strip('\n')와 같이 strip 메서드로 \n을 삭제했습니다.
    왜냐하면 파일에서 읽어온 문자열에는 '안녕하세요.\n'와 같이 \n이 이미 들어있기 때문입니다.
    만약 strip('\n')을 생략하면 문자열 한 줄을 출력할 때마다 빈 줄이 계속 출력됩니다.
    즉, 문자열 안에 든 \n과 print가 출력하는 \n 때문에 줄바꿈이 두 번 일어납니다.
"""




### 27.2.5  for 반복문으로 파일의 내용을 줄 단위로 읽기
"""
while 반복문에서 readline을 사용하니 동작 방식이 조금 헷갈리죠? 파이썬에서는 for 반복문으로 좀 더 간단하게 파일의 내용을 읽을 수 있습니다.
다음은 for 반복문에 파일 객체를 지정하여 줄 단위로 파일의 내용을 읽습니다.
"""
with open('hello.txt', 'r') as file :    # hello.txt 파일을 읽기 모드(r)로 열기
    for line in file :    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
"""
(1) with open('hello.txt', 'r') as file :    # hello.txt 파일을 읽기 모드(r)로 열기
    - with 다음에 open으로 파일을 열고 as 뒤에 파일 객체를 지정합니다.

(2)     for line in file :    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
    - 파일을 한 줄씩 읽어와 line 변수에 저장합니다. 파일 끝까지 각 줄을 반복합니다.

(3) print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
    - 읽어온 줄 끝에 있는 줄바꿈 문자 \n을 제거하고 출력합니다.

(4) 설명
    for line in file:로 간단하게 파일의 내용을 한 줄씩 읽었습니다.
    이렇게 for 반복문에 파일 객체를 지정하면 반복을 할 때마다 파일의 내용을 한 줄씩 읽어서 변수에 저장해줍니다.
"""




#### 참고 : 파일 객체는 이터레이터
"""
파일 객체는 이터레이터입니다. 따라서 변수 여러 개에 저장하는 언패킹(unpacking)도 가능합니다(이터레이터는 'Unit 39 이터레이터 사용하기' 참조).
"""
file = open('hello.txt', 'r')
a, b, c = file
print(a, b, c)
"""
물론 a, b, c = file과 같이 사용하려면 hello.txt에는 문자열 3줄이 들어있어야 합니다.
즉, 할당할 변수의 개수와 파일에 저장된 문자열의 줄 수가 일치해야 합니다.
"""
