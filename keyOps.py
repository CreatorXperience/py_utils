# keywords
yo = (10 > 5) 
yola = (4 < 10)
val = yo and yola
print(val)


# alias
import calendar as cldr
# val = 202
leap = cldr.isleap(2020)
print(leap)


val = 2020
assert val == 2020
print(val)

# break  keyword 

for i in range(5,10):
    if i > 8: 
        break
    print(i)


# The class Keyword
    class insert():
        item = 10000
        quantity: 1

s = insert()
print(s.item)


for i in range(6):
    if i >  2: 
        print("this are greater than 2", i)
        continue
    print(i)


# the def keyword
def multiply_by_2(x):
 print(x *  2)

multiply_by_2(10)


# the del keyword

v = "letter v"
print(v)
del(v)
#print(v)  #throws an error



# the if keyword
score = 2


if score >= 8: 
    print(f"you are qualified for the next stage, {score}")
elif score >= 5:
    print(f"Average value, {score}")
else: 
    print("Yo you are disqualified and will repeat previous %s and your score is %.2f"%("test", 0.45 ))


# the try keywords
    

var = None

try: 
    print( var.isalpha() == True)
except: 
    print("variable var is not defined ")

finally:
    var = str("Alpha".isalpha()).lower() 
    print(f"finally variable var is defined and it's {var}ly an alphabet")


# the for keyword
    
    for i in range(10): 
        print(i)

# the import keyword

import numbers


# the from keyword
from  numbers import Rational


# the global keyword
greetings= "Hi"

def  greet ():
    global greetings
    greetings = "Hello"
    print(greetings)

greet()
print(greetings)


# the in keyword

arr  = ["Programmer","Javascript", "Python", "React"]

print("Python" in  arr)


# the is keyword

cart =  ["shoe", "T-shirt", "bag", "Laptop"]
clone_cart = cart

print(cart is clone_cart)





def samples(val,total):
 total.append(val*2)
 return total

# the  lambda keyword

multiply = lambda x,y:int(x)*int(y)
print(multiply(5,10))
print(multiply("5","2"))


total = []
# the nonlocal keyword  / recursion


def switch(status): 
    switch = status

    def key(switch):
        switch += 1

        if switch < 10:
             key(switch)
        return samples(switch, total)
    key(switch)   
    print(total)




switch(0)

# the not keyword
falsy  = 0
truthy = not falsy
print(truthy)

def choose_one(x):
    if x: 
        print("you are trustworthy")
    if not x:
        print("you are not trustworthy")
    
    elif x or not x:
        print("well you tried")

choose_one("money")

# the pass keyword
def useless():
    pass


def add(x,y):
    if not type(x) or not type(y) is int: 
        print('x or y is not an integer')
        return
    else:
       total =  x + y
       print(total)
       return total 

add(2,5)


is_what =  not type(10) is int
print(is_what)
is_what =  not type(10) is int
print(is_what)

# the with keyword
# with open("", "a",1,"utf-8") as file 
# file.write("ghjk")