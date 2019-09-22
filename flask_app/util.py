import os
from io import BytesIO
import cv2
import numpy as np

def arrToPng(arr):
    image = (np.reshape(arr,(64,64,3)).clip(0,1))*255
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    ret, png = cv2.imencode('.png', image)
    return png.tobytes()

def getAverageFace(pcaobj):
    return arrToPng(pcaobj.mean_)

def getImageFromPCA(pcaobj,pca_array):
    img_arr = pcaobj.inverse_transform(pca_array)
    return arrToPng(img_arr)

def getPCADimCount(pcaobj):
    pcaobj.mean_.size