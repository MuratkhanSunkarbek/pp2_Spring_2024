#1
mytuple = ("ford","bmb","mustang")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))






#2
a=("mustang")
b=iter(a)

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))









#3
a=("apple","banana")
for x in a:
    print(x)






#4
a=("strawberry")
for x in a:
    print(x)








#5
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a+=1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))






#6
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x

        else:
            raise StopIteration

myclass=MyNumbers()
myiter=iter(myclass)



for x in myiter:
    print(x)