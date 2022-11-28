
# Table of Contents

1.  [事前にやること](#org4a844e4)
2.  [使い方](#orgc5ef180)
    1.  [excel.py](#org1165adc)
    2.  [`find_file.py`](#org09c0e4e)
    3.  [pdf2txt.py](#orge341e4f)
    4.  [`pdf_ocr.py`](#orgd20b8e8)
    5.  [word2txt.py](#orga6380d9)
    6.  [`logo_injection.py`](#org8f17568)
    7.  [`prefix_image.py`](#org7dc2b95)
    8.  [`resize_image.py`](#org86f8310)
    9.  [whisper.py](#orgbc1af5c)
    10. [pdf2wordcloud.py](#org895a988)
    11. [txt2wordcloud.py](#org7fda382)


<a id="org4a844e4"></a>

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


<a id="orgc5ef180"></a>

# 使い方


<a id="org1165adc"></a>

## excel.py

excelを読み込み、データを取得したり書き込んだりします。

    python excel.py


<a id="org09c0e4e"></a>

## `find_file.py`

file, pdf, excel, wordの文章を検索して、与えた文字列が含まれているファイルを表示します。

l92-93を適宜変更してから実行

    python find_file.py


<a id="orge341e4f"></a>

## pdf2txt.py

pdfをテキストに変換します。

    python pdf2txt.py ./sample_file/sample.pdf


<a id="orgd20b8e8"></a>

## `pdf_ocr.py`

pdfを画像として読み込みOCRしてテキストに変換します。

l37を適宜変更してから実行

    python pdf_ocr.py


<a id="orga6380d9"></a>

## word2txt.py

wordをテキストに変換します。

l5を適宜変更してから実行

    python word2txt.py


<a id="org8f17568"></a>

## `logo_injection.py`

画像の四隅にロゴを貼り付けます。

l47-l61を適宜変更してから実行

    python logo_injection.py


<a id="org7dc2b95"></a>

## `prefix_image.py`

画像のファイル名にprefixをつけます。

l16を適宜変更してから実行

    python prefix_image.py


<a id="org86f8310"></a>

## `resize_image.py`

画像のサイズを変更します。

l10-12を適宜変更してから実行

    python resize_image.py


<a id="orgbc1af5c"></a>

## whisper.py

whisperで動画をテキストに変換します。

l4を適宜変更してから実行

    python whisper.py


<a id="org895a988"></a>

## pdf2wordcloud.py

pdfをテキストに変換し、wordcloudを作成します。

    python pdf2wordcloud.py


<a id="org7fda382"></a>

## txt2wordcloud.py

文字列をwordcloudに変換します。

l7を適宜変更してから実行

    python txt2wordcloud.py

