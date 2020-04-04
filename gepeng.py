import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
h,w,d = image.shape

flatted = cv2.resize(image, (h,int(h*1.8)))
cv2.imshow("Ur weeb material had been flatted", flatted)
cv2.imwrite("eat_that_weebs.jpg", flatted)
cv2.waitKey(0)
