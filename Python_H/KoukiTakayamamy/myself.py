from introduce import Intro
import sys

args = sys.argv

output = Intro(args[1],int(args[2]))

print(output.name_out())
print(output.age_out())
