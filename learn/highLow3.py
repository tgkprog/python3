import random
import sys
from datetime import datetime
def main():
    numMax = inputInt("Enter max of my (Compe's) secret number for our high-low game :");
    numLow = inputInt("Enter min of my secret number :");

    if numLow > numMax:
        numLow = numMax - 20;
    randInt = random.randint(numLow, numMax)
    print(f"I Compe have guessed a number between {numMax} and {numLow}")
    diff = 1 + numMax - numLow
    if diff < 5:
        print(f"Not much of a spread, only {diff}; quite easy to guess  :-), lets play")
    guess = randInt + 1
    while guess != randInt:
        
        guess = inputInt("Enter your guess of my number :");
        
     
        if guess == randInt:
            now = datetime.now()
            formattedDate = now.strftime("%Y-%b-%d %H:%M:%S")
            print (f"On {formattedDate} you got Compe's number. It was {guess} yay! bye.");
            return;
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
            
def inputInt(prompt: str):
    try:
        user_input = input(prompt)
        if len(user_input) == 0:
            return 0
        if len(user_input) > 1:
            return 0
        ch = user_input[0]
        if ord(ch) < ord('0') or ord(ch) > ord('9'):
            return 0
        return int(ch)
    except:
        return 0




if __name__ == '__main__':
    main() 