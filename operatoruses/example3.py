class P:
   def __init__(self):
      self.__x=100
      self.y=200
   def print(self):
      print(self.__x, self.y)
class C(P):
   def __init__(self):
      super().__init__()
      self.__x=300
      self.y=400
d = C()
d.print()