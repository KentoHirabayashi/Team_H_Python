class Intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def name_out(self):
        nametxt = "私の名前は、{0}です".format(self.name)
        return nametxt
    
    def age_out(self):
        agetxt = "年齢は、{0}歳です".format(self.age)
        return agetxt