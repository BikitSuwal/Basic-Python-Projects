menu = {
    'baja taco' : 4.25,
    'burrito' : 6.25,
    'owl' : 7.25,
    'quesadilla' : 5.25,
    'nachos' : 6.75,
    'salad' : 5.75,
    'chips' : 2.25,
    'salsa' : 0.75,
    'guacamole' : 1.50,
    'drink' : 1.50,
    'catering' : 250.00,
    'taco' : 3.25,
}
for i in menu:
    print(f"{i.title()}: ${menu[i]:.2f}")
def main():
    total = 0.0
    print("Welcome to the taco stand!")
    print("Here is the menu:")
    print("Press CTRL + D + Enter to finish your order.")
    while True:
        try:
            item = input("Item: ").lower().strip()
            if item in menu:
                total += menu[item]
                print(f"Added {item} for ${menu[item]:.2f}. Current total: ${total:.2f}")
            else:
                print(f"Sorry, we don't have {item} on the menu.")
        except EOFError:
            print('Order Complete.')
            print(f"Your total is ${total:.2f}.")
            break

if __name__ == "__main__":
    main()  
