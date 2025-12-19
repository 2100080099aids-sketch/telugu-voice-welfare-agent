from faster_whisper import WhisperModel
from gtts import gTTS
import uuid

model = WhisperModel("small")

def stt_whisper(audio_path):
    segments, _ = model.transcribe(audio_path, language="te")
    text = " ".join([segment.text for segment in segments])
    return text.strip()

def tts_telugu(text):
    tts = gTTS(text=text, lang="te")
    filename = f"output_{uuid.uuid4()}.mp3"
    tts.save(filename)
    return filename
