expression = input("Expression: ")

x,y,z = expression.split()

x = int(x)
z = int(z)

if y == "+":
    print(f"{x+z:.2f}")

elif y == "-":
    print(f"{x - z:.2f}")

elif y == "*":
    print(f"{x * z:.2f}")

elif y == "/":
    if z == 0:
        print("Error: Division by zero")
    else:
        print(f"{x / z:.1f}")
else:
    print("Error: Invalid operator")
