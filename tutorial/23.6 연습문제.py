## 23.6 연습문제
"""
3차원 리스트 만들기
다음 소스 코드를 완성하여 높이 2, 세로 크기 4, 가로 크기 3인 3차원 리스트를 만드세요(리스트 표현식 사용).

a = [_________________________________________________________________]
print(a)

- 실행 결과 -
[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
"""

a = [[[0 for col  in range(3)] for row in range(4)] for depth in range(2)]
print(a)    # [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]

"""
3차원 리스트는 다음과 같이 높이×가로×세로 형태로 이루어져 있습니다.

리스트 = [[[값, 값], [값, 값]], [[값, 값], [값, 값]], [[값, 값], [값, 값]]]
리스트[높이인덱스][세로인덱스][가로인덱스]
리스트[높이인덱스][세로인덱스][가로인덱스] = 값

가로×세로 평면(2차원 리스트)이 여러 겹 있는 모양입니다. 따라서 한 면을 완성한 뒤 다른 면을 완성하는 방식으로 작성해야 합니다.
"""

"""
리스트 표현식으로 세로 4, 가로 3인 2차원 리스트를 만드는 방법은 다음과 같습니다.
[[0 for col in range(3)] for row in range(4)]

이렇게 만든 2차원 리스트를 여러 번 반복해주면 3차원 리스트가 됩니다.
여기서는 높이가 2라고 했으므로 for depth in range(2)와 같이 반복합니다.
이때 2차원 리스트가 다시 안쪽 리스트가 될 수 있도록 [ ]로 묶어주어야 합니다.
[[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
"""
