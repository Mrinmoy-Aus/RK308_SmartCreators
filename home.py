import os
import cv2
# importing shutil module 
import shutil 
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import threading
import shutil
#from facerec import *
from register import *
from dbHandler import *
from tkinter.ttk import * 
from tkinter import Tk, Button
from tkinter import *
from tkinter import messagebox
from PIL import Image 
from selenium import webdriver
from selenium import*
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as urllib2
#from match import *
from selenium import webdriver
from selenium import*
from selenium.webdriver.common.keys import Keys
from selenium. common. exceptions import *
import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as urllib2
from test import *
import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import sklearn as sk 
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.io as pio
from selenium import webdriver
from selenium import*
from selenium.webdriver.common.keys import Keys
import time
import pynput
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as urllib2
from pynput.keyboard import Key, Controller
import codecs
import nltk
from textblob import TextBlob
import re
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np



active_page = 0
thread_event = None
left_frame = None
right_frame = None
heading = None
webcam = None
img_label = None
img_read = None
img_list = []
slide_caption = None
slide_control_panel = None
current_slide = -1



root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.iconphoto(False, tk.PhotoImage(file='SmartCreators.png'))
root.title('SmartCreators')
#root.geometry('1500x900+200+100')
root.geometry("%dx%d+0+0" % (w, h))
root.resizable(True, True)




# create Pages
pages = []
for i in range(4):
    pages.append(tk.Frame(root, bg="#660033"))
    pages[i].pack(side="top", fill="both", expand=True)
    pages[i].place(x=0, y=0, relwidth=1, relheight=1)


def goBack():
    global active_page, thread_event, webcam

    if (active_page==3 and not thread_event.is_set()):
        thread_event.set()
        webcam.release()

    for widget in pages[active_page].winfo_children():
        widget.destroy()

    pages[0].lift()
    active_page = 0


def basicPageSetup(pageNo):
    global left_frame, right_frame, heading

    back_img = tk.PhotoImage(file="back.png")
    back_button = tk.Button(pages[pageNo], image=back_img, bg="#660033", bd=0, highlightthickness=0,
           activebackground="#660033", command=goBack)
    back_button.image = back_img
    back_button.place(x=1, y=0)

    heading = tk.Label(pages[pageNo], fg="white", bg="#660033", font="Arial 20 bold", pady=10)
    heading.pack()

    content = tk.Frame(pages[pageNo], bg="#660033", pady=20)
    content.pack(expand="true", fill="both")

    left_frame = tk.Frame(content, bg="#660033")
    left_frame.grid(row=0, column=0, sticky="nsew")

    right_frame = tk.LabelFrame(content, text="Detected Criminals", bg="#660033", font="Arial 20 bold", bd=4,
                             foreground="#2ea3ef", labelanchor="n")
    right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    content.grid_columnconfigure(0, weight=1, uniform="group1")
    content.grid_columnconfigure(1, weight=1, uniform="group1")
    content.grid_rowconfigure(0, weight=1)


def showImage(frame, img_size):
    global img_label, left_frame

    img = cv2.resize(frame, (img_size, img_size))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    if (img_label == None):
        img_label = tk.Label(left_frame, image=img, bg="#660033")
        img_label.image = img
        img_label.pack(padx=20)
    else:
        img_label.configure(image=img)
        img_label.image = img

def getNewSlide(control):
    global img_list, current_slide

    if(len(img_list) > 1):
        if(control == "prev"):
            current_slide = (current_slide-1) % len(img_list)
        else:
            current_slide = (current_slide+1) % len(img_list)

        img_size = left_frame.winfo_height() - 200
        showImage(img_list[current_slide], img_size)

        slide_caption.configure(text = "Image {} of {}".format(current_slide+1, len(img_list)))


def selectMultiImage(opt_menu, menu_var):
    global img_list, current_slide, slide_caption, slide_control_panel

    filetype = [("images", "*.jpg *.jpeg *.png")]
    path_list = filedialog.askopenfilenames(title="Choose an image", filetypes=filetype)

    if(len(path_list) < 0):
        messagebox.showerror("Error", "Choose an images.")
    else:
        img_list = []
        current_slide = -1

        # Resetting slide control panel
        if (slide_control_panel != None):
            slide_control_panel.destroy()

        # Creating Image list
        for path in path_list:
            img_list.append(cv2.imread(path))

        # Creating choices for profile pic menu
        menu_var.set("")
        opt_menu['menu'].delete(0, 'end')

        for i in range(len(img_list)):
            ch = "Image " + str(i+1)
            opt_menu['menu'].add_command(label=ch, command= tk._setit(menu_var, ch))
            menu_var.set("Image 1")


        # Creating slideshow of images
        img_size =  left_frame.winfo_height() - 200
        current_slide += 1
        showImage(img_list[current_slide], img_size)

        slide_control_panel = tk.Frame(left_frame, bg="#660033", pady=20)
        slide_control_panel.pack()

        back_img = tk.PhotoImage(file="previous.png")
        next_img = tk.PhotoImage(file="next.png")

        prev_slide = tk.Button(slide_control_panel, image=back_img, bg="#660033", bd=0, highlightthickness=0,
                            activebackground="#660033", command=lambda : getNewSlide("prev"))
        prev_slide.image = back_img
        prev_slide.grid(row=0, column=0, padx=60)

        slide_caption = tk.Label(slide_control_panel, text="Image 1 of {}".format(len(img_list)), fg="#ff9800",
                              bg="#660033", font="Arial 15 bold")
        slide_caption.grid(row=0, column=1)

        next_slide = tk.Button(slide_control_panel, image=next_img, bg="#660033", bd=0, highlightthickness=0,
                            activebackground="#660033", command=lambda : getNewSlide("next"))
        next_slide.image = next_img
        next_slide.grid(row=0, column=2, padx=60)

