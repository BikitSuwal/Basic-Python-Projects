def main():
    try:
        dollars = dollar_to_float(input("How much was the price($...)? "))
        percent = percent_to_float(input("What percent woruld you like to tip? "))
        tip = dollars * percent
        print(f"Leave ${tip:.2f} tip.")
    except ValueError:
        print("Enter Price in this format: $10.00")
        print("Enter Percent in this format: 15%")
def dollar_to_float(d):
    return float(d.replace('$', '').strip())

def percent_to_float(p):
    return float(p.replace('%','').strip())/100

main()

