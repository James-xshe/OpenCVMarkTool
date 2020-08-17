import cv2 as cv
import os
import numpy as np
import json

global img, points
ix = 0
iy = 0
drawing = False

def OnMouse(event, x, y, flag, params):
    global img, ix, iy, drawing, points
    img2 = img.copy()
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        cv.imshow('image', img2)

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.rectangle(img2, (ix, iy), (x,y), (0,0,255), 1)
            cv.imshow('image', img2)

    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img2, (ix, iy), (x,y), (0,0,255), 1)
        cv.imshow('image', img2)
        drawing = False
        # print('left top:',ix,iy)
        # print('right bot:',x,y)
        # print('left bot:', ix, y)
        # print('right, top:', x, iy)
        # print('--------------')   
        points = {'left top': (ix,iy), 'right bot': (x, y)}

def main():
        global img, points
        filenames = os.listdir('./test')
        for filename in filenames:
            img = cv.imread(os.path.join('./test',filename))
            cv.imshow('image', img)
            # img=cv.resize(img,None,fx=0.4,fy=0.4)
            cv.namedWindow('image')
            cv.setMouseCallback('image', OnMouse)
            cv.imshow('image', img)
            k = cv.waitKey(0) & 0xff
            if k == 27:
                break
            elif k == ord('n'):
                with open(os.path.join('./test',filename)+'.txt', mode='w') as f:
                    f.write(json.dumps(points))
                continue
        cv.destroyAllWindows()
main()