# for registering criminal
def register(entries, required, menu_var):
    global img_list

    # Checking if no image selected
    if(len(img_list) == 0):
        messagebox.showerror("Error", "Select Images first.")
        return

    # Fetching data from entries
    entry_data = {}
    for i, entry in enumerate(entries):
        val = entry[1].get()

        if (len(val) == 0 and required[i] == 1):
            messagebox.showerror("Field Error", "Required field missing :\n\n%s" % (entry[0]))
            return
        else:
            entry_data[entry[0]] = val.lower()


    # Setting Directory
    path = os.path.join('face_samples', "temp_criminal")
    if not os.path.isdir(path):
        os.mkdir(path)

    no_face = []
    for i, img in enumerate(img_list):
        # Storing Images in directory
        id = registerCriminal(img, path, i + 1)
        if(id != None):
            no_face.append(id)

    # check if any image doesn't contain face
    if(len(no_face) > 0):
        no_face_st = ""
        for i in no_face:
            no_face_st += "Image " + str(i) + ", "
        messagebox.showerror("Registration Error", "Registration failed!\n\nFollowing images doesn't contain"
                        " face or Face is too small:\n\n%s"%(no_face_st))
        shutil.rmtree(path, ignore_errors=True)
    else:
        # Storing data in database
        rowId = insertData(entry_data)

        if(rowId!=""):
            messagebox.showinfo("Success", "Criminal Registered Successfully.")
            shutil.move(path, os.path.join('face_samples', entry_data["Name"]))

            # save profile pic
            profile_img_num = int(menu_var.get().split(' ')[1]) - 1
            if not os.path.isdir("profile_pics"):
                os.mkdir("profile_pics")
            cv2.imwrite("profile_pics/criminal %s.png"%rowId, img_list[profile_img_num])

            goBack()
        else:
            shutil.rmtree(path, ignore_errors=True)
            messagebox.showerror("Database Error", "Some error occured while storing data.")


## update scrollregion when all widgets are in canvas
def on_configure(event, canvas, win):
    canvas.configure(scrollregion=canvas.bbox('all'))
    canvas.itemconfig(win, width=event.width)

## Register Page ##
def getPage1():
    global active_page, left_frame, right_frame, heading, img_label
    active_page = 1
    img_label = None
    opt_menu = None
    menu_var = tk.StringVar(root)
    pages[1].lift()

    basicPageSetup(1)
    heading.configure(text="Register Criminal")
    right_frame.configure(text="Enter Details")

    btn_grid = tk.Frame(left_frame, bg="#660033")
    btn_grid.pack()

    tk.Button(btn_grid, text="Select Images", command=lambda: selectMultiImage(opt_menu, menu_var), font="Arial 15 bold", bg="#2196f3",
           fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
           activeforeground="white").grid(row=0, column=0, padx=25, pady=25)


    # Creating Scrollable Frame
    canvas = tk.Canvas(right_frame, bg="#660033", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand="true", padx=30)
    scrollbar = tk.Scrollbar(right_frame, command=canvas.yview, width=20, troughcolor="#660033", bd=0,
                          activebackground="#00bcd4", bg="#2196f3", relief="raised")
    scrollbar.pack(side="left", fill="y")

    scroll_frame = tk.Frame(canvas, bg="#660033", pady=20)
    scroll_win = canvas.create_window((0, 0), window=scroll_frame, anchor='nw')

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda event, canvas=canvas, win=scroll_win: on_configure(event, canvas, win))


    tk.Label(scroll_frame, text="* Required Fields", bg="#660033", fg="yellow", font="Arial 13 bold").pack()
    # Adding Input Fields
    input_fields = ("Name", "Father's Name", "Mother's Name", "Gender", "DOB(yyyy-mm-dd)", "Blood Group",
                    "Identification Mark", "Nationality", "Religion", "Crimes Done", "Profile Image")
    ip_len = len(input_fields)
    required = [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0]

    entries = []
    for i, field in enumerate(input_fields):
        row = tk.Frame(scroll_frame, bg="#660033")
        row.pack(side="top", fill="x", pady=15)

        label = tk.Text(row, width=20, height=1, bg="#660033", fg="#ffffff", font="Arial 13", highlightthickness=0, bd=0)
        label.insert("insert", field)
        label.pack(side="left")

        if(required[i] == 1):
            label.tag_configure("star", foreground="yellow", font="Arial 13 bold")
            label.insert("end", "  *", "star")
        label.configure(state="disabled")

        if(i != ip_len-1):
            ent = tk.Entry(row, font="Arial 13", selectbackground="#90ceff")
            ent.pack(side="right", expand="true", fill="x", padx=10)
            entries.append((field, ent))
        else:
            menu_var.set("Image 1")
            choices = ["Image 1"]
            opt_menu = tk.OptionMenu(row, menu_var, *choices)
            opt_menu.pack(side="right", fill="x", expand="true", padx=10)
            opt_menu.configure(font="Arial 13", bg="#2196f3", fg="white", bd=0, highlightthickness=0, activebackground="#90ceff")
            menu = opt_menu.nametowidget(opt_menu.menuname)
            menu.configure(font="Arial 13", bg="white", activebackground="#90ceff", bd=0)

    tk.Button(scroll_frame, text="Register", command=lambda: register(entries, required, menu_var), font="Arial 15 bold",
           bg="#2196f3", fg="white", pady=10, padx=30, bd=0, highlightthickness=0, activebackground="#091428",
           activeforeground="white").pack(pady=25)

