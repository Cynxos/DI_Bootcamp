def get_random_temp(season):
    if season == 'winter':
        return round(random.uniform(-10, 16), 1)
    elif season == 'spring':
        return round(random.uniform(0, 23), 1)
    elif season == 'summer':
        return round(random.uniform(16, 40), 1)
    elif season == 'autumn' or season == 'fall':
        return round(random.uniform(0, 23), 1)
    else:
        return "Invalid season"

import random

def main():
    month = int(input("Please enter the number of the month (1-12): "))
    if month in [12, 1, 2]:
        season = 'winter'
    elif month in [3, 4, 5]:
        season = 'spring'
    elif month in [6, 7, 8]:
        season = 'summer'
    elif month in [9, 10, 11]:
        season = 'autumn'
    else:
        print("Invalid month")
        return

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Wow, that’s freezing! Make sure to wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget to bring a coat.")
    elif 16 <= temp < 24:
        print("We have some nice weather! Enjoy your day.")
    elif 24 <= temp < 32:
        print("It's warm! Perfect for a day out.")
    elif 32 <= temp <= 40:
        print("It's hot! Stay hydrated.")

main()