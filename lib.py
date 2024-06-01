import os
import shutil
import sys
import re
import math
import random
import statistics
import functools
from Decorator import do_twice,measure_runtime,debug
# import smtplib
import glob
# import sys
# from datetime import datetime

print(sys.argv)
print(glob.glob("*.js"))
print(os.getcwd())
# print(os.chdir("/etc/"))
print(os.getcwd())
try:
    print(os.system("rm -r new_dir"))
except:
    print("cannot remove missing directory")

finally:
    print("finally")

print(sys.argv)
shutil.copy("./lib.py", "./extlib.py")
# shutil.move("./java.json", "./sec")
print("What is your name?")
read=sys.stdin.readlines(1)
print(read)
sys.stderr.write("error occured in lib.py \n")

print(re.findall(r"pe\w+", "peter peter pepper penguin pat zarticly particles"))
recompiler = re.compile(r"\w+")
print(recompiler.search("anime"))

regez=re.finditer(r"\w+\@","me@ you@ life@")
resub = re.sub(r"\@","$","peter@ habeeb@")
print(resub)
print(next(regez))
print(next(regez))

print("weather for two".replace("two", "one"))
print(math.remainder(2.5,5))
print(math.cos(90))
print(random.sample(range(1,100),10))
print(random.choice([1,2,4,5,6]))
data = [1,2,3,4,5,6,7,8,1,4,0]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))
print(statistics.variance(data))
# server = smtplib.SMTP("localhost", 80)
# server.sendmail("peterparker@gmail.com", "spider@nan.com", "Are you a spider man?")
# server.quit()


value = input("what's your eye color\n")
print(value)
print(os.error.__reduce__)
message = 2000
sys.stdout.write("Logout \n")
sys.stderr.write("an Error occurred \n")
print(f"{message:+^30.2f}")


def sum_total(func):
    def wrapper():
        return func()*5
    return wrapper

# Traditionnal way of calling function
@sum_total
def say_whee():
    return 5
# say_whee = sum_total(say_whee)
print(say_whee())

@do_twice
def print_total(greeting):
    """
        Print greeting
    """
    print(greeting)
    return greeting

print(print_total("Hello Motherfucker"))

# print(help(Decorator))
print(print_total.__name__)
print(help(print_total))

@measure_runtime
def print_items(items):
    for item in enumerate(items):
        if item[1] > 5:
            print(item)
        else:
            print(item[1]+2)

@debug
def consolelog(message):
    return message

consolelog("Hello World")

print_items([1,5,6,79,20,2,3,9,66,10,12,5,6,0,1,12,6])



def calculateAmount(getExpenses):
    expenses = getExpenses()
    return expenses + 20


def calculateExpenses():
    return 10


print(calculateAmount(calculateExpenses))



x = open("index.html", "+r");

print(help(open))

def do_something():
    """

        Print Something

    """
    def hello_world(): 
        """
        print hello world
        """
    return hello_world


print(help(do_something()))

def loop():
    ref = 0
    while ref < 10 :
        ref = ref + 1
        yield ref




arr = ["shoe", "bag", "peter", "whatever"]
print(arr[2:5])
# listing = (x if x % 2 == 0 else "" for x in range(11))


let = loop()
print(next(let))
print(next(let))


def my_func(your_func):
    @functools.wraps(your_func)
    def exec_func(*arg, **kwarg):
        print("Hello WOrld")
        your_func(*arg,**kwarg)

    return exec_func


@my_func
def custom_func(event):
    """

    hello

    """
    print(f"you look up it {event} time")


print(help(custom_func))