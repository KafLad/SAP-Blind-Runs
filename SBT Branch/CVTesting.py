import cv2
import os

path = r'SBT Branch/Feesh.png'
img = cv2.imread(path, cv2.IMREAD_COLOR)
print(img)


cv2.imshow("Image Test", img)

cv2.waitKey(0)

cv2.destroyAllWindows()