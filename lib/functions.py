def add_numbers(num1, num2):
    """
    Takes two numbers and returns their sum
    """

    return num1 + num2


def is_even(number):
    """takes one parameter,
    the %2 == 0 means quotient is a whole number, no reminder.
    returns a bool, true
    """
    return number % 2 == 0 


def reverse_string(text):
    """takes one parameter.
    uses slice[start: stop:-1] 
    returns reveresd string"""

    return text[::-1]

def count_vowels(text):
    """takes a string, returns the number of vowels
    """
    vowels = "aeiou"
    text = text.lower()
    return sum(1 for char in text if char in vowels)

def calculate_factorial(n):
    """takes n as param, bverifies that 0 is not an integer,
    loops through the integer from 1 through n, n included"""
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def decorator_func(func):
    """takes a func as an argument,
    returns wrapper: decorator applied"""

    def wrapper():
        print("Decorator Applied")
        return func()
    return wrapper

def apply_decorator(func):
    """Takes a function and applies the decorator to it."""
    return decorator_func(func)

def sort_by_age(list_of_tuples):
    """
    Takes a list of tuples (name, age) and sorts it
    by age in ascending order.
    """
    return sorted(list_of_tuples, key=lambda x: x[1])


def merge_dictionaries(dict1, dict2):
    """merges two dicts. if the have the same keys, their values are summed iups"""
    # copy dict1 to avoid modifying the original dictionary
    merged_dict = dict1.copy()
    
    # Iterate through dict2 to merge or add the key-value pairs
    for key, value in dict2.items():
        if key in merged_dict:
            # If the key is already in merged_dict, sum the values
            merged_dict[key] += value
        else:
            # Otherwise, add the key-value pair to merged_dict
            merged_dict[key] = value
    
    return merged_dict