from functools import reduce

def multiply_list(numbers):
    if not numbers:
        return None
    return reduce(lambda x, y: x * y, numbers)

my_list = [1, 2, 3, 4, 5]
result = multiply_list(my_list)
print("The product of all numbers in the list:", result)









def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


input_string = "Hello World"
upper, lower = count_upper_lower(input_string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)












def is_palindrome(string):
    
    processed_string = string.lower().replace(" ", "")
    
    return processed_string == processed_string[::-1]


input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")










import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")


number = 25100
milliseconds = 2123
delayed_square_root(number, milliseconds)











def all_true(tup):
    return all(elem for elem in tup)


my_tuple = (True, True, True, True)
print(all_true(my_tuple))  

my_tuple = (True, False, True, True)
print(all_true(my_tuple))  



