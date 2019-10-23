#####################################
## Team ID #2457
## Author List Shreyas Shubhankar, Rudra Narayan Pandey
## Filename: Image Processing
## Theme Harvester Bot
## Functions: fruit_estimate(int,int,int),fruit_size_estimate(),main() 
## Global Variables : 
#####################################

import numpy as np
import cv2
import serial
ser=serial.Serial('/dev/ttyUSB0')
#####################################
## Global Variables
#####################################

current_fruit=0  #Current side of the tree being faced by bot in clockwise manner
Fire_output1=1
first_deposition=0 #First Deposition Zone
apple=[0,0,0]  #[small,large,max]
orange=[0,0,0]
blueberry=[0,0,0]
######################################
##Fruit Estimating Function
######################################
def fruit_estimate(hsv,low_threshold,high_threshold):
    #Recognising the fruit in image
    #Fruit is recognised based on which hsv range has a contour of maximum area in it
    mask=cv2.inRange(hsv,low_threshold,high_threshold)  #The image is being masked in the hue of interest
    kernel = np.ones((5,5),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)   #Removing noise and filling gaps in the thresholded binary image
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    image, contours, hierarchy = cv2.findContours(mask,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)  #Finding Contours in the binary image
    contour_array_size=len(contours) #Size of Contour array length
    area_max=0 #Max Area of contour found in the image
    current_contour=0
    for i in contours[0:contour_array_size]:
        v=contours[current_contour]
        contour_area=int(cv2.contourArea(v)) #Finding area of contour
        if contour_area>area_max:
            area_max=contour_area #Finding a contour of max area in the image
            image=cv2.drawContours(img,contours,current_contour,(100,100,0),3)
        #print(p)
            cv2.imshow('image',image)
        current_contour=current_contour+1
    return area_max #Returning the max area
######################################
## Fruit Size Estimating Function
######################################
def fruit_size_estimate(fruit_area,fruit_number):  #Finding the size of fruit
    if fruit_number == 0:  ##Red
        if fruit_area in range(0,10000):
            fruit_size=2  #0-Large fruit, 1-Max Fruit, 2-Small Fruit
            apple[2]=apple[2]+1  #Keeping count of the fruits recognised
            req_fruits_table[0,2]=req_fruits_table[0,2]-1  #Subtracting the found fruit from required fruits table
            return fruit_size
        elif fruit_area in range(10000,20000):
            fruit_size=0
            apple[0]=apple[0]+1
            req_fruits_table[0,0]=req_fruits_table[0,0]-1
            return fruit_size
        elif fruit_area in range(20000,70000):
            fruit_size=1
            apple[1]=apple[1]+1
            req_fruits_table[0,1]=req_fruits_table[0,1]-1
            return fruit_size
    elif fruit_number == 2: #Orange
        if fruit_area in range(0,10000):
            fruit_size=2
            orange[2]=orange[2]+1
            req_fruits_table[2,2]=req_fruits_table[2,2]-1
            return fruit_size
        elif fruit_area in range(10000,60000):
            fruit_size=0
            orange[0]=orange[0]+1
            req_fruits_table[2,0]=req_fruits_table[2,0]-1
            return fruit_size
        elif fruit_area in range(60000,100000):
            fruit_size=1
            orange[1]=orange[1]+1
            req_fruits_table[2,1]=req_fruits_table[2,1]-1
            return fruit_size
    elif fruit_number == 1: #Blueberry
        if fruit_area in range(0,10000):
            fruit_size=2
            blueberry[2]=blueberry[2]+1
            req_fruits_table[1,2]=req_fruits_table[1,2]-1
            return fruit_size
        elif fruit_area in range(10000,20000):
            fruit_size=0
            blueberry[0]=blueberry[0]+1
            req_fruits_table[1,0]=req_fruits_table[1,0]-1
            return fruit_size
        elif fruit_area in range(20000,70000):
            fruit_size=1
            blueberry[1]=blueberry[1]+1
            req_fruits_table[1,1]=req_fruits_table[1,1]-1
            return fruit_size

capture_frame = cv2.VideoCapture(0) #Starting video input from the camera

#######################
## Get Input from User
#######################
#tree_config=input('Enter the Arena Configuration')
tree_config=[9,18,29]
tree_config=np.array(tree_config)
print(tree_config)

##fruit_table=input('Enter the Fruit Table')
fruit_table=[3,6,1,4],[5,2,3,3],[8,3,0,4]
fruit_table=np.array(fruit_table)
print(fruit_table)

