import customtkinter as ctk
import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile as wav

FILENAME_FROM_MIC = "RECORDING.WAV"

class VoiceToTextApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🎙 Voice to Text")
        self.geometry("500x400")
        self.resizable(False, False)

        # Dark / Light mode toggle
        ctk.set_appearance_mode("System")  # "Dark", "Light", or "System"
        ctk.set_default_color_theme("blue")  # themes: "blue", "green", "dark-blue"

        self.recognizer = sr.Recognizer()

        # Title
        self.title_label = ctk.CTkLabel(self, text="Voice to Text", font=("Segoe UI", 24, "bold"))
        self.title_label.pack(pady=15)

        # Record button
        self.record_button = ctk.CTkButton(self, text="🎤 Record Voice", command=self.record_voice, height=40, width=200, font=("Segoe UI", 14, "bold"))
        self.record_button.pack(pady=15)

        # Text area
        self.text_area = ctk.CTkTextbox(self, width=450, height=200, font=("Consolas", 12))
        self.text_area.pack(pady=10, padx=10)

    def record_voice(self):
        self.record_button.configure(text="⏺ Recording...", state="disabled")
        self.update()

        SAMPLE_RATE = 44100
        duration = 5  # seconds
        audio_recording = sd.rec(duration * SAMPLE_RATE, samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()
        wav.write(FILENAME_FROM_MIC, SAMPLE_RATE, audio_recording)

        self.record_button.configure(text="🔍 Recognizing...")
        self.update()

        try:
            text = self.recognize_from_file(FILENAME_FROM_MIC)
            self.text_area.delete("1.0", "end")
            self.text_area.insert("end", text)
        except sr.UnknownValueError:
            self.text_area.delete("1.0", "end")
            self.text_area.insert("end", "[❌ Could not understand audio]")
        except Exception as e:
            self.text_area.delete("1.0", "end")
            self.text_area.insert("end", f"[⚠ Error: {str(e)}]")

        self.record_button.configure(text="🎤 Record Voice", state="normal")

    def recognize_from_file(self, filename):
        with sr.AudioFile(filename) as source:
            audio_data = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio_data)
            return text


if __name__ == "__main__":
    app = VoiceToTextApp()
    app.mainloop()
