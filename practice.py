num = 5+2.5
print(num)
print(type(num))

#7.5
#'float'


num_int =int(5.7)
print(num_int)

#5

num_float = float("3.14")
print(num_float)
print(type(num_float))
num_str=str(num_float)
print("converted value:",num_float)


#3.14
#'float'

message = str(42)
print(message)
print(type(message))


#42
#str

is_true=bool(1)
is_false=bool(0)
print(is_true)   #true
print(is_false)  #false
print(type(is_true),type(is_false))


#<class 'bool'> <class 'bool'>


#non_numeric_string ="hello"
#num_int=int(non_numeric_string)
#print("Converted value:",num_int)

#ValueError: invalid literal for int() with base 10: 'hello'

char_a = 'A'
ascii_value_a =ord(char_a)
print("ASCII value of 'A' is:",ascii_value_a)

#ASCII value of 'A' is: 65

char_b ='B'
ascii_value_b=ord(char_b)
print("ASCII value of 'B' is:",ascii_value_b)

#ASCII value of 'B' is: 66

