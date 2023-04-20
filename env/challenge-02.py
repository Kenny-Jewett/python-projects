from functools import reduce



# def my_func(params):
#     print(f"I love {params}")

# my_func("args")


# my_list = [2, 5, 7 , 32, 100, 9, 56, 74, 97, 22, 13, 80]

# evens = list(filter(lambda x: x % 2 == 0, my_list))

# print(evens)

# by_3 = list(map(lambda x: x * 3, my_list))

# print(by_3)

# my_reduce = reduce(lambda x, y: x + y, my_list)

# print(my_reduce)

def is_palindrome(str): 
   lower_str = str.lower()   
   clean_str = reduce(lambda x, y: x + y, lower_str.split(" "))

   if clean_str[::-1] == clean_str:
      return True
   else:
      return False
     
   
    
# user_str = input("Enter a string to check if it is a palindrome: ")    

# is_palindrome(user_str)

my_palindromes = ["kayak", "deified", "rotator", "not a palindrom", "Poor Dan is in a droop", "We panic in a pew"]


def palindrom_list(arg):
   i = 0
   while i < len(arg):
    print(is_palindrome(arg[i]))
    i += 1

palindrom_list(my_palindromes)