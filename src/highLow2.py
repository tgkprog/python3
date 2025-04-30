import random
import sys
from datetime import datetime
def main2():
    numMax = int(input("Enter max of my (Compe's) secret number for our high-low game :"));
    numLow = int(input("Enter min of my secret number :"));
    if numMax < 0:
        numMax = 10;
    if numLow > numMax:
        numLow = numMax - 20;
    randInt = random.randint(numLow, numMax)
    print(f"I Compe have guessed a number between {numMax} and {numLow}")
    diff = numMax - numLow
    if diff < 5:
        print(f"Not much of a spread, only {diff}; quite easy to guess  :-), lets play")
    guess = randInt + 1
    while guess != randInt:
        guess = int(input ("Enter your guess of my number :"));
        if guess == randInt:
            now = datetime.now()
            formattedDate = now.strftime("%Y-%b-%d %H:%M:%S")
            print (f"On {formattedDate} you got Compe's number. It was {guess} yay! bye.");
            sys.exit();
        elif guess < randInt:
            if guess < numLow:
                print(f"Your guess {guess} is lower than lower bound {numLow} too")
            else:
                print(f"Your guess {guess} is lower than my number")
        else:
            if guess > numMax:
                print(f"Your guess {guess} is higher than the higher bound {numMax} too")
            else:
                print(f"Your guess {guess} is higher than my number")
            



if __name__ == '__main__':
    main2()