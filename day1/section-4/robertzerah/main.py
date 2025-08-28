score = int(input("Enter your exam score (0-100): "))

# write your if/elif/else statements here
#70 and above → "A"
#60–69 → "B"
#50–59 → "C"
#40–49 → "D"
#below 40 → "F"

if score >= 70:
    print("Your grade is A")
elif score >= 60:
    print("Your grade is B")
elif score >= 50:
    print("Your grade is C")
elif score >= 40:
    print("Your grade is D")
else:
    print("Your grade is F")
