import speech_recognition as sr
from translate import Translator
from gtts import gTTS
import os
import pygame
import tkinter as tk
from tkinter import simpledialog, messagebox

# Initialize Pygame mixer
pygame.mixer.init()

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_dir, "output.mp3")


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio_data = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""


def translate_text(text, dest_lang='en'):
    translator = Translator(to_lang=dest_lang)
    try:
        translation = translator.translate(text)
        return translation
    except Exception as e:
        print("Translation error:", e)
        return ""


def text_to_speech(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(output_file)
        sound = pygame.mixer.Sound(output_file)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)  # Adjust playback speed
        os.remove(output_file)
    except Exception as e:
        print("Text-to-speech error:", e)


def main():
    # Initialize tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    def get_languages():
        source = simpledialog.askstring("Input", "Please enter source language (e.g., en, fr, es):")
        dest = simpledialog.askstring("Input", "Please enter destination language (e.g., en, fr, es):")
        if not source or not dest:
            messagebox.showerror("Error", "Source and destination languages are required!")
            return None, None
        return source, dest

    # Get initial languages
    source_lang, dest_lang = get_languages()
    if not source_lang or not dest_lang:
        return

    # Display a message box with instructions
    messagebox.showinfo("Voice Translator", "Press OK and then speak something to translate.")

    while True:
        input_text = recognize_speech()
        if input_text:
            translated_text = translate_text(input_text, dest_lang)
            if translated_text:
                print("Translated Text:", translated_text)
                text_to_speech(translated_text, dest_lang)
            else:
                print("Failed to translate the text.")
            print("")

        # Ask the user if they want to translate another phrase or change the language
        action = messagebox.askquestion("Next Action",
                                        "Do you want to translate another phrase, change the language, or stop?",
                                        icon='question', type=messagebox.YESNOCANCEL, default=messagebox.YES,
                                        detail='Yes: Translate another\nNo: Change language\nCancel: Stop')

        if action == 'cancel':
            break
        elif action == 'no':
            source_lang, dest_lang = get_languages()
            if not source_lang or not dest_lang:
                return


if __name__ == "__main__":
    main()