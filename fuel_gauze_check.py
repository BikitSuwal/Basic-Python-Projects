def main():
    fraction = get_int("fraction(max-4/4): ")
    print(f"Fuel : {fraction}%")

def get_int(prompt):
    while True:
        try:
            fraction = input(prompt)
            x,z = fraction.split("/")
            x = int(x)
            z = int(z)

            if z == 0:
                print("Error")
                continue

            fuel = round((x / z) * 100)
            if fuel  >= 0 and fuel <= 100:
                return fuel
        
        except (ValueError, ZeroDivisionError):
            print("Invalid input")

if __name__ == "__main__":
    main()
            