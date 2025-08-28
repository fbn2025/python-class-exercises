Exam = int(input("What is your exam score? "))

if Exam >= 70:
    print ("you got A")

elif Exam >= 60 and Exam <= 69:
    print("You got B")

elif Exam >= 50 and Exam <= 59:
    print("You got C")

elif Exam >= 40 and Exam <= 49:
    print("You got D")

else:
    print("You got F")
