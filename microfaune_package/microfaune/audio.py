import librosa
import numpy as np
from scipy.io import wavfile
import signal


def load_wav(path, decimate=None):
    """Load audio data.

        Parameters
        ----------
        path: str
            Wav file path.
        decimate: int
            If not None, downsampling by a factor of `decimate` value.

        Returns
        -------
        S: array-like
            Array of shape (Mel bands, time) containing the spectrogram.
    """
    fs, data = wavfile.read(path)

    data = data.astype(np.float32)

    if decimate is not None:
        data = signal.decimate(data, decimate)
        fs /= decimate

    return fs, data


def cut_audio(old_path, new_path, start, end):
    """
        Cut audio data to specific starting and end point and save it as a new wav file

        Parameters
        ----------
        old_path : str
            Original wav file path.
        new_path : str
            New wav file path.
        start : float
            Desired start time of new audio in seconds.
        end : float
            Desired end time of new audio in seconds.

    """
    fs, data = wavfile.read(old_path)
    indx_start = int(start*fs)
    indx_end = int(end*fs)+1
    wavfile.write(new_path,fs,data[indx_start:indx_end])


def create_spec(data, fs, n_mels=32, n_fft=2048, hop_len=1024):
    """Compute the Mel spectrogram from audio data.

        Parameters
        ----------
        data: array-like
            Audio data.
        fs: int
            Sampling frequency in Hz.
        n_mels: int
            Number of Mel bands to generate.
        n_fft: int
            Length of the FFT window.
        hop_len: int
            Number of samples between successive frames.

        Returns
        -------
        S: array-like
            Array of shape (Mel bands, time) containing the spectrogram.
    """
    # Calculate spectrogram
    S = librosa.feature.melspectrogram(
      data, sr=fs, n_fft=n_fft, hop_length=hop_len, n_mels=n_mels)
    S = S.astype(np.float32)

    # Convert power to dB
    S = librosa.power_to_db(S)

    return S


def wav2spc(wav_file, fs=44100, n_mels=40, n_fft=2048, hop_len=1024,
            duration=10):
    """Load a wav file and compute its MEL spectogram.

       Parameters
       ----------
       wave_file: str
           path to a wav file.
       fs: int
           Sampling frequency in Hz.
       n_mels: int
           Number of Mel bands to generate.
       n_fft: int
           Length of the FFT window.
       hop_len: int
           Number of samples between successive frames.
       duration: int
           Duration of the sound to consider (starting at the beginning)

       Returns
       --------
       spec: array-like
           Array of shape (Mel bands, time) containing the spectrogram.
    """

    x_fs, x = load_wav(wav_file)

    if x_fs != fs:
        raise ValueError(f"wav file with wrong frequency {x_fs}: {wav_file}")
    spec = create_spec(x[:fs*duration], fs, n_mels, n_fft, hop_len)
    return spec
