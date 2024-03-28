list  = []
list  = ["hi"]
list[0] = "Hello"
list = [1,2,3,4,5]
list[0:3] = [9,10,11]

list.extend([10, 11, 20])
list.append(10)
list.remove(10)
list.pop(2)
index  =  list.index(10)
list.insert(len(list), {"id": "yo"})
print(list)
lens = list.index({"id": "yo"})
clone = [1,2]
clone.extend(list)
# list.extend()
print(clone)

wordd = "this is another type of string in %s and it cost %.3f dollar"%("javascript", 10)
print(wordd)
my_words = "this is a string in name and {val}"
print(my_words)