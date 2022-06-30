import copy
import cv2
from cv2 import ROTATE_90_CLOCKWISE
from cv2 import ROTATE_180
from cv2 import ROTATE_90_COUNTERCLOCKWISE
import numpy as np

# can only rotate some pi/2 radius
def rotate(mat,mode):
    if mode == 1:
        mat2 = cv2.rotate(mat,ROTATE_90_CLOCKWISE)

    elif mode == 2:
        mat2 = cv2.rotate(mat,ROTATE_180)

    elif mode == 3:
        mat2 = cv2.rotate(mat,ROTATE_90_COUNTERCLOCKWISE)

    else:
        raise "illeagal mode"
    return mat2

# can rotate any radius
def freeRotate(mat,angle):
    # might make pixels out of frame, to be fixed
    w,h = mat.shape
    rmat = cv2.getRotationMatrix2D((w//2,h//2),angle,1)
    rotated = cv2.warpAffine(mat, rmat, (w, h))
    return rotated

# add gaussian noise of pepper-salt noise
def addNoise(mat,mode,*args):
    if mode == 'gaussian':
        # arg1:gaussian noise mean, arg2:g-noise std
        noise = np.random.standard_normal(mat.shape)
        print(noise)
        noise = noise * args[1] + args[0]
        return mat+noise
    elif mode == 'pepper':
        # arg1:pepper noise probability, arg2:salt noise prob
        mat2 = copy.deepcopy(mat)
        black =  np.random.uniform(0,1,mat2.shape)
        mat2[black<args[0]]=0
        white = np.random.uniform(0,1,mat2.shape)
        mat2[white<args[1]]=255
        return mat2
    else:
        raise "illeagal mode"
