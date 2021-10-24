print("Hello, world!")

# Name 
input("Name: ")
print("Hello, " + Name)
print(f"Hello, {name}")

# Conditions
n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0
    print("n is negative")
else:
    print("n is zero")

# Sequences
names = ["John","Harry", "Aurick"]

print(name[0])

# lists, Define a list of names
names = ["Harry", "Ron", "Hermione", "Ginny" ]

names.append("Carlo")

names.sort()

print(names)

#Sets, Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

s.remove(2)
print(s)

print(f"The set has {len(s)}")

#loops
for i in range(100):
    print(i)

names = {"Harry", "Ron", "Hermione"}

for character in names:
    print(character)

#Dictionaries
houses = {"Harry": "Gryffindor", "Draco", "Slytherin"}

houses["Hermione"] = "Gryffindor"

print(house["Harry"])

#Functions 
def square(x):
    return x * x

#Squares
from functions import square

for i in range(10)
    print(f"The squiare of {i} id {square(i)}")

#Classes
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
         if not self.open_seats():
             return False
        self.passengers.append(name)
        return True

    def open_seats (self):
        return self.capacity - len(self.passengers)

flight= Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passengers(person):
        print(f"Added {person} to flight successfuly")
    else:
        print(f"No available seats for {person}")
    
#Decorators
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper 

@announce
def hello():
    print("Hello, world")

hello()

#Lambda
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lamda person: person["name"])


print(people)

#Exceptions
import sys 

try:

    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")    
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")    

print(f"{x} / {y} = {result}")















