#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

print(f"Last digit of {number} is", end=" ")

if last_digit > 5 and number > 0:
    print(f"{last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{last_digit } and is 0")
elif last_digit < 6 or number < 0:
    last_digit = -last_digit if number < 0 else last_digit
    print(f"{last_digit} and is less than 6 and not 0")
