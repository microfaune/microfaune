import numpy as np
import json
import matplotlib.pyplot as plt
import pylab
from scipy import interpolate
from scipy.io import wavfile

from microfaune import audio, plot

def read_json_file(json_file_path):
    """ Count labels in json file.

                Parameters
                ----------
                json_file_path : str
                    Path of json file.

                Returns:
                -------
                data_dict : list
                    List of labels, each label is a dictionnary item with entries 'id', 'start', 'end', 'annotation'
    """
    with open(json_file_path) as json_data:
        data_dict = json.load(json_data)
    return data_dict

def number_labels(json_file_path):
    """ Count labels in json file.

            Parameters
            ----------
            json_file_path : str
                Path of json file.

            Returns:
            -------
            nb_labels : int
                Number of labels in json file
        """
    data_dict = read_json_file(json_file_path)
    nb_labels = len(data_dict)
    return nb_labels


def prop_labeled(json_file_path, audio_file_path):
    """ Compute proportion of the ratio of labels duration compared to total duration of audio

        Parameters
        ----------
        json_file_path : str
            Path of json file.
        audio_file_path : str
            Path of audio file.

        Returns:
        -------
        ratio : float
            Ratio of duration of labeled segments and total duration of audio.
    """

    fs, data = audio.load_audio(audio_file_path)
    total_duration = len(data) / fs

    data_dict = read_json_file(json_file_path)

    bird_song_duration = 0

    for label in data_dict:
        bird_song_duration += label['end'] - label['start']
    ratio = round(bird_song_duration / total_duration, 2)

    return ratio


def charac_function_audio(json_file_path, audio_file_path):
    """ Derive the characteristic function from the labels in json file
            Parameters
            ----------
            json_file_path : str
                Path of json file.
            audio_file_path : str
                Path of audio file.

            Returns:
            -------
            charac_func : numpy array (nb bites in audio,1)
                Characteristic function derived on audio time scale, equal to 1 on labeled segments, 0 elsewhere
    """
    fs, data = audio.load_audio(audio_file_path)
    charac_func = np.zeros((len(data), 1))

    data_dict = read_json_file(json_file_path)

    for label in data_dict:
        indx_start = int(label['start'] * fs)
        indx_end = int(label['end'] * fs)
        charac_func[indx_start:indx_end + 1, 0] = 1

    return charac_func


def plot_charac_audio(json_file_path, audio_file_path):
    """ Plot the characteritic function from the labels in json file
                Parameters
                ----------
                json_file_path : str
                    Path of json file.
                audio_file_path : str
                    Path of audio file.

    """
    charac_func = labeling.audio_charac_function_audio(json_file_path, audio_file_path)

    fs, data = audio.load_audio(audio_file_path)
    t_plot = np.array(range(len(data)))
    t_plot = t_plot / fs

    pylab.rcParams['figure.figsize'] = (20, 2)
    plt.close()

    plt.plot(t_plot, charac_func)
    plt.xlabel('time [s]')
    plt.xlabel('label')
    plt.show()

    return None


def charac_function_spec(audio_file_path, window_length, overlap, charac_func_audio):
    """ Derive the characteristic function from the labels in json file
            Parameters
            ----------
            audio_file_path : str
                Path of audio file.
            window_length : float
                Length of the FFT window in seconds.
            overlap : float
                Overlap of the FFT windows.
            charac_func_audio : numpy array (nb bites in audio,1)
                Characteristic function derived in audio time scale, equal to 1 on labeled segments, 0 elsewhere

            Returns:
            -------
            charac_func_spec : numpy array (nb bites in audio,1)
                Characteristic function derived in spectrogram time scale, equal to 1 on labeled segments, 0 elsewhere
        """

    fs, data = audio.load_audio(audio_file_path)
    duration = len(data) / fs
    size_spec = 2 + int(duration / (window_length * (1 - overlap)))
    size_audio = len(charac_func_audio)
    regroup_factor = int(size_audio / size_spec)

    charac_func_spec = np.zeros((size_spec, 1))

    for i in range(size_spec):
        label_local = np.mean(charac_func_audio[i * regroup_factor: (i + 1) * regroup_factor])
        if label_local > 0.5:
            charac_func_spec[i] = 1

    return charac_func_spec


def charac_function_fs(fs, window_length, overlap, charac_func_spec):
    """ Convert the scale of a characteristic function from spec time scale to another time scale with the desired sampling rate
        Parameters
        ----------
            fs: int
                Sampling frequency in Hz.
            window_length : float
                Length of the FFT window in seconds.
            overlap : float
                Overlap of the FFT windows.
            charac_func_spec: numpy array (nb bites in spec,1)
                Characteristic function derived in spectrogram time scale, equal to 1 on labeled segments, 0 elsewhere

        Returns:
        -------
            charac_func_fs : numpy array (fs*duration,1)
                Characteristic function derived with the desired sampling rate
        """

    dt_spec = window_length * (1 - overlap)
    fs_spec = 1./dt_spec
    duration = len(charac_func_spec) * dt_spec

    t_spec = np.linspace(0, duration, num=len(charac_func_spec))
    t_fs = np.linspace(0, duration, num=duration*fs)
    f = interpolate.interp1d(t_spec, charac_func_spec[:,0])
    charac_func_fs = np.zeros((int(duration*fs),1))
    charac_func_fs[:,0] = f(t_fs)

    return charac_func_fs


def create_wav_with_label(fs, charac_func_fs, file_path):
    """ Create a false wav file with characteristic function.
        Used in Audacity to plot spectrogram and label at the same time
            Parameters
            ----------
                fs: int
                    Sampling frequency in Hz.
                charac_func_fs : numpy array (fs*duration,1)
                    Characteristic function derived with the desired sampling rate
                file_path : str
                    Path of the wav file path saved
    """
    wavfile.write(file_path, fs, charac_func_fs[:, 0])

    return None

