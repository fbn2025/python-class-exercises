my_internet_profile = {
    "name": "Adam Sunday",                          # string
    "twitter_handle": "@adamsunday1",               # string
    "favorite_physics_constant": 6.626e-34,         # float (Planck's constant)
    "age": 28,                                      # integer
    "finished_uni": True,                           # boolean
    "hobbies": ("reading", "coding", "football"),   # tuple
    "skills": ["Python", "SQL", "Data Analysis"],   # list
    "personal_quotes": {
        "Keep pushing, even when the road gets tough.",
        "Faith and persistence always open doors."
    },                                              # set
    "contact_info": {                               # dictionary (nested)
        "phone_number": "08123456789",              # string (not int, to preserve leading zeros)
        "email": "adam@example.com",                # string
        "website": "https://adamprofile.me",        # string
    },
}

print(my_internet_profile)
