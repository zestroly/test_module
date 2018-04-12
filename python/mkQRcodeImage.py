#!/usr/bin/python
import qrcode
import numpy
from PIL import Image
import cv2

import matplotlib.pyplot as plt

import qrcode


def matplotlibShow(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def matplotlibShowMultiple(img):
    l_1 = img[:,:,0]
    plt.imshow(l_1)
    #plt.axis('off')
    plt.imshow('lena_1', cmap='Greys_r')
    plt.show()

    img = plt.imshow('lena_1')
    img.set_cmap('gray')

    plt.show()

def opencvShow(img):
    cv_img = cv2.cvtColor(numpy.asarray(img),cv2.COLOR_RGB2BGR)
    cv2.imshow("OpenCV", cv_img)
    cv2.waitKey(1000)





import qrcode
import random
import string
import sys

from scipy import misc



def mkQRcodeImage(strdata):
    qr = qrcode.QRCode(
            version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                        border=4,
                        )
    qr.add_data(strdata)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    rgb_img=img.convert('RGB')
    return rgb_img

def mkRandomStr():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return salt
    #STR = [chr(i) for i in range(48,123)]




while(1):
    strdata=mkRandomStr()
    img=mkQRcodeImage(strdata)
    img=misc.imresize(img, 0.5)

    opencvShow(img)

cv2.destrolyAllWindows()
#matplotlibShow(img)















