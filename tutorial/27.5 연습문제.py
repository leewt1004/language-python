## 27.5 연습문제
"""
파일에서 10자 이하인 단어 개수 세기
단어가 줄 단위로 저장된 words.txt 파일이 주어집니다. 
다음 소스 코드를 완성하여 10자 이하인 단어의 개수가 출력되게 만드세요.

anonymously
compatibility
dashboard
experience
photography
spotlight
warehouse

(1)___________________________________
    count = 0
    (2)_________________________
    ...

    print(count)

- 실행 결과 -
4
"""

lines = ['anonymously\n', 'compatibility\n', 'dashboard\n', 'experience\n', 'photography\n', 'spotlight\n', 'warehouse\n']      # 주어진 단어를 lines라는 변수에 리스트로 저장

with open('words.txt', 'w') as file :                   # words.txt 파일을 쓰기 모드(w)로 열기
    file.writelines(lines)                              # writelines메서드를 사용

count = 0                                               # count 변수를 0으로 초기화
with open('words.txt', 'r') as file :                   # words.txt 파일을 읽기 모드(r)로 열기
    for line in file :                                  # for 반복문을 통해 각 줄을 반복
        if len(line.strip('\n')) <= 10:                 # if 조건문을 통해 단어의 개수를 비교
            count += 1                                  # count 변수를 1씩 증가
            print(line.strip('\n'))                     # '\n' 제거 후 출력
print(count)                                            # 단어의 총 개수 출력

"""
(1) lines = ['anonymously\n', 'compatibility\n', 'dashboard\n', 'experience\n', 'photography\n', 'spotlight\n', 'warehouse\n']
    - lines라는 변수에 단어들이 줄바꿈 문자(\n)와 함께 리스트 형태로 저장되며, 각 단어가 한 줄씩 저장된 파일을 만드는 데 사용됩니다.

(2) with open('words.txt', 'w') as file:
        file.writelines(lines)
    - words.txt 파일을 **쓰기 모드(w)**로 열고, lines 리스트에 있는 단어들을 한 줄씩 파일에 씁니다.
    - file.writelines(lines)는 리스트의 각 항목을 파일에 그대로 작성합니다.

(3) count = 0
    - 10자 이하의 단어 개수를 세기 위해 count 변수를 0으로 초기화합니다.

(4) with open('words.txt', 'r') as file:
    - words.txt 파일을 **읽기 모드(r)**로 엽니다. 이후 파일에서 내용을 읽습니다.

(5) for line in file:
    - 파일의 각 줄을 반복해서 읽습니다. 파일의 첫 번째 줄부터 마지막 줄까지 line에 한 줄씩 저장되며, 반복문이 한 번 실행될 때마다 다음 줄로 이동합니다.

(6) if len(line.strip('\n')) <= 10:
    - line.strip('\n')을 통해 줄 끝에 있는 줄바꿈 문자(\n)를 제거한 후, 그 줄의 길이를 측정합니다.
    - 측정한 길이가 10자 이하인 경우에만 다음의 코드를 실행합니다.

(7) count += 1
    - 10자 이하인 단어가 발견되면 count를 1 증가시킵니다.

(8) print(line.strip('\n'))
    - 조건을 만족한 단어(10자 이하의 단어)를 화면에 출력합니다. 이때 strip('\n')으로 줄바꿈을 제거하고 출력합니다.

(9) print(count)
    - 10자 이하 단어의 총 개수를 출력합니다.

"""
