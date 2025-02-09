# Jarvis Voice Assistant with Language Selection

This project is a voice assistant application built using Python, which allows users to interact with the assistant in multiple languages. The assistant can recognize voice input in different languages and display the transcribed text.

## Features:
- **Language Selection**: The application supports multiple languages such as English, Bengali, Hindi, Spanish, and French.
- **Speech Recognition**: The assistant listens to your voice and transcribes the input text.
- **Output Display**: The transcribed text is displayed in a text box on the GUI.
- **Exit Command**: You can say "exit" to stop the program.
- **Easy to Use**: Simply select your preferred language and press the "Start Recognition" button to begin.

## Requirements:
- Python 3.x
- `speech_recognition` library: For recognizing the voice input.
- `tkinter` library: For creating the graphical user interface (GUI).
- A working internet connection: The speech recognition service uses Google's API.

### Installation:

1. Clone or download the repository:
   ```bash
   git clone https://github.com/Mong-kya/jarvis-voice-assistant.git
2. Install the required libraries:
  pip install speechrecognition
  pip install tkinter
3. Run the jarvis_voice_assistant.py script:
  python jarvis_voice_assistant.py

How It Works:
      1. Language Selection: Select your preferred language (English, Bengali, Hindi, Spanish, or French) from the dropdown.
      2. Voice Recognition: After selecting a language, click on the "Start Recognition" button. The application will listen to your voice, recognize the speech, and display the transcribed text.
      3. Exit Command: If you want to stop the program, just say "exit" and the application will close.
###Example:
        When the user says "How are you?", the assistant will display the recognized text.
        If you say "exit", the program will stop
