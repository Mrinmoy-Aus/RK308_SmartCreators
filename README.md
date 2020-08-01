<img src="https://github.com/argho28/RK308_SmartCreators/blob/master/sih2020.png">

### Smart India Hackathon 2020 Grand Finale

### Team Name: SmartCreators
<img src="https://github.com/argho28/RK308_SmartCreators/blob/master/SmartCreators2020.png">

### Problem Statement
REAL-TIME BASED FACIAL RECOGNITION SYSTEMS

### Problem Statement Number: RK-308

### Organization
BUREAU OF POLICE RESEARCH & DEVELOPMENT

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)   

### Sourcerer
<a href="https://pralaysarkar.tk/"><img src="https://pralaysarkar.tk/assets/img/me.jpg" height="50px" width="50px" alt=""/></a>

### Code Requirements
- Opencv(`pip install opencv-contrib-python`)
- If you are using python3.x and opencv==4.1.0 then use following commands First of all
(`python -m pip install --user opencv-contrib-python`)
- Tkinter(Available in python)
- PIL (`pip install Pillow`)
- Pandas(`pip install pandas`)

### What steps you have to follow??
- Download my Repository 
- Create a `TrainingImage` folder in a project.
- Open a `AMS_Run.py` and change the all paths with your system path
- Run `AMS_Run.py`.

### Project Structure

- After run you need to give your face data to system so enter your ID and name in box than click on `Take Images` button.
- It will collect 200 images of your faces, it save a images in `TrainingImage` folder
- After that we need to train a model(for train a model click on `Train Image` button.
- It will take 5-10 minutes for training(for 10 person data).
- After training click on `Automatic Attendance` ,it can fill attendace by your face using our trained model (model will save in `TrainingImageLabel` )
- it will create `.csv` file of attendance according to time & subject.
- You can store data in database (install wampserver),change the DB name according to your in `AMS_Run.py`.
- `Manually Fill Attendace` Button in UI is for fill a manually attendance (without facce recognition),it's also create a `.csv` and store in a database.

### Screenshots

### Basic UI
<img src="https://github.com/PralaySarkar/Automatic-Attendance-Management-System/blob/master/1.PNG">

### Check register students
*Username: IIITK<br>
Password: iiit@20<br>*
<img src="https://github.com/PralaySarkar/Automatic-Attendance-Management-System/blob/master/2.PNG">

### Manually attendance filling UI
<img src="https://github.com/PralaySarkar/Automatic-Attendance-Management-System/blob/master/3.PNG">

### When it's Recognise me
<img src="https://github.com/PralaySarkar/Automatic-Attendance-Management-System/blob/master/4.PNG">

### When it's fill a attendace
<img src="https://github.com/PralaySarkar/Automatic-Attendance-Management-System/blob/master/5.PNG">



### How it works? See:)

<img src="https://github.com/PralaySarkar/Automatic-Attendance-Management-System/blob/master/AAMSgif.gif">


