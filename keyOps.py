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
    quantity =  1
    items =  [1,2,3,4]
    # calculate = lambda amount:  amount * amount TODO: line 32

s = insert()
print(s.items)
# print(s.calculate()) TODO: depends on line 50
print(s.quantity)


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

strs= "         hello apple  this is apple and i want apple"
print(strs.lstrip())



setter = {"hi", "lion", "GOAT"}
setter2  = ["DRAGON", "lion"]
print(setter)

print(setter.intersection(setter2))
print(setter.issuperset(setter2))

# setter.union(setter2)
print(setter)


# newer = setter | setter2
#  unsuported operand error
# print(newer) unsuported operand error

setter_x =  {"peter", "parker"}
turple_x = ("manny", "nonso")
setter_x.update(turple_x)
print(setter_x)


sym_set = {1,2,3}
set_sym = {1,4}
new_sym_set = sym_set.symmetric_difference(set_sym)
print(new_sym_set)


diff_set = {5,4,3,2}
set_diff = {6,5,4}
diff_set.difference_update(set_diff)
print(diff_set)

sym_diff = {1,2,3}
diff_sym = {4,3,2}
sym_diff.symmetric_difference_update(diff_sym)
print(sym_diff)



sym_diff = {1,2,3}
diff_sym = {4,3,2}
diff = sym_diff ^ diff_sym
print(diff)


a,b = 1,2
print(a)


# TODO!!! 262-298

# rec  = [[3,3], [5,4], [2,8]] 

# def pass_items(item,start=0):
#     end = len(item) -1
    
#     if item.index(item[start]) == end  and  item[start] % 2 == 0 :
#         return True
#     if item.index(item[start]) == end and item[start] % 2 != 0:
#         return False
#     if item[start] % 2  == 0 :
#         return True
#     if start < end :
#         start+1 
#     return pass_items(item,start)

# def recusiv(items):
#     length = len(items)
#     end = length-1

#     start = 0

#     sub_item = items[start]  
#     if not type(sub_item) is list:
#         value = pass_items(items)
#         if value == False and start != end: 
#             start + 1
#             return "not found"
#         else:
#             return  value
      
#     return   recusiv(sub_item)


# value = recusiv(rec)
# print(value)



data_point = True
data_value = 0

while data_point == data_value: 
    print("equal")
    data_value= not data_value

# while loop else clause
count = 0
value = 6
while count  != value :
    print(count)
    count+=1
else:
    print("the loop is over")    


items = ["Apple", "Ball", "Cat","DOG"]

for item in items :
    print(str(items.index(item)) + "." + item)


dict = {"name": "peter", "surname": "Parker"}

print(dict.items())

for key,value in dict.items():
    print(f"{key} is {value}")

for table_value in range(1, 10):
    for multiplier in range(1, 11):
        answer = table_value * multiplier
        print(answer, end=' ')
        print()
else:
    print('For loop is over!')


# List comprehension

[i**3 for i in range(10)]



val = [i for i in range(20) if i%2==0 if i%3==0]
print(val)

intet = [str(i) + "    " +  "EVEN" if i % 2 ==0 else str(i) + "    "  +  "ODD" for i in range(20)]
print(intet)



var = int("20" + str(1))


print("this is  %i dollar"%(var))


val  = [i * 3  for i in range(1,5) if i % 2]
print(val)