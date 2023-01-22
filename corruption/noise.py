import numpy as np


def gaussian(img, mean, std):
    gauss = np.random.normal(mean,std,img.shape)
    noisy = img + gauss
    return np.clip(noisy, 0, 255)
    
def saltAndPepper(img, s_vs_p, amount):
    out = np.copy(img)
    
    # Salt mode
    num_salt = np.ceil(amount * img.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape]
    out[coords] = 255
    
    # Pepper mode
    num_pepper = np.ceil(amount* img.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in img.shape]
    out[coords] = 0
    return out
    
def poisson(img,var):
    poi = np.random.poisson(var,img.shape)
    noisy = img + poi
    return np.clip(noisy, 0, 255)
    
def speckle(img,weight):
    img = img/np.max(img)
    if len(img.shape) > 2:
        row,col,ch = img.shape
        gauss = np.random.randn(row,col,ch)
    else:
        row,col = img.shape
        gauss = np.random.randn(row,col)

    noisy = img + img * gauss * weight
    return np.clip(noisy*255, 0, 255)

