# Put your code here
import random

name = raw_input("What is your name? ")
while True:
    try:
        guess = int(raw_input("%s, I'm thinking of a number between 1 and 100. Try to guess my number. " % name))
        break
    except ValueError:
        print("I'm not sure that was a number. Try again: ")


#generate random number
random_number = random.randint(1, 100)
print random_number
count = 1

#loop
while guess != random_number:
    if random_number > guess:
        print "too low"
    else: 
        print "too high"
    while True:
        try:
            guess = int(raw_input("Guess again: "))
            break
        except ValueError:
            print("I'm not sure that was a number. Try again: ")
    count += 1
    # print count


print "Well done, %s! You found my number in %s trys." % (name, count)

print "testing!"
