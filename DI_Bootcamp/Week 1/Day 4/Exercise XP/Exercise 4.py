import random

def compare_numbers(user_number):
    if not 1 <= user_number <= 100:
        return "Please enter a number between 1 and 100."

    random_number = random.randint(1, 100)
    if user_number == random_number:
        return f"Success! Both numbers are {user_number}."
    else:
        return f"Fail! Your number: {user_number}, Random number: {random_number}."

user_input = 66
result = compare_numbers(user_input)
print(result)
