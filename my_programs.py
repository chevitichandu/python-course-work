
# my_programs.py

def armstrong_number():
    print(" Program: Armstrong Number")
    print("""
def is_armstrong(num):
    s = 0
    temp = num
    while temp > 0:
        d = temp % 10
        s += d ** len(str(num))
        temp //= 10
    return s == num
""")
    print(" Test Case 1: is_armstrong(153) → True")
    print(" Test Case 2: is_armstrong(123) → False")
    print(" Explanation: Sum of digits raised to the power of total digits equals the number.")

def swap_numbers():
    print(" Program: Swap Two Numbers")
    print("""
def swap(a, b):
    a, b = b, a
    return a, b
""")
    print(" Test Case 1: swap(10, 20) → (20, 10)")
    print(" Test Case 2: swap(-5, 3) → (3, -5)")
    print(" Explanation: Uses tuple unpacking to swap without temp variable.")

def count_vowels():
    print(" Program: Count Vowels in String")
    print("""
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)
""")
    print(" Test Case 1: count_vowels('hello') → 2")
    print(" Test Case 2: count_vowels('PYTHON') → 1")
    print(" Explanation: Iterates string and counts vowels.")

def gcd_two_numbers():
    print(" Program: GCD of Two Numbers")
    print("""
import math
def gcd(a, b):
    return math.gcd(a, b)
""")
    print(" Test Case 1: gcd(54, 24) → 6")
    print(" Test Case 2: gcd(10, 5) → 5")
    print(" Explanation: Uses Euclidean algorithm via math.gcd.")

def reverse_number():
    print(" Program: Reverse a Number")
    print("""
def reverse_num(n):
    return int(str(n)[::-1])
""")
    print(" Test Case 1: reverse_num(123) → 321")
    print(" Test Case 2: reverse_num(400) → 4")
    print(" Explanation: Converts number to string, reverses, converts back.")

def count_words():
    print(" Program: Count Words in a Sentence")
    print("""
def count_words(s):
    return len(s.split())
""")
    print(" Test Case 1: count_words('Hello World') → 2")
    print(" Test Case 2: count_words('Python is fun to learn') → 5")
    print(" Explanation: Splits sentence by spaces and counts words.")

def title_case():
    print(" Program: Convert String to Title Case")
    print("""
def to_title(s):
    return s.title()
""")
    print(" Test Case 1: to_title('hello world') → 'Hello World'")
    print(" Test Case 2: to_title('python programming') → 'Python Programming'")
    print(" Explanation: Uses built-in title() to capitalize words.")

def palindrome_check():
    print(" Program: Palindrome Check")
    print("""
def is_palindrome(s):
    return s == s[::-1]
""")
    print(" Test Case 1: is_palindrome('madam') → True")
    print(" Test Case 2: is_palindrome('hello') → False")
    print(" Explanation: A string is palindrome if it equals its reverse.")

def factorial():
    print(" Program: Factorial of a Number")
    print("""
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)
""")
    print(" Test Case 1: factorial(5) → 120")
    print(" Test Case 2: factorial(0) → 1")
    print(" Explanation: Uses recursion to calculate factorial.")

def fibonacci():
    print(" Program: Fibonacci Series")
    print("""
def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a+b
    return seq
""")
    print(" Test Case 1: fibonacci(5) → [0,1,1,2,3]")
    print(" Test Case 2: fibonacci(7) → [0,1,1,2,3,5,8]")
    print(" Explanation: Iteratively builds Fibonacci sequence.")

def decimal_to_binary():
    print(" Program: Convert Decimal to Binary")
    print("""
def to_binary(n):
    return bin(n).replace('0b','')
""")
    print(" Test Case 1: to_binary(10) → '1010'")
    print(" Test Case 2: to_binary(7) → '111'")
    print(" Explanation: Uses bin() and strips '0b' prefix.")

def prime_check():
    print(" Program: Prime Number Check")
    print("""
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
""")
    print(" Test Case 1: is_prime(7) → True")
    print(" Test Case 2: is_prime(10) → False")
    print(" Explanation: Checks divisibility up to √n.")

def custom_sort():
    print(" Program: Custom Sorting (Descending)")
    print("""
def custom_sort(lst):
    return sorted(lst, reverse=True)
""")
    print(" Test Case 1: custom_sort([3,1,4,2]) → [4,3,2,1]")
    print("Test Case 2: custom_sort([10,5,8]) → [10,8,5]")
    print(" Explanation: Uses sorted() with reverse=True.")

def largest_in_list():
    print(" Program: Largest Element in a List")
    print("""
def largest(lst):
    return max(lst)
""")
    print(" Test Case 1: largest([1, 5, 3]) → 5")
    print(" Test Case 2: largest([10, 20, 15]) → 20")
    print(" Explanation: Uses max() to find largest element in list.")

def temperature_conversion():
    print(" Program: Temperature Conversion")
    print("""
def c_to_f(c):
    return (c * 9/5) + 32
def f_to_c(f):
    return (f - 32) * 5/9
""")
    print(" Test Case 1: c_to_f(0) → 32.0")
    print(" Test Case 2: f_to_c(212) → 100.0")
    print(" Explanation: Applies standard Celsius ↔ Fahrenheit formulas.")


