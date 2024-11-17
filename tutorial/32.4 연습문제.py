## 32.4 연습문제
"""
이미지 파일만 가져오기
다음 소스 코드를 완성하여 확장자가 .jpg, .png인 이미지 파일만 출력되게 만드세요.
여기서는 람다 표현식을 사용해야 하며 출력 결과는 리스트 형태라야 합니다. 
람다 표현식에서 확장자를 검사할 때는 문자열 메서드를 활용하세요.

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(                                                                           )

- 실행 결과 - 
['1.png', '10.jpg', '2.jpg', '3.png']
"""
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))
"""
----- 코드 흐름 및 설명 -----

(1) files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
    - 리스트 files 정의

(2) filter()
    - filter 함수 사용 / filter는 리스트의 각 요소에 대한 조건을 확인하여, 조건을 만족하는 요소만 포함하는 새로운 리스트를 생성합니다.

(3) lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, file
    - 각 파일 x에 대하여 .jpg 문자열을 포함하고 있다면 True 또는, .png 문자열을 포함하고 있다면 True
    - 둘 중 하나라도 참이면 해당 파일 이름이 필터링 결과에 포함됩니다.

(4) 해설
    리스트 files에는 여러 종류의 파일 이름이 들어있는데 .jpg, .png 파일만 가져오려면 filter를 사용해야 합니다.
    그리고 filter는 lambda 또는 함수의 반환값이 True일 때 해당 요소를 가져옵니다. 
    따라서 람다 표현식을 작성할 때 매개변수가 '.jpg', '.png'이면 True를 반환하도록 만듭니다.
    먼저 문자열에서 find 메서드를 사용하면 찾을 문자열이 있을 때 인덱스를 반환하고 없을 때는 -1을 반환합니다.
    그래서 조건식은 x.find('.jpg') != -1 or x.find('.png') != -1과 같이 만들고 .jpg, .png 둘 중 하나라도 참이면 되므로 find를 or 연산자로 연결해주면 됩니다.

(5) find 메서드의 -1은 공식적인 반환 값
    find 메서드에서 문자열이 없는 경우 항상 -1을 반환합니다.
    Python 표준 라이브러리의 설계에서 "존재하지 않음"을 표현하기 위한 규칙적인 값으로 -1을 사용하는 거예요.
    이건 Python뿐 아니라 다른 언어(Java, C 등)에서도 비슷한 방식으로 사용됩니다.

    text = "hello world"
    print(text.find("Python"))  # -1 ('Python'은 없으므로 -1 반환) / 출력 시 -1을 반환
"""
