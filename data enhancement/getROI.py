import cv2
import os
import matplotlib.pyplot as plt
kind = 'train'
type = 'abnormal'



# generate mask for Region of Interest
def mask_roi(img):
    # convert colorspace to HSV
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # get saturation channel and value channel
    _,s,v = cv2.split(img2)
    # run canny edge detector on value channel
    edge = cv2.Canny(v,32,128)   
    # enhance edge on s channel
    new = cv2.addWeighted(s,.6,edge,.4,0)
    # do threshold to get roi
    _,b = cv2.threshold(new,30,255,cv2.THRESH_BINARY)
    return b

def mask_roi_blur(img):
    # doing mean blur on the mask can get a sharpper masked result
    b = mask_roi(img)
    return cv2.blur(b,3,3)

src_dir = './dataplus/{}/{}'.format(kind,type)
dest_dir = './data_masked/{}/{}'.format(kind,type)
for name in os.listdir(src_dir):
    
    img = cv2.imread(src_dir+'/{}'.format(name))
    if img is None:
        continue
    elif len(img.shape)<3:
        continue
    print(name)

    # get ROI mask
    b = mask_roi(img)

    # set ROI mask
    img[b<1]=[0,0,0]
  
    plt.imshow(img[:,:,::-1])
    plt.show()

    # write to disk
    # cv2.imwrite(dest_dir+'/{}'.format(name),img)