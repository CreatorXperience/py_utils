"""
    FORMAT SPECIFIER: using f-string(formatted strings literal) 
    and string format method ->> "".format()

    replacement_field ::=  "{"
            f_expression
            ["="]
            ["!" conversion]
            [":" format_spec]
            "}"

"""


#For Example:
class Persona:
    """
        Creates a personal class for individual

        create a class with your information:

        Attributes:
            name: specifies the name of the person
            age: specifies the age of the person
            __str__: returns a str indicating the usage of the class
            __repr__: return a developer friendly message about the class usage
    """

    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age


    def __str__(self)-> str:
        return f"This person name is {self.name} and he/she is {self.age} age years old"

    def __repr__(self) -> str:
        return "create an instance of a person using the class-> example : Person(name, age)"
    


new_person = Persona("Habeeb", "unknown")


amount = "five thousand"
remark = f"You bought goods @ the rate of {amount!r}"
remark = "Your balance is {} and expenses are {} from {person!r}".format(2000,3000,person=new_person)
# message = "your name is {name}".format(name)
print(remark)


# print(list(set([1,2,2])))

# arr = [1,2]
# arr.extend([3,4])
# {} = {1:"hi", 2: "hire"} =[1,2,3,4]

# print(arr)
def array_diff(a:list, b:list):
    positions = []
    clone = []
    clone.extend(a)
    for index,i in enumerate(a):
        for pos,k in enumerate(b):
            if i == k:
                print("index",index)
                positions.append(index)


    print(positions)
    for ind_x,i in enumerate(positions):
        a[i] = None
    


    another_array = []

    for i, value in enumerate(a):
        if value is not None:
            another_array.append(value)
        
             
    return another_array


print(array_diff([6,2,8,9,0],[]))


# def array_differ_ence(a:list, b:list):
#     for i in zip(a,b):
#         print(i)

# array_differ_ence([1,2,3,8],[4,5,6,2])