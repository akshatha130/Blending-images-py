import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\python\Python Program\Io\Lenna.png")
img2 = cv2.imread(r"C:\Users\aksha\OneDrive\Desktop\python\Python Program\Io\chess-board.png")

img1 = cv2.resize(img1,(400,400))
img2 = cv2.resize(img2,(400,400))

res1 = img1 + img2 #numpy addition,dis advantage- pixal will get damaged

res2 = cv2.add(img1,img2)

res3 = cv2.addWeighted(img1,0.3,img2,0.7,0)
# 0 at the end is a gamma value (saturation)

cv2.imshow("res1",res1)
cv2.imshow("res2",res2)
cv2.imshow("res3",res3)
cv2.imshow("Orginal_img1",img1)
cv2.imshow("Original_img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()