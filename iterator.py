"""
    Iterator 
    
"""
import random
tup = ("peter", "paul", "shark")
iterator = iter(tup)


first = next(iterator)
second = next(iterator)
third = next(iterator)





class ForEach:
    """
        ForEach iterator class

    """
    def __init__(self):
        self.a  = 0

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
    """
        Parent Object
    """
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def talk(self) -> int:
        """
            talk Method
        """
        print(f"I am {self.name}")

    def __str__(self) -> str:
        print(f"I'm the parent {self.name}")
        return f"I'm the parent {self.name}"




class Child(Parent):
    """
        child class
    """

    def speech(self):
        """
            child speech method
        """
        self.talk()

    def __str__(self) -> str:
        return f"{self.talk}"


human =  Child("emma", 10)
# print(human)

# num:int = "hi"


class Bird:
    """
        Bird object blueprint

    """
    def __init__(self, name, color):
        self.name = name
        self.color = color


    def __str__(self)-> str:
        return f"{self.name} is a bird"

    def reproduce(self):
        """
            reproduce method
        """
        print(f"{self.name} can reproduce")


class Eagle(Bird):
    """
        Eagle Object blueprint

    """
    def __init__(self, name,color,speed):
        super().__init__(name,color)
        self.speed = speed

    def fly(self):
        """
            eagle fly method
        """
        print(f"{self.name} can fly")

    def dive(self):
        """
            eagle dive method

        """
        print(f"{self.name} can dive")

    def prey(self):
        """
            eagle prey method

        """
        print(f"{self.name} can prey")


# bird  = Bird("Eagle", "Black")
eagle  = Eagle("Eagle", "Black", "Fast")
eagle.reproduce()



class Iterand:
    """
        class iterator in python
        
    """
    def __init__(self, item:list[int]):
        self.item = item

    def __iter__(self):
        self.item = self.item
        return self

    def __next__(self):
        length = len(self.item)

        n  = random.randint(0, length-1)
        return [self.item[n]]


loop = Iterand([1,2,5,6,7])
iterator = iter(loop)
print(next(iterator))

F = "hi"
def print_num():
    """
        prints num

    """
    print(F)

print_num()

print(F)
