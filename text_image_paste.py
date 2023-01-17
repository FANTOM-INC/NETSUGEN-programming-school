from PIL import Image, ImageDraw, ImageFont

IMAGE_PATH = "sample_file/base.jpg"
OUT_PATH = "text_paste_image.png"

FONT_PATH = "setting/NotoSansJP-Bold.otf"
FONT_SIZE = 40
FONT_COLOR = (255, 255, 255)
TEXT = "Pythonでプログラミング"

font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

image = Image.open(IMAGE_PATH)
image = image.convert("RGB")
draw = ImageDraw.Draw(image)

(font_w, font_h), (offset_x, offset_y) = font.font.getsize(TEXT)
img_w, img_h = image.size

position = ((img_w - font_w) / 2, (img_h - font_h) / 2)

draw.text(position, TEXT, font=font, fill=FONT_COLOR)
image.save(OUT_PATH, "PNG")
