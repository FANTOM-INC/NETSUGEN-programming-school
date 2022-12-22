from PIL import Image


def graysclae(img):
    new_img = img.convert('L')
    return new_img


if __name__ == '__main__':
    img = Image.open('sample_file/sample2.png')
    img = graysclae(img)
    img.save('image_gray.png')
