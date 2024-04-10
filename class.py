class action:
    x =  "peter"

let = action()
print(let.x)


class Actor:
    def __init__(self,name,passw):
        self.name = name
        self.passwd = passw

    def __str__(self):
        return f"{self.name} {self.passwd}"
    
    def delete_act(self):
        return f"{self.name} is deleted"

act = Actor("vin", "diesel")
print(act.delete_act()) 
