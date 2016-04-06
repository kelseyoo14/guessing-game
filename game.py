# Put your code here
from random import randint

# function for prompting guessing, using recursion with a counter
def guessing(num, count=1):
    # test to make sure guess is an integer
    try:
        guess = int(raw_input("Take a guess: "))
    except ValueError:
        print("Was that a number? Try again.")
        return guessing(num, count)
    # if integer, check if too high, too low, between 1 and 100, mocking user
    if guess != random_number:
        if guess < 1 or guess > 100:
            print("You idiot!! Please pick a number between 1 and 100.")
            return guessing(num, count)
        else:
            if num > guess:
                print "too low"
                #count += 1
                return guessing(num, count+1)
            else: 
                print "too high"
                #count += 1
                return guessing(num, count+1)
            count += 1
    else:
        return count


# Initial prompt
name = raw_input("What is your name? ")
print("Hi %s. I'm thinking of a number between 1 and 100." % name)

# playing loop
play = True
while play:
# generate random number
    random_number = randint(1, 100)
    # for testing
    # print random_number
    count = guessing(random_number)
    print "Well done, %s! You found my number in %s trys." % (name, count)
    answer = raw_input("Would you like to play again? (y/n): ")
    if answer.lower() == "y":
        continue
    else:
        play = False