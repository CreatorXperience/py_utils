from  collections import deque
# stacks

arr = ["peter", "kelvin", "apple", "cat", "ball"]
arr.sort()
arr.reverse()
print(arr)
stack = [1,2,3]
stack.append(4)
stack.pop()
print(stack)

# deque
queue = deque(["Java", "Rust", "Golang"],5)
queue.append("javascript")
queue.append("python")
queue.popleft()
queue.popleft()


print(queue)

