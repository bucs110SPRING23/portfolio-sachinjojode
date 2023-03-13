import random

num = random.randint(1,10)
    
for i in range(3):
    guess = int(input("Please guess a number: "))
    if guess == num:
        print("correct!")
        break
    elif guess < num:
        print("Too Low")
    elif guess > num:
        print("Too High")