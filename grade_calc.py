num_questions = int(input("Please enter the number of questions: \n"))

num_right = int(input("Please enter the number you got right: \n"))


grade = num_right/num_questions * 100

print("Your grade was " + str(grade))
