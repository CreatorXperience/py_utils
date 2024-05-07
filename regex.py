"""

     Regular Expression
    -searching for pattern in strings

    """
import re
import math
recipient = '''Ezra Koenig <ekoenig@vpwk.come>,
...: Rostam Batmanglij <rostam@vpwk.com>,
...: Chris Tomson <ctomson@vpwk.com,
...: Bobbi Baio <bbaio@vpwk.com''' 

print(re.search(r"Toms[o,i]n",recipient))
print(re.search(r"chr[a-z][a-z]", recipient,2))
print(re.search(r"[a-zA-z]{6}", recipient))
print(re.search(r"[a-z]+@[a-z]+\.[a-z]{3}", recipient))
print(re.search(r"\w+\@+\w+\.\w{3}", recipient))

yum="abc".split("*")
print(yum)

# yum.reverse()
# print(yum)
# # re.search(r"(\w+)\@(\w+)")
# string = "This".split(" ")
# sort  = sorted(string)
# sort.reverse()
# for index,item in enumerate(sort):
#     strs+=item

# print(strs)


# def reverse_str(strt: str):
#     seperator=""
#     for index,item in  enumerate(strt):
#         if item == " ":
#             seperator+=item
#             if strt[index+1] == " ":
#                 seperator+=item
#                 print("ho", end=seperator)
#             break

# reverse_str("This  is  good")


space=""
def check_space(strg: str, indexes:int=0):
    """
        check space between characters
    """
    intg:str  =  strg[indexes]
    global space
    print(intg,indexes)
    if intg == " ":
        space+=" "
        print(space, end="x")
        check_space(strg, indexes+1)
    elif indexes != 0 and strg[indexes-1] == " " and  strg[indexes].isalpha():
        return 
    elif strg[indexes].isalpha() and strg[indexes+1].isalpha():
        check_space(strg, indexes+1)
    elif strg[indexes].isalpha() and not strg[indexes+1].isalpha():
        check_space(strg,indexes+1)
    return strg

print()

value = check_space("double  spaces",0)
reversed_val=value[::-1]
splitted=reversed_val.split(space)
reversedd=splitted[::-1]
print(reversedd)
# print("".join([str(element) for element in reversedd]))
my_str=""
for indx,item in enumerate(reversedd):
    if indx != len(reversedd)-1:
        my_str+=item+space
        continue
    my_str+=item
print(my_str)

# print(yo[::-1])

# input n
# (n/n-1)
