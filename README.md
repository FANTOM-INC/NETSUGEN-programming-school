
# Table of Contents

1.  [事前にやること](#org47a6e46)
2.  [使い方](#org5e68955)
    1.  [excel.py](#org8bd18e6)
    2.  [`find_file.py`](#org94f98fe)
    3.  [pdf2txt.py](#org5545407)
    4.  [`pdf_ocr.py`](#orgd0929d2)
    5.  [word2txt.py](#org19e2026)
    6.  [`logo_injection.py`](#org9e41156)
    7.  [`prefix_image.py`](#org6b967f5)
    8.  [`resize_image.py`](#orgb6c7797)
    9.  [whisper.py](#org0ab1ba6)
    10. [pdf2wordcloud.py](#org43f7fbc)
    11. [txt2wordcloud.py](#orga5a6fad)
    12. [`get_tweet.py`](#org9001f31)
    13. [`tweet_to_csv.py`](#orgbf0c1ff)
    14. [`plot_nikkei.py`](#org95956cb)


<a id="org47a6e46"></a>

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


<a id="org5e68955"></a>

# 使い方


<a id="org8bd18e6"></a>

## excel.py

excelを読み込み、データを取得したり書き込んだりします。

    python excel.py


<a id="org94f98fe"></a>

## `find_file.py`

file, pdf, excel, wordの文章を検索して、与えた文字列が含まれているファイルを表示します。

l92-93を適宜変更してから実行

    python find_file.py


<a id="org5545407"></a>

## pdf2txt.py

pdfをテキストに変換します。

    python pdf2txt.py ./sample_file/sample.pdf


<a id="orgd0929d2"></a>

## `pdf_ocr.py`

pdfを画像として読み込みOCRしてテキストに変換します。

l37を適宜変更してから実行

    python pdf_ocr.py


<a id="org19e2026"></a>

## word2txt.py

wordをテキストに変換します。

l5を適宜変更してから実行

    python word2txt.py


<a id="org9e41156"></a>

## `logo_injection.py`

画像の四隅にロゴを貼り付けます。

l47-l61を適宜変更してから実行

    python logo_injection.py


<a id="org6b967f5"></a>

## `prefix_image.py`

画像のファイル名にprefixをつけます。

l16を適宜変更してから実行

    python prefix_image.py


<a id="orgb6c7797"></a>

## `resize_image.py`

画像のサイズを変更します。

l10-12を適宜変更してから実行

    python resize_image.py


<a id="org0ab1ba6"></a>

## whisper.py

whisperで動画をテキストに変換します。

l4を適宜変更してから実行

    python whisper.py


<a id="org43f7fbc"></a>

## pdf2wordcloud.py

pdfをテキストに変換し、wordcloudを作成します。

    python pdf2wordcloud.py


<a id="orga5a6fad"></a>

## txt2wordcloud.py

文字列をwordcloudに変換します。

l7を適宜変更してから実行

    python txt2wordcloud.py


<a id="org9001f31"></a>

## `get_tweet.py`

ツイートを取得します

    python get_tweet.py
    xxxx (検索したい文字列)


<a id="orgbf0c1ff"></a>

## `tweet_to_csv.py`

ツイートをcsvに変換します

    python tweet_to_csv.py
    xxxx (検索したい文字列)


<a id="org95956cb"></a>

## `plot_nikkei.py`

日経平均のcsvを読み込み、グラフを作成します

    python plot_nikkei.py

