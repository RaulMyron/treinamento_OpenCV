import numpy as np
import cv2

image = cv2.imread('lena.png')

print('hello')
dimensions = image.shape
print(dimensions)
cv2.imshow('Img', image) #show img
cv2.waitKey(0) #when 0, lock till pressing a key
