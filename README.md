# AI_Voice

AI_Voice is a microservice designed to provide text-to-speech and speech recognition functionality for integration into other programs or applications. This microservice is built using Python and Flask, leveraging the Google Text-to-Speech (gTTS) library for text-to-speech conversion and the SpeechRecognition library for speech recognition through Google's Web Speech API.

## Features

- **Text-to-Speech (TTS):** Convert text into spoken words using the gTTS library.
- **Speech Recognition:** Capture audio input from the microphone and recognize speech using Google's Web Speech API.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- gTTS (Google Text-to-Speech)
- SpeechRecognition

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/overlordLoki/AI_Voice
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

   The microservice will be accessible at `http://127.0.0.1:8088/`.

2. Utilize the provided API endpoints:

   - **Text-to-Speech (TTS):**
   
     Send a POST request to `http://127.0.0.1:8088/speak` with JSON data:

     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello, this is a test."}' http://127.0.0.1:8088/speak
     ```

   - **Speech Recognition:**
   
     Send a GET request to `http://127.0.0.1:8088/listen`:

     ```bash
     curl -X GET http://127.0.0.1:8088/listen
     ```

     Note: Speech recognition may not work as expected with a simple `curl` command, as it requires real-time microphone input. Consider integrating a WebSocket solution for more accurate testing.

## Contributing

Contributions are welcome! If you have suggestions, enhancements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
