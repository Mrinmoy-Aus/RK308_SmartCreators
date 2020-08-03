import os 
import shutil 
destination = "2.jpg"
currentframe = 0

for i in range(0, 200):
    source = 'data/frame' + str(currentframe) + '.jpg'
    dest = shutil.copyfile(source, destination)
    os.system("python3 yolo_opencv.py --image 2.jpg --config yolo3.cfg --weights yolov3_custom_28000.weights --classes yolov3.txt")
    currentframe += 1
    
