import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import pandas as pd
# データの読み込み
with open('sample_file/nikkei_stock.csv', 'r') as f:
    data = [s.strip().replace("\"", "").split(',') for s in f.readlines()]

# pandasのDataFrameに変換

df = pd.DataFrame(data[1:], columns=data[0])
df[['High', 'Low', 'Open', 'Close']] = df[[
    'High', 'Low', 'Open', 'Close']].astype(float)

# matplotlibでプロット

fig = plt.figure(figsize=(11, 8))
plt.title("Nikkei 225")
gs = gridspec.GridSpec(ncols=1, nrows=3)
for i in range(1, 4):
    ax = fig.add_subplot(gs[i-1, 0])
    ax.plot(df['Date'], df[df.columns[i]], label=df.columns[i])
    # plt.grid()
    plt.legend(bbox_to_anchor=(1, 1), loc='upper right',
               borderaxespad=0, fontsize=9)
plt.tight_layout()
plt.show()
