import random

num = random.randint(1,1000)
x=0   
for i in range(1000):
    guess = int(input("Please guess a number: "))
    if guess == num:
        print("correct!")
        break
    elif guess < num:
        print("Too Low")
        x=x+1
    elif guess > num:
        print("Too High")
        x=x+1
print(x)
print(num)
