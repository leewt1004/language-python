# for 1 줄 코딩
# 1. 리스트 만들기
# 2. 딕셔너리 만들기

# x =  [ i for i in range(0, 10)]
# y = { i:i for i in range(0, 10) }

# x = []
# for i in range(0, 10) :
#     x.append(i)

# y = {}
# for i in range(1,11) :
#     y.update([[i, i]])



# class Calculrator():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def add(self, note):
#         print(self.x + self.y, note)
#         return self.x + self.y
    
#     def sub(self):
#         return self.x + self.y

#     def mul(self):
#         return self.x + self.y
        

#     def div(self):
#         return self.x + self.y

# calc = Calculrator(50, 10)
# calc.add(note='add function!')
# calc.sub()
# calc.mul()
# calc.div()





class Calculrator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, note):
        print(self.x + self.y, note)
        return self.x + self.y
    
    def sub(self):
        return self.x + self.y

    def mul(self):
        return self.x + self.y
        
    def div(self):
        return self.x + self.y



init, iter, next, ui
