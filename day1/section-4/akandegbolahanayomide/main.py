score = int(input("Enter your exam score (0-100): "))

# write your if/elif/else statements here

if score >= 70:
    print("You are doing exceptionally well. Your Grade is A")
elif score >= 60 and score <= 69:
    print("Keep it up. Your Grade is B")
elif score >= 50 and score <= 59:
    print("You’re making progress. Aim higher! Your Grade is C")
elif score >= 40 and score <= 49:
    print("Needs improvement. Stay focused! Your Grade is D")
else:
    print("Don’t give up! Work harder next time. Your Grade is F")
