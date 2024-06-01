"""

     Regular Expression
    -searching for pattern in strings

    """
import re
import sys
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
find_iter= re.finditer(r"\w+\@\w+\.\w+", recipient)
print(find_all)
print(grp_all)
domains=[y+"."+z for x,y,z in grp_all] 
print(domains)
print(find_iter)

# print(next(find_iter))
# print(next(find_iter))
# print(next(find_iter))
# print(next(find_iter))




machala = re.finditer(r"(?P<name>\w+)\@(?P<service>\w+)\.(?P<domain>\w+)", recipient)
print(machala)

# for item in machala:
#     print(item.groupdict())


# user = re.sub("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)",
#         "\g<TLD>.\g<SLD>.\g<name>", recipient)
# print(user)



regex=re.compile(r"\w+\@\w+\.\w+")
print(regex.search(recipient))
# print(regex)


def count(n):
    while True:
        n=n+1
        yield n

# c=count(1)
# print(next(c))

def fibonnaci():
    first = 0
    last = 1
    while True:
        first,last = last, first+last
        yield first

f = fibonnaci()
print(next(f))
print(next(f))
print(next(f))


for x in  f:
    print(x)
    if x > 12:
        break


gen_comprehension = (x for x in range(100))
list_comprehension = [x for x in range(100)]
print(next(gen_comprehension))
print(next(gen_comprehension))
print(next(gen_comprehension))



size = sys.getsizeof(gen_comprehension)
size_l = sys.getsizeof(list_comprehension)
print(size)
print(size_l)


word = "smogtether"

new_s = "".join([x.capitalize() for x in word])
print([new_s])



def alt():
    boo=0
    while True:
        if boo == 0:
            boo = 1
            yield False
        elif boo == 1:
            boo = 0
            yield True

a = alt()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

line = ''' 127.0.0.1 - rj [13/Nov/2019:14:43:30] "POST HTTP/1.0" 200
127.0.0.1 - rj [13/Nov/2019:14:43:30] "DELETE HTTP/1.0" 404
127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 301
127.0.0.1 - rj [13/Nov/2019:14:43:30] "PATCH HTTP/1.0" 200
127.0.0.1 - rj [13/Nov/2019:14:43:30] "POST HTTP/1.0" 500
127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200
 '''

ip = re.search(r"(?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
dates = re.search(r'\[(?P<DATE>\d{1,2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]', line)
print(dates.group("DATE"))
crud_type = re.search(r"\"(?P<TYPE>\w+\s\w+/\d\.\d)\"", line)
status = re.search(r"(?P<STATUS>\s\d{3})",line)
print(ip.group("IP"))
print(crud_type.group("TYPE"))
print(status.group("STATUS"))

r = r"(?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
r +=   r" -\s(?P<USER>\w+)"
r += r" \[(?P<DATE>\d{1,2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]"
r += r" \"(?P<TYPE>\w+\s\w+/\d\.\d)\""
r += r"(?P<STATUS>\s\d{3})"

print(r)

reiter = re.finditer(r,line)
for it in reiter:
    print(it.group("STATUS"))