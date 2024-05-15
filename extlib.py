import os
import shutil
import sys
import re
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
sys.exit(0)