# fetching the criminal details from the firebase database
def showCriminalProfile(name):
    top = tk.Toplevel(bg="#660033")
    top.title("Criminal Profile")
    top.geometry("1500x900+%d+%d"%(root.winfo_x()+10, root.winfo_y()+10))

    tk.Label(top, text="Criminal Profile", fg="white", bg="#660033", font="Arial 20 bold", pady=10).pack()

    content = tk.Frame(top, bg="#660033", pady=20)
    content.pack(expand="true", fill="both")
    content.grid_columnconfigure(0, weight=3, uniform="group1")
    content.grid_columnconfigure(1, weight=5, uniform="group1")
    content.grid_rowconfigure(0, weight=1)

    (id, crim_data) = retrieveData(name)

    path = os.path.join("profile_pics", "criminal %s.png"%id)
    # profile_img = cv2.imread(path)

    # #profile_img = cv2.resize(profile_img, (500, 500))
    # img = cv2.cvtColor(profile_img, cv2.COLOR_BGR2RGB)
    # img = Image.fromarray(img)
    # img = ImageTk.PhotoImage(img)
    # img_label = tk.Label(content, image=img, bg="#660033")
    # img_label.image = img
    # img_label.grid(row=0, column=0)

    info_frame = tk.Frame(content, bg="#660033")
    info_frame.grid(row=0, column=1, sticky='w')

    for i, item in enumerate(crim_data.items()):
        tk.Label(info_frame, text=item[0], pady=15, fg="yellow", font="Arial 15 bold", bg="#660033").grid(row=i, column=0, sticky='w')
        tk.Label(info_frame, text=":", fg="yellow", padx=50, font="Arial 15 bold", bg="#660033").grid(row=i, column=1)
        val = "---" if (item[1]=="") else item[1]
        tk.Label(info_frame, text=val.capitalize(), fg="white", font="Arial 15", bg="#660033").grid(row=i, column=2, sticky='w')

#image recognition
def startRecognition():
    global img_read, img_label

    if(img_label == None):
        messagebox.showerror("Error", "No image selected. ")
        return

    crims_found_labels = []
    for wid in right_frame.winfo_children():
        wid.destroy()

    frame = cv2.flip(img_read, 1, 0)
    #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coords = detect_faces(gray_frame)

    if (len(face_coords) == 0):
        messagebox.showerror("Error", "Image doesn't contain any face or face is too small.")
    else:
        (known_face_names, known_face_encodings) = train_model()
        #print(names)
        print('Training Successful. Detecting Faces')
        (frame, name) = recognize_face(frame,known_face_names,known_face_encodings)

        img_size = left_frame.winfo_height() - 40
        #frame = cv2.flip(frame, 1, 0)
        showImage(frame, img_size)

        if (len(name) == 0):
            messagebox.showerror("Error", "No criminal recognized.")
            return
        print(name)

        for i in range(len(name)):
            crims_found_labels.append(tk.Label(right_frame, text=name[i], bg="orange",
                                            font="Arial 15 bold", pady=20))
            crims_found_labels[i].pack(fill="x", padx=20, pady=10)
            crims_found_labels[i].bind("<Button-1>", lambda e, name=name[i]:showCriminalProfile(name))


def selectImage():
    global left_frame, img_label, img_read
    for wid in right_frame.winfo_children():
        wid.destroy()

    filetype = [("images", "*.jpg *.jpeg *.png")]
    path = filedialog.askopenfilename(title="Choose a image", filetypes=filetype)

    if(len(path) > 0):
        img_read = cv2.imread(path)

        img_size =  left_frame.winfo_height() - 40
        showImage(img_read, img_size)

def selectvideos():
    global left_frame, img_label, img_read
    for wid in right_frame.winfo_children():
        wid.destroy()

    filetype = [("videos", "*.mp4")]
    path = filedialog.askopenfilename(title="Choose a video", filetypes=filetype)
    source = path
    print(path)
    cam = cv2.VideoCapture(path)

    try:
        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
    # frame 
    currentframe = 0

    messagebox.showinfo("Show Information","Under Process")
    for i in range(0, 200):
        # reading from frame
        ret,frame = cam.read()
        print(ret)
        if ret: 
            # if video is still left continue creating images
            name = './data/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)

            cv2.imwrite(name, frame)

            currentframe += 1
            print("hi")
        else:
            print("hello")
        
            break
    
    messagebox.showinfo("Show Information","Completed")
    cam.release() 
    cv2.destroyAllWindows() 

    if(len(path) > 0):
        img_read = cv2.imread(path)


