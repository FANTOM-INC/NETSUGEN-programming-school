from PIL import Image, ImageFilter


def scale_to_width(img, width):
    height = round(img.height * width / img.width)
    return img.resize((width, height))


if __name__ == '__main__':
    img = Image.open('sample_file/sample2.png')
    img = scale_to_width(img, 800)
    img.save('image_resized.jpg')
