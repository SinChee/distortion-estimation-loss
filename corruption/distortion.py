import cv2
import numpy as np


def gaussianBlur(img, size):
    img = cv2.GaussianBlur(img.copy(),(size,size),0)
    return img

def averageBlur(img,size):
    img = img.astype(np.float32)
    kernel = np.ones((size,size), np.float32)
    kernel = kernel/np.sum(kernel)
    output = cv2.filter2D(img.copy(),-1,kernel)
    return output
    
def medianBlur(img,size):
    median = cv2.medianBlur(img,size)
    return median
    
def motionBlur(img, l, w, a):
    h = int(max(l,w)*1.5)
    kernel = motion_kernel(a,l,w,h)
    kernel = kernel/np.sum(kernel)
    blur = cv2.filter2D(img.copy(), -1, kernel)
    return blur
            
def motion_kernel(angle, d, w, sz=500):
    kern = np.ones((w, d), np.float32)
    c, s = np.cos(angle), np.sin(angle)
    A = np.float32([[c, -s, 0], [s, c, 0]])
    sz2 = sz // 2
    A[:, 2] = (sz2, sz2) - np.dot(A[:, :2], ((d-1)*0.5, 0))
    kern = cv2.warpAffine(kern, A, (sz, sz), flags=cv2.INTER_CUBIC)
    return kern
        