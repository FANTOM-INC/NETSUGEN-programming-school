from PIL import Image, ImageFilter


def scale_to_width(img, width):
    height = round(img.height * width / img.width)
    return img.resize((width, height))


if __name__ == '__main__':
    img = Image.open('setting/logo.png')
    img = scale_to_width(img, 100)
    img.save('image_resized.jpg')
