import cv2
pic1 = 'new.jpg'
pic2 = 'logob.jpg'
pic3 = 'logow.jpg'
img1=cv2.imread(pic1)
img2=cv2.imread(pic2)
img3 = cv2.imread(pic3)
rows,cols,channels = img2.shape
b,g,r,x=cv2.mean(img1[0:rows,0:cols])
if(((b+g+r)/3) < 80):
    img2=img3
    roi = img1[20:rows+20, 20:cols+20 ]
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 150, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
    dst = cv2.add(img1_bg,img2_fg)
    #img1[20:rows+20, 20:cols+20 ] = dst
    img1[20:rows+20 , 20:cols+20]=cv2.addWeighted(img1[20:rows+20,20:cols+20],0.7,dst,0.3,0)
else:
    roi = img1[20:rows+20, 20:cols+20 ]
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 150, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
    dst = cv2.add(img1_bg,img2_fg)
    #img1[20:rows+20, 20:cols+20 ] = dst
    img1[20:rows+20 , 20:cols+20]=cv2.addWeighted(img1[20:rows+20,20:cols+20],0.6,dst,0.4,0)
#cv2.imwrite(pic1,img1)
cv2.imshow('window',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



