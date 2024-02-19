x = lambda a: a + 10
print(x(10))



x = lambda a, b: a * b
print(x(8, 5))



x = lambda a, b, c: a + b + c
print(x(9, 11, 16))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(33))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(15)) 
print(mytripler(15))

