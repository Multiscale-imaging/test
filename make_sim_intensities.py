from PIL import Image
import numpy as np
import configparser
import matplotlib.pyplot as plt


fn = './Data/Realspace.tiff'
out_fn = './Data/Bogoe.tiff'


im = Image.open(fn)
arr = np.array(im)
ff = np.fft.fftshift(np.fft.fft2(arr))

plt.subplot(1,2,1)
plt.imshow(np.log(np.abs(ff)))
plt.subplot(1,2,2)
plt.imshow(np.abs(arr))
plt.show()


I = np.abs(ff)**2
I = I /np.max(I)
im_out = Image.fromarray(I)

im.show()

whatwhat = np.array(im_out)
plt.imshow(whatwhat)
plt.show()



im_out.save(out_fn)