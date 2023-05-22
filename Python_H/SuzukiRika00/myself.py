import sys
from introduce import Intro
args = sys.argv

txt = Intro(args[1], args[2])

print(txt.name_out()) 
print(txt.age_out())  