import random


def is_valid_number(s):
    if s.isdigit() and 1 <= int(s) <=100:
        return True
    else:
        return False



def main():
    number = random.randint(1,100)
    guessed_number = False
    guess = input("Guess a number from 1 to 100: ")
    number_guess = 0
    while not guessed_number:
        if not is_valid_number(guess):
            guess = str(input("I won't count that one. A number between 1 and 100: "))
        else:
            number_guess +=1
            guess = int(guess)
        if guess < number:
            guess = str(input("Too low. Guess again: "))
        elif guess > number:
            guess = str(input("Too high. Guess again:  "))
        else:
            print("You got it in" ,number_guess," guesses!")
            guessed_number = True
    print("Thanks for playing.")

if __name__ == '__main__':
    main()
