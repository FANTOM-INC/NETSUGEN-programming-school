
# Table of Contents

1.  [使い方](#org702ee60)
    1.  [excel.py](#org9400666)
    2.  [`find_file.py`](#orga8daf51)
    3.  [pdf2txt.py](#orgfe82f70)
    4.  [`pdf_ocr.py`](#orge83727f)
    5.  [word2txt.py](#org6259b53)
    6.  [`logo_injection.py`](#org66329e3)
    7.  [`prefix_image.py`](#org87300e6)
    8.  [`resize_image.py`](#orgd0a8269)
    9.  [whisper.py](#org1ce62fe)


<a id="org702ee60"></a>

# 使い方


<a id="org9400666"></a>

## excel.py

excelを読み込み、データを取得したり書き込んだりします。

    python excel.py


<a id="orga8daf51"></a>

## `find_file.py`

file, pdf, excel, wordの文章を検索して、与えた文字列が含まれているファイルを表示します。

l92-93を適宜変更してから実行

    python find_file.py


<a id="orgfe82f70"></a>

## pdf2txt.py

pdfをテキストに変換します。

    python pdf2txt.py ./sample_file/sample.pdf


<a id="orge83727f"></a>

## `pdf_ocr.py`

pdfを画像として読み込みOCRしてテキストに変換します。

l37を適宜変更してから実行

    python pdf_ocr.py


<a id="org6259b53"></a>

## word2txt.py

wordをテキストに変換します。

l5を適宜変更してから実行

    python word2txt.py


<a id="org66329e3"></a>

## `logo_injection.py`

画像の四隅にロゴを貼り付けます。

l47-l61を適宜変更してから実行

    python logo_injection.py


<a id="org87300e6"></a>

## `prefix_image.py`

画像のファイル名にprefixをつけます。

l16を適宜変更してから実行

    python prefix_image.py


<a id="orgd0a8269"></a>

## `resize_image.py`

画像のサイズを変更します。

l10-12を適宜変更してから実行

    python resize_image.py


<a id="org1ce62fe"></a>

## whisper.py

whisperで動画をテキストに変換します。

l4を適宜変更してから実行

    python whisper.py

