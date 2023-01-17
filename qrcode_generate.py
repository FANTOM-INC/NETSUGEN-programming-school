import qrcode

url = "https://www.pref.gunma.jp/"

img = qrcode.make(url)
img.save("qrcode.png")
