# write your if/elif/else statements here
"""
score exercise
THis program will ask the user to input their score
and it will print out their grade based on the score 
A: 70 and above
B: 60 - 69
C: 50 - 59
D: 40 - 49
F: below 40
"""
score = int(input ("Enter your exam score(0-100): ")) 
if score >= 70:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
elif score >= 40:
    print("D")
elif score < 40:
    print("F")
else:
    print("Enter your correct score!")
