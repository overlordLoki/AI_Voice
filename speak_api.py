from gtts import gTTS
import os
import pygame
import speech_recognition as sr
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS if accessed from a frontend

# Initialize pygame for audio playback
pygame.init()
pygame.mixer.init()

def speak(text: str):
    """
    Converts text to speech and plays it.
    Uses gTTS for TTS and pygame for playback.
    """
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    try:
        tts.save(filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait for playback to finish
            continue
    except Exception as e:
        print(f"Error during playback: {e}")
    # finally:
    #     if os.path.exists(filename):
    #         os.remove(filename)

def get_audio():
    """
    Captures audio from the microphone and converts it to text using Google Speech Recognition.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            said = recognizer.recognize_google(audio)
            return said
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/speak', methods=['POST'])
def speak_api():
    """
    Flask API endpoint to convert text to speech and play it.
    Expects JSON input with a 'text' field.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON input"}), 400

    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "'text' field is required"}), 400

    speak(data['text'])
    return jsonify({"message": "Speech played successfully"}), 200

@app.route('/listen', methods=['GET'])
def listen_api():
    """
    Flask API endpoint to capture audio and return the recognized text.
    """
    audio_text = get_audio()
    return jsonify({"recognized_text": audio_text}), 200

if __name__ == "__main__":
    app.run(port=8088, debug=True)
