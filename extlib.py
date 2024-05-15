import os
import shutil
import sys
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
sys.exit(0)