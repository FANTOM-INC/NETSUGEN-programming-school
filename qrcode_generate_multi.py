import qrcode

with open('sample_file/url.txt') as f:
    for i, line in enumerate(f):
        img = qrcode.make(line)
        img.save(f"{str(i)}.png")

