## 22.2 리스트의 할당과 복사 알아보기
""" 리스트의 할당과 복사에 대해 알아보겠습니다. 할당과 복사는 비슷한 것 같지만 큰 차이점이 있습니다. """
a = [0, 0, 0, 0, 0]
b = a       # b = a와 같이 리스트를 다른 변수에 할당하면 리스트는 두 개가 될 것 같지만 실제로는 리스트가 한 개입니다.

""" a와 b를 is 연산자로 비교해보면 True가 나옵니다. 즉, 변수 이름만 다를 뿐 리스트 a와 b는 같은 객체입니다. """
a is b
True

""" 리스트 b의 요소를 변경하면 리스트 a와 b에 모두 반영됩니다. """
b[2] = 99
a
[0, 0, 99, 0, 0]
b
[0, 0, 99, 0, 0]

""" 리스트 a와 b를 완전히 두 개로 만들려면 copy 메서드로 모든 요소를 복사해야 합니다. """
a = [0, 0, 0, 0, 0]
b = a.copy()        # b = a.copy()와 같이 copy를 사용한 뒤 b에 할당해주면 리스트 a의 요소가 모두 b에 복사됩니다.

"""
a와 b를 is 연산자로 비교해보면 False가 나옵니다. 
즉, 두 리스트는 다른 객체입니다. 그러나 복사된 요소는 모두 같으므로 ==로 비교하면 True가 나옵니다.
"""
a is b
False
a == b
True

""" 리스트 a와 b는 별개이므로 한쪽의 값을 변경해도 다른 리스트에 영향을 미치지 않습니다. """
b[2] = 99
a
[0, 0, 0, 0, 0]
b
[0, 0, 99, 0, 0]
