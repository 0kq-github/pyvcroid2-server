import pyvcroid2
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
import uvicorn
import sys

app = FastAPI()

@app.get("/generate", response_class=FileResponse)
def generate(
  text:str, 
  speaker:str, 
  mode:str = "standard",
  speed:float = 1,
  pitch:float = 1, 
  volume:float = 1,
  emphasis:float = 1,
  pauseMiddle:int = 100,
  pauseLong:int = 100,
  pauseSentence:int = 100,
  masterVolume:float = 1
  ):
  with pyvcroid2.VcRoid2() as vc:
    #話者の読み込み
    vc.loadVoice(speaker)
    vc.loadLanguage(mode)

    #各種パラメーターの適用
    vc.param.speed = speed
    vc.param.pitch = pitch
    vc.param.volume = volume
    vc.param.emphasis = emphasis
    vc.param.pauseMiddle = pauseMiddle
    vc.param.pauseLong = pauseLong
    vc.param.pauseSentence = pauseSentence
    vc.param.masterVolume = masterVolume

    #読み上げ不可な文字の除外
    for i in text:
      try:
        i.encode("shift-jis")
      except:
        text = text.replace(i,"")

    text = text.replace("\ufe0f","")
    speech, _ = vc.textToSpeech(text)
    return Response(content=speech,media_type="audio/wav")

@app.get("/speakers",)
def speakers():
  with pyvcroid2.VcRoid2() as vc:
    return {"speakers":vc.listVoices(),"modes":vc.listLanguages()}

if __name__ == "__main__":
  uvicorn.run(app=app,host="0.0.0.0",port=int(sys.argv[1]))