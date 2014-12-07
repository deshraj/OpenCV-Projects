import numpy as np
import cv2

img = cv2.imread('test_images/1.jpg')

#Teams can add other helper functions which can be \
#added here

def play(im):
    '''
    img-- a single test image as input argument
    letter -- returns the single character specifying the target that was 
    hit  eg. 'A', 'D', etc
    '''
    h1,w1,w2,h2,w3,h3=0,0,0,0,0,0
    h,w,ch = im.shape
    flag=0
    for i in range(0,h-1):
        for j in range(0,w):
            if(9<=im.item(i,j,0)<=15 and 99<=im.item(i,j,1)<=102 and 246<=im.item(i,j,2)<=255):
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
            if( 208<=im.item(i,j,0)<=212 and 45<=im.item(i,j,1)<=47 and 8<=im.item(i,j,2)<=12):
                # print i,j
                w2= j
                h2 = i
                flag=1
                break
        if(flag==1):
            break
    # w3=w-40
    h3 = 50
    # print "h1= ",h1,"w1=",w1
    # print "h2= ",h2,"w2=",w2
    # print w3
    #CHECK THE BELOW MATHEMATICAL EQUATION FOR GETTING THE H3. I THINK I HAVE COMMITED MISTAKE IN THIS.
    #*******************************************
    # if (h1>h2):
    #     print "1st one"
    #     w3 = (w2)+(((w2-w1)*(h3-h2))/(h2-h1))
        # h3 = int(math.ceil(h2+(((h2-h1)*(w3-w2))/(w1-w2))))
        # h3 = abs(h3)
        # print "the calc w3 is ",w3
        # h3 = abs(abs(h3)-h)
        # print "w3 = ",w3
    #   # h3 = h2+ (((h2-h1)/(w2-w1))*(w3-w2))
    #   h3 = h-h3
    # else:
        # print "2nd one"
        # h3 = int(math.ceil(h2+(((h2-h1)*(w3-w2))/(w1-w2))))
        # h3 =((h2-h1)/(w1-w2))*(w3-w2) 
        # h3 = h3+h2
    w3 = (w2)+(((w2-w1)*(h3-h2))/(h2-h1))
        # h3 = (h2)+(((h2-h1)*(w3-w2))/(w2-w1))
        # h3 = abs(h3-h)
        # print "w3 = ",w3
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
    letter = chr(80+int(w3/70))
    if ((80+int(w3/70))<80):
        letter = 'None'
    return letter

if __name__ == "__main__":
    #checking output for single image
    # img = cv2.imread('test_images/1.jpg')
    # balloon_letter = play(img)
    # print balloon_letter, " balloon in range"
    #checking output for all images
    alpha_list = []
    for file_number in range(1,11):
        file_name = "test_images/"+str(file_number)+".jpg"
        pic = cv2.imread(file_name)
        balloon_letter = play(pic)
        alpha_list.append(balloon_letter)
    print alpha_list
