name = input("What is your name? ")
print()   # adds a blank line

age = int(input("How old are you? "))  # convert to integer
print()

interest1 = input("What is your first interest? ")
print()

interest2 = input("What is your second interest? ")
print()

interest3 = input("What is your third interest? ")
print()


combined = (
    f"Your name is {name}, you are {age} years old, "
    f"and your interests are {interest1}, {interest2}, and {interest3}."
)

print(combined)
