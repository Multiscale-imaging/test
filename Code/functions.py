from PIL import Image
import numpy as np
import configparser


def ReadIni(fn):

    config = configparser.ConfigParser()
    config.read(fn)
    config = dict(config['DEFAULT'])
    config['support_thresh'] = float(config['support_thresh'])
    config['blurr_n'] = float(config['blurr_n'])
    return config


def InitializeSupport(faser):

    # Load intensities
    pat = np.abs(np.fft.fftshift(np.fft.fft2(faser.I)))
    std = np.std(pat)
    support = pat > faser.config['support_thresh'] * std

    return support

def ReadIntens(fn):
    im = Image.open(fn)
    I = np.array(im)
    return I