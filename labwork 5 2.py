import datetime

def user_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    birth_year = int(input("Enter your birth year: "))
    fav_number = int(input("Enter your favorite number: "))
    age = datetime.datetime.now().year - birth_year
    print(f"\nHello, {first_name} {last_name}! You are {age} years old.")
    print(f"The square of your favorite number ({fav_number}) is {fav_number ** 2}.")

user_info()