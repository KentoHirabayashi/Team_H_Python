import qrcode

img = qrcode.make("https://github.com/KentoHirabayashi/Team_H_Python/tree/main/Python_H/SeiyaYoshida515")
img.save("qrcode-test.png")