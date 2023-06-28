def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ", answer)


score = 0
print("Guess the Animal")
guess1 = input("What color is polar bear skin? ")
check_guess(guess1, "black")
guess2 = input("Which bear lives at the North Pole? ")
check_guess(guess2, "polar bear")
guess3 = input("Which is the fastest land animal? ")
check_guess(guess3, "Cheetah")
guess4 = input("Which is the largest animal? ")
check_guess(guess4, "Blue Whale")
guess5 = input("The only mammal capable of flight is ")
check_guess(guess5, "Bat")
guess6 = input("Which animal has four noses? ")
check_guess(guess6, "Slugs")
guess7 = input("Which animal doesn't have a brain? ")
check_guess(guess7, "Starfish")
guess8 = input("Which animal doesn't stick their tongue out? ")
check_guess(guess8, "Crocodiles")
guess9 = input("Which bird can fly backwards? ")
check_guess(guess9, "Hummingbird")
guess10 = input("Which animal can jump 350 times its body length? ")
check_guess(guess10, "Fleas")
print("Your Score is " + str(score))