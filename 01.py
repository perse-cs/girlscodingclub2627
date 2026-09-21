print("Welcome to this very fun quiz!")

score = 0

answer1 = input("Which word is spelled incorrectly in the dictionary? ")
if answer1 == "incorrectly":
    print("Correct :)")
    score = score + 1
else:
    print("Incorrect")

# ==> ADD MORE OF YOUR OWN QUESTIONS - BE AS CREATIVE AS YOU LIKE (WITH THE QUESTIONS AND THE SCORING)

print("That is the end of this very fun quiz")
print("Your score is", score)
