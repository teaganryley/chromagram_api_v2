import librosa
import librosa.display


def analyze(audio_path):
    # sampling at 44.1 KHz
    y, sr = librosa.load(audio_path, sr=44100)

    # Harmonic-percussive source separation
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    # generate chromagram
    c = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)
    return c.tolist()

