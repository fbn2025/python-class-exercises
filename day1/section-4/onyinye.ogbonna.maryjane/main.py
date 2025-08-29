score = int(input("Enter your exam score (0-100): "))

# write your if/elif/else statements here

if score >= 70:
    print ("A")
elif score >= 60:
    print ("B")
elif score >= 50:
    print ("C")
elif score >= 40:
    print ("D")
elif score < 40:
    print ("F")
else:
    print ("Invalid number! Enter a number between 0-100")



