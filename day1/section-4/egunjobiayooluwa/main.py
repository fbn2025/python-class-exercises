def gradingSystem ():
    score = float(input("Enter your score (0-100): "))

    if score >= 70 and score <= 100:
        print('You had an excellent performance in your exam. Your grade is A')
    elif score >= 60 and score < 70:
        print('You had a very good performance in your exam. Your grade is B')
    elif score >=50 and score < 60:
        print('You had a good performance in your exam. Your grade is C')
    elif score >=40 and score < 50:
        print('You had a poor performance in your exam, please try harder next time. Your grade is D')
    elif score >= 0 and score < 40:
        print('You failed your exam. Your grade is F')
    else:
        print('You entered an invalid score. Please enter a score between 0 and 100.')
        gradingSystem()

gradingSystem()