##depo_zone=input('Enter the Deposition Zone')
depo_zone=[37,38,44,45],[35,36,42,43],[40,41,47,48]
depo_zone=np.array(depo_zone)
print(depo_zone)
##
##req_fruits_table=input('Enter the Required Fruits Table')
req_fruits_table=[1,1,1],[1,1,1],[0,2,0]
req_fruits_table=np.array(req_fruits_table)
print(req_fruits_table)

    
######################################
## Main Program
######################################
apple_deposit=0  #After recognising the fruits the required deposition zone will be found
orange_deposit=0
blueberry_deposit=0
t1=str(tree_config[0])
ser.write(t1)  #Writing Tree Table to Firebird V
ser.write('n')             #This is used to communicate that one element has been sent
ser.write(str(tree_config[1]))
ser.write('n')
ser.write(str(tree_config[2]))
ser.write('n')

Fire_output1=ser.read(); #Bot reaches in front of tree
print(Fire_output1)
while(1):
    print('inside while')
    if(Fire_output1=='1'):
        print('inside if')
        while (current_fruit<4): #Till bot has faced all the sides of the tree
        

            ret, img = capture_frame.read() #Image is captured
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #Conversion to hsv
            max_area_red=0
            max_area_orange=0
            max_area_blue=0

            low_threshold_red=np.array([155,100,100])   #Red Threshold in HSV range
            high_threshold_red=np.array([180,255,255])
            max_area_red=fruit_estimate(hsv,low_threshold_red,high_threshold_red)
            print(max_area_red)

            low_threshold_orange=np.array([0,100,100])       #Orange Threshold in HSV range
            high_threshold_orange=np.array([40,255,255])
            max_area_orange=fruit_estimate(hsv,low_threshold_orange,high_threshold_orange)
            print(max_area_orange)

            low_threshold_blue=np.array([75,100,100])    #Blue Threshold in HSV range
            high_threshold_blue=np.array([130,255,255])
            max_area_blue=fruit_estimate(hsv,low_threshold_blue,high_threshold_blue)
            print(max_area_blue)

            if max_area_red>max_area_orange and max_area_red>max_area_blue:
                fruit_size=fruit_size_estimate(max_area_red,0)
                print (fruit_size)
                print('apple')
                if (req_fruits_table[0,fruit_size]>=0):
                    ser.write(fruit_table[0,current_fruit])   ##Send the position of fruit block
                    ser.write('n')
                else:
                    ser.write('0')
                    ser.write('n')
                current_fruit=current_fruit+1
                apple_deposit=1 #Deposit in the apple deposition zone
                orange_deposit=0
                blueberry_deposit=0
            elif max_area_blue>max_area_red and max_area_blue>max_area_orange:
                fruit_size=fruit_size_estimate(max_area_blue,1)
                print (fruit_size)
                print('Blueberry')
                if (req_fruits_table[1,fruit_size]>=0):
                    ser.write(fruit_table[1,current_fruit])   ##Send the position of fruit block
                    ser.write('n')
                else:
                    ser.write('0')
                    ser.write('n')
                current_fruit=current_fruit+1
                apple_deposit=0
                orange_deposit=0
                blueberry_deposit=1  #Deposit in the blueberry deposition zone
            elif max_area_orange>max_area_blue and max_area_orange>max_area_red:
                fruit_size=fruit_size_estimate(max_area_orange,2)
                print (fruit_size)
                print('Orange')
                if (req_fruits_table[2,fruit_size]>=0):
                    ser.write(fruit_table[2,current_fruit])   ##Send the position of fruit block
                    ser.write('n')
                else:
                    ser.write('0')
                    ser.write('n')
                current_fruit=current_fruit+1
                apple_deposit=0
                orange_deposit=1  #Deposit in the orange deposition zone
                blueberry_deposit=0

           

            Fire_output1=ser.read()        ##Waiting for Firebird to reach the next side of the tree
            current_fruit=current_fruit+1

        if (Fire_output1==1):
            if(apple_deposit==1):
                ser.write(depo_zone[0,1])  #Deposition Zone of Apple
                ser.write('n')
            elif(blueberry_deposit==1):
                ser.write(depo_zone[1,1])  #Deposition Zone of Blueberry
                ser.write('n')
            elif(orange_deposit==1):
                ser.write(depo_zone[2,1])  #Deposition Zone of Orange
                ser.write('n')
        apple_deposit=0
        orange_deposit=0
        blueberry_deposit=0
        current_fruit=0
        Fire_output1=ser.read();  #Till bot reaches the side of tree again and the loop is repeated

    else:
        break  #Task Completed


#######################################
cv2.waitKey(0)
cv2.destroyAllWindows()


