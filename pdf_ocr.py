# -*- coding: utf-8 -*-
from PIL import Image
import sys
import pyocr
import pyocr.builders
import pdf2image
import os
from pathlib import Path

# jpn.traineddataを指定
os.environ["TESSDATA_PREFIX"] = (Path.cwd() / "setting").as_posix()


def get_text(pdf_path):
    content = ""
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        # tesseractがインストールされていない場合はここで終了
        sys.exit(1)
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))

    images = pdf2image.convert_from_path(pdf_path, dpi=200, fmt='jpg')
    lang = 'jpn'
    for image in images:
        txt = tool.image_to_string(
            image,
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        txt = txt.replace(" ", "").replace("　", "").replace("\n", "")
        content += txt
    return content


if __name__ == "__main__":
    pdf_path = "sample_file/sample.pdf"
    content = get_text(pdf_path)
    print(content)
