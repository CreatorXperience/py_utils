import random
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

# for x in iterator:
    # if x == 7 : 
    #     break
    # print(x)






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
        return f"{self.talk}"


human =  Child("emma", 10)
# print(human)

# num:int = "hi"


class Bird:
    def __init__(self, name, color):
        self.name = name
        self.color = color


   
    def __str__(self)-> str:
        return f"{self.name} is a bird"
   
    def reproduce(self):
        print(f"{self.name} can reproduce")


class Eagle(Bird):

    def __init__(self, name,color,speed):
        super().__init__(name,color)
        self.speed = speed

    def fly(self):
        print(f"{self.name} can fly")

    def dive(self):
        print(f"{self.name} can dive")
    
    def prey(self):
        print(f"{self.name} can prey")


# bird  = Bird("Eagle", "Black")
eagle  = Eagle("Eagle", "Black", "Fast")
eagle.reproduce()



class iterand: 
    def __init__(self, item:list[int]):
        self.item = item

    def __iter__(self):
        self.item = self.item
        return self
    
    def __next__(self):
        length = len(self.item)
        if length > 3 : 
            n  = random.randint(0, length-1)
            return [self.item[n]]

        raise StopIteration

loop = iterand([1,2])
iterator = iter(loop)
print(next(iterator))




try: 
    i = 0

except: 
    print("ma")   
    