# -*- coding: utf-8 -*-
from PIL import Image
import sys
import pyocr
import pyocr.builders
import pdf2image
import matplotlib.pyplot as plt
import os
from pathlib import Path
from wordcloud import WordCloud
from pyknp import Juman

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
    pdf_path = "sample_file/sample2.pdf"
    content = get_text(pdf_path)
    print(content)

    # 形態素解析
    text = ""
    juman = Juman(command="jumanpp", timeout=1000)
    result = juman.analysis(content)

    exclude_list = ["等", "進", "実", "強", "組", "こと", "ため",
                    "め", "が", "て", "し", "か", "き", "ひ", "り", "け", "え", "の", "ほど", "しょ"]
    result = [mrph.midasi for mrph in result.mrph_list() if (
        mrph.hinsi == "名詞") and not (mrph.midasi in exclude_list) and (len(mrph.midasi) > 1)]
    word_chain = ' '.join(result)
    text = text + word_chain

    # WordCloud
    wc = WordCloud(background_color="white",
                   font_path="~/Library/Fonts/Arial Unicode.ttf", prefer_horizontal=1)
    wc.generate(text)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    plt.savefig("wordcloud.png")
