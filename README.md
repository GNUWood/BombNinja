# BombNinja



![banner.png](./image/banner.png)

BombNinjaは、質問箱サービス「Ninjar」専用のスパムツールです。



## 必要なモノ

- Python 3.8以上

- PIP

- - cloudscraper
  
  - requests
  
  - re
  
  - fake_useragent
  
  - random
  
  - sys
  
  - threading
  
  - os
  
  - ctypes ←NT系(Windows)のみ

- (VPN又はProxy)



## 使い方

1. [Ninjar]([https://www.ninjar.jp/)より、ユーザー名("https://www.ninjar.jp/users"の後の部分)をコピーする。

2. 同梱されている ninjar.txt に、送りたい文章を入力する。（改行することでランダムに送ることが出来る。）

3. プログラムを起動し、表示されている手順に沿っていく。



## 注意点

誹謗中傷やその他犯罪に関わるメッセージを送信しても、開発者側は一切の責任を負いかねます。

また、サービスに負荷をかけるような使い方を想定したツールでは無いため、サーバーに負荷をかけるような利用はしないでください。

