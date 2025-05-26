amount_due = 50  # Amount due in cents
print("Amount due: ", amount_due)
while amount_due > 0:
    coin = int(input("Insert coin:  "))
    if coin in [25,10,5]:
        amount_due -=coin
        if amount_due > 0:
            print("Amount due: ", amount_due)
        else:
            print("Change owed: ",amount_due)
    else:
        print("Invalid coin.")

