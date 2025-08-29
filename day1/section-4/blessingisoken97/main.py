score = int(input("Enter your exam score (0-100): "))

# write your if/elif/else statements here


if score > 100 or score < 0:
    print("Invalid score! Please enter a value between 0 and 100.")
elif score >= 70:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
elif score >= 40:
    print("D")
else:
    print("F")
