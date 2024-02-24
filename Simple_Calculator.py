print("Select your choice of operation to perform.")
print("1-Add\n2-Subtract\n3-Multiply\n4-Divide\n5-Modulus")

while(1):
    choice = int(input("Enter choice(1/2/3/4/5): "))

    if choice in (1,2,3,4,5):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            print(num1, "+", num2, "=", (num1+num2))

        elif choice == 2:
            print(num1, "-", num2, "=", (num1-num2))

        elif choice ==3:
            print(num1, "*", num2, "=", (num1*num2))

        elif choice == 4:
            print(num1, "/", num2, "=", (num1/num2))

        elif choice == 5:
            print(num1, "%", num2, "=", (num1%num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")