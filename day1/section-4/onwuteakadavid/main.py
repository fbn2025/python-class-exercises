score = int(input("Enter your exam score (0-100): "))

# write your if/elif/else statements here
if score >= 70:
    print("A")
elif score < 70 and score >= 60 :
    print("B")
elif score < 60 and score >= 50 :
    print("C")
elif score < 50 and score >= 40 :
    print("D")
else :
    print("F")
