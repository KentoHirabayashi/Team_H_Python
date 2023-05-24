import sys 

from myself import Intro

class IntroFam(Intro):

    def __init__(self, name, age, cat_name) -> None:
        super().__init__(name, age)
        self.cat_name = cat_name

    def cat_out(self):
        return  f"飼い猫の名前は、{self.cat_name}です"
    
    def __str__(self) -> str:
        return f"私の名前は、{self.name}です\n年齢は、{self.age}歳です\n飼い猫の名前は、{self.cat_name}です"
    

if __name__ == "__main__": 
    args = sys.argv
    name = args[1]
    age = args[2]
    cat_name = args[3]

    myinfo = IntroFam(name, age, cat_name)
    print(myinfo)