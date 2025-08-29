# Get the score
score = float(input("What is your exam score: "))

# Get grade when score is above 70
if score >= 70:
    print("Your Grade is A")

# Get grade when score is from 60 to 69
elif score >= 60:
    print("Your Grade is B")

# Get grade when score is from 50 to 59
elif score >=50:
    print("Your Grade is C")

# Get grade when score is from 40 to 49
elif score >= 40:
    print("Your Grade is D")

# Get grade when score is below 40
else:
    print("Your Grade is F")
