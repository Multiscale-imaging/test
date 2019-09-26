import matplotlib.pyplot as plt
import Code.faser as faser
import numpy as np

# Initialize
HIO = faser.Faser('example.ini')
beta = 1
ER = faser.Faser('example.ini')

plt.subplot(1,2,1)
img_HIO = plt.imshow(np.abs(HIO.g))
plt.title('HIO, n = %d' % (HIO.n))

plt.subplot(1,2,2)
img_ER = plt.imshow(np.abs(ER.g))
plt.title('ER, n = %d' % (ER.n))

plt.pause(1)
plt.draw()


for ii in range(10):
    for jj in range(10):
        HIO.HIO_one_iteration(beta)
        ER.ER_one_iteration()


    plt.subplot(1,2,1)
    img_HIO.set_data(np.abs(HIO.g)*HIO.support)
    plt.title('HIO, n = %d' % (HIO.n))
    plt.subplot(1,2,2)
    img_ER.set_data(np.abs(ER.g)*ER.support)
    plt.title('ER, n = %d' % (ER.n))
    plt.pause(1)
    plt.draw()
    ER.UpdateSupport()
    HIO.UpdateSupport()

    
plt.show()
