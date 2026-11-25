# STEP 1: Welcome
# print() shows words on the screen. Words go inside quote marks.
#
#   print("Welcome to the Pizza Quiz!")
#
# Your turn: print a welcome for your own quiz.



# STEP 2: Ask their name
# input() asks a question and saves the answer in a variable.
#
#   name = input("What is your name? ")
#   print("Hello", name)
#
# Your turn: ask for the player's name and say hello.



# STEP 3: First question
# if / else lets the program decide. Don't forget the colons and the
# indent. Use two equals signs ==
#
#   answer = input("What is the capital of France? ")
#   if answer == "Paris":
#       print("Correct!")
#   else:
#       print("Wrong!")
#
# Your turn: ask your own question. Type the answer exactly,
# including capital letters.



# STEP 4: Keep score
# A variable can store the score. Start it at 0, add 1 for a right answer.
#
#   score = 0                  <- put this ABOVE your question
#
#   if answer == "Paris":
#       print("Correct!")
#       score = score + 1      <- add this line
#
# Your turn: add a score to your question, then at the very bottom
# of your file add:
#
#   print("Your score is", score)



# STEP 5: More questions
# Copy your question and paste it 3 times. Change the question and the
# answer each time. Don't copy score = 0 again!
#
# Your turn: you should end up with 4 questions.



# STEP 6: Final message
# Put this at the very bottom, with your own words:
#
#   if score == 4:
#       print("Perfect!")
#   else:
#       print("Good try!")
#
# Your turn: add your own final message.



# FINISHED? Pick an extra:
#
# EXTRA 1: Use the player's name at the end.
#   print("Well done,", name)
#
# EXTRA 2: Players can type paris instead of Paris. Add .lower()
#   after the input, and make your right answer lowercase.
#
#   answer = input("What is the capital of France? ").lower()
#   if answer == "paris":
#
# EXTRA 3: Swap seats and play your partner's quiz. Try to break it.