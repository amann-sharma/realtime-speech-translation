
# Voice Translator

A Python application that translates spoken words into a different language and converts the translated text into speech. The application utilizes speech recognition, translation, and text-to-speech synthesis libraries to perform real-time translation.

## Features

- Speech recognition to convert spoken words into text.
- Translation of recognized text to a specified language.
- Text-to-speech conversion to vocalize the translated text.
- User-friendly graphical interface using Tkinter for language input and interaction.

## Requirements

- Python 3.x
- `speech_recognition` library
- `translate` library
- `gtts` library
- `pygame` library
- `tkinter` library (usually included with Python)

## Installation

1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages using pip:

   ```bash
   pip install SpeechRecognition translate gtts pygame
   ```

## Usage

1. Run the `main.py` script:

   ```bash
   python main.py
   ```

2. A Tkinter window will prompt you to enter the source and destination languages (e.g., `en`, `fr`, `es`).

3. Follow the on-screen instructions:
   - Press OK and speak a phrase you want to translate.
   - The application will recognize your speech, translate it, and play the translated text as speech.

4. You can choose to translate another phrase, change the languages, or stop the application based on the prompts.

## Code Overview

- **recognize_speech()**: Captures audio input and converts it to text using Google Speech Recognition.
- **translate_text(text, dest_lang)**: Translates the recognized text into the specified destination language.
- **text_to_speech(text, lang)**: Converts the translated text into speech and plays it.
- **main()**: Initializes the Tkinter GUI, manages language input, and controls the translation loop.

## Troubleshooting

- **Error in Speech Recognition**: Ensure your microphone is working and is properly set up. Check your internet connection as the speech recognition service requires it.
- **Translation Error**: Ensure the `translate` library is properly installed and configured. If errors persist, check the translation API documentation for possible issues.
- **Text-to-Speech Issues**: Ensure that the `gtts` and `pygame` libraries are installed correctly and that your system supports audio playback.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements for this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
