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
        return f"This person name is {self.name} and he/she is {self.age}.age years old"

    def __repr__(self) -> str:
        return "create an instance of a person using the class-> example : Person(name, age)"
    


new_person = Persona("Habeeb", 21)

amount = "two thousand"
remark = f"You bought goods @ the rate of {amount:=^30}"

print(remark)