## Detection Page ##
def getPage2():
    global active_page, left_frame, right_frame, img_label, heading
    img_label = None
    active_page = 2
    pages[2].lift()

    basicPageSetup(2)
    heading.configure(text="Detect Criminal")
    right_frame.configure(text="Detected Criminals")

    btn_grid = tk.Frame(left_frame, bg="#660033")
    btn_grid.pack()

    tk.Button(btn_grid, text="Select Image", command=selectImage, font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=0, column=0, padx=25, pady=25)
    tk.Button(btn_grid, text="Recognize", command=startRecognition, font="Arial 15 bold", padx=20, bg="#2196f3",
           fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
           activeforeground="white").grid(row=0, column=1, padx=25, pady=25)


def getCSV ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path)
    print (import_file_path)
    print(df.head)
    if df is not None:
        messagebox.showinfo(title='Loader',message='Data load complete...')
    
def getPage6():
    global active_page,  heading, df
    img_label = None
    active_page = 2
    pages[2].lift()

    basicPageSetup(2)
    heading.configure(text="Predict and Analysis Crime")
    #right_frame.configure(text="Detected Criminals")

    btn_grid = tk.Frame(left_frame, bg="#660033")
    btn_grid.pack()
    
    
    tk.Button(btn_grid, text="Enter the CSV File", command=getCSV, font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=0, column=0, padx=25, pady=25)
    
    tk.Button(btn_grid, text="Analytics Model", command=getPage7, font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=1, column=0, padx=25, pady=25)
    tk.Button(btn_grid, text="Prediction Model", command=getPage8, font="Arial 15 bold", padx=20, bg="#2196f3",
           fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
           activeforeground="white").grid(row=1, column=1, padx=25, pady=25)
def on_cancel(self):
        self.destroy()
#crime prediction
def map1():
    global df
    plt.rcParams['figure.figsize'] = (20, 9)
    plt.style.use('dark_background')
    sns.countplot(df['Crm Cd Desc'], palette = 'gnuplot')
    plt.title('Major Crimes in Sanfrancisco', fontweight = 20, fontsize = 10)
    plt.xticks(rotation = 90)
    plt.savefig('image1.png')
    plt.show()
def map2():
    global df
    plt.rcParams['figure.figsize'] = (20, 9)
    plt.style.use('grayscale')

    color = plt.cm.spring(np.linspace(0, 1, 15))
    df['AREA NAME'].value_counts().plot.bar(color = color)

    plt.title('District with Most Crime',fontsize = 30)
    plt.xticks(rotation = 90)
    plt.savefig('image2.png')
    plt.show()
def map3():
    global df
    plt.rcParams['figure.figsize'] = (20, 9)
    plt.style.use('Solarize_Light2')

    color = plt.cm.ocean(np.linspace(0, 1, 15))
    df['LOCATION'].value_counts().head(15).plot.bar(color = color)

    plt.title('Top 15 Regions in Crime',fontsize = 20)
    plt.xticks(rotation = 90)
    plt.savefig('image3.png')
    plt.show()

def map4():
    global df
    plt.style.use('seaborn')

    color = plt.cm.winter(np.linspace(0, 10, 20))
                          
    df['Status Desc'].value_counts().plot.bar(color = color, figsize = (15, 8))

    plt.title('Resolutions for Crime',fontsize = 20)
    plt.xticks(rotation = 90)
    plt.savefig('image4.png')
    plt.show()
def map5():
    global df
    color = plt.cm.twilight(np.linspace(0, 5, 100))
    df['TIME OCC'].value_counts().head(20).plot.bar(color = color, figsize = (15, 9))
    plt.title('Distribution of crime over the day', fontsize = 20)
    plt.savefig('image5.png')
    plt.show()
def map6():
    global df
    df1 = pd.crosstab(df['Crm Cd Desc'], df['AREA NAME'])
    color = plt.cm.Greys(np.linspace(0, 1, 10))
    df1.div(df1.sum(1).astype(float), axis = 0).plot.bar(stacked = True, color = color, figsize = (18, 12))
    plt.title('District vs Category of Crime', fontweight = 30, fontsize = 20)
    plt.xticks(rotation = 90)
    plt.savefig('image6.png')
    plt.show()
def map7():
    global df
    df['Date'] = pd.to_datetime(df['DATE OCC'])

    df['Month'] = df['Date'].dt.month

    plt.style.use('fivethirtyeight')
    plt.rcParams['figure.figsize'] = (15, 8)

    sns.countplot(df['Month'], palette = 'autumn',)
    plt.title('Crimes in each Months', fontsize = 20)
    plt.savefig('image7.png')
    plt.show()
 

#root.destroy    
def getPage7():
    global active_page, left_frame, right_frame, heading, img_label, df
    img_label = None
    opt_menu=None
    menu_var = tk.StringVar(root)
    active_page = 3
    pages[3].lift()

    tk.Button( text="Back",command=goBack1,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=0, column=1, padx=25, pady=25)

    tk.Button( text="Major Crimes",command=map1,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=1, column=1, padx=25, pady=25)
    tk.Button( text="District with crime",command=map2 ,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=1, column=2, padx=25, pady=25)
    tk.Button( text="15 Top crime",command=map3,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=1, column=3, padx=25, pady=25)
    tk.Button( text="Resolution of Crime",command=map4 ,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=1, column=4, padx=25, pady=25)
    tk.Button( text="Each day Crime",command=map5,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=2, column=1, padx=25, pady=25)
    tk.Button( text="Distric Vs Crime catagory",command=map6 ,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=2, column=2, padx=25, pady=25)
    tk.Button( text="Each Month Crime",command=map7 ,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=2, column=3, padx=25, pady=25)

