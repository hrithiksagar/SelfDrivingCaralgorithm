#lesson 1 of self driving car
#shoing image in matrix form ,to chcek bright and dark pixels
import numpy as np
import cv2
img=cv2.imread('lane.jpg')
print(img)
imgcopied=np.copy(img)
print(imgcopied)
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgshow=cv2.imshow('image',img)
imgshow1=cv2.imshow('image2',grey)

#gaussian blurr method (how it'll work)
blurr=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('blur',blurr)
edgesofimage=cv2.Canny(blurr,50,150)
cv2.imshow('im',edgesofimage)


cv2.waitKey(0)

