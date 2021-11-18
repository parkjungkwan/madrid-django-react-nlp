import cv2
import sys
import numpy


class MyOpenCV:
    def __init__(self):
        pass

    def execute(self):

        argvs = sys.argv
        if (len(argvs) != 2):
            print(f'Usage: # python {argvs[0]} imagefilename')
            quit()

        imagefilename = argvs[1]
        try:
            img = cv2.imread(imagefilename, 1)
        except:
            print
            'faild to load %s' % imagefilename
            quit()

        imgshape = img.shape
        roiWidth = imgshape[1] / 4
        roiHeight = imgshape[0] / 4
        sx = imgshape[1] / 2 - roiWidth
        sy = imgshape[0] / 2 - roiHeight
        ex = imgshape[1] / 2 + roiWidth
        ey = imgshape[0] / 2 + roiHeight

        # extract roi as array
        roi = img[sy:ey, sx:ex]

        # invert roi area
        img[sy:ey, sx:ex] = cv2.bitwise_not(roi)

        cv2.imshow('roi image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    m = MyOpenCV()
    m.execute()