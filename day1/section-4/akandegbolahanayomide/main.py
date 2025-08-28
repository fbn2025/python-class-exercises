score = int(input("Enter your exam score (0-100): "))

# write your if/elif/else statements here

if score >= 70:
    print("A")
elif score >= 60 and score <= 69:
    print("B")
elif score >= 50 and score <= 59:
    print("C")
elif score >= 40 and score <= 49:
    print("D")
else:
    print("F")
