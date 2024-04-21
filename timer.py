from collections import Counter
import array
import math
# allocated_time = 60

# game_over = False

# start_time = time()
# print(start_time)


# elapsed_time = time() - start_time

# while game_over  == False:
#     elapsed_time  =  time() - start_time


# if elapsed_time >= allocated_time : 
#     game_over = True
#     print("game over")

val = 0

def add(*args):
    for  arg in args :
        global val
        val += arg
    return val

 

print(
     add(1, 2, 3, 4, 5) == 15
)
# def test_add():
#     assert add(1, 2, 3, 4, 5) == 15
#     assert add(10, 20, 30) == 60
#     assert add(2.5, 3.7, 1.8) == 8.0
#     assert add(0) == 0
#     assert add(-1, -2, -3, -4, -5) == -15


# test_add()


count = Counter([1,2,3,4,5,6,78,])
item = Counter.popitem({1:1})
print(count)

diction = {"key1": "yo",  "key2": "man"}

new_dict = {}
for key,value in  diction.copy().items():
    if value == "yo":
        del key
    else: 
        new_dict[key] = value

print(new_dict)



def http_error(status: int):
    match status:
        case "404":  
            return "Not found"
        case "400": 
            return "Bad request"
        case "200":
            return "Successfull"
        case "500": 
            return "Internal Server Error"
        case "304":
            return "Not modified"
        
http_error(False)


class Points:
    __match_args__ = ("x","a")
    def __init__(self,x,y):
        self.x = x
        self.y = y
  
points  = Points(0,0)
#     case 0,1:
#         print("found")
#     case 0,2:
#         print("0,2 not this")
#     case 0,3:
#         print("0,3 not at all")


# match points: 
#     case 1,y: 
#         print(f"Y={y}")
#     case x,1:
#         print(f"X={x}")


# print(Points(0,2)) 


match points:
    case Points(a=0,y=0):
        print("Origin")
    case Points(x=0, y=y):
        print(f"Y={y}")
    case Points():
        print("Somewhere else")
    case _ : 
        print("nothing else")
 


def multiply(x: int,y:int,z=20):
    tot = x+y+z
    print(f"x{x} + y{y}+ z{z} = {tot}")


multiply(z=10,x=40,y=10)

#python code

def join(x:int, arr: list =array.array("i", [])):
    if x : 
        arr.append(x)
        return arr

print(join(20))  # returns  [20]
print(join(50,[])) # returns  [50]
print(join(40))  # returns [20,40]





def cheeseburger(cheese:str, *request:str, **props ):
    print(f"do you have cheese {cheese}")
    for req in request:
        print(type(req),req)
    
    
    for prop,vala in props.items(): 
        print(prop,":",vala)



cheeseburger("burgers","burger is good", "the you want more", "what the heck", "this is amazing", peter="you are sick in the head", paul="you aint okay")

def poskwd(pst,/,pt, *,kwd):
    print(pst, "keyword", kwd, pt)

poskwd(20,1, kwd="different pattern")


def foo(name, **kwds):
    return 'peter' in kwds

print(foo("peter", **{"peter": "parker"}))



def pwd(d, /, **f):
    print("name" in f)

pwd("hello", name="obj")

pwd("yo", **{"name": "peter"})


print("yo".join(("1","2","3","4")))

lslist = [1,6]
tuplee  = tuple(lslist)
print(list(range(*lslist)))


def parrot(voltage, state="a stiff",action='VOOM'):

    print("-- This parrot wouldn't",action, end=' ')
    print("if you put", voltage,"volts through it")
    print("E's ", state, "!")
d = {"voltage": "four million", "state":"bleedin' demised", "action": "VOOM"}


parrot(**d)


def calculateDistance(lat:int): 
    return lambda long: long + lat


getlocation = calculateDistance(20)
print(getlocation(30))

pair = [(1, "one"),  (2,"two"), (3, "three"), (4, "four")] 

pair.sort(key=lambda item: item[1], reverse=True)
print(pair)

print((1,2,3)+(4,5,6))


ext = [1,2,3]
ext.extend([4,5,6])
print(ext)


questions = ["name", "quest", "favorite color"]
answers = ["peter parker",  "spider man", "red and black"]


for q,a in zip(questions, answers):
    print(f"what is your {q} ? it is {a}")



for i in range(1,10,2):
    print(i)


cart = ["apple", "berry", "orange", "pineapple"]
for fruit in sorted(cart):
    print(fruit)


floatss = [56.2, float('NaN'), 57.8, float('NaN'), 5.23, 2.96, float('NaN')]
new_floats = []

for i in floatss:
    if not math.isnan(i):
        new_floats.append(i)


print(new_floats)


first_item = ["one", "two","three", "four", "five"]
sec_item = ["Ball", "Cat", "Dog", "Egg", "Banana","Apple"]
items_set =  []

#zipped = zip(first_item, sec_item)
#for  item1, item2  in zipped:
 #   items_set.append((item1, item2))


#print(items_set)


class Merge:
    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2= item2
        self.length = -1

    def __iter__(self):
        self.item1 = self.item1
        self.item2 =  self.item2
        return self

    def __next__(self):
        try:

            self.length = self.length+1
            if self.length <= (len(self.item1) -1):
                return (self.item1[self.length], self.item2[self.length])
            else:
                raise StopIteration
        except:
            raise StopIteration

    def __str__():
        return  "this is a class utility for merging iterators"



for  item1,item2 in Merge(first_item, sec_item):
        print(item1,item2)
