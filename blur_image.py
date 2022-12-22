from PIL import Image, ImageFilter


def blur_image(img):
    new_img = img.filter(ImageFilter.GaussianBlur(10))
    return new_img


if __name__ == '__main__':
    img = Image.open('sample_file/sample2.png')
    img = blur_image(img)
    img.save('image_blur.png')
