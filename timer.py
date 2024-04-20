# from time import time
from collections import Counter 
import array 
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