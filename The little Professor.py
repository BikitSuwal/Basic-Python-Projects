import random

def main():
    
    level = get_level()
    score = 0 

    for i in range(5):
        x = random.randint(1, level * 10 )
        y = random.randint(1, level * 10)
        answer = x + y

        if correct_answer(x, y, answer):
            score +=1

    print(f"Final score: {score}")

def get_level():
    while True:
        try:        
            level = int(input("Level (1 - 3): "))
            if level < 1 and level > 3:
                print("NO level as entered")
                continue
            return level
        except ValueError:
            print("Invalin input")


def correct_answer(x, y, answer):

    attemps = 0 
    while attemps < 3:
        try:
            
            user_answer = int(input(f"{x} + {y} = "))
            if user_answer == answer:
                return True
            else:
                print("EEE")
                attemps +=1
                
        except ValueError:
            print("EEE")

    print(f"{x} + {y} = {answer}")
    return False

if __name__=='__main__':
    main()