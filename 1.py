
#1
mytuple = ("ford","bmb","mustang")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
=======

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






