
# Table of Contents

1.  [事前にやること](#org7fd144f)
2.  [使い方](#orge00bb7f)
    1.  [excel.py](#orgbb08c6f)
    2.  [`find_file.py`](#orgd882d10)
    3.  [pdf2txt.py](#orgc38738b)
    4.  [`pdf_ocr.py`](#orgd2fe6b6)
    5.  [word2txt.py](#org5242f5c)
    6.  [`logo_injection.py`](#org4031c4f)
    7.  [`prefix_image.py`](#orgbd46297)
    8.  [`resize_image.py`](#org65a1c50)
    9.  [whisper.py](#orgf61f609)


<a id="org7fd144f"></a>

# 事前にやること

    sudo apt-get install libjpeg-dev
    sudo apt-get install -y poppler-utils
    sudo apt -y install tesseract-ocr tesseract-ocr-jpn libtesseract-dev libleptonica-dev tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert 

その後requirements.txtをpip3 installする


<a id="orge00bb7f"></a>

# 使い方


<a id="orgbb08c6f"></a>

## excel.py

excelを読み込み、データを取得したり書き込んだりします。

    python excel.py


<a id="orgd882d10"></a>

## `find_file.py`

file, pdf, excel, wordの文章を検索して、与えた文字列が含まれているファイルを表示します。

l92-93を適宜変更してから実行

    python find_file.py


<a id="orgc38738b"></a>

## pdf2txt.py

pdfをテキストに変換します。

    python pdf2txt.py ./sample_file/sample.pdf


<a id="orgd2fe6b6"></a>

## `pdf_ocr.py`

pdfを画像として読み込みOCRしてテキストに変換します。

l37を適宜変更してから実行

    python pdf_ocr.py


<a id="org5242f5c"></a>

## word2txt.py

wordをテキストに変換します。

l5を適宜変更してから実行

    python word2txt.py


<a id="org4031c4f"></a>

## `logo_injection.py`

画像の四隅にロゴを貼り付けます。

l47-l61を適宜変更してから実行

    python logo_injection.py


<a id="orgbd46297"></a>

## `prefix_image.py`

画像のファイル名にprefixをつけます。

l16を適宜変更してから実行

    python prefix_image.py


<a id="org65a1c50"></a>

## `resize_image.py`

画像のサイズを変更します。

l10-12を適宜変更してから実行

    python resize_image.py


<a id="orgf61f609"></a>

## whisper.py

whisperで動画をテキストに変換します。

l4を適宜変更してから実行

    python whisper.py

