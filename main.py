import random

max_num = 10

while True:
    command = ''
    num = random.randint(1,max_num)
    print(f"Okay, try to guess number that i'm thinking about, it's between 1 and {max_num}")
    while True:
        your_num = input()
        your_num = int(your_num)
        if(your_num == num):
            print("You are so motherfucking correct!!")
            break
        elif(your_num < num):
            print("Too low")
        elif(your_num > num):
            print("Too high")
        else:
            print("nope, try again")
    while True:
        command = input("Do you want to continue?(y/n): ")
        print(command)
        if((command == "n") or (command == "y")):
            break
        else:
            print("Wrong command try  again")
    if(command == "n"):
        break