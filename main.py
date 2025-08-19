import my_programs as mp

def menu():
    print("\n------ FUNCTION MENU ------")
    print("1. Armstrong Number")
    print("2. Swap Two Numbers")
    print("3. Count Vowels in String")
    print("4. GCD of Two Numbers")
    print("5. Reverse a Number")
    print("6. Count Words in a Sentence")
    print("7. Convert String to Title Case")
    print("8. Palindrome Check")
    print("9. Factorial")
    print("10. Fibonacci Series")
    print("11. Convert Decimal to Binary")
    print("12. Prime Number Check")
    print("13. Custom Sorting")
    print("14. Largest in a List")
    print("15. Temperature Conversion")
    print("0. Exit")
    print("----------------------------")

while True:
    menu()
    choice = input("Enter your choice: ")
    
    if choice == "1": mp.armstrong_number()
    elif choice == "2": mp.swap_numbers()
    elif choice == "3": mp.count_vowels()
    elif choice == "4": mp.gcd_two_numbers()
    elif choice == "5": mp.reverse_number()
    elif choice == "6": mp.count_words()
    elif choice == "7": mp.title_case()
    elif choice == "8": mp.palindrome_check()
    elif choice == "9": mp.factorial()
    elif choice == "10": mp.fibonacci()
    elif choice == "11": mp.decimal_to_binary()
    elif choice == "12": mp.prime_check()
    elif choice == "13": mp.custom_sort()
    elif choice == "14": mp.largest_in_list()
    elif choice == "15": mp.temperature_conversion()
    elif choice == "0":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
