import random
import time 
import os
import msvcrt 
def clear_keyboard_buffer(): 

    """Remove any pending keystrokes from the keyboard buffer.""" 

    while msvcrt.kbhit(): 

        msvcrt.getwch() 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    clear_keyboard_buffer()
digilist = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
turn = 1
word = ""
answer = ""
def ans_check(word,answer):
    if word == answer:
        return True
    else:
        return False
def display():
    print(f"Round reached: {turn}")
    print(f"correct answer: {word}")
    print(f"Your answer: {answer}")    
    if turn ==1:
        print("That was a missclick, right?")
    elif  turn <= 4:
        print("Do you understand the concept of, memory?")
    elif turn <8 and turn >4:
        print("Not bad, but also not good")
    elif turn >100:
        print("How did you even do that?")
    else:
        print("Hey, that's pretty good")
while True:
    if turn == 1:
        terminate = input("play or quit (p or q respectively)").lower().strip()
        if terminate == "q":
            break
        elif terminate == "p":
            pass
        else:
            print("error, try again")
    else:
        pass
    clear()
    word = random.choice(digilist)
    word += random.choice(digilist)
    word += random.choice(digilist)
    times = turn
    while times != 0:
        word += (random.choice(digilist))
        times -= 1    
    print(f"level {turn}\nword: {word}")
    for i in ".....":
        print(i,end="",flush=True)
        time.sleep(1)
    clear()
    answer = input("Enter the string you just saw (case insensitive): ").lower().strip()  
    word = word.lower().strip()
    good = ans_check(word,answer)
    if good == True:
        print("Good Job")
        time.sleep(3)
        turn += 1
    else:
        clear()
        print("Nope")
        time.sleep(1)
        clear()
        while True:
            display()
            yn = input("play again? y or n:").strip().lower()
            if yn == "y":
                turn = 1
                break
            elif yn == "n":
                print("have a good day")
                break
            else:
                print("error")
        if yn == "n":
            break
        else:
            pass