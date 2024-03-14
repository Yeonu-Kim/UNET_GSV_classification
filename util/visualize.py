import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def showHist(data):
    plt.hist(data)
    plt.show()

def showImg(img):
    plt.imshow(img)
    plt.show()