def getPage71():
    global active_page, left_frame, right_frame, heading, img_label, df
    img_label = None
    opt_menu=None
    menu_var = tk.StringVar(root)
    active_page = 3
    pages[3].lift()
    basicPageSetup(3)
def goBack1():
    global active_page, thread_event, webcam

    if (active_page==5 and not thread_event.is_set()):
        thread_event.set()
        webcam.release()

    for widget in pages[active_page].winfo_children():
        widget.destroy()

    pages[2].lift()
    active_page = 2




def upLoad():
    global img_list, current_slide, slide_caption, slide_control_panel
    img_read=cv2.imread("image1.png")
    lab=Label(left_frame,text='image')
    img_size=200
    showImage(img_read,img_size)
    lab.pack()


def getMap():
    data1=pd.read_csv("crime_report_2010_to_2019225.csv")
    print(data1)
    data1=data1.sample(n = 40)
    print(data1)
    data2=data1.to_csv("sample1.csv")
    pd2=pd.read_csv("/home/argho/Desktop/RK308_SmartCreators-master/sample1.csv")
    print(pd2)
    fig = px.scatter_mapbox(pd2, lat="LAT", lon="LON", hover_name="AREA ", hover_data=["Premis Cd", "Weapon Used Cd"],
                        color_discrete_sequence=["fuchsia"], zoom=10, height=1000)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    pio.write_html(fig, file='Name.html', auto_open=True)
    fig.show()
    
    
def getPage8():
    global active_page,df
    img_level=None
    active_page =3
    pages[3].lift()
    
    tk.Button( text="Back",command=goBack1,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=0, column=1, padx=25, pady=25)
    tk.Button( text="Train",command=cleandata ,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=1, column=1, padx=25, pady=25)

    tk.Button( text="Predict Crime",command=trainData ,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=1, column=2, padx=25, pady=25)

    tk.Button( text="Get Map",command=getMap,  font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=1, column=3, padx=25, pady=25)


def cleandata():
    global df,data,X,Y,days,day_index
    df =df.drop(['DR_NO','Date Rptd','DATE OCC','AREA NAME','Crm Cd Desc','Mocodes','Vict Sex','Vict Descent','Premis Desc','Weapon Desc','Status','Status Desc','LOCATION','Cross Street','Crm Cd 2','Crm Cd 3','Crm Cd 4'],axis=1)
    df =df.replace('',0.0)
    df = df.to_csv('crime_report_2010_to_2019225.csv')
    data = pd.read_csv('crime_report_2010_to_2019225.csv')
    X = data.drop(['Crm Cd 1'], axis = 1)
    Y = data['Crm Cd 1']
    Y = Y.values.reshape(-1, 1)
    day_index = 798
    days = [i for i in range(Y.size)]
    col_mask=data.isnull().any(axis=0)
    row_mask=data.isnull().any(axis=1)
    print(data)
    print(data.loc[row_mask,col_mask])
    clf = LinearRegression()
    clf.fit(X, Y)
    inp = np.array([[74], [60], [45], [67], [49], [43], [33], [45], 
                [57], [29.68], [10], [7], [2], [0], [20], [4], [31]]) 
    inp = inp.reshape(1, -1)
    #print('The precipitation of the crime for the input is:', clf.predict(inp))
    print("the crime precipitation trend graph: ") 
    plt.scatter(days, Y, color = 'g') 
    plt.scatter(days[day_index], Y[day_index], color ='r') 
    plt.title("Prediction level") 
    plt.xlabel("Days") 
    plt.ylabel("crime description") 
  
    plt.savefig("image8.png")
    plt.show()

def trainData():
    x_vis = X.filter(['TIME OCC', 'Rpt Dist No', 'Vict Age', 
                   'Weapon Used Cd', 'Premis Cd'], axis = 1)
    print("Crime description vs selected attributes graph: ") 
  
    for i in range(x_vis.columns.size):
        plt.subplot(3, 2, i + 1) 
        plt.scatter(days, x_vis[x_vis.columns.values[i][:100]], 
                                               color = 'g') 
  
        plt.scatter(days[day_index],  
                x_vis[x_vis.columns.values[i]][day_index], 
                color ='r') 
  
        plt.title(x_vis.columns.values[i]) 
    plt.savefig("image9.png")
    plt.show()

