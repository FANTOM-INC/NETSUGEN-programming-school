import numpy as np
from PIL import Image, ImageFilter


def transparency(img, alpha):
    img = np.array(img)
    img[img[..., 3] != 0, 3] = alpha
    img = Image.fromarray(img)
    return img


def logo_injection(im, logo_right_above, logo_right_below, logo_left_above, logo_left_below):
    """
    ロゴ埋め込み
    """
    if logo_info_right_above != None:
        logo_right_above = transparency(scale_to_width(
            Image.open(logo_info_right_above["path"]), logo_info_right_above["width"]), logo_info_right_above["alpha"])
        im.paste(logo_right_above,
                 (im.size[0]-logo_right_above.size[0], 0), logo_right_above)

    if logo_info_right_below != None:
        logo_right_below = transparency(scale_to_width(
            Image.open(logo_info_right_below["path"]), logo_info_right_below["width"]), logo_info_right_below["alpha"])
        im.paste(logo_right_below, (im.size[0]-logo_right_below.size[0],
                                    im.size[1]-logo_right_below.size[1]), logo_right_below)

    if logo_info_left_above != None:
        logo_left_above = transparency(scale_to_width(
            Image.open(logo_info_left_above["path"]), logo_info_left_above["width"]), logo_info_left_above["alpha"])

        im.paste(logo_left_above, (0, 0), logo_left_above)
    if logo_info_left_below != None:
        logo_left_below = transparency(scale_to_width(
            Image.open(logo_info_left_below["path"]), logo_info_left_below["width"]), logo_info_left_below["alpha"])
        im.paste(logo_left_below,
                 (0, im.size[1] - logo_left_below.size[1]), logo_left_below)
    return im


def scale_to_width(img, width):
    height = round(img.height * width / img.width)
    return img.resize((width, height))


if __name__ == "__main__":
    logo_info_right_above = {"path": "setting/logo.png",
                             "alpha": 50,
                             "width": 100}

    logo_info_right_below = {"path": "setting/logo.png",
                             "alpha": 100,
                             "width": 200}

    logo_info_left_above = {"path": "setting/logo.png",
                            "alpha": 200,
                            "width": 700}

    logo_info_left_below = None

    im = Image.open('sample_file/sample2.png')
    im = logo_injection(im, logo_info_right_above, logo_info_right_below,
                        logo_info_left_above, logo_info_left_below)

    im.save('out.png')
