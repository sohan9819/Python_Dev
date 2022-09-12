# Inline Comment
""" 
Multiline Comment
"""

print("""Data Types in Python 
- int 
- string 
- boolean
- list 
- tuple
- dictonary
""")

a = "Abhiram"
print("a : " + str(type(a)))

b = 19
print("b : ", type(b))

c = [1, 2, 3, 5, -6, -3, -1]
# ?   0  1  2  4   5   6   7

c[2] = 15
print("c : ", c)  # ! [1, 2, 15, 5, -6, -3, -1]

d = ["asdas", "ASDad", "Asdas", "asDASD"]

print("c : ", type(c))
print("d : ", type(d))

e = {"S": "Sohan", "A": "Abhiram"}
print("e : ", type(e))

f = (10, 12, 13)
print("f : ", type(f))

age = 20
name = "Sohan"

# print("Hello I am ", name, ", my age is ", age)
print(f'Hello I am {name} , my age is {age}')
# print("""
# Hello I am Sohan ,
# my age is 20
#  """)
