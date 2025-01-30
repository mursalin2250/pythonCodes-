from random import randint
secretNumber = randint(1, 101)
print("Welcome to guess the number game.")
while True:
    guess = int(input("Enter your guess: "))
    if guess == secretNumber:
        print("Good Job!")
        break
    elif guess > secretNumber:
        print("You guessed a higher number.")
    elif guess < secretNumber:
        print("You guessed a lower number.")