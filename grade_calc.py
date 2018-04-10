num_questions = int(input("Please enter the number of questions: \n"))

num_right = int(input("Please enter the number you got right: \n"))


grade = num_right/num_questions * 100

if grade >= 90:
    print("Your grade was {} A".format(str(grade)))
elif grade < 90 or grade >=80:
    print("Your grade was {} B".format(str(grade)))
elif grade < 80 or grade >=70:
    print("Your grade was {} C".format(str(grade)))
