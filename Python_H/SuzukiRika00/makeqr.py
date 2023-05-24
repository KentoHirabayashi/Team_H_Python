import os
import sys
import qrcode

args = sys.argv

img = qrcode.make(args[1])

img.save(os.path.join("../../../","files", args[2])) 
