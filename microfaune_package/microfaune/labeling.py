import numpy as np
import json
import matplotlib.pyplot as plt
import pylab

from microfaune import audio, plot

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
    with open(json_file_path) as json_data:
        data_dict = json.load(json_data)
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

    with open(json_file_path) as json_data:
        data_dict = json.load(json_data)

    bird_song_duration = 0

    for label in data_dict:
        bird_song_duration += label['end'] - label['start']
    ratio = round(bird_song_duration / total_duration, 2)

    return ratio


def audio_charac_function_audio(json_file_path, wav_file_path):
    fs, data = audio.load_wav(wav_file_path)
    charac_func = np.zeros((len(data), 1))

    with open(json_file_path) as json_data:
        data_dict = json.load(json_data)

    for label in data_dict:
        indx_start = int(label['start'] * fs)
        indx_end = int(label['end'] * fs)
        charac_func[indx_start:indx_end + 1, 0] = 1

    return charac_func


def plot_charac(json_file_path, wav_file_path):
    charac_func = audio_charac_function_audio(json_file_path, wav_file_path)
    fs, data = audio.load_wav(wav_file_path)

    t_plot = np.array(range(len(data)))
    t_plot = t_plot / fs

    plt.plot(t_plot, charac_func)
    plt.show()

    return None


def audio_charac_function_spec(window_length, overlap, charac_func_audio):
    size_spec = 2 + int(duration / (window_length * (1 - overlap)))
    size_audio = len(charac_func_audio)
    regroup_factor = int(size_audio / size_spec)

    charac_func_spec = np.zeros((size_spec, 1))

    for i in range(size_spec):
        label_local = np.mean(charac_func_audio[i * regroup_factor: (i + 1) * regroup_factor])
        if label_local > 0.5:
            charac_func_spec[i] = 1

    return charac_func_spec


pylab.rcParams['figure.figsize'] = (20, 2)