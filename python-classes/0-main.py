#!/usr/bin/python3
Square = __import__('0-square').Square #import module

my_square = Square(3)   
print(type(my_square))  #square values
print(my_square.__dict__)

try:
    print(my_square.size)    #exception handling
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
