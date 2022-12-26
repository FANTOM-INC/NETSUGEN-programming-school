
# Table of Contents

1.  [事前にやること](#orgbda80b8)
2.  [使い方](#org8b32e41)
    1.  [excel.py](#org80f8b9a)
    2.  [`find_file.py`](#orgf04388d)
    3.  [pdf2txt.py](#orgce11ce7)
    4.  [`pdf_ocr.py`](#orgf03a15a)
    5.  [word2txt.py](#orgab7faed)
    6.  [`logo_injection.py`](#orgc038fac)
    7.  [`prefix_image.py`](#org0a5e7ee)
    8.  [`resize_image.py`](#org853653e)
    9.  [whisper.py](#org786073a)
    10. [pdf2wordcloud.py](#org7d1d3da)
    11. [txt2wordcloud.py](#org93814bc)
    12. [`get_tweet.py`](#orgbb72d2e)
    13. [`tweet_to_csv.py`](#orgf0d2426)
    14. [`plot_nikkei.py`](#org4cbcf27)
    15. [`plot_nikkei_weekly.py`](#org919992e)


<a id="orgbda80b8"></a>

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


<a id="org8b32e41"></a>

# 使い方


<a id="org80f8b9a"></a>

## excel.py

excelを読み込み、データを取得したり書き込んだりします。

    python excel.py


<a id="orgf04388d"></a>

## `find_file.py`

file, pdf, excel, wordの文章を検索して、与えた文字列が含まれているファイルを表示します。

l92-93を適宜変更してから実行

    python find_file.py


<a id="orgce11ce7"></a>

## pdf2txt.py

pdfをテキストに変換します。

    python pdf2txt.py ./sample_file/sample.pdf


<a id="orgf03a15a"></a>

## `pdf_ocr.py`

pdfを画像として読み込みOCRしてテキストに変換します。

l37を適宜変更してから実行

    python pdf_ocr.py


<a id="orgab7faed"></a>

## word2txt.py

wordをテキストに変換します。

l5を適宜変更してから実行

    python word2txt.py


<a id="orgc038fac"></a>

## `logo_injection.py`

画像の四隅にロゴを貼り付けます。

l47-l61を適宜変更してから実行

    python logo_injection.py


<a id="org0a5e7ee"></a>

## `prefix_image.py`

画像のファイル名にprefixをつけます。

l16を適宜変更してから実行

    python prefix_image.py


<a id="org853653e"></a>

## `resize_image.py`

画像のサイズを変更します。

l10-12を適宜変更してから実行

    python resize_image.py


<a id="org786073a"></a>

## whisper.py

whisperで動画をテキストに変換します。

l4を適宜変更してから実行

    python whisper.py


<a id="org7d1d3da"></a>

## pdf2wordcloud.py

pdfをテキストに変換し、wordcloudを作成します。

    python pdf2wordcloud.py


<a id="org93814bc"></a>

## txt2wordcloud.py

文字列をwordcloudに変換します。

l7を適宜変更してから実行

    python txt2wordcloud.py


<a id="orgbb72d2e"></a>

## `get_tweet.py`

ツイートを取得します

    python get_tweet.py
    xxxx (検索したい文字列)


<a id="orgf0d2426"></a>

## `tweet_to_csv.py`

ツイートをcsvに変換します

    python tweet_to_csv.py
    xxxx (検索したい文字列)


<a id="org4cbcf27"></a>

## `plot_nikkei.py`

日経平均のcsvを読み込み、グラフを作成します

    python plot_nikkei.py


<a id="org919992e"></a>

## `plot_nikkei_weekly.py`

日経平均のcsvを読み込み、年毎に価格を平均化してグラフを作成します

    python plot_nikkei_weekly.py

