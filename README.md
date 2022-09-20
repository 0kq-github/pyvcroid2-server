# pyvcroid2-server

pyvcroid2 + FastAPIのVOICEROID2用APIサーバー  
/generateにリクエストを飛ばすと音声をwave形式で返します  

## Usage
VOICEROID2のbit数に合わせたpythonのインストール  
```pip install -r requirements.txt```  を実行して必要なパッケージをインストール  
VOICEROID2がインストールされたマシンでserver.pyを起動  
ブラウザで`http://マシンのアドレス/docs`にアクセス

## API エンドポイント

### `GET /generate`
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

#### Response
|code|content-type|
|:-:|:-:|
|200|audio/wav|
|500|text/plain|


### `GET /speakers`

#### Response
|code|content-type|
|:-:|:-:|
|200|application/json|
|500|text/plain|

