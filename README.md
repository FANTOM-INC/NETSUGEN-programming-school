
# Table of Contents

1.  [事前にやること](#org87b258c)
2.  [使い方](#org3c14937)
    1.  [excel.py](#org0786121)
    2.  [`find_file.py`](#org9c2edbd)
    3.  [pdf2txt.py](#org728accc)
    4.  [`pdf_ocr.py`](#orge2cf3fd)
    5.  [word2txt.py](#org2a71078)
    6.  [`logo_injection.py`](#org462af0d)
    7.  [`prefix_image.py`](#org1bd5315)
    8.  [`resize_image.py`](#org3671aea)
    9.  [whisper.py](#org51a431e)
    10. [pdf2wordcloud.py](#org7c37b4f)
    11. [txt2wordcloud.py](#org304f758)
    12. [`get_tweet.py`](#orgf2cb4d8)
    13. [`tweet_to_csv.py`](#orgeb0ff4e)


<a id="org87b258c"></a>

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


<a id="org3c14937"></a>

# 使い方


<a id="org0786121"></a>

## excel.py

excelを読み込み、データを取得したり書き込んだりします。

    python excel.py


<a id="org9c2edbd"></a>

## `find_file.py`

file, pdf, excel, wordの文章を検索して、与えた文字列が含まれているファイルを表示します。

l92-93を適宜変更してから実行

    python find_file.py


<a id="org728accc"></a>

## pdf2txt.py

pdfをテキストに変換します。

    python pdf2txt.py ./sample_file/sample.pdf


<a id="orge2cf3fd"></a>

## `pdf_ocr.py`

pdfを画像として読み込みOCRしてテキストに変換します。

l37を適宜変更してから実行

    python pdf_ocr.py


<a id="org2a71078"></a>

## word2txt.py

wordをテキストに変換します。

l5を適宜変更してから実行

    python word2txt.py


<a id="org462af0d"></a>

## `logo_injection.py`

画像の四隅にロゴを貼り付けます。

l47-l61を適宜変更してから実行

    python logo_injection.py


<a id="org1bd5315"></a>

## `prefix_image.py`

画像のファイル名にprefixをつけます。

l16を適宜変更してから実行

    python prefix_image.py


<a id="org3671aea"></a>

## `resize_image.py`

画像のサイズを変更します。

l10-12を適宜変更してから実行

    python resize_image.py


<a id="org51a431e"></a>

## whisper.py

whisperで動画をテキストに変換します。

l4を適宜変更してから実行

    python whisper.py


<a id="org7c37b4f"></a>

## pdf2wordcloud.py

pdfをテキストに変換し、wordcloudを作成します。

    python pdf2wordcloud.py


<a id="org304f758"></a>

## txt2wordcloud.py

文字列をwordcloudに変換します。

l7を適宜変更してから実行

    python txt2wordcloud.py


<a id="orgf2cb4d8"></a>

## `get_tweet.py`

ツイートを取得します

    python get_tweet.py


<a id="orgeb0ff4e"></a>

## `tweet_to_csv.py`

ツイートをcsvに変換します

    python tweet_to_csv.py

