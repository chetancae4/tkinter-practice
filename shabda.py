from gtts import gTTS
import os
f=open("1.txt")
x=f.read()
language="en"
audio=gTTS(text=x,lang=language,slow=False)
audio.save("1.wav")
os.system("1.wav")
  #after this open power shell and make sure path is same then enter:---
  #python filename.py   ex:--python shabda.py