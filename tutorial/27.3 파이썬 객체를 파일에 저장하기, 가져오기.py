## 27.3 파이썬 객체를 파일에 저장하기, 가져오기
"""
파일에서 문자열만 읽고 쓴다면 조금 불편하겠죠? 파이썬은 객체를 파일에 저장하는 pickle 모듈을 제공합니다.
다음과 같이 파이썬 객체를 파일에 저장하는 과정을 피클링(pickling)이라고 하고, 파일에서 객체를 읽어오는 과정을 언피클링(unpickling)이라고 합니다.
pickle 모듈은 파이썬 객체(예: 리스트, 딕셔너리, 문자열 등)를 파일에 저장하거나, 저장된 파일에서 객체를 불러오는 데 사용됩니다.
"""




### 27.3.1  파이썬 객체를 파일에 저장하기
""" 그럼 파이썬 객체를 파일에 저장하는 피클링을 해보겠습니다. 피클링은 pickle 모듈의 dump 메서드를 사용합니다. """
import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korea' : 90, 'english' : 95, 'mathematics' : 85, 'science' : 82}

with open('james.p', 'wb') as file :    # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
"""
(1) import pickle
    - 파이썬의 pickle 모듈을 가져오는 코드입니다. 

(2) name, age, address, scores
    - 변수 선언 및 각각 문자열, 정수, 문자열, 딕셔너리 데이터가 저장합니다.

(3) with open('james.p', 'wb') as file :
    - 파일 james.p를 바이너리 쓰기 모드(wb)로 열고, 파일을 자동으로 닫습니다.

(4) pickle.dump(data, file)
    - 각 변수를 파일에 저장합니다.
    - dump()는 데이터를 바이너리 형식으로 저장하므로, 파일이 일반 텍스트처럼 보이지 않습니다.

(5) 설명
    소스 코드를 실행하면 .py 파일이 있는 폴더에 james.p 파일이 생성됩니다. 여기서는 확장자를 pickle의 p를 사용했지만 다른 확장자를 사용해도 상관없습니다.
    특히 pickle.dump로 객체(값)를 저장할 때는 open('james.p', 'wb')와 같이 파일 모드를 'wb'로 지정해야 합니다.
    b는 바이너리(binary)를 뜻하는데, 바이너리 파일은 컴퓨터가 처리하는 파일 형식입니다. 따라서 메모장 같은 텍스트 편집기로 열어도 사람이 알아보기 어렵습니다.
    지금까지 사용한 .txt 파일은 사람이 알아보기 쉽도록 만든 파일 형식이며 텍스트(text) 파일이라고 부릅니다.
"""




### 27.3.2  파일에서 파이썬 객체 읽기
"""
이제 파일에서 파이썬 객체를 읽어오는 언피클링을 해보겠습니다. 
언피클링은 pickle 모듈의 load를 사용합니다. 그리고 언피클링을 할 때는 반드시 파일 모드를 바이너리 읽기 모드 'rb'로 지정해야 합니다.
"""
import pickle

with open('james.p', 'rb') as file :    # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
"""
(1) import pickle
    - 파이썬의 pickle 모듈을 가져오는 코드입니다. 

(2) with open('james.p', 'rb') as file :
    - 파일 james.p를 바이너리 읽기 모드(rb)로 열고, 파일을 자동으로 닫습니다.

(3) name, age, address, scores = pickle.load(file)
    - pickle.load(file)을 사용해 파일에서 저장된 데이터를 한 번에 하나씩 읽어옵니다.
    - name, age, address, scores에 파일에서 읽어온 데이터를 순서대로 저장합니다.
    - pickle.load(file)을 호출할 때마다 파일에 저장된 객체가 순서대로 복원됩니다.

(4) print(name), print(age), print(address), print(scores)
    - 각각의 데이터를 출력합니다.

(5) 설명
    앞에서 james.p 파일을 저장할 때 pickle.dump를 네 번 사용했습니다. 
    마찬가지로 파일에서 객체(값)를 가져올 때도 pickle.load를 네 번 사용해야 합니다.
    즉, name, age, address, scores 순으로 저장했으므로 가져올 때도 같은 순서로 가져오면 됩니다.
"""




#### 참고 : 다른 파일 모드는 없나요?
"""
사실 파일 모드는 조합에 따라 여러 종류가 있습니다. 읽기 'r', 쓰기 'w' 이외에 추가 'a', 배타적 생성 'x'도 있습니다. 
추가 모드는 이미 있는 파일에서 끝에 새로운 내용을 추가할 때 사용하고, 
배타적 생성 모드는 파일이 이미 있으면 에러(FileExistsError)를 발생시키고 없으면 파일을 만듭니다. 'x'는 베타적 생성(exclusive creation)의 x입니다

또한, 파일의 형식도 함께 지정할 수 있는데, 텍스트 모드 't'와 바이너리 모드 'b'가 있습니다.
이 파일 형식과 읽기, 쓰기 모드를 조합한 텍스트 모드 'rt', 'wt'는 파일을 텍스트 모드로 엽니다.
특히 텍스트 모드는 생략할 수 있어서 그냥 'r', 'w'도 텍스트 모드입니다.
그리고 바이너리 모드 'rb', 'wb' 등은 피클링을 사용하거나 바이너리 데이터를 직접 저장할 때 사용합니다.

그다음에 '+'가 있는데 파일을 읽기/쓰기 모드로 엽니다. 
이 모드는 'r+t', 'w+t', 'r+', 'w+', 'r+b', 'w+b' 등으로 조합할 수 있으며 읽기/쓰기 모드인 것은 같지만 파일 처리 방법이 조금씩 다릅니다.
"""
