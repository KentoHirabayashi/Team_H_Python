from introduce import Intro

class IntroFam(Intro):
    def __init__(self, name, age, cat): # コンストラクタ
        self.name = name
        self.age = age
        self.cat = cat

    #猫  
    def cat_out(self):
        cattxt = "飼い猫の名前は、{0}です".format(self.cat)
        return cattxt 
    
