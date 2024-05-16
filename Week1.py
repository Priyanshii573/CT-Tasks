# TASK 1
# Largest no. among three no.

def find_max(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    max_number = find_max(num1, num2, num3)
    print("The maximum number among", num1, ",", num2, "and", num3, "is:", max_number)

main()



# TASK 2
# Reverse of a string

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

def main():
    input_string = input("Enter a string: ")
    reversed_string = reverse_string(input_string)
    
    print("Reversed string:", reversed_string)

main()









