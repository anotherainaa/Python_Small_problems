# https://launchschool.com/exercises/dfa7db2c
# Write a method that takes one integer argument, which may be positive, negative, or zero. 
# This method returns true if the number's absolute value is odd. 
# You may assume that the argument is a valid integer value.

# We have to be explicit when returning values?
def is_odd(num):
    return num % 2 != 0

print(is_odd(2))    # => false
print(is_odd(5))    # => true
print(is_odd(-17))  # => true
print(is_odd(-8))   # => false
print(is_odd(0))    # => false
print(is_odd(7))    # => true