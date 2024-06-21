from collections import deque
from array import array

# stacks

arr = ["peter", "kelvin", "apple", "cat", "ball"]
arr.sort()
arr.reverse()
print(arr)
stack = [1, 2, 3]
stack.append(4)
stack.pop()
print(stack)


# deque

queue = deque(["Java", "Rust", "Golang"], 5)
queue.append("javascript")
queue.append("python")
queue.popleft()
queue.popleft()


print(queue)


# dictionary
product = {
    "name": "T-shirt",
    "quantity": 1,
    "amount": 50,
    "colors": ["yellow", "blue", "green", "black", [1, 2, 3]],
    "others": {"bonus": "flower", "2": "1"},
}

product["others"]["bonus"] = "lotus flower"

print(product["others"]["bonus"])
print(product["colors"][len(product["colors"]) - 1][1])
del product["others"]["2"]
print(len(product))
print(type(product.items()))
print(product.keys())
print(product.values())
product.pop("quantity")
clone = product.copy()
clone.clear()
product.clear()
print(product)


# update deque
item = {"name": "shoe"}
item2 = {"product": "bag"}
new_item = {}
new_item.update(item2)
new_item.update(item)
print(new_item)

# Sets

set = {"Joha", "Bullshit", "C", "Java"}
set.add("Garbage")
set.update(["Python", "Javascript"])
set.add("Python")
set.remove("Bullshit")
set.discard("Garbage")

new_set = {"Java"}
unity = set.union(new_set)
intersect = set.intersection(new_set)
diff = set.difference(new_set)
sub = set.issubset(new_set)
joint = set.isdisjoint(new_set)
sup = set.issuperset(new_set)
print(sup)
