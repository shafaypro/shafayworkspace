import functools
import numpy as np  # this is the numpy array
from PIL import Image  # the header library which will be used to open the image!
import matplotlib.pyplot as plt
import statistics
import time
import math
from collections import Counter


def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x+=1
        except Exception as e:
            print(str(e))

    print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    highest = 0
    itemslist = list()
    for item in x:
         itemslist.append(x[item])
         print (x[item])


    graphX = []
    graphY = []

    ylimi = 0

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        ylimi = x[eachThing]



    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)

    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align='center')
    plt.ylim(400)

    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()


def createExamples():
     numberArrayExamples = open('numArEx.txt', 'a')
     numbersWeHave = range(0, 10)
     versionwehave = range(1, 10)
     for eachNum in numbersWeHave:
          # print eachNum
          for furtherNum in versionwehave:
               # you could also literally add it *.1 and have it create
               # an actual float, but, since in the end we are going
               # to use it as a string, this way will work.
               print(str(eachNum) + '.' + str(furtherNum))
               imgFilePath = 'numbers/' + str(eachNum) + '.' + str(furtherNum) + '.png'
               ei = Image.open(imgFilePath)
               eiar = np.array(ei)
               eiarl = str(eiar.tolist())

               print(eiarl)
               lineToWrite = str(eachNum) + '::' + eiarl + '\n'
               numberArrayExamples.write(lineToWrite)


# function to convert the image to black and white:-->
def threshold(imageArray):
     balanceAr = []
     newAr = imageArray
     from statistics import mean  # this is the satictics file to import the mean function
     for eachRow in imageArray:  # calculate the each row
          for eachPix in eachRow:  # calculate the each pixel in the row
               avgNum = mean(eachPix[:3])  # store their average value in the balance
               balanceAr.append(avgNum)

     balance = mean(balanceAr)  # most consistant mean is stored in the balance
     for eachRow in newAr:
          for eachPix in eachRow:
               if mean(eachPix[:3]) > balance:
                    eachPix[0] = 255
                    eachPix[1] = 255
                    eachPix[2] = 255
                    eachPix[3] = 255
               else:
                    eachPix[0] = 0
                    eachPix[1] = 0
                    eachPix[2] = 0
                    eachPix[3] = 255
     return newAr


'''
i = Image.open('numbers.txt/0.1.png')
iar = np.array(i) # passing the image and then converting them in to an array
i2 = Image.open('numbers.txt/y0.4.png')
iar2 = np.array(i2)
i3 = Image.open('numbers.txt/y0.5.png')
iar3 = np.array(i3)
i4 = Image.open('sentdex.png')
iar4 = np.array(i4)
iar = threshold(iar)
iar2 = threshold(iar2)
iar3 = threshold(iar3)
iar4 = threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)
'''
createExamples()
whatNumIsThis('test.png')
# plt.show()
