import speech_recognition as sr
r=sr.Recognizer()
a=sr.AudioFile('1.wav')
with a as source:
    audio=r.record(source)

text=r.recognize_google(audio)
file=open(r"C:\Users\HOME\PycharmProjects\tkint\autorecorded.txt","a")
file.writelines(text)
file.close()
