import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile as wav

FILENAME_FROM_MIC = "RECORDING.WAV"

class VoiceToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice to Text")
        self.root.geometry("400x300")

        self.recognizer = sr.Recognizer()

        self.record_button = tk.Button(root, text="Record Voice", command=self.record_voice)
        self.record_button.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(pady=10)

    def record_voice(self):
        self.record_button.config(text="Recording...", state=tk.DISABLED)
        self.root.update()

        SAMPLE_RATE = 44100
        duration = 5  # seconds
        # Record audio using sounddevice
        audio_recording = sd.rec(duration * SAMPLE_RATE, samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()
        # Save the recording to a WAV file
        wav.write(FILENAME_FROM_MIC, SAMPLE_RATE, audio_recording)

        self.record_button.config(text="Recognizing...")
        self.root.update()

        # Recognize speech using your function
        try:
            text = self.recognize_from_file(FILENAME_FROM_MIC)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, text)
        except sr.UnknownValueError:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, "[Could not understand audio]")
        except Exception as e:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, f"[Error: {str(e)}]")

        self.record_button.config(text="Record Voice", state=tk.NORMAL)

    def recognize_from_file(self, filename):
        with sr.AudioFile(filename) as source:
            audio_data = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio_data)
            return text


if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceToTextApp(root)
    root.mainloop()
