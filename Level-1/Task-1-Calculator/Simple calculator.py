#ad function performs addition
def ad(a, b):
    return a + b

#subtract function performs subtraction
def subtract(a, b):
    return a - b

#multiply function performs multiplication
def multiply(a, b):
    return a * b

#divide function performs division
def divide(a, b):
    if b == 0:
        return n
    return a / b

#sqrt function determines Square root of a number
def sqrt(x):
    return x ** 0.5

#percentage function used to calculate the percentage
def percentage(part, total):
    return (part / total) * 100

print("Welcome! Here is your simple calculator")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square root\n6. Percentage calcualtion")

choice = int(input("Enter you choice before performing the operation!"))

if choice == 1:
    m = int(input("Enter your 1st number : "))
    n = int(input("Enter your 2nd number : "))

    print("Addition of ", m, " + ", n, " is: ", ad(m, n))

elif choice == 2:
    m = int(input("Enter your 1st number : "))
    n = int(input("Enter your 2nd number : "))
    
    print("Subtraction of ", m, " - ", n, " is: ", subtract(m, n))

elif choice == 3:
    m = int(input("Enter your 1st number : "))
    n = int(input("Enter your 2nd number : "))
    
    print("Multiplication of ", m, " * ", n, " is: ", multiply(m, n))

elif choice == 4:
    m = int(input("Enter your 1st number : "))
    n = int(input("Enter your 2nd number : "))

    result = divide(m, n)

    if result is n:
        print("Error: cannont be divided by zero")
    else:
        print("Division of ", m, " / ", n, " is: ", result)

elif choice == 5:
    m = int(input("Enter the number to find square root: "))

    print("Square root of ", m, "is : ", sqrt(m))

elif choice == 6:
    m = int(input("Enter the part: "))
    n = int(input("Enter total: "))

    print("Percentage of ",m ,"and", n,"is : ", percentage(m, n)," %")


else:
    print("Invalid choice")
