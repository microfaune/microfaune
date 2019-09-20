import matplotlib.pyplot as plt


def plot_spec(S):
    """Plot a spectrogram.

        Parameters
        ----------
        S : array-like
            Spectrogram.
    """
    plt.figure(figsize=(10, 2))
    plt.imshow(S, cmap=plt.get_cmap('inferno'), aspect='auto', origin='lower')
    plt.axis('off')


def plot_audio(fs, data):
    """
        Plot audio data.

        Parameters
        ----------
        data : array-like
            Audio data.
        fs : int
            Sampling frequency in Hz.

        Returns:
        -------
        None
    """
    plt.figure()
    sampled_points = len(data)
    time = [ti * 1. / fs for ti in range(sampled_points)]
    plt.plot(time, data)
    plt.xlabel('t [s]')
    plt.ylabel('P [W]')
    plt.show()
    plt.close()

    return None