import random
import string
def generate_password():
    a = int(input("How many letters would you like in your password? "))
    b = int(input("How many symbols would you like? "))
    c = int(input("How many numbers would you like? "))
    letters = random.choices(string.ascii_letters, k=a)
    symbols = random.choices(string.punctuation, k=b)
    numbers = random.choices(string.digits, k=c)
    password = ''.join(letters + symbols + numbers)
    print(password)
generate_password()






































import random
import string
def generate_password():
    a = int(input())
    b = int(input())
    c = int(input())
    letters = random.choices(string.ascii_letters, k = a)
    symbols = random.choices(string.punctuation, k = b)
    numbers = random.choices(string.digits, k = c)
    passwords = ''.join(letters + symbols + numbers)
    print(password)
generate_password()


