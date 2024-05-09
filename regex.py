"""

     Regular Expression
    -searching for pattern in strings

    """
import re
import math
recipient = '''Ezra Koenig <ekoenig@vpwk.come>,
...: Rostam Batmanglij <rostam@vpwk.com>,
...: Chris Tomson <ctomson@vpwk.com,
www.google.com,www.internetexplorer.edu
...: Bobbi Baio <bbaio@vpwk.com'''

print(re.search(r"Toms[o,i]n",recipient))
print(re.search(r"chr[a-z][a-z]", recipient,2))
print(re.search(r"[a-zA-z]{6}", recipient))
print(re.search(r"[a-z]+@[a-z]+\.[a-z]{3}", recipient))
grouping=re.search(r"(\w+)\@+(\w+)\.(\w{3})",recipient)
print(grouping.group(3))

yum="abc".split("*")
print(yum)

def reversed_word(item:str):
    """
    reversed word
    """
    words=item.split(" ")
    reversed_words=[word[::-1] for word in words]
    print(" ".join(reversed_words))
reversed_word("This  is  a  word")

matched = re.search(r"(?P<name>\w+)\@(?P<service>\w+)\.(?P<domain>\w{3})", "ed@gmail.com")
print(matched.group("domain"))


find_all = re.findall(r"\w+\@\w+\.\w+", recipient)
grp_all= re.findall(r"(\w{3})\.(\w+)\.(\w{2,3})",recipient)
print(find_all)
print(grp_all)
domains=[y+"."+z for x,y,z in grp_all] 
print(domains)