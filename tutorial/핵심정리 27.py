## 핵심정리





# 파일 열기, 닫기
"""
파일 읽기/쓰기를 하기 전에는 open 함수로 파일을 열어서 파일 객체를 얻어야 합니다. 그다음에 파일 읽기/쓰기 작업이 끝났다면 반드시 close로 파일 객체를 닫아줍니다.

파일객체 = open(파일이름, 파일모드)     # 파일열기
파일객체.close()                        # 파일 객체 닫기

with open(파일이름, 파일모드) as 파일객체 :         # 파일을 사용한 뒤 자동으로 파일 객체를 닫아줌
    코드
"""




# 파일 모드
""" 파일을 열 때는 용도에 따라 다양한 파일 모드를 지정해야 합니다. """

"""
r       읽기 전용                   파일을 읽기 전용으로 열기. 단, 파일이 반드시 있어야 하며 파일이 없으면 에러 발생
w       쓰기 전용                   쓰기 전용으로 새 파일을 생성. 만약 파일이 있으면 내용을 덮어씀
a       추가                        파일을 열어 파일 끝에 값을 이어 씀. 만약 파일이 없으면 파일을 생성
x       배타적 생성(쓰기)           파일을 쓰기 모드로 생성. 파일이 이미 있으면 에러 발생
r+      읽기/쓰기                   파일을 읽기/쓰기용으로 열기. 단, 파일이 반드시 있어야 하며 파일이 없으면 에러 발생
w+      읽기/쓰기                   파일을 읽기/쓰기용으로 열기. 파일이 없으면 파일을 생성하고, 파일이 있으면 내용을 덮어씀
a+      추가(읽기/쓰기)             파일을 열어 파일 끝에 값을 이어 씀. 만약 파일이 없으면 파일을 생성. 읽기는 파일의 모든 구간에서 가능하지만, 쓰기는 파일의 끝에서만 가능함
x+      배타적 생성(읽기/쓰기)      파일을 읽기/쓰기 모드로 생성. 파일이 이미 있으면 에러 발생
t       텍스트 모드                 파일을 읽거나 쓸 때 개행 문자 \n과 \r\n을 서로 변환, t를 생략하면 텍스트 모드 
b       바이너리 모드               파일의 내용을 그대로 읽고, 값을 그대로 씀
"""




# 파일 메서드
"""
read()                          파일에서 문자열을 읽음
write('문자열')                  파일에 문자열을 씀
readline()                      파일의 내용을 한 줄 읽음
readlines()                     파일의 내용을 한 줄씩 리스트 형태로 가져옴
writelines(문자열리스트)         파일에 리스트의 문자열을 씀, 리스트의 각 문자열에는 \n을 붙여주어야 함
pickle.load(파일객체)            파일에서 파이썬 객체를 읽음
pickle.dump(객체, 파일객체)      파이썬 객체를 파일에 저장
"""




# 파일 연 뒤에는 왜 파일을 닫아야 하나요?
"""
파이썬에는 사용이 끝난 메모리를 정리해주는 가비지 컬렉터가 있어서 파일을 닫지 않아도 가비지 컬렉터가 파일을 닫아줍니다.
하지만 프로그래머가 파일을 직접 닫아야 하는 이유는 다음과 같습니다.

(1) 너무 많은 파일을 열어 두면 그만큼 메모리 공간을 차지하므로 성능에 영향을 줄 수 있습니다.

(2) 파일을 닫지 않으면 데이터가 쓰기가 완료되지 않을 수도 있습니다. 운영체제는 파일을 처리할 때 성능을 위해서 데이터를 버퍼(임시 공간)에 저장한 뒤 파일에 씁니다.
    때에 따라서는 파일이 닫히는 시점에 버퍼의 내용이 파일에 저장됩니다.

(3) 이론적으로 운영체제에서 열 수 있는 파일의 개수는 한계가 있습니다.

(4) 운영체제에 따라 파일을 열었을 때 파일을 잠금 상태로 처리하는 경우가 있습니다. 실질적으로 파일 처리가 끝났더라도 파일을 닫지 않으면 다른 프로그램에서 파일을 사용할 수 없는 상태가 됩니다.

보통은 파일을 닫지 않아도 큰 문제가 없습니다. 하지만 실무에서는 사소한 실수로도 큰 문제가 발생하는 경우가 있으므로 파일을 정확히 닫는 습관을 기르는 것이 좋습니다. 
파이썬에서는 주로 with as를 사용하여 파일을 자동으로 닫는 방식을 사용합니다.
"""
