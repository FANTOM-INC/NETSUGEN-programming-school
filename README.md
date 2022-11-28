
# Table of Contents

1.  [事前にやること](#org32e1408)
2.  [使い方](#orgd9b26f8)
    1.  [excel.py](#orged2e4f4)
    2.  [`find_file.py`](#org9cca2dd)
    3.  [pdf2txt.py](#orgdd1346d)
    4.  [`pdf_ocr.py`](#orgf80cec9)
    5.  [word2txt.py](#org7875080)
    6.  [`logo_injection.py`](#org334358b)
    7.  [`prefix_image.py`](#org497a39d)
    8.  [`resize_image.py`](#org9201f82)
    9.  [whisper.py](#orge53382a)
    10. [pdf2wordcloud.py](#org88f3be1)


<a id="org32e1408"></a>

# 事前にやること

    sudo apt-get install libjpeg-dev
    sudo apt-get install -y poppler-utils
    sudo apt -y install tesseract-ocr tesseract-ocr-jpn libtesseract-dev libleptonica-dev tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert 

JUMAN++をインストールする

    wget http://lotus.kuee.kyoto-u.ac.jp/nl-resource/jumanpp/jumanpp-1.02.tar.xz
    tar xJvf jumanpp-1.02.tar.xz
    cd jumanpp-1.02
    ./configure
    make
    sudo make install

その後requirements.txtをpip3 installする


<a id="orgd9b26f8"></a>

# 使い方


<a id="orged2e4f4"></a>

## excel.py

excelを読み込み、データを取得したり書き込んだりします。

    python excel.py


<a id="org9cca2dd"></a>

## `find_file.py`

file, pdf, excel, wordの文章を検索して、与えた文字列が含まれているファイルを表示します。

l92-93を適宜変更してから実行

    python find_file.py


<a id="orgdd1346d"></a>

## pdf2txt.py

pdfをテキストに変換します。

    python pdf2txt.py ./sample_file/sample.pdf


<a id="orgf80cec9"></a>

## `pdf_ocr.py`

pdfを画像として読み込みOCRしてテキストに変換します。

l37を適宜変更してから実行

    python pdf_ocr.py


<a id="org7875080"></a>

## word2txt.py

wordをテキストに変換します。

l5を適宜変更してから実行

    python word2txt.py


<a id="org334358b"></a>

## `logo_injection.py`

画像の四隅にロゴを貼り付けます。

l47-l61を適宜変更してから実行

    python logo_injection.py


<a id="org497a39d"></a>

## `prefix_image.py`

画像のファイル名にprefixをつけます。

l16を適宜変更してから実行

    python prefix_image.py


<a id="org9201f82"></a>

## `resize_image.py`

画像のサイズを変更します。

l10-12を適宜変更してから実行

    python resize_image.py


<a id="orge53382a"></a>

## whisper.py

whisperで動画をテキストに変換します。

l4を適宜変更してから実行

    python whisper.py


<a id="org88f3be1"></a>

## pdf2wordcloud.py

pdfをテキストに変換し、wordcloudを作成します。

    python pdf2wordcloud.py

