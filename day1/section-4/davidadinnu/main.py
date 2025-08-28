
#Conditionals
score = int(input("What is your score: "))

if score in range(70, 100):
    print("A")
elif score in range(60, 69):
    print("B")
elif score in range(50, 59):
    print("C")
elif score in range(40, 49):
    print("D")
else:
    print("F")

