#OpenCV to detect form elements on the screen and provide coordinates 

import cv2
import numpy as np
import sys

class e:

    def __init__(self, i, iT):

        img_rgb = cv2.imread(i)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        template = cv2.imread(iT,0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        y=0

        for pt in zip(*loc[::-1]):
            y=1
            #print(pt)

        print(y)
		
#arguments accepts 
if __name__ == "__main__":
    i=str(sys.argv[1])
    iT=str(sys.argv[2])#Template
    error=e(i,iT)