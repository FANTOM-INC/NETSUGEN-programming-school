# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pyknp import Juman

if __name__ == "__main__":
    content = """IoTセンサで温湿度など収集→クラウド蓄積→見えるか(ダシュボ)＆閾値超過時アラート(自動メールなど)
集客、予約管理(予約。新規とそれ以外、リマインダー機能など)、
ファイルを探すのがやっかい
リピート品は全体の20%ほどの製造業なので、受発注を入力したら工程管理が出来て値段も出る。人に頼らない仕組みが出来たら有難いです
製造業現場で使うIoTデバイスを操作したい
現在、キントーンを導入しており、より使いこなして、使いやすくするために《JavaScript、 CSS》を勉強したい
実現したいこと：自動車管理一覧の入力・出力システムの構築。AWS全般についても興味があります。
集計処理（ただし、プログラミングについての知識がないため、何ができるかが分からない。）
IoT機器からのデータの収集・監視・通知（soracom）、画像分析・テキスト分析
業務上最も時間を割かれるのが「探すこと」なので、ファイルの検索の効率化に興味があります。現状、法令の解釈本（４冊）、県の指導基準や内規、国の通知、過去の事例などを読み込んで業務にあたっていますが、探し出すのが大変なのと、職員の異動があるとなかなか知識が継承されません。散逸した情報を有機的に結びつける方法はないでしょうか。
集計処理（今具体的に実現したいことは思い浮かばないのですが、どんなことができるのか知りたいです）
集計処理の自動化""".replace(" ", "").replace("　", "").replace("\n", "")
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
                   font_path="setting/NotoSansJP-Bold.otf", prefer_horizontal=1)
    wc.generate(text)
    plt.imshow(wc)
    plt.axis("off")
    # plt.show()
    plt.savefig("wordcloud.png")
