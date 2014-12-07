import numpy as np
import cv2
import math

img = cv2.imread('test_images/1.jpg')

#Teams can add other helper functions which can be \
#added here

def play(im):
	'''
	img-- a single test image as input argument
	ball_number  -- returns the single integer specifying the target that was 
	hit  eg. 1, 5, etc
	'''
	h1,w1,w2,h2,w3,h3=0,0,0,0,0,0
	h,w,ch = im.shape
	flag=0
	for i in range(0,h-1):
		for j in range(0,w):
			if(123<=im.item(i,j,0)<=126 and 0<=im.item(i,j,1)<=1 and 217<=im.item(i,j,2)<=223):
				# print i,j
				w1= j
				h1 = i
				flag=1
				break
		if(flag==1):
			break
		
	for i in range(0,h-1):
		flag=0
		for j in range(0,w):
			if( 103<=im.item(i,j,0)<=106 and 219<=im.item(i,j,1)<=223 and 0<=im.item(i,j,2)<=3):
				# print i,j
				w2= j
				h2 = i
				flag=1
				break
		if(flag==1):
			break
	w3=w-40
	# print "h1= ",h1,"w1=",w1
	# print "h2= ",h2,"w2=",w2
	# print w3
	#*******************************************
	if (h1>h2):
		# print "1st one"
		h3 = (h2)+(((h2-h1)*(w3-w2))/(w2-w1))
		# h3 = int(math.ceil(h2+(((h2-h1)*(w3-w2))/(w1-w2))))
		# h3 = abs(h3)
		# print "the calc h3 is ",h3
		# h3 = abs(abs(h3)-h)
		# print "h3 = ",h3
	# 	# h3 = h2+ (((h2-h1)/(w2-w1))*(w3-w2))
	# 	h3 = h-h3
	else:
		# print "2nd one"
		# h3 = int(math.ceil(h2+(((h2-h1)*(w3-w2))/(w1-w2))))
		# h3 =((h2-h1)/(w1-w2))*(w3-w2)	
		# h3 = h3+h2
		h3 = (h2)+(((h2-h1)*(w3-w2))/(w2-w1))
		# h3 = abs(h3-h)
		# print "h3 = ",h3
		# h3 = (h2+420)-((h1-h2)/(w2-w1))*(w3-w2)
		# h3 = abs(h-h3)
		# h3 = 420-h3
	# r = h%h3
	# h3 = h2+ (((h2-h1)/(w2-w1))*(w3-w2)
	# h3 = 233
	#*******************************************
	# print h3
	# pt1 = w2,h2
	# pt2 = w3,h3
	# cv2.line(im, pt1, pt2, (255,0,0), 2)
	# pt1 = w2,h2
	# pt2 = w1,h1
	# cv2.line(im, pt1, pt2, (255,0,0), 2)

	b = im.item(h3,w3,0)
	g = im.item(h3,w3,1)
	r = im.item(h3,w3,2)
	# pt1 = w1,h1
	# pt2 = w2,h2
	# cv2.line(im, pt1, pt2, (0,0,255), 2) 
	# pt1 = w3,h3
	# pt2 = w1,h1
	# cv2.line(im, pt1, pt2, (0,255,0),2)
	# cv2.imshow("circles",im)
	# cv2.waitKey()
	ball_number = (h3/60)+1
	return ball_number


if __name__ == "__main__":
	#checking output for single image
	# img = cv2.imread('test_images/1.jpg')
	# ball_number = play(img)
	# print ball_number, " number ball at target range"
	#checking output for all images
	num_list = []
	for file_number in range(1,11):
		file_name = "test_images/"+str(file_number)+".jpg"
		pic = cv2.imread(file_name)
		ball_number = play(pic)
		num_list.append(ball_number)
	print num_list
