import speech_recognition as sr
from app.utils.file_utils import write_file_safe
import os
from app.config import DATA_DIR

def run() -> str:
    """
    B8: Transcribe audio from /data/audio.mp3 and write the transcript to /data/audio-transcript.txt.
    """
    audio_path = os.path.join(DATA_DIR, "audio.mp3")
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    try:
        transcript = recognizer.recognize_google(audio_data)
    except Exception as e:
        raise Exception("Audio transcription failed: " + str(e))
    write_file_safe("audio-transcript.txt", transcript)
    return "Audio transcribed successfully."
