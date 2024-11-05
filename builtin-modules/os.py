

- main
  |-- sub01
      |-- module01
          |-- submodule01
          |-- submodule02
          |-- submodule03
      |-- module02
          |-- submodule01
          |-- submodule02
          |-- submodule03
      |-- module03
          |-- submodule01
          |-- submodule02
          |-- submodule03
  |-- sub02
      |-- module01
          |-- submodule01
          |-- submodule02
          |-- submodule03
      |-- module02
          |-- submodule01
          |-- submodule02
          |-- submodule03
      |-- module03
          |-- submodule01
          |-- submodule02
          |-- submodule03
  |-- sub03
      |-- module01
          |-- submodule01
          |-- submodule02
          |-- submodule03
      |-- module02
          |-- submodule01
          |-- submodule02
          |-- submodule03
      |-- module03
          |-- submodule01
          |-- submodule02
          |-- submodule03


# 첫 번째 코드
import os 

"""
os.listdir() : path 에서 주어진 디렉토리의 항목 이름이 포함된 목록을 반환합니다 .
os.mkdir() : 폴더를 생성해주는 함수
os.makedir() : makedirs 함수는 첫 번째 인자로 들어온 경로상에 적혀있는 폴더를 다 만들어주는 함수입니다.
os.rmdir() : 디렉토리를 제거하는 데 사용합니다. 먼저 디렉터리 안의 파일을 삭제하고 디렉터리를 삭제합니다.
os.getcwd() : getcwd 함수로 현재 경로를 얻을 수 있다는 것만 기억하기 바랍니다.
"""

"""
첫 번째 폴더 생성 후 두 번째 폴더를 생성하면 에러가 나는데, 그 이유는 이미 첫 번째 폴더가 생성이 되었기 때문이다.
"""

# d:/python/ 경로안에 main 폴더 생성
os.mkdir('d:/python/main') 

# d:/python/main 경로 안에 sub01 하위 폴더 생성
os.makedirs('d:/python/main/sub01/module01/submodule01') # main폴더 안에 sub01/module01/submodule01 하위폴더 생성
os.mkdir('d:/python/main/sub01/module01/submodule02') # module01폴더 안에 submodule02폴더생성
os.mkdir('d:/python/main/sub01/module01/submodule03') # module01폴더 안에 submodule03폴더생성

os.makedirs('d:/python/main/sub01/module02/submodule01') # sub01폴더 안에 module02/submodule01 하위폴더 생성
os.mkdir('d:/python/main/sub01/module02/submodule02') # module02폴더 안에 submodule02폴더생성
os.mkdir('d:/python/main/sub01/module02/submodule03') # module02폴더 안에 submodule03폴더생성

os.makedirs('d:/python/main/sub01/module03/submodule01') # sub01폴더 안에 module02/submodule01 하위폴더 생성
os.mkdir('d:/python/main/sub01/module03/submodule02') # module02폴더 안에 submodule02폴더생성
os.mkdir('d:/python/main/sub01/module03/submodule03') # module02폴더 안에 submodule03폴더생성

# d:/python/main 경로 안에 sub02 하위 폴더 생성
os.makedirs('d:/python/main/sub02/module01/submodule01') # main폴더 안에 sub02/module01/submodule01 하위폴더 생성
os.mkdir('d:/python/main/sub02/module01/submodule02') # module01폴더 안에 submodule02폴더생성
os.mkdir('d:/python/main/sub02/module01/submodule03') # module01폴더 안에 submodule03폴더생성

os.makedirs('d:/python/main/sub02/module02/submodule01') # sub02폴더 안에 module02/submodule01 하위폴더 생성
os.mkdir('d:/python/main/sub02/module02/submodule02') # module02폴더 안에 submodule02폴더생성
os.mkdir('d:/python/main/sub02/module02/submodule03') # module02폴더 안에 submodule03폴더생성

os.makedirs('d:/python/main/sub02/module03/submodule01') # sub02폴더 안에 module02/submodule01 하위폴더 생성
os.mkdir('d:/python/main/sub02/module03/submodule02') # module02폴더 안에 submodule02폴더생성
os.mkdir('d:/python/main/sub02/module03/submodule03') # module02폴더 안에 submodule03폴더생성

# d:/python/main 경로 안에 sub03 하위 폴더 생성
os.makedirs('d:/python/main/sub03/module01/submodule01') # main폴더 안에 sub03/module01/submodule01 하위폴더 생성
os.mkdir('d:/python/main/sub03/module01/submodule02') # module01폴더 안에 submodule02폴더생성
os.mkdir('d:/python/main/sub03/module01/submodule03') # module01폴더 안에 submodule03폴더생성

os.makedirs('d:/python/main/sub03/module02/submodule01') # sub03폴더 안에 module02/submodule01 하위폴더 생성
os.mkdir('d:/python/main/sub03/module02/submodule02') # module02폴더 안에 submodule02폴더생성
os.mkdir('d:/python/main/sub03/module02/submodule03') # module02폴더 안에 submodule03폴더생성

os.makedirs('d:/python/main/sub03/module03/submodule01') # sub03폴더 안에 module02/submodule01 하위폴더 생성
os.mkdir('d:/python/main/sub03/module03/submodule02') # module02폴더 안에 submodule02폴더생성
os.mkdir('d:/python/main/sub03/module03/submodule03') # module02폴더 안에 submodule03폴더생성

"""
불편한 점
01. 코드 가독성 : 주석이 없으면 코드를 읽기가 힘들어지고, 코딩전체 길이가 길어짐
02. main 폴더안에 sub01, 02, 03폴더를 한번에 만들고 그 경로를 따라 들어가서 마찬가지로 
    각각의 module01, 02, 03을 만들고, 또 그 경로를 찾아가서 submodule01, 02, 03을 만들어야 해서 코딩을 하면서도 헷갈림 
03. 테스트용으로 main폴더 부터 sub01,module01,submodule01까지 만들었을 때 삭제를 하려면 하위 폴더 부터 삭제를 해야함. 즉, 전체삭제가 안됨
04. 한번에 만들 수가 없어서 일일이 확인 후 삭제하고 만들어야 함
05. 계속 반복하다 보니 짜증남 ㅋㅋㅋ 그나마, 한번 테스트 한 후 된다 싶으면 ctrl + c를 통한 복붙이 가능함
"""


# 수정된 코드
import os
from itertools import product

[os.makedirs(os.path.join(*pe)) for pe in product(['main'], ['sub01', 'sub02', 'sub03'], ['module01', 'module02', 'module03'], ['submodule01', 'submodule02', 'submodule03'])]
