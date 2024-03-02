#1
def myfunc():
    x=250
    print(x)
    
myfunc()    




#2
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


#3
x=200
def myfunc ():
    print(x)

myfunc()
print(x)






#4
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)



#5
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)