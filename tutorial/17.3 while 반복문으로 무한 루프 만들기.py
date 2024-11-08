## 17.3 while 반복문으로 무한 루프 만들기
""" while 반복문으로 무한 루프를 만들어보겠습니다. 

while True : # while에 True를 지정하면 무한 루프
    print('Hello, world!')

while에 조건식 대신 True를 지정하면 무한히 반복하는 무한 루프가 만들어집니다.
따라서 조건식이 항상 참(True)이므로 변화식도 필요 없습니다.
"""


""" while에 True 대신 True로 취급하는 값을 사용해도 무한 루프로 동작합니다. 
while 1: # 0이 아닌 숫자는 True로 취급하여 무한 루프로 동작
    print('Hello, world!')

while 'Hello' :  # 내용이 있는 문자열은 True로 취급하여 무한 루프로 동작
    print('Hello, world!')
"""

"""
while 반복문은 조건식이 참(True)일 때 반복하고 거짓(False)일 때 반복을 끝냅니다.
특히 while 반복문은 반복 횟수가 정해져 있지 않을 때 자주 사용하므로 이 부분을 꼭 기억해두세요.
반면 for 반복문은 반복 횟수가 정해져 있을 때 자주 사용합니다. 
그러므로 for와 while의 차이점을 정확히 익혀 두고 적절한 곳에 사용하는 것이 좋습니다.
"""
