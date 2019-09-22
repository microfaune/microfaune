"""Module containing models for bird song detection"""


class RNNDetector:
    """Class wrapping a rnn model

    """
    def __init__(self, weights_file=""):
        """Initialization function"""
        self.weights_file = weights_file
        self.weights_loaded = False

    def create_model(self):


    def free_mem(self):
        """Release GPU memory."""
        self._model = None
