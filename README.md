# Voice to Text

A simple Python application that records audio from the microphone, converts speech to text using Google's Speech Recognition API, and displays the result in a desktop GUI built with Tkinter.

***

## Features

- Record audio from microphone (default 5 seconds)
- Save recorded audio as WAV file
- Convert recorded speech to text using Google Speech Recognition
- Display transcribed text in a scrollable GUI text box
- Basic error handling for recognition failures

***

## Requirements

- Python 3.6 or above
- Packages:
  - `speechrecognition`
  - `sounddevice`
  - `scipy`
  - `tkinter` (usually included with Python)
  
- **System dependencies** (Linux):
  - PortAudio library (install via `sudo apt install portaudio19-dev`)

***

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd Voice_to_Text
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # Linux/macOS
   .\env\Scripts\activate   # Windows
   ```

3. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install PortAudio system dependency (Linux):

   ```bash
   sudo apt update
   sudo apt install portaudio19-dev
   ```

***

## Usage

Run the application:

```bash
python VoiceText.py
```

The window will open with a button **Record Voice**. Click it to record 5 seconds of audio from your microphone. The recognized text will be displayed in the text box below.

***

## File Structure

- `VoiceText.py` — Main application script with Tkinter GUI and speech recognition
- `RECORDING.WAV` — Temporary audio file saved during recording
- `requirements.txt` — Python package requirements

***

## Troubleshooting

- If you get an error like `OSError: PortAudio library not found`, install the system PortAudio development package (see Installation).
- If recognition returns `[Could not understand audio]`, ensure you speak clearly and your microphone captures sound correctly.

***

## License

This project is licensed under the [MIT License](LICENSE).

