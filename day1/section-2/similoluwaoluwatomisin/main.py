#This is my Internet Profile

from math import pi

my_internet_profile = {
    "favorite_physics_constant": pi,     # float
    "twitter_handle": "https://x.com/Similoluwa_O",                # string
    "favorite_physics_constant": pi,     # float
    "age": 40,                           # integer (you can lie about this lol)
    "finished_uni": True,                  # boolean
    "hobbies": "Watching Movies, Reading",      # tuple
    "skills": ["Analytical, Adaptability"],                        # list
    "personal_quotes": "It is well",               # set (one or two)
    "contact_info": {                      # dictionary (nested)
        "phone_number": 8022965852,              # integer (you can put a fake one)
        "email": "similoluwaoluwatomisin@gmail.com",                     # string (you can put a fake one)
        "website": "Similoluwa.com",                   # string
    },
}

print(my_internet_profile)

name = input("What is your name: ")
age = input("What is your age: ")
interest1 = input("What is your number 1 interest: ")
interest2 = input("What is your number 2 interest: ")
interest3 = input("What is your number 3 interest: ")

combined = f"My name is {name} and I am {age} and my interests are {interest1[0]}, {interest2[1]}, and {interest3[2]}"

print(combined)
