import librosa
import numpy as np

def load_audio(file):
    audio, sr = librosa.load(file, sr=16000, mono=True)
    audio = audio / max(abs(audio))
    return audio
