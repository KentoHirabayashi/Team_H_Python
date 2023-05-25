import qrcode
import sys
import os


args = sys.argv

url = args[1]
file_name = args[2]

path = os.path.join("../../../","day4",file_name + ".png")

img = qrcode.make(url)

img.save(path)