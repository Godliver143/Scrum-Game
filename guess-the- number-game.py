import random
import  math

small = int(input("Enter a lower bound number:"))

large = int(input("Enter an upper bound number:"))

a = random.randint(small,large)

print("You have ",round(math.log(large-small +1 ,2)), "chances left to guess the number!")

count = 3

while count< math.log(large-small + 1,2 ):
    count+=1
    guess = int (input ("Guess a number:"))
    
    if a == guess:
        print("You did it in:",count, "try")
        break
    elif a > guess:
        print ("You guessed too low!")
    elif a < guess:
         print ("You guessed too high!")

if count >= math.log(large - small + 1 , 2):
    print ("The number is %d" % a)

    print("Try again some other time!")