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
