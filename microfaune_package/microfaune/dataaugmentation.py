#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:18:32 2019

@author: christian
"""
import numpy as np
from microfaune import plot
from keras.preprocessing.image import ImageDataGenerator

class data_augmentation:
    """Class to generate image data for rnn modeling
    """
    datagenerator_list = None

    def __init__(self, width_shift_range=[-40,40], horizontal_flip=True, brightness_range=[0.4,0.9]):
        """Initialization data generators

        Parameters
        ----------
        width_shift_range: list
            width of the random horizontal shift
        horizontal_flip: bool
            moving all pixels of the image horizontally,
            while keeping the image dimensions the same.
        brightness_range: list
        The brightness can be augmented by randomly darkening images,
        where has no effect on darkness

        Initiate
        -------
        datagenerator_list: list
            image data generators
        """

        datagen_width_shift = ImageDataGenerator(width_shift_range=width_shift_range)
        datagen_horizontal_flip = ImageDataGenerator(horizontal_flip=horizontal_flip)
        datagen_brightness = ImageDataGenerator(brightness_range=brightness_range)
        self.datagenerator_list = [datagen_width_shift, datagen_horizontal_flip, datagen_brightness]

    def generate_augmentation(self, S, y, my_range=5, to_display=False):
        """ data augmentation of one Spectrogram 
        Parameters
        ----------
        S spectogram
        y classification value
        
        RETURNS
        -------
        list_S
            list of Spectograms with Y list (duplicate from y input)
            the first Spectograms is the given input S
        list_y
            All y have the value of the given y
        """
        list_S = [S]
        list_y = [y]
        for datagen in self.datagenerator_list:
            data = np.expand_dims(S, axis=2)

            # expand dimension to one sample
            samples = np.expand_dims(data, 0)
            # prepare iterator
            it = datagen.flow(samples, batch_size=1)
            # generate samples and plot
            for i in range(my_range):
                batch = it.next()
                # convert to unsigned integers for viewing
                image = batch[0].astype('uint8')
                image = image[:,:,0]
                list_S.append(image)
                list_y.append(y)
                if to_display==True:
                    plot.plot_spec(image)
        return list_S, list_y
    
    def generate_augmentation_list(self, list_S, list_y, my_range=5, to_display=False):
        """ data augmentation of a  list of Spectrograms 
        Parameters
        ----------
        list_S  vector of spectograms
        list_y  vector of y
        
        RETURNS
        -------
        list_S_augmented
            list of Spectograms augmented 
        list_y_augmented
            list of y augmented with duplicate values
        """
        list_S_augmented = []
        list_y_augmented = []
        for S, y in zip(list_S, list_y):
            lstx, lsty = self.generate_augmentation(S, y, my_range, to_display)
            list_S_augmented += lstx
            list_y_augmented += lsty
        return list_S_augmented, list_y_augmented
    
            

