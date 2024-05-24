import os
import shutil
import sys
import re
import math
import random
import statistics
import Decorator
# import smtplib
import glob
import sys
from datetime import datetime

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

@Decorator.do_twice
def print_total(greeting):
    print(greeting)
    return greeting

print(print_total("Hello Motherfucker"))

print(help(Decorator))

sys.exit()