
# Table of Contents

1.  [事前にやること](#org3bb542d)
2.  [使い方](#org4d6e86c)
    1.  [excel.py](#org028e7ca)
    2.  [`find_file.py`](#orgc97fb0d)
    3.  [pdf2txt.py](#orgc96c4a2)
    4.  [`pdf_ocr.py`](#org469016f)
    5.  [word2txt.py](#org3b8f0c0)
    6.  [`logo_injection.py`](#orga863bc0)
    7.  [`prefix_image.py`](#orgafa576f)
    8.  [`resize_image.py`](#orga3895cb)
    9.  [whisper.py](#org16da336)
    10. [pdf2wordcloud.py](#org04e689e)
    11. [txt2wordcloud.py](#orgb6d638c)
    12. [`blur_image.py`](#orgf7b93gc)


<a id="org3bb542d"></a>

# 事前にやること

    sudo apt update -y
    sudo apt upgrade -y

    sudo apt-get install libjpeg-dev
    sudo apt-get install -y poppler-utils
    sudo apt -y install tesseract-ocr tesseract-ocr-jpn libtesseract-dev libleptonica-dev tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert 

JUMAN++をインストールする

    sudo apt install libboost-all-dev
    wget https://github.com/ku-nlp/jumanpp/releases/download/v2.0.0-rc3/jumanpp-2.0.0-rc3.tar.xz
    tar xvf jumanpp-2.0.0-rc3.tar.xz
    sudo apt install build-essential -y
    sudo apt install cmake -y
    cd jumanpp-2.0.0-rc3/
    mkdir buil
    cd build/
    cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local
    make
    sudo make install

その後requirements.txtをpip3 installする


<a id="org4d6e86c"></a>

# 使い方


<a id="org028e7ca"></a>

## excel.py

excelを読み込み、データを取得したり書き込んだりします。

    python excel.py


<a id="orgc97fb0d"></a>

## `find_file.py`

file, pdf, excel, wordの文章を検索して、与えた文字列が含まれているファイルを表示します。

l92-93を適宜変更してから実行

    python find_file.py


<a id="orgc96c4a2"></a>

## pdf2txt.py

pdfをテキストに変換します。

    python pdf2txt.py ./sample_file/sample.pdf


<a id="org469016f"></a>

## `pdf_ocr.py`

pdfを画像として読み込みOCRしてテキストに変換します。

l37を適宜変更してから実行

    python pdf_ocr.py


<a id="org3b8f0c0"></a>

## word2txt.py

wordをテキストに変換します。

l5を適宜変更してから実行

    python word2txt.py


<a id="orga863bc0"></a>

## `logo_injection.py`

画像の四隅にロゴを貼り付けます。

l47-l61を適宜変更してから実行

    python logo_injection.py


<a id="orgafa576f"></a>

## `prefix_image.py`

画像のファイル名にprefixをつけます。

l16を適宜変更してから実行

    python prefix_image.py


<a id="orga3895cb"></a>

## `resize_image.py`

画像のサイズを変更します。

l10-12を適宜変更してから実行

    python resize_image.py


<a id="org16da336"></a>

## whisper.py

whisperで動画をテキストに変換します。

l4を適宜変更してから実行

    python whisper.py


<a id="org04e689e"></a>

## pdf2wordcloud.py

pdfをテキストに変換し、wordcloudを作成します。

    python pdf2wordcloud.py


<a id="orgb6d638c"></a>

## txt2wordcloud.py

文字列をwordcloudに変換します。

l7を適宜変更してから実行

    python txt2wordcloud.py


<a id="orgf7b93gc"></a>
## blur_image.py

画像にガウスをかけてぼかします。（ブラー）

    python blur_image.py