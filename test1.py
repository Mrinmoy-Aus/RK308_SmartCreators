# importing libraries 
import cv2 
import numpy as np

# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture('C:/Users/Anushree Khan/Downloads/videoplayback.mp4') 

# Check if camera opened successfully 
if (cap.isOpened()== False): 
    print("Error opening video file") 

# Read until video is completed 

while(cap.isOpened()== True): 
	
    #Capture frame-by-frame 
    ret, frame = cap.read() 
    if ret == True:
        # Display the resulting frame 
        cv2.imshow('Frame', frame) 

	# Press Q on keyboard to exit 
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release 
# the video capture object 
cap.release() 

# Closes all the frames 
cv2.destroyAllWindows() 

