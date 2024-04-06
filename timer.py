# from time import time
from collections import Counter 
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