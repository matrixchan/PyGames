# -*- coding: utf-8 -*-
import random

def main():
    print("Hello What is your name?")
    name = input()
    print("Well, "+name+"."+"I am thinking of a number between 1 and 20")

    counter = 0
    number = random.randint(1,20)

    while counter < 6:
        print("Take a guess")
        guess = int(input())
        counter = counter + 1
        if guess > number:
            print("Your guess is too high.")
        if guess < number:
            print("Your guess is too low.")
        if guess == number:
            print("Good job, "+name+".You guessed my number in "+str(counter) + " guess")
            break
        
    if guess != number:
        number = str(guess)
        print('Noope, The number I was thinking of was ' + number)

    #print(number)
    #print(guess)

if __name__ == '__main__':
    main()
