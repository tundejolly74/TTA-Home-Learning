# Write your code here :-)
# store a random number(1-10)in a variable
import random
myName = input("Hello! What is your name? ")
number = random.randint(1, 10)
print("Well," + myName + "I am thinking of a number between 1 and 10.")
guess = int(input("Take a guess."))

if guess == number:
    print("Good job, + myName +  you guessed my number")
elif guess:
    print("Wrong,better luck next time")




