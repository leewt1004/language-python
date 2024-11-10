## 22.9 연습문제
"""
리스트에서 특정 요소만 뽑아내기
다음 소스 코드를 완성하여 리스트 a에 들어있는 문자열 중에서 길이가 5인 것들만 리스트 형태로 출력되게 만드세요(리스트 표현식 사용).

practice_list_comprehension.py
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [                           ]

print(b)

- 실행 결과 - 
['alpha', 'bravo', 'delta', 'hotel', 'india']
"""

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
for i in a:
    if len(i) == 5:
        print(i)  # 길이가 5인 단어만 출력됨
