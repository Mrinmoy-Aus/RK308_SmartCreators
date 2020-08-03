
import cv2
import argparse
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
import sys
import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#from home.py import *
def selectImage():
    global left_frame, img_label, img_read
    for wid in right_frame.winfo_children():
        wid.destroy()

    filetype = [("images", "*.jpg *.jpeg *.png")]
    path = filedialog.askopenfilename(title="Choose a image", filetypes=filetype)
    a = path
    print(a)
    
    if(len(path) > 0):
        img_read = cv2.imread(path)

        img_size =  left_frame.winfo_height() - 40
        showImage(img_read, img_size)

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help = 'path to input image')
ap.add_argument('-c', '--config', required=True,
                help = 'path to yolo config file')
ap.add_argument('-w', '--weights', required=True,
                help = 'path to yolo pre-trained weights')
ap.add_argument('-cl', '--classes', required=True,
                help = 'path to text file containing class names')
args = ap.parse_args()


def breaker():
    fig = plt.figure()
    image1 = plt.subplot(121)
    image2 = plt.subplot(122)
    img_source1 = mpimg.imread('outputs\object-detection.jpg')
    img_source2 = mpimg.imread('croped_faces/frame1.jpg')
    _ = image1.imshow(img_source1)
    _ = image2.imshow(img_source2)
            
    image1.axis("off")
    image2.axis("off")
    plt.show()
    import pp1

def breaker1():
    fig = plt.figure()
    image1 = plt.subplot(121)
    image2 = plt.subplot(122)
    image3 = plt.subplot(123)
    img_source1 = mpimg.imread('outputs\object-detection.jpg')
    img_source2 = mpimg.imread('croped_faces/frame1.jpg')
    img_source3 = mpimg.imread('croped_faces/frame2.jpg')
    _ = image1.imshow(img_source1)
    _ = image2.imshow(img_source2)
    _ = image3.imshow(img_source3)


    image1.axis("off")
    image2.axis("off")
    image3.axis("off")
    plt.show()
    
    import pp1
def breaker2():
    fig = plt.figure()
    image1 = plt.subplot(121)
    image2 = plt.subplot(122)
    image3 = plt.subplot(123)
    image4 = plt.subplot(124)

    img_source1 = mpimg.imread('outputs\object-detection.jpg')
    img_source2 = mpimg.imread('croped_faces/frame1.jpg')
    img_source3 = mpimg.imread('croped_faces/frame2.jpg')
    img_source4 = mpimg.imread('croped_faces/frame3.jpg')
    _ = image1.imshow(img_source1)
    _ = image2.imshow(img_source2)
    _ = image3.imshow(img_source3)
    _ = image4.imshow(img_source4)

    image1.axis("off")
    image2.axis("off")
    image3.axis("off")
    image4.axis("off")
    plt.show()
    import pp1
def breaker3():
    fig = plt.figure()
    image1 = plt.subplot(121)
    image2 = plt.subplot(122)
    image3 = plt.subplot(123)
    image4 = plt.subplot(124)
    image5 = plt.subplot(125)

    img_source1 = mpimg.imread('outputs\object-detection.jpg')
    img_source2 = mpimg.imread('croped_faces/frame1.jpg')
    img_source3 = mpimg.imread('croped_faces/frame2.jpg')
    img_source4 = mpimg.imread('croped_faces/frame3.jpg')
    img_source5 = mpimg.imread('croped_faces/frame4.jpg')
    _ = image1.imshow(img_source1)
    _ = image2.imshow(img_source2)
    _ = image3.imshow(img_source3)
    _ = image4.imshow(img_source4)
    _ = image5.imshow(img_source5)
    image1.axis("off")
    image2.axis("off")
    image3.axis("off")
    image4.axis("off")
    image4.axis("off")
    plt.show()
    import pp1

def fun(name,cc):
    image = cv2.imread(name)
    ### Detect and crop face from images###
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")    #--------> Making interest box to crop the faces
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
    )
    g=len(faces)
    ###
   
    z=1
   #currentframe=0
    if (cc==1):
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_color = image[y:y + h, x:x + w]
            d=cv2.imwrite('croped_faces/frame{}'.format(z)+ '.jpg',roi_color)
            
            
            z=z+1
            

            
        print(z-1)
        if z==2:
            breaker()

        if z==3:
            breaker1()

            


        if z==4:
            breaker2()

            

        if z==5:
            breaker3()

            
    else:
        exit()

    

    
      
def get_output_layers(net):
    
    layer_names = net.getLayerNames()
    
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers


def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):

    label = str(classes[class_id])

    color = COLORS[class_id]

    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    
image = cv2.imread(args.image)

Width = image.shape[1]
Height = image.shape[0]
scale = 0.00392

classes = None

with open(args.classes, 'r') as f:
    classes = [line.strip() for line in f.readlines()]

COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

net = cv2.dnn.readNet(args.weights, args.config)

blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

net.setInput(blob)

outs = net.forward(get_output_layers(net))

class_ids = []
confidences = []
boxes = []
conf_threshold = 0.5
nms_threshold = 0.4


for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * Width)
            center_y = int(detection[1] * Height)
            w = int(detection[2] * Width)
            h = int(detection[3] * Height)
            x = center_x - w / 2
            y = center_y - h / 2
            class_ids.append(class_id)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])


indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

for i in indices:
    i = i[0]
    box = boxes[i]
    x = box[0]
    y = box[1]
    w = box[2]
    h = box[3]
    draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))

#cv2.imshow("object detection", image)
#cv2.waitKey()
    
status = cv2.imwrite("outputs\object-detection.jpg", image)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
cc=1
cv2.destroyAllWindows()
name ='outputs\object-detection.jpg'
#status = cv2.imwrite('faces_detected.jpg', image)
#print("[INFO] Image faces_detected.jpg written to filesystem: ", status)


fun(name,cc)


#call the face crop function
   
