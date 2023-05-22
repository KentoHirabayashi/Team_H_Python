import sys
from introfamily import IntroFam
args = sys.argv

txt = IntroFam(args[1], args[2], args[3])

print(txt.name_out()) 
print(txt.age_out())  
print(txt.cat_out())  