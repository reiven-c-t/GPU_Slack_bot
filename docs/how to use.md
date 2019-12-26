# 使用方法

requirements.txt install

Slack APIにてアプリ作成[https://api.slack.com/apps?new_app=1]。
チャンネルに連携させ、OAuth&Permissionあたりでwrite関連を適宜on.
.envにSlackのAuthや連携させたいチャンネルIDを記入。
チャンネルIDはWeb版slackでチャンネルを開いた時に表示されるURLの最後の/xxxxx/部分。

gpu_state.sqlite3がどこにも存在しない場合はDataManager.pyを一回走らせる。

src/config/datapath.pyの中に.envへの絶対パス指定があるので、修正する必要あり。

src/をPYTHONPATHに絶対パス指定

python app.py実行


## 注意

GPUが8個ちょうどでないとDBの整合が壊れる。


