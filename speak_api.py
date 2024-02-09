from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import flask

def speak(text : str):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print(f"Error in recognition: {e}")
    return said

app = flask.Flask(__name__)

@app.route('/speak', methods=['POST'])
def speak_api():
    data = flask.request.json
    speak(data['text'])
    return "OK"

@app.route('/listen', methods=['GET'])
def listen_api():
    return get_audio()


if __name__ == "__main__":
    app.run(port=8088)
