## 26.8 연습문제
"""
공배수 구하기
다음 소스 코드를 완성하여 1부터 100까지 숫자 중 3과 5의 공배수를 세트 형태로 출력되게 만드세요.

a = (1)_______________________________________________
b = (2)_______________________________________________

print(a & b)

- 실행 결과 - 
{75, 45, 15, 90, 60, 30}
"""

a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}
print(a & b)                    # {75, 45, 15, 90, 60, 30}


""" 해설 """

"""
✴️ for i in range(1, 101) ✴️
range(1, 101)은 1부터 100까지의 숫자를 생성합니다.
for i in range(1, 101)은 각 숫자 i를 순차적으로 가져와서 반복문 안의 조건문과 실행문에 사용합니다.

✴️ if i % 3 == 0 ✴️
i % 3 == 0은 숫자 i가 3의 배수인지 확인하는 조건입니다.
i % 3은 i를 3으로 나눈 나머지를 계산하며, 나머지가 0이면 i는 3의 배수입니다.
이 조건에 따라, 3의 배수인 경우에만 i가 집합 a에 추가됩니다.

✴️ for i in range(1, 101) ✴️
1부터 100까지의 숫자 중에서 각 숫자 i를 순차적으로 가져옵니다.

✴️ if i % 5 == 0 ✴️
i % 5 == 0은 숫자 i가 5의 배수인지 확인하는 조건입니다.
나머지가 0이면 i는 5의 배수입니다.
이 조건에 따라, 5의 배수인 경우에만 i가 집합 b에 추가됩니다.

✴️ a & b ✴️
a & b는 두 집합의 교집합을 구하는 연산입니다.
교집합 연산은 두 집합에 모두 포함된 요소들만 남깁니다.
print(a & b)는 교집합 집합을 출력하며, 3과 5의 공배수만이 포함된 결과를 표시합니다.
"""
