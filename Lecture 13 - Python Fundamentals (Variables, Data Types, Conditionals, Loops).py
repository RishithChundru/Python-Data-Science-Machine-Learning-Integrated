# Variables
name="john dae"
print(name)

# Data types
# Integer
num=10
print(abs(num))
print(bin(num))
print(hex(num))
print(oct(num))
print(pow(num,2))
print(divmod(num,3))

# Float
price=99.99
print(round(price))
print(abs(price))
print(int(price))
print(float("123.45"))
print(price.is_integer())

# String
greeting="Hello, World"
print(greeting.lower())
print(greeting.upper())
print(greeting.replace("World","Python"))
print(greeting.split())
print(greeting.find("World"))
print(len(greeting))

# List
fruits=["apple","banana","cherry"]
fruits.append("orange")
print(fruits)
fruits.extend(["grape","melon"])
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.pop()
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(len(fruits))
print(fruits.index("cherry"))
print("apple" in fruits)

# Tuple: it is unchangable
coordinates=(10.0,20.0)
print(coordinates)
print(coordinates.count(10.0))
print(coordinates.index(20.0))
print(len(coordinates))
li=list(coordinates)
print(li)
li[1]="hi"
print(li)

# Dictionary: it is combination of key and value pairs
person={"name":"John","Age":30}
print(person.keys())
print(person.values())
print(person.items())
print(person.get("name"))
print(person.get("Age"))
person.update({"height":100})
print(person)
person.pop("Age")
print(person)
print(len(person))

# Set: it will not allow duplicates
se={1,2,3,4}
print(se)
se1={1,1,1,1}
print(se1)
print(len(se))
se.add(9)
print(se)
se.update({10,11,12})
print(se)
se.remove(10)
print(se)

# Boolean
is_active=True
print(int(is_active))
print(bool(0))
print(bool(1))
print(bool("Hello"))
print(is_active and False)
print(is_active or False)
print(not is_active)

# Conditionals
# Basic if-elif-else statement
age=20
if age<18:
    print("Minor")
elif age>=18 and age<65:
    print("Adult")
else:
    print("Senior")
    
# Checking Even or odd number
number=42
if number%2==0:
    print("Even Number")
else:
    print("Odd Number")
    
# Grade Evaluation
score=85
if score>=90:
    print("Grade: A")
elif score>=80:
    print("Grade: B")
elif score>=70:
    print("Grade: C")
elif score>=60:
    print("Grade: D")
else:
    print("Grade: F")
    
# Temperature Check
temp=30
if temp>30:
    print("It is hot day")
elif temp>=20:
    print("It is a nice day")
else:
    print("It is cold day")
    
# Nested Conditionals for BMI calculation
weight=70
height=1.75
bmi=weight/(height**2)
if bmi<18.5:
    print("UnderWeight")
else:
    if bmi<24.9:
        print("Normal Weight")
    else:
        if bmi<29.9:
            print("OverWeight")
        else:
            print("Obesity")
            
# Traffic Light System
traffic_light="Green"
if traffic_light=="Red":
    print("Stop!")
elif traffic_light=="Yellow":
    print("Caution")
elif traffic_light=="Green":
    print("Go")
else:
    print("Invalid traffic light colour")

# User Login Status
is_logged_in=True
has_permission=True
if is_logged_in:
    if has_permission:
        print("Access Granted!")
    else:
        print("Access Denied: insufficient Permissions!")
else:
    print("Access denied: User not logged in")

# Age-based Discount
age=70
if age<18:
    print("Eligible for child discount")
elif age>=65:
    print("Eligible for senior discount")
else:
    print("Regular Pricing!")   
    
# Loops
# For Loop   
for i in range(5):
    print(i) 
    
# Iterating Over a list
fruits=["apple","banana","cherry","date"]
for i in fruits:
    print(i)
    
# Iterating over a string
greeting="Hello"
for char in greeting:
    print(char)
    
# Iterating over a dictionary
person={"Name":"John","Age":30,"City":"New York"}
for key,value in person.items():
    print(f"{key}:{value}")
    
# Usint the 'range()' Function with a step
for i in range(0,10,2):
    print(i)
    
# Nested for loops
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
        
# Using the 'enumerate()' Function
fruits=["apple","banana","cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    
# While Loop
count=0
while count<5:
    print(count)
    count += 1
    
# While Loop with break
count=0
while True:
    print(count)
    count += 1
    if count>=5:
        break
    
# While Loop With Continue
count=0
while count<10:
    count+=1
    if count%2 == 0:
        continue
    print(count)
    
# Using a while loop to process User Input
user_input=""
while user_input.lower() != "quit":
    user_input=input("Enter something (or type 'quit' to exit): ")
    print(f"You Entered: {user_input}")

# Simulating a CountDown
countdown=10
while countdown>0:
    print(countdown)
    countdown-=1
print("Blast off!")

# Using a while loop for validation
password=""
while len(password)<8:
    password=input("Enter a password (must be at least 8 characters long): ")
    if len(password)<8:
        print("Password is too short. Try Again!")
print("Password accepted!")

# Variables in Store inventory data
store_name="Green Grocery"
inventory={
    "apples":50,
    "bananas":30,
    "cherries":20
}

# Data Type: Dictionary to store Inventory
# Data type: Integer for item quantities

# Conditional check inventory status
def check_inventory(item):
    if inventory[item] > 0:
        return f"{item.capitalize()} are in stock: {inventory[item]}"
    else:
       return f"{item.capitalize()} are out of stock." 
 
# Loop: Update inventory
def update_inventory(item, quantity):
    if item in inventory:
        inventory[item]+=quantity
    else:
        inventory[item]=quantity       
# Check and update inventory
print(check_inventory("apples"))
update_inventory("apples", -10)
print(check_inventory("apples"))
update_inventory("oranges", 40)
print(check_inventory("oranges"))