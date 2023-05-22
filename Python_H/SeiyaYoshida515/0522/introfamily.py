import introduce as intro

class Introfam(intro.Intro):
    def __init__(self, name, age, cat_name):
        super().__init__(name, age)
        self.cat_name = cat_name
    
    def cat_name_out(self):
        nametxt = "飼い猫の名前は、{0}です".format(self.cat_name)
        return nametxt