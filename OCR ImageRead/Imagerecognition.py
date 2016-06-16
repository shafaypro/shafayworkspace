import functools

import numpy as np  # this is the numpy array
from PIL import Image  # the header library which will be used to open the image!
import matplotlib.pyplot as plt
import statistics
import time
import math
# function to convert the image to black and white:-->
def threshold(imageArray):
     print ('Threshold function is in progress')
     balanceAr = []
     newAr = imageArray
     newAr.flags.writeable = True
     for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)
     balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
     for eachrow in newAr:
          for eachpixel in eachrow:
               if reduce(lambda x, y: x + y, eachpixel[:3]) / len(eachpixel[:3]) > balance:
                    eachpixel[0] = 255
                    eachpixel[1] = 255
                    eachpixel[2] = 255
                    eachpixel[3] = 255
               else:
                    eachpixel[0] = 0
                    eachpixel[1] = 0
                    eachpixel[2] = 0
                    eachpixel[3] = 255
          return newAr
i = Image.open('numbers/0.1.png')
iar = np.array(i)
i2 = Image.open('numbers/y0.4.png')
iar2 = np.array(i2)
i3 = Image.open('numbers/y0.5.png')
iar3 = np.array(i3)
i4 = Image.open('sentdex.png')
iar4 = np.array(i4)


fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)


plt.show()