from introduce import Intro
import sys

args = sys.argv

class IntroFam(Intro):
    def __init__(self, name, age, cat):

        self.name = name

        self.age = age

        self.cat = cat

    def cat_out(self):
        outtext = f"飼い猫の名前は{self.cat}です"
        return outtext