import matplotlib.pyplot as plt


def plot_spec(S):
    """Plot a spectrogram.

        Parameters
        ----------
        S : array-like
            Spectrogram.
    """
    fig = plt.figure(figsize=(10, 2))
    plt.imshow(S, cmap=plt.get_cmap('inferno'), aspect='auto', origin='lower')
    plt.axis('off')