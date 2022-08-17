![image](https://user-images.githubusercontent.com/88820769/184725862-542f6035-ee73-4ffd-b51a-5a5c6cf7adde.png)

# 操作説明

- python manageTask.py setup [ユーザー token] :
- python manageTask.py : タスク一覧を表示
- python manageTask.py [タスク ID] : タスクを表示
- python manageTask.py [タスク ID] delete : タスクを削除
- python manageTask.py [タスク ID] (引数) : タスクを追加 or 編集※組み合わせ、順不同可

# 引数一覧

- ?[状態] :　状態を設定
- +[ {}h{}m or {}h or {}m] : 時間を加算
- -[ {}h{}m or {}h or {}m] : 時間を減算
- =[タイトル]　: タイトルを設定
- :[開始日] : 開始日を設定
- ~[終了日] : 終了日を設定
- start : 開始日を今日に状態を progress に設定

# コマンド例

- python manageTask.py A-10 +1h ?proggress =スタイリング ~8/23

1. `A-10`があれば選択なければ作成
2. 時間を`１時間`加算
3. 状態を`progress`に設定
4. タイトルを`スタイリング`に設定
5. 期限を`8/23`に設定

# 実装予定(メモ)

- tool : this
- db : azure or firebase
- web-backend(api) : django or typescript
- web-frontend : react,typescript

- ツールから web アプリを操作できる機能

1. web アプリにログインして token を取得
2. token を環境変数に設定
3. token を用いて api から情報を取得,編集 ※通信を暗号化して token の漏洩を防ぐ