# live video recognition
def videoLoop(known_face_names, known_face_encodings):
    global thread_event, left_frame, webcam, img_label
    webcam = cv2.VideoCapture(0)
    old_recognized = []
    crims_found_labels = []
    img_label = None

    try:
        while not thread_event.is_set():
            # Loop until the camera is working
            while (True):
                # Put the image from the webcam into 'frame'
                (return_val, frame) = webcam.read()
                if (return_val == True):
                    break
                else:
                    print("Failed to open webcam. Trying again...")

            # Flip the image (optional)
            frame = cv2.flip(frame, 1, 0)
            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect Faces
            face_coords = detect_faces(gray_frame)
            (frame, names) = recognize_face(frame,known_face_names,known_face_encodings)

            # Recognize Faces
            recog_names = [item[0] for item in names]
            if(recog_names != old_recognized):
                for wid in right_frame.winfo_children():
                    wid.destroy()
                del(crims_found_labels[:])

                for i in range(len(names)):
                    crims_found_labels.append(tk.Label(right_frame, text=names[i], bg="orange",
                                            font="Arial 15 bold", pady=20))
                    crims_found_labels[i].pack(fill="x", padx=20, pady=10)
                    crims_found_labels[i].bind("<Button-1>", lambda e, name=names[i]:showCriminalProfile(name))

                old_recognized = recog_names

            # Display Video stream
            img_size = min(left_frame.winfo_width(), left_frame.winfo_height()) - 20

            showImage(frame, img_size)

    except RuntimeError:
        print("[INFO]Caught Runtime Error")
    except tk.TclError:
        print("[INFO]Caught Tcl Error")

# facebook matcher
def facebook_match():
#    import asd
    global img_read, img_label

    if(img_label == None):
        messagebox.showerror("Error", "No image selected. ")
        return

    crims_found_labels = []
    for wid in right_frame.winfo_children():
        wid.destroy()

    frame = cv2.flip(img_read, 1, 0)

    def data(cc):
        
        r = requests.get(cc)
        s = BeautifulSoup(r.text,"html.parser")
        p = s.find("meta",property ="og:image").attrs['content']
        with open("a"+".jpg","wb") as pic:
                binary = requests.get(p).content
                pic.write(binary)
 




    (known_face_names, known_face_encodings) = train_model()
    #unknown_image = face_recognition.load_image_file("img3.jpg")
    unknown_image = cv2.resize(frame,(500,500))
    face_locations = detect_faces(frame)

    (frame,name) = recognize_face(frame,known_face_names,known_face_encodings)
    #print(name)
           
            
    username=''
    password=''
    abc= ' '.join([str(elem) for elem in name])
    url='http://www.facebook.com/'

    driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    driver.get(url)
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_xpath('//button[@id="u_0_b"]').click()


    time.sleep(5)
    search = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/label/input')
    search.send_keys(abc,Keys.ENTER)





    i=0
    while(True):
            try:
                    action = webdriver.common.action_chains.ActionChains(driver)
                    a=action.move_to_element_with_offset(search,136,320)
                    time.sleep(3)
                    a.click()
                    action.click()
                    action.perform()
                    time.sleep(3)
            except:
                    action = webdriver.common.action_chains.ActionChains(driver)
                    a=action.move_to_element_with_offset(search,136,310)
                    time.sleep(3)
                    a.click()
                    action.click()
                    action.perform()
                    time.sleep(3)
            
            
            try:
                    driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t d2edcug0 rj1gh0hx buofh1pr g5gj957u hpfvmrgz dp1hu0rb']//"+"div"+"["+str(i)+"]"+"//div[1]//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//span[1]//div[1]//a[1]//span[1]").click()
                    print("enter the account")
                    time.sleep(3)
                    url = driver.current_url
                    data(url)
                    image = face_recognition.load_image_file("a.jpg")
                    image = cv2.resize(image,(500,500))
                    (frame,names) = recognize_face(image,known_face_names,known_face_encodings)
                    named = ' '.join([str(elem) for elem in names])
                    if named==abc:
                        copiedText = driver.find_element_by_class_name('sjgh65i0').text
                        xxx=driver.find_element_by_css_selector('#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div > div > div > div.d2edcug0.cbu4d94t.j83agx80.bp9cbjyn > div.rq0escxv.d2edcug0.ecyo15nh.hv4rvrfc.dati1w0a.tr9rh885 > div > div.rq0escxv.l9j0dhe7.du4w35lb.d2edcug0.o387gat7.buofh1pr.g5gj957u.hpfvmrgz.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5.rek2kq2y > div > div > div > div:nth-child(1) > div').text
                        print(copiedText)
                        zz='a'+str(".txt")
                        file_object  = open(str(zz),'w+')
                        file_object.write(xxx)
                        file_object.close()
                        file_object  = open(str(zz),'a')
                        file_object.write("\n"+url)
                        file_object.close()
                        print("scraping complete")
                        time.sleep(3)
                        # driver.execute_script("window.history.go(-1)")
                        # i+=1
                        driver.close()
                        file_object  = open("a.txt",'r')
                        img_read = cv2.imread("a.jpg")
                        lab = Label(right_frame,bg="#660033",text=file_object.read(),font="Helvetica 10 bold italic",fg ="yellow")
                        img_size = 200
                        showImage(img_read, img_size)
                        lab.pack()
                    else:
                        driver.execute_script("window.history.go(-1)")
                        i+=1
            except ElementNotInteractableException:
                driver.execute_script("window.history.go(-1)")
                i+=1
            except NoSuchElementException:
                driver.execute_script("0, 100*document.body.scrollHeight;")
                i+=1
            except AttributeError:
                driver.execute_script("window.history.go(-1)")
                i+=1
            except InvalidSessionIdException:
                print("Completed")


            
    f.close()

