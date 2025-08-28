# Define the contents for each section
section2='my_internet_profile = {
    "name": None,                          # string
    "twitter_handle": None,                # string
    "favorite_physics_constant": None,     # float
    "age": None,                           # integer (you can lie about this lol)
    "finished_uni": None,                  # boolean
    "hobbies": None,                       # tuple
    "skills": None,                        # list
    "personal_quotes": None,               # set (one or two)
    "contact_info": {                      # dictionary (nested)
        "phone_number": None,              # integer (you can put a fake one)
        "email": None,                     # string (you can put a fake one)
        "website": None,                   # string
    },
}

print(my_internet_profile)
'

section3='score = int(input("Enter your exam score (0-100): "))

# write your if/elif/else statements here
'

section4='accounts = ["1234567890", "9876543210", "5555555555", "1111222233"]

account_to_search = input("Enter account number to search: ")

# TODO: use a for loop to check if search_account is in accounts
# Hint: loop through accounts and compare the `account_to_search` to the looped element
'

section5='while True:
    account_number = input("Enter your 10-digit account number: ")

    # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking
'

section6='def find_min_max(*args):
  min_num = float("-inf") # smallest possible number in python
  max_num = float("inf") # largest possible number in python
  
  return (min_num, max_num)

# TODO: write test cases and pass them to the function. Print the results
'

section7='class CalculatorHistory:
    def __init__(self):
        # add the remaining
        self.addition = []

    def __str__(self):
        return f"""
            Addition: {self.addition}
        """

class Calculator:
    def __init__(self, log_results: bool = False):
        self.log_results = log_results
        self.history = {
            "addition": []
        }

    def add(self, num1: float, num2: float):
        result = num1 + num2

        if self.log_results:
            print(f"The sum of {num1} and {num2} is {result}")

        self.history["addition"].append((num1, num2, result))
        # goal 
        # self.history.addition.append((num1, num2, result))

        return result


calculator = Calculator()

calculator.add(4, 5)
calculator.add(20, 25)
calculator.add(-20, 30)

print(calculator.history)
'

section8='class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        pass  # implement this

    def withdraw(self, amount):
        pass  # implement this

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"

# TODO: Create a SavingsAccount class that inherits from BankAccount

# Example usage
account = BankAccount("Alice", 1000)
print(account)
'

# Loop through sections and drop a main.py inside each username folder
for section in {2..8}; do
  for userdir in day1/section-$section/*; do
    case $section in
      2) echo "$section2" > "$userdir/main.py" ;;
      3) echo "$section3" > "$userdir/main.py" ;;
      4) echo "$section4" > "$userdir/main.py" ;;
      5) echo "$section5" > "$userdir/main.py" ;;
      6) echo "$section6" > "$userdir/main.py" ;;
      7) echo "$section7" > "$userdir/main.py" ;;
      8) echo "$section8" > "$userdir/main.py" ;;
    esac
  done
done
