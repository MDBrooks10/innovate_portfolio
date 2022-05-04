import random

# print is how we display information in a terminal
print("This is my current file")

# greeting is a variable
greeting = "Wasson?"

print(greeting)

# strings are for representing characters
print ("This is a string")
print ("1234")

# this is an interger - a whole number
print(1234)

# this is a floating point - anything with a decimal
print(123.4)

# booleans - True and False
print(True)
print(False)

# None - a blank, or null type

###############################################

# Strings have methods which can be used to minipulate them

# index position - starts it's count at 0
print("Hello"[-1])

# dot notation - .upper() will uppercase everything
print(greeting.upper())
print("Hello worLD".upper())


# Libraries - imported the random library at the top
print(random.random())
print(random.uniform(1,10))
print(random.randint(1,10))
print(random.randint(1, 17))

# Libraries can be imported as such
import random
from random import random,randint,uniform


# Variables are like boxes that can be used to store data
my_name = "Mark"    # Variable with a string
my_age = 37         # Variable with an interger
student = True      # Variable with a boolean

print(my_name)


# Comparison operators
# == Equals
# =! Not equal
# >= Greater or equal to
# <= Less than or equal to
# > Greater than
# < Less than


music = "classical"

if music == "classical":
    print("Oh no! Not Bach.")
elif music == "Pop":
    print("Turn it up!")
else:
    print("Yay!")


num1 = 10
num2 = 20

if num1 > num2:
    print("Number 1 is bigger")
elif num1 < num2:
    print("Number 2 is bigger")
else:
    print("Numbers are the same")


num = 21

if num%7==0 and num%3==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%7==0:
    print("Buzz")
else:
    print(num)


# Functions - Takes data, does something with it, and returns 

def light_switch():
    print("Who turned out the lights?")

light_switch()


#Functions with parameters

def cash_withdrawal (amount, accnum):
    print(f"Withdrawing £{amount} from account #{accnum}")

cash_withdrawal (300, 50449921)
cash_withdrawal (130, 12340987)
cash_withdrawal (50, 34527564)


# Lists

coffee_order = [
    "Alex - Cortado",
    "Ben - Latte",
    "Charlie - Whatevers new"
]

print(coffee_order[1])