import matplotlib.pyplot as plt
import Code.faser as faser
import numpy as np

# Initialize
HIO = faser.Faser('example.ini')
beta = 1
ER = faser.Faser('example.ini')


# Plot
ax_HIO = plt.subplot(1,2,1)
img_HIO = plt.imshow(np.abs(HIO.g))
plt.title('HIO, n = %d' % (HIO.n))
ax_ER = plt.subplot(1,2,2)
img_ER = plt.imshow(np.abs(ER.g))
plt.title('ER, n = %d' % (ER.n))
plt.pause(1)
plt.draw()

# Run phasing
for ii in range(10):
    
    for jj in range(10):
        # Do one step
        HIO.HIO_one_iteration(beta)
        ER.ER_one_iteration()


    plt.sca(ax_HIO)
    img_HIO.set_data(np.abs(HIO.g)*HIO.support)
    plt.title('HIO, n = %d' % (HIO.n))
    plt.sca(ax_ER)
    img_ER.set_data(np.abs(ER.g)*ER.support)
    plt.title('ER, n = %d' % (ER.n))
    plt.pause(1)
    plt.draw()
    # Update support
    ER.UpdateSupport()
    HIO.UpdateSupport()

    
plt.show()
