tup = ("peter", "paul", "shark")
iterator = iter(tup)


first = next(iterator)
second = next(iterator)
third = next(iterator)





class ForEach:
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a == 7:
            return StopIteration
        else: 
            val = self.a + 1 
        
            self.a = val
            return val


loo = ForEach()
iterator = iter(loo)

for x in iterator:
    if x == 7 : 
        break
    print(x)






class Parent: 
    def __init__(self, name, age):
        self.name =  name
        self.age = age
    

    def talk(self) -> int: 
        print(f"I am {self.name}")

    def __str__(self) -> str: 
        print(f"I'm the parent {self.name}")
        return f"I'm the parent {self.name}"




class Child(Parent): 
    def speech(self):
        self.talk()
    
    def __str__(self) -> str:
        return super().__str__()


human =  Child("emma", 10)
print(human)

# num:int = "hi"