
# Day 2 - Personal Details and Calculator

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n--- Personal Details ---")
print(f"Name: {name}")
print(f"Age: {age}")

num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n--- Calculator Results ---")
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")

if num2 != 0:
    print(f"Division: {num1 / num2}")
else:
    print("Division is not possible because the second number is zero.")
