import qrcode
import sys

args = sys.argv

url = args[1]
fail_name = args[2]

path = qrcode.make(url)

path.save("./files/qrcode.png")