import sys

class intro:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def name_out(self):
        return  f"私の名前は、{self.name}です"
    
    def age_out(self):
        return  f"年齢は、{self.name}歳です"
    
    def __str__(self) -> str:
        return f"私の名前は、{self.name}です\n年齢は、{self.age}歳です"
    
args = sys.argv
name = args[1]
age = args[2]

myinfo = intro(name, age)
print(myinfo)