# Python program to perfrom Addition, Subtraction, etc.

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
print("Enter which operation would you like to perform? ")
ch = input("Enter any of these characters for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
   result = num1 / num2

else:
    print("char is not supported")

print(num1, ch, num2, ":", result)






