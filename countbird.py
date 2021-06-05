color_thres = 100;
size_thres = 5;

import skimage.io as io
import numpy as np

def open_pic(path_str):
    img = io.imread(path_str)
    return(img)

def preprocess(img):
    img = np.average(img,axis=2)
    imbool = img<100
    return(imbool)

def search_bird(searched,imbool,i,j,width,height):
    if (searched[i][j]==True or imbool[i][j]==False):
        return 0
    searched[i][j] = True
    cnt = 1
    if (i>0):
        cnt += search_bird(searched,imbool,i-1,j,width,height)
    if (i<height-1):
        cnt += search_bird(searched,imbool,i+1,j,width,height)
    if (j>0):
        cnt += search_bird(searched,imbool,i,j-1,width,height)
    if (j<width-1):
        cnt += search_bird(searched,imbool,i,j+1,width,height)
    return(cnt)


def birdcount(imbool):
    bird_cnt = 0
    height = imbool.shape[0]
    width = imbool.shape[1]
    mark = np.zeros((height,width))
    searched = (mark==1) # starts all False
    for i in range(height):
        for j in range(width):
            if (searched[i][j]==False):
                pix_cnt = search_bird(searched,imbool,i,j,width,height)
                if (pix_cnt > size_thres):
                    
                    mark[i][j] = True
                    if (i>0):
                        mark[i-1][j] = True
                    if (i<height-1):
                        mark[i+1][j] = True
                    if (j>0):
                        mark[i][j-1] = True
                    if (j<width-1):
                        mark[i][j+1] = True

                    bird_cnt += 1
    return(mark,bird_cnt)
    
def run_output(path,c_thres=100,s_thres=5):
    color_thres = c_thres
    size_thres = s_thres
    im = open_pic(path)
    pim = preprocess(im)
    markim,cnt = birdcount(pim)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if (markim[i][j]==True):
                im[i][j][0] = 255
                im[i][j][1] = 0
                im[i][j][2] = 0
    return(im,cnt)
