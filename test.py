# stack=[]
# def push(val):
#     stack.append(val)
#
# def pop():
#     val=stack[-1]
#     del stack[-1]
#     return val
#
# push(3)
# push(2)
# push(1)
#
# print(pop())
# print(pop())
# print(pop())




class Zhivot:
    def __init__(self):
        self.hodit="На конечностях"

class Zvuk(Zhivot):
    def __init__(self):
        Zhivot.__init__(self)
        self.zvuki="Мяу"

koshka=Zvuk()

print(koshka.zvuki)
print(koshka.hodit)