#twitter matcher
def twitter_match():
    global img_read, img_label

    if(img_label == None):
        messagebox.showerror("Error", "No image selected. ")
        return

    crims_found_labels = []
    for wid in right_frame.winfo_children():
        wid.destroy()

    frame = cv2.flip(img_read, 1, 0)

    def data(cc):
        
        r = requests.get(cc)
        s = BeautifulSoup(r.text,"html.parser")
        p = s.find("meta",property ="og:image").attrs['content']
        with open("a"+".jpg","wb") as pic:
                binary = requests.get(p).content
                pic.write(binary)
 




    (known_face_names, known_face_encodings) = train_model()
    #unknown_image = face_recognition.load_image_file("img3.jpg")
    unknown_image = cv2.resize(frame,(500,500))
    face_locations = detect_faces(frame)

    (frame,name) = recognize_face(frame,known_face_names,known_face_encodings)
    abc= ' '.join([str(elem) for elem in name])
    cc='https://twitter.com/search?q=%20'
    dd='%20'
    ee='&src=typed_query&f=user'
    zz=str(cc)+str(abc)+str(ee)
    print(zz)

    driver = webdriver.Chrome("/usr/local/bin/chromedriver")

    driver.get(zz)
    time.sleep(2)
    i=1
    j = 82
    while(True):
            location = driver.find_element_by_xpath("//body//div[@class='css-1dbjc4n']//div[@class='css-1dbjc4n']//div["+str(i)+"]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//a[1]//div[1]//div[1]//div[1]//span[1]//span[1]").location['y']
            size = driver.find_element_by_xpath("//body//div[@class='css-1dbjc4n']//div[@class='css-1dbjc4n']//div["+str(i)+"]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//a[1]//div[1]//div[1]//div[1]//span[1]//span[1]").size['height']
            #print(location)
            driver.find_element_by_xpath("//body//div[@class='css-1dbjc4n']//div[@class='css-1dbjc4n']//div["+str(i)+"]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//a[1]//div[1]//div[1]//div[1]//span[1]//span[1]").click()
            time.sleep(1)
            cc = driver.current_url
            #print(cc)
            driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div > div > div > div > div > div > div:nth-child(1) > div.css-1dbjc4n.r-ku1wi2.r-1j3t67a.r-m611by > div.css-1dbjc4n.r-obd0qt.r-18u37iz.r-1w6e6rj.r-1wtj0ep > a").click()
            time.sleep(1)
            driver.save_screenshot("profile_pic.png")
            driver.back()
            image = face_recognition.load_image_file("profile_pic.png")
            image = cv2.resize(image,(500,500))
            (frame,names) = recognize_face(image,known_face_names,known_face_encodings)
            named = ' '.join([str(elem) for elem in names])
            print(named)
            if named==abc:
                print("scrapping started")
                time.sleep(2)
                dd=driver.find_element_by_xpath("//div[@class='css-1dbjc4n r-ku1wi2 r-1j3t67a r-m611by']").text
                file_object  = open("output_twitter.txt",'w')
                file_object.write(dd)
                file_object.close()
                file_object  = open("output_twitter.txt",'a')
                file_object.write("\n"+cc)
                file_object.close()  
                time.sleep(2)
                print("scarapping complete")
                keyboard = Controller()

                #url= cc
                #driver = webdriver.Chrome("/usr/local/bin/chromedriver")

                #driver.get(url)

                time.sleep(2)
                dd=driver.find_element_by_xpath("//body").text
                print(dd)
                cc=str(dd)
                file_object  = codecs.open("output_twitter.txt","w","utf-8")
                file_object.write(cc)
                file_object.close()
                #driver.quit()
                reviews_train=[]
                #text3.txt
                file1 = open('output_twitter.txt',encoding="utf8")
                for line in file1:
                    reviews_train.append(line.strip())
                print("The train file look like is:")
                print(reviews_train[0:10])
                REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
                REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

                def preprocess_reviews(reviews):
                    reviews = [REPLACE_NO_SPACE.sub("", line.lower()) for line in reviews]
                    reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]
                    
                    return reviews

                reviews_train_clean = preprocess_reviews(reviews_train)
                negatives=[]
                neutrals=[]
                positives=[]
                sum1=0
                sum2=0
                sum3=0
                cont=0
                cont1=0
                cont2=0
                cont3=0
                n1=[]
                n2=[]
                n3=[]
                #print("\n the clean train file is:")
                #print(reviews_train_clean[:10])
                #print("The negative comments are:")
                for i in range(0,len(reviews_train_clean)):
                    blob1=TextBlob(reviews_train_clean[i])
                    et1,et2=blob1.sentiment
                    
                    if et1<0 and et1>=-1:
                        negatives.append(reviews_train_clean[i]+" "+str(et1))
                        sum1=sum1+et1
                        cont=cont+1
                        print(reviews_train_clean[i])
                        print("Polarity:{}".format(et1))
                        cont1=cont1+1
                        n1.append(et1)
                    elif et1==0:
                        neutrals.append(reviews_train_clean[i]+" "+str(et1))
                        sum2=sum2+et1
                        cont=cont+1
                        cont2=cont2+1
                        n2.append(et1)
                    else:
                        positives.append(reviews_train_clean[i]+" "+str(et1))
                        sum3=sum3+et1
                        cont=cont+1
                        cont3=cont3+1
                        n3.append(et1)


                tweets=[cont1,cont2,cont3]
                bars=['Violent','Neutral','Non-Violent']
                y_pos=np.arange(len(bars))
                plt.bar(y_pos,tweets,color=['red','blue','green'])
                plt.xticks(y_pos,bars)
                plt.xlabel("Classification of Tweet")
                plt.ylabel("Number of Tweet")
                plt.savefig("violence.png")
                driver.close()
                file_object  = open("output_twitter.txt",'r')
                img_read = cv2.imread("profile_pic.png")
                lab = Label(right_frame,bg="#660033",text=file_object.read(),font="Helvetica 10 bold italic",fg ="yellow")
                img_size = 200
                showImage(img_read, img_size)
                lab.pack()
                plt.show()
            driver.execute_script("window.history.go(-1)")
            driver.execute_script("window.scrollTo("+(str(location))+","+(str(j))+")")
            i = i+1
            j = j+82

