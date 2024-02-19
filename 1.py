
#1
mytuple = ("ford","bmb","mustang")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
=======
<<<<<<< HEAD
def my_function(name):
  print(name  +  " Hello ")

my_function( "Sunkarbek")




def my_function(fname):
    print(fname + " How are you?")

my_function("Sunkarbek")
my_function("Muratkhan")
my_function("Galymzhan")



def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Sunkarbek", "Refsnes")




def my_function(*name):
  print("My name is  " + name[2])

my_function("Emil", "Tobias", "Sunkarbek")




def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("USA")
my_function()
my_function("Kazakhstan")




def my_function(x):
  return 5 * x

print(my_function(11))
print(my_function(2))
print(my_function(8))
>>>>>>> 340940753cd116101a948b98e5129283554737dc





<<<<<<< HEAD

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
a=("appleeee","banana")
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
=======
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
=======
txt ="Hello world"
x= txt[2:5]
print (x)

x = "Hello world"
print(len(x))

txt ="Hello world"
x=txt[0]
print (x)

txt ="Hello world"
txt=txt.upper()
print(txt)

txt="Hello world"
txt=txt.lower()
print(txt)


age = 36
txt = "My name is John, and I am {}"

print(txt.format(age))
>>>>>>> cc74ff4dc86162b91024b0c06fec7fe5959cd402
>>>>>>> 340940753cd116101a948b98e5129283554737dc
