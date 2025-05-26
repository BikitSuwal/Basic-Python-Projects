import random

def main():
    while True:
        try:
            level = int(input("Level:"))
            if level < 1:
                continue
            else:
                break
        except ValueError:
            pass
    
    num = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess:"))
            if guess < 1:
                continue
            elif guess < num:
                print("Too small!")
            elif guess > num:
                print("Too large!")
            else:
                print("Just right!")
        except ValueError:
            pass

if __name__ == "__main__":
    main()  