## 25.7 연습문제
"""
평균 점수 구하기
다음 소스 코드를 완성하여 평균 점수가 출력되기 만드세요.

maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

___________________________________________                                          
print(average)

- 실행 결과 -
89.25
"""
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
avg = sum(maria.values()) / len(maria)
print(avg)

"""
maria는 학생의 과목별 점수를 저장한 딕셔너리입니다.
각 과목의 이름('korean', 'english', 'mathematics', 'science')이 키이고, 점수가 값입니다.
maria.values()는 딕셔너리 maria에서 각 과목의 점수만을 추출하여 반환합니다: [94, 91, 89, 83]
sum(maria.values())는 점수의 합을 구합니다: 94 + 91 + 89 + 83 = 357
len(maria)는 딕셔너리 maria의 항목 개수, 즉 과목 수를 반환합니다: 4
전체 합 357을 과목 수 4로 나누어 평균을 계산합니다

sum()함수 : 숫자의 합계를 계산하는 함수입니다.
len()함수 : 객체의 길이(항목의 개수)를 반환하는 함수입니다.
"""
