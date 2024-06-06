"""
CRYPTO X Hashlib

"""
from cryptography.fernet import Fernet
import hashlib

key = Fernet.generate_key()
f_obj = Fernet(key)
word = b"This is Fernet at work"
byts = f_obj.encrypt(word)
print(byts)


md5_obj = hashlib.md5(b"Hello World", usedforsecurity=True)
print(md5_obj.digest())
def puff(func):
    def func_wrapper():
        print("hello world")
        func()
    return func_wrapper
@puff
def jagaban():
    print("hello world")

jagaban()