from introfamily import IntroFam
import sys

args = sys.argv

output = IntroFam(args[1],int(args[2]),args[3])

print(output.name_out())
print(output.age_out())
print(output.cat_out())
