import random
x=random.randint(1,9)
y=int(input("Enter your guess from 1 to 9: "))
chances=1
while chances < 5:
    if y == x:
        print("Congratulations!! YOU WON! You guessed the number in "+str(chances)+" chances.")
        break
    elif y > x:
        print("Try again. Your guess was too high.")
        y=int(input("Enter your guess less than "+str(y)+":"))
        chances=chances+1
    elif y < x:
        print("Try again. Your guess was too low.")
        y=int(input("Enter your guess more than "+str(y)+":"))
        chances=chances+1
    if not chances < 5:
        print("YOU LOST! Better Luck Next time. The number was "+str(x))
        break
