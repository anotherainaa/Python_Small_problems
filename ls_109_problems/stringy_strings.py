# Stringy Strings
# Write a method that takes one argument, a positive integer, and returns a string of alternating 1s and 0s, always starting with 1. 
# The length of the string should match the given integer.
# - iterate num times, add to an existing string, alternating 1 and 0s

def stringy(num):
    result = ""
    currentNum = "1"
    for i in range(num):
        result += currentNum
        if currentNum == "1":
            currentNum = "0"
        else:
            currentNum = "1"
    
    return result

# Ternary operators?
def stringy2(num):
    result = ''
    currentNum = '1'
    for i in range(num):
        result += currentNum
        currentNum = "1" if currentNum == "0" else "0"

    return result

print(stringy(6) == '101010') 
print(stringy(9) == '101010101')
print(stringy(4) == '1010') 
print(stringy(7) == '1010101') 

print(stringy2(6)) 