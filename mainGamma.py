import cv2
import numpy as np
image=cv2.imread("lenagray.jpg",0)
def outGamma(gamma):
    invGamma=1.0/gamma
    table=[]
    for i in np.arange(0,255):
        table.append(((i/255.0)**invGamma)*255)
    table=np.array(table).astype("uint8")
    return table
# for gamma in np.arange(0.5,2.5):
#     LUT = outGamma(gamma)
#     outImage=LUT[image]
#     cv2.putText(outImage,f"Gamma = {gamma}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
#     cv2.imshow("imag",np.hstack([image,outImage]))
#     cv2.waitKey (0)

#gamma 0.5
LUT=outGamma(0.5)
outHalb=LUT[image]
cv2.putText(outHalb,f"Gamma = {0.5}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
LUT=outGamma(2.5)
outDopplt=LUT[image]
cv2.putText(outDopplt,f"Gamma = {2.5}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
cv2.putText(image,"Orginal",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
out=np.hstack([image,outDopplt,outHalb])
cv2.imwrite("vergleichGamma.png",out)
cv2.imshow("out",out)
cv2.waitKey(0)