def facebook():
    global active_page, left_frame, right_frame, img_label, heading
    img_label = None
    active_page = 2
    pages[2].lift()

    basicPageSetup(2)
    heading.configure(text="Detect Criminal")
    right_frame.configure(text="Detected Criminals")

    btn_grid = tk.Frame(left_frame, bg="#660033")
    btn_grid.pack()

    tk.Button(btn_grid, text="Select Image", command=selectImage, font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=0, column=0, padx=25, pady=25)
    #tk.Button(btn_grid, text="Recognize", command=startRecognition, font="Arial 15 bold", padx=20, bg="#2196f3",
           #fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
           #activeforeground="white").grid(row=0, column=1, padx=25, pady=25)
    tk.Button(btn_grid, text="facebook_match", command=facebook_match, font="Arial 15 bold", padx=20, bg="#2196f3",
           fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
           activeforeground="white").grid(row=0, column=1, padx=25, pady=25)
    tk.Button(btn_grid, text="twitter_match", command=twitter_match, font="Arial 15 bold", padx=20, bg="#2196f3",
           fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
           activeforeground="white").grid(row=0, column=2, padx=25, pady=25)


def showImage1(frame, img_size):
    global img_label, left_frame

    img = cv2.resize(frame, (img_size, img_size))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    if (img_label == None):
        img_label = tk.Label(right_frame, image=img, bg="#660033")
        img_label.image = img
        img_label.pack(padx=20)
    else:
        img_label.configure(image=img)
        img_label.image = img


def a1():
    import pp
    
def violence():
    global active_page, left_frame, right_frame, img_label, heading
    img_label = None
    active_page = 2
    pages[2].lift()

    basicPageSetup(2)
    heading.configure(text="Detect Criminal")
    right_frame.configure(text="Detected Criminals")

    btn_grid = tk.Frame(left_frame, bg="#660033")
    btn_grid.pack()
    
     
    img_read = cv2.imread("outputs/object-detection.jpg")
    img_size = 200
    showImage1(img_read, img_size)

    tk.Button(btn_grid, text="Select Video", command=selectvideos, font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=0, column=0, padx=25, pady=25)
    #tk.Button(btn_grid, text="Recognize", command=startRecognition, font="Arial 15 bold", padx=20, bg="#2196f3",
         #  fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
         #  activeforeground="white").grid(row=1, column=0, padx=25, pady=25)
    tk.Button(btn_grid, text="Recognize", command=a1, font="Arial 15 bold", padx=20, bg="#2196f3",
           fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
           activeforeground="white").grid(row=0, column=1, padx=25, pady=25)


## video surveillance Page ##
def getPage3():
    global active_page, video_loop, left_frame, right_frame, thread_event, heading
    active_page = 3
    pages[3].lift()

    basicPageSetup(3)
    heading.configure(text="Video Surveillance")
    right_frame.configure(text="Detected Criminals")
    left_frame.configure(pady=40)

    (known_face_names, known_face_encodings) = train_model()
    print('Training Successful. Detecting Faces')

    thread_event = threading.Event()
    thread = threading.Thread(target=videoLoop, args=(known_face_names, known_face_encodings))
    thread.start()


######################################## Home Page ####################################
tk.Label(pages[0], text="Criminal Identification System", fg="white", bg="#660033",
      font="Arial 35 bold", pady=30).pack()

logo = tk.PhotoImage(file = "logo.png")
tk.Label(pages[0], image=logo, bg="#660033").pack()

btn_frame = tk.Frame(pages[0], bg="#660033", pady=30)
btn_frame.pack()

tk.Button(btn_frame, text="Register Criminal", command=getPage1)
tk.Button(btn_frame, text="Detect Criminal", command=getPage2)
tk.Button(btn_frame, text="Video Surveillance", command=getPage3)
tk.Button(btn_frame, text="Social Media", command=facebook)
tk.Button(btn_frame, text="Crime Prediction", command=getPage6)
tk.Button(btn_frame, text="Violence Detection", command=violence)



for btn in btn_frame.winfo_children():
    btn.configure(font="Arial 20", width=15, bg="#000000", fg="white", 
        pady=-2, bd=0, highlightthickness=0, activebackground="#000000", activeforeground="red")
    btn.pack(pady=10)


pages[0].lift()
root.mainloop()
