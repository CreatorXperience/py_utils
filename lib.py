import os
import shutil
import sys
import re
import math
import random
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
sys.exit(0)