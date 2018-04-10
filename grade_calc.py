num_questions = int(input("Please enter the number of questions: \n"))

num_right = int(input("Please enter the number you got right: \n"))

# Calculates the percent of a grade for a test. 
grade = num_right/num_questions * 100

# I have no idea if this is Python 3 or 2 code.
# It works either way and I think it's easy to understand.
if (100 <= grade >= 90):
    print("Your score was {} A".format(str(grade)))
elif (80 < grade > 70):
    print("Your score was a {} B".format(str(grade)))
elif (70 <= grade > 60):
    print("Your score was a {} C".format(str(grade)))
elif (60 <= grade > 50):
    print("Your score was a {} D".format(str(grade)))
    print("You did not pass.")
else:
    print("Your score was a {} F".format(str(grade)))
    print("You did not pass.")