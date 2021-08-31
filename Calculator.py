def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Select Operation \n" \
    "1. Addition\n" \
    "2. Subtraction\n" \
    "3. Multiplication\n" \
    "4. Division\n")


operation = int(input("Select Operation: 1, 2, 3, 4 :"))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if operation == 1:
    print(number1, "+", number2, "=",
                    add(num1, num2))
  
elif operation == 2:
    print(number1, "-", number2, "=",
                    subtract(num1, num2))
  
elif operation == 3:
    print(number1, "*", number2, "=",
                    multiply(num1, num2))
  
elif operation == 4:
    print(number1, "/", number2, "=",
                    divide(num1, num2))
else:
    print("Invalid Operation")