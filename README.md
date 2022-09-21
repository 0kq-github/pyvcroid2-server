# pyvcroid2-server

[pyvcroid2](https://github.com/Nkyoku/pyvcroid2) + FastAPIのVOICEROID2用APIサーバー  
特に理由がなければ[voiceroid_daemon](https://github.com/Nkyoku/voiceroid_daemon)を使った方がいいです(多分)  
/generateにリクエストを飛ばすと音声をwave形式で返します  

## クイックスタート
VOICEROID2のbit数に合わせたpythonのインストール  
```pip install -r requirements.txt```  を実行して必要なパッケージをインストール  
VOICEROID2がインストールされたマシンでserver.pyを起動  
ブラウザで`http://マシンのアドレス/docs`にアクセス

## API エンドポイント

### `GET /generate`

音声の生成

|パラメーター|説明|型|
|:-:|:-:|:-:|
|text|読み上げ文字列|str|
|speaker|話者|str|
|mode|モード|str|
|speed|読み上げ速度|float|
|pitch|ピッチ|float|
|volume|音量|float|
|emphasis|抑揚|float|
|pauseMiddle|短ポーズ時間|int|
|pauseLong|長ポーズ時間|int|
|pauseSentence|文末ポーズ時間|int|
|masterVolume|マスター音量|float|

### Response
|code|content-type|
|:-:|:-:|
|200|audio/wav|
|500|text/plain|


### `GET /speakers`

話者とモードの一覧を表示

### Response
|code|content-type|
|:-:|:-:|
|200|application/json|
|500|text/plain|

## 既知の不具合
音声生成中に生成リクエストが飛んでくると生成に失敗する

## License
MIT License
