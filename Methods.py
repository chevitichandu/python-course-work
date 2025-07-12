#  1.Case Conversion Methods

text="hello world"
print(text.upper())
#HELLO WORLD

text="HELLO WORLD"
print(text.lower())
#hello world

text="hello world"
print(text.capitalize())
#Hello world


text="hello world"
print(text.title())
#Hello World

text="HeLlO wOrLd"
print(text.swapcase())
#hElLo WoRlD


# 2.Alignment & Formatting Methods

text="hello"
print(text.ljust(10,'-'))
#hello-----
text="hello"
print(text.ljust(10,'+'))
#hello+++++

text="hello"
print(text.rjust(10,'+'))
#+++++hello
text="hello"
print(text.rjust(10,'-'))
#-----hello

# 3.Search & Find Methods
text = "hello world"
print(text.find("hello"))
#0
print(text.find("world"))
#6
print(text.find("hello world"))
#0

text = "hello world hello"
print(text.rfind("hello"))
#12
print(text.rfind("world"))
#6

text = "Python is fun. Python is powerful."
print(text.index("Python"))
#0
print(text.index("Python",6))
#15

text = "abc abc abc"
print(text.rindex("abc"))
#8

text = "apple banana apple mango apple"
print(text.count("apple", 10))
#2
print(text.count("banana"))
#1
print(text.count("mango"))
#1







