
# Table of Contents

1.  [事前にやること](#org4393e9e)
2.  [使い方](#org2c8971d)
    1.  [excel.py](#org55e06d6)
    2.  [`find_file.py`](#org6053e01)
    3.  [pdf2txt.py](#org6b742bc)
    4.  [`pdf_ocr.py`](#org208a5aa)
    5.  [word2txt.py](#orgd3fdc91)
    6.  [`logo_injection.py`](#orgbfa7c8f)
    7.  [`prefix_image.py`](#org3908978)
    8.  [`resize_image.py`](#orgd7877c2)
    9.  [whisper.py](#orgd7dd5cb)
    10. [pdf2wordcloud.py](#org777079e)
    11. [txt2wordcloud.py](#org8c1710e)
    12. [`get_tweet.py`](#org909dc78)
    13. [`tweet_to_csv.py`](#org915754f)
    14. [`plot_nikkei.py`](#orga837893)
    15. [= plot<sub>nikkei</sub><sub>weekly.py</sub>=](#org9ecc83e)


<a id="org4393e9e"></a>

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


<a id="org2c8971d"></a>

# 使い方


<a id="org55e06d6"></a>

## excel.py

excelを読み込み、データを取得したり書き込んだりします。

    python excel.py


<a id="org6053e01"></a>

## `find_file.py`

file, pdf, excel, wordの文章を検索して、与えた文字列が含まれているファイルを表示します。

l92-93を適宜変更してから実行

    python find_file.py


<a id="org6b742bc"></a>

## pdf2txt.py

pdfをテキストに変換します。

    python pdf2txt.py ./sample_file/sample.pdf


<a id="org208a5aa"></a>

## `pdf_ocr.py`

pdfを画像として読み込みOCRしてテキストに変換します。

l37を適宜変更してから実行

    python pdf_ocr.py


<a id="orgd3fdc91"></a>

## word2txt.py

wordをテキストに変換します。

l5を適宜変更してから実行

    python word2txt.py


<a id="orgbfa7c8f"></a>

## `logo_injection.py`

画像の四隅にロゴを貼り付けます。

l47-l61を適宜変更してから実行

    python logo_injection.py


<a id="org3908978"></a>

## `prefix_image.py`

画像のファイル名にprefixをつけます。

l16を適宜変更してから実行

    python prefix_image.py


<a id="orgd7877c2"></a>

## `resize_image.py`

画像のサイズを変更します。

l10-12を適宜変更してから実行

    python resize_image.py


<a id="orgd7dd5cb"></a>

## whisper.py

whisperで動画をテキストに変換します。

l4を適宜変更してから実行

    python whisper.py


<a id="org777079e"></a>

## pdf2wordcloud.py

pdfをテキストに変換し、wordcloudを作成します。

    python pdf2wordcloud.py


<a id="org8c1710e"></a>

## txt2wordcloud.py

文字列をwordcloudに変換します。

l7を適宜変更してから実行

    python txt2wordcloud.py


<a id="org909dc78"></a>

## `get_tweet.py`

ツイートを取得します

    python get_tweet.py
    xxxx (検索したい文字列)


<a id="org915754f"></a>

## `tweet_to_csv.py`

ツイートをcsvに変換します

    python tweet_to_csv.py
    xxxx (検索したい文字列)


<a id="orga837893"></a>

## `plot_nikkei.py`

日経平均のcsvを読み込み、グラフを作成します

    python plot_nikkei.py


<a id="org9ecc83e"></a>

## = plot<sub>nikkei</sub><sub>weekly.py</sub>=

日経平均のcsvを読み込み、年毎に価格を平均化してグラフを作成します

    python plot_nikkei_weekly.py

