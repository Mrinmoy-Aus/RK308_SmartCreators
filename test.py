#input------>conected to opencv.py

lst=[1,1,1,1,1,0,0,0,1]
#replaced string
gun=lst[0]
bullets=lst[1]
blood=lst[2]
knifes=lst[3]
gloves=lst[4]
clothes=lst[5]
glass=lst[6]
dead_body=lst[7]
needles=lst[8]
string1=[int(gun),int(bullets),int(blood),int(knifes),int(gloves),int(clothes),int(glass),int(dead_body),int(needles)]

string=['gun','bullets','blood','knifes','gloves','clothes','glass','dead body','needles']

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
