#!/usr/bin/env python3

"""
    FORMAT SPECIFIER: using f-string(formatted strings literal) 
    and string format method ->> "".format()

    replacement_field ::=  "{"
            f_expression
            ["="]
            ["!" conversion]
            [":" format_spec]
            "}"

    format_spec     ::=  [[fill]align][sign]["z"]["#"]["0"][width]
                     [grouping_option]["." precision][type]

    fill            ::=  <any character>
    align           ::=  "<" | ">" | "=" | "^"
    sign            ::=  "+" | "-" | " "
    width           ::=  digit+
    grouping_option ::=  "_" | ","
    precision       ::=  digit+
    type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" |
                        "G" | "n" | "o" | "s" | "x" | "X" | "%"

"""
from math import pi
from datetime import datetime
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

print(array_diff([1,2,3,8],[4,5,6,2]))


def array_differ_ence(a:list, b:list):
    return [x for x in a if not x in b]


print(array_differ_ence([1,2,3,8],[4,5,6,2]))


MY_STRS  = "hello"

print(f"{MY_STRS:*^30}")


def  type_rep():
    """

    Representation Type 	Type 	Description
    b -	Binary 	Converts the number to base 2
    c 	Character 	Converts the number to the corresponding Unicode character
    d -	Decimal Integer 	Converts the number to base 10 c - 	Character 	Converts the number to 
        the corresponding Unicode character
    o -	Octal 	Converts the number to base 8
    x - or X 	Hexadecimal 	Converts the number to base 16, using lowercase or uppercase
        letters for the digits above 9
    n -	Number 	Works the same as d, except that it uses the current locale setting to insert the 
         appropriate thousand separator characters
         None 	Decimal Integer 	Works the same as d
    e or E 	- Scientific notation with the separator character in lowercase or uppercase,
             respectively
    f or F -  Fixed-point notation with nan and inf in lowercase or in uppercase,
              respectively
    g or G - General format where small numbers are represented in fixed-point notation and larger 
             numbers in scientific notation
    n - General format (same as g), except that it uses a locale-aware character
         as a thousand separator

"""
    print(f"{30:b}")
    print(f"{30:c}")
    print(f"{30:d}")
    print(f"{30:x}")
    print(f"{30:o}")
    print(f"{30:n}")
    print(f"{30:e}")
    print(f"{30.1:f}")
    print(f"{30:g}")
    inf = float("inf")
    print(f"{inf:f}")
    print(f"{inf:F}")





type_rep()

print(f"{pi:.4f}")

number = 12345689


print(f"{number:,}")
print(f"{number:_}")
print(f"{number:,.2f}")

total  = 123456.78
print(f"{total:$>10}")

print(f"Total:{total:.>30,.2f}")

now = datetime.now()

print(f"Today's Date is {now:%a %b %Y %H:%M %p}")