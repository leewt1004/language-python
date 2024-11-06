## 7.4 연습문제

"""
다음 소스 코드를 완성하여 날짜와 시간이 출력되게 만드세요.

year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, (1)__________)
print(hour, minute, second, (2)_____)

- 실행결과 -
2000/10/27/ 11:43:59
"""

year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, sep = '/', end = ' ')
print(hour, minute, second, sep = ":")

"""
end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됩니다.
end를 따로 설정하지 않으면 기본 값인 \n이 적용되어 출력 후 줄 바꿈이 됩니다.
"""
