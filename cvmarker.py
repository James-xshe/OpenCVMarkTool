import cv2 as cv
import os
import numpy as np
import json
import time

global img, point1, point2, points
drawing = False

def OnMouse(event, x, y, flag, params):
    global img, point1, point2, drawing, points
    img2 = img.copy()
    
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        point1 = (x, y)
        cv.imshow('image', img2)

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            point2 = (x, y)
            cv.rectangle(img2, point1, point2, (0,0,255), 1)
            cv.imshow('image', img2)

    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img2, point1, point2, (0,0,255), 1)
        cv.imshow('image', img2)
        drawing = False
        points = (point1, point2)

def main():
        global img, points
        imgtypedic = {'.png', '.jpg'}
        filenames = os.listdir('./test')
        for filename in filenames:
            if os.path.splitext(filename)[1] not in imgtypedic:
                continue

            if os.path.getsize(os.path.join('./test', filename) + '.txt') != 0:
                with open(os.path.join('./test', filename) + '.txt') as f:
                    js = f.read()
                    data = json.loads(js)
                    points = (tuple(data[0]), tuple(data[1]))
            img = cv.imread(os.path.join('./test',filename))

            cv.rectangle(img, points[0], points[1], (0,0,255), 1) 

            # cv.imshow('image', img)
            # img=cv.resize(img,None,fx=0.4,fy=0.4)

            cv.namedWindow('image')
            cv.setMouseCallback('image', OnMouse)
            cv.imshow('image', img)
            k = cv.waitKey(0) & 0xff
            if k == 27:
                with open(os.path.join('./test',filename)+'.txt', mode='w') as f:
                    f.write(json.dumps(points))
                break
            elif k == ord('n'):
                with open(os.path.join('./test',filename)+'.txt', mode='w') as f:
                    f.write(json.dumps(points))
                    continue
            else:
                ## Halt the program until get the right key
                os.system('pause')
    
        cv.destroyAllWindows()
main()