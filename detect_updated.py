import cv2
import argparse
import numpy as np
from tkinter import *  
from tkinter import messagebox  
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

lst1=[0,0,0,0,0,0,0,0,0]
lst = []
st = ['gun','bullet','blood','knife','glove','scissors','glass','body','needles']

def get_output_layers(net):
    
    layer_names = net.getLayerNames()
    
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    return output_layers


def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):

    global label
    label = str(classes[class_id])
    print("hi")
    #print(label)

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

cv2.imshow("object detection", image)
cv2.waitKey()
#print(label)
i=0
for i in range(len(st)):
    #print("hello")
    #print(string[i])
    if(label == st[i]):
        print("yes")
        lst1[i]=1
        #top = Tk()  
        #top.geometry("100x100")      
        messagebox.showinfo("information","Most useful forensic item detected")  
  
        #top.mainloop()  
        ####print the list####
        #print(lst)
    else:
        continue
lst = lst1
print(lst)
print(type(lst1))
#lst = [0, 1, 0, 1, 0, 1, 0, 1, 0] 
gun=lst[0]
bullet=lst[1]
blood=lst[2]
knife=lst[3]
glove=lst[4]
scissors=lst[5]
glass=lst[6]
body=lst[7]
needles=lst[8]
string1=[int(gun),int(bullet),int(blood),int(knife),int(glove),int(scissors),int(glass),int(body),int(needles)]
string = ['gun','bullet','blood','knife','glove','scissors','glass','body','needles']

if string1[0]==1:
    a=string[0]
    a=80
if string1[0]==0:
    a=string[0]
    a=0
if string1[1]==1:
    b=string[1]
    b=10
if string1[1]==0:
    b=string[1]
    b=0
if string1[2]==1:
    c=string[2]
    c=25
if string1[2]==0:
    c=string[2]
    c=0
if string1[3]==1:
    d=string[3]
    d=50
if string1[3]==0:
    d=string[3]
    d=0
if string1[4]==1:
    e=string[4]
    e=60
if string1[4]==0:
    e=string[4]
    e=0
if string1[5]==1:
    f=string[5]
    f=35
if string1[5]==0:
    f=string[5]
    f=0
if string1[6]==1:
    g=string[6]
    g=10
if string1[6]==0:
    g=string[6]
    g=0
if string1[7]==1:
    h=string[7]
    h=90
if string1[7]==0:
    h=string[7]
    h=0
if string1[8]==1:
    i=string[8]
    i=75
if string1[8]==0:
    i=string[8]
    i=0
lst=[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h),int(i)]


  
# sorting the list 
lst.sort()
#print greatest value
cc=lst[-1]   
if int(cc)==int(a):
	print(string[0])
if int(cc)==int(b):
	print(string[1])
if int(cc)==int(c):
	print(string[2])
if int(cc)==int(d):
	print(string[3])
if int(cc)==int(e):
	print(string[4])
if int(cc)==int(f):
	print(string[5])
if int(cc)==int(g):
	print(string[6])
if int(cc)==int(h):
	print(string[7])
if int(cc)==int(i):
	print(string[8])

cv2.imwrite("object-detection.jpg", image)
cv2.destroyAllWindows()

