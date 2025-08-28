my_internet_profile = {
"profile": {
    "name": "ADAM SUNDAY",                          # string
    "twitter_handle": "adamsunday.1",                # string
    "favorite_physics_constant": 6.626e-34,          # float (Planck’s constant for fun)
    "age": 99,                                       # integer
    "finished_uni": True,                            # boolean
    "hobbies": ("reading", "writing", "coding", "football"),   # tuple
    "skills": ["problem solving", "public speaking", "SQL", "Python", "data analysis"],   # list
    "personal_quotes": {
        "Keep pushing, even when the road gets tough.",
        "Faith and persistence always open doors."
    },                                               # set
    "contact_info": {                                # dictionary (nested)
        "phone_number": +238138413441,               # string (kept as string, safer than int)
        "email": "adsun0607@gmail.com",              # string
        "website": "I don't have one",               # string
    },
}}

print(my_internet_profile)
