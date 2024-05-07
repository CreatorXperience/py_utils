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

def reversed_word(item:str):
    words=item.split(" ")
    reversed_words=[word[::-1] for word in words]
    print(" ".join(reversed_words))

reversed_word("This  is  a  word") 