# https://launchschool.com/exercises/a018e581
# Write a method that takes two arguments, a string and a positive integer, and prints the string as many times as the integer indicates.

# Python ranges
def repeat(string, number):
    for _ in range(number):
        print(string)

repeat('Hello', 3)
repeat('Hello', 0)
repeat('World', 5)

# Experimenting with while loops
def repeat2(str, num):
    n = 1
    while n <= num:
        print(str)
        n += 1

repeat2('Konnichiwa', 2)

