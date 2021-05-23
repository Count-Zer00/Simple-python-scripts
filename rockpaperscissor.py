import random

while True:
    Input = input("Rock, Paper or Scissors?: ")
    Choice = ['Rock', 'Paper', 'Scissors']
    cpu = random.choice(Choice)

    print(f"you chose {Input} and computer chose {cpu}\n")


    if Input == cpu:
        print(f"Tie! {Input}")

    elif Input == "Rock":
        if cpu == "Scissors":
            print("You win!")
        else:
            print("you lose!")

    elif Input == "Paper":
        if cpu == "Rock":
            print("You win!")
        else:
            print("you lose!")

    elif Input == "Scissors":
        if cpu == "Paper":
            print("You win!")
        else:
            print("you lose!")


