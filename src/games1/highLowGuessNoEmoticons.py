import random
"""
To try this on Whatsapp Send a whatsapp message to...
+1 (415) 728-3856
With the text message...
54F5KF
Can use the link : https://wa.me/14157283856?app_absent=web&text=54F5KF&source=sel2in
Whats app web works too.
"""

def main():
    num_rounds = 0 # actually played, end message depends on this
    msg = """              Welcome to the High-Low Game!\n           ----------------------------------\n\n
    Type quit or q to not guess and quit or 
    Type h or higer to guess that your number is higher than the computer's number or 
    l, m or lower to guess that your number is lower than the computer's number. 
    
    After 5 round's your asked to enter how many rounds more or if you want to stop (0 or n or q)
    In each round the computer pick's a random number for itself and you. Let the better guesser win.
    We only parse the first letter of input so hi is taken as higher. and q or qui is taking as quit
    
    Enter y if want answers for testing/ study the flows : """
    cheat = (input(msg).lower() + ' ')[0]
    score = 0
    round_num = 1 # for printing round number, this is nearly the same as num_rounds, could have used just 1
    rounds_left = 5 # this is for the while loop to count how many in to ask in current loop. its not a constant as after current loop we ask user how many more rounds they want to play (or if they want to quit)
    curr_rounds = 1 # for the while loop again, counter of how many of rounds_left left.
    while curr_rounds  <= rounds_left:
        player_num = random.randint(1, 100)
        comp_num = random.randint(1, 100)
        clue = ''
        if(cheat == 'y'):
            clue = f'  C {comp_num}' # for debugging the flows and to see the flows
        print(f"Round {round_num}\nYour number is {player_num}{clue}")
        guess = ''
        while guess == '' or guess == 'n':
            if(guess == ''): # first time asking this round
                # make sure atleast one char in guess and lower case it so easy to compare first char
                guess = input("Do you think your number is higher or lower than the computer's?: ").lower() + " " 
            else:
                guess = input("Please enter either higher (h) or lower(l/m) or q: ").lower() + " "
            guess = guess[0] # only interestested in first char of guess
            if guess != 'h' and guess != 'l' and guess != 'm' and guess != 'q' :
                guess = 'n'
        if guess == 'q':
            break # user does not want to guess and stop playing now

        if (guess == 'h' and player_num > comp_num) or ((guess == 'l' or guess == 'm') and player_num < comp_num):
            print(f"You were right! The computer's number was {comp_num}")
            score += 1 
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")
        print(f"Your score is now {score}")
        if guess != 'q':
            num_rounds += 1
        round_num += 1        
        if curr_rounds == rounds_left:
            curr_rounds = 1
            play = input("\nEnter how many more rounds you'd like to play, or type 0, 'n', 'q', or 'no' to stop :").lower()
            c = (play + ' ')[0]
            if(c == 'n' or c == 'q' or c == '0'):
                break
            elif c == 'y' or c == ' ':
                rounds_left = 5
            else:
                try:                
                    play = int(play)  # try to convert to integer                
                    rounds_left = play
                except ValueError:
                    # print("Not a number")
                    p = ((play + " ").lower())[0]
                    if p == 't' and p == 'y':
                        rounds_left = 0
                    else:
                        print("Could not parse so assume 5 more plays! Enter q in guess to quit.")
                        rounds_left = 5
        else:
            curr_rounds += 1
        print()
        
    
    if(num_rounds < 1):
        msg = ("Bye!")
    elif (num_rounds < 2):
        msg = ("Thanks for playing!")
    else:
        # using half as mid rounded up for round down use (num_rounds // 2)
        half = round(num_rounds / 2, 0)
        if(score == num_rounds and num_rounds > 3):
            msg = ("Wow! You played perfectly!")
        elif (score > half):
            msg = ("Good job, you played really well!")
        elif (score == half):            
            msg = "Well done, half were correct."
        else:
            msg = ("Better luck next time!")
    m2 = ''
    if cheat == 'y':
        m2 = '\n\nCheats were on though'
    print(f"\n{num_rounds} round(s) completed, score : {score}\n\n{msg}{m2}")    
if __name__ == "__main__":
    main()