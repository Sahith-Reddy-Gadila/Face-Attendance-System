import cv2
import cv2.cv as cv
import sqlite3
import numpy as np
import sys
from datetime import *

from PIL import Image

import os

from Tkinter import *

root=Tk()

root.title("enter details")

root.configure(bg="#795548")


def insertOrUpdate(id,name):
    print id
    print name
    conn=sqlite3.connect("facebase.db")
    cmd="SELECT * FROM people WHERE ID="+str(id);
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if isRecordExist==1 :
        print "error"
    else :
        cmd="INSERT INTO people(id,Name) values("+str(id)+","+str(name)+")"
        conn.execute(cmd)
        conn.commit()
        conn.close()
        

    return id


def main_program(usd) :
 detector=cv2.CascadeClassifier('C:\Sahith PC\Education\Mini Project\Rough\MINIPP\haarcascade_frontalface_default.xml')
 cap=cv2.VideoCapture(0)
 offset=50
 sampleNum=0
 while (True):
            ret,img=cap.read()
            if ret==True:
                  gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                  faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
                  for (x,y,w,h) in faces:
                     
                    cv2.rectangle(img,(x-50,y-50),(x+w+50,y+h+50),(255,255,0),2)
                    sampleNum=sampleNum+1
                    cv2.imwrite("dataSet\User."+usd +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
    
                    cv2.imshow('Frame',img[y-offset:y+h+offset,x-offset:x+w+offset])
                    sampleNum =sampleNum+1
                  if cv2.waitKey(100) & 0xFF==ord('q'):
                      break
                  elif sampleNum>40 :
                   cap.release()
                   cv2.destroyAllWindows()
                   break
 print("Registered Successfully")                
 
def enter_the_value():

    usn=e1.get()
    print usn
    Name=e2.get()
    print Name
    insertOrUpdate(usn,Name)
    main_program(usn)

Label(root,text="Enter Student detail", font=("helvatica",40),bg="#F44336", fg="#0a0800").grid(rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="Enter USN: ",fg="#42A5F5",bg="#795548",font=("chiller",20)).grid(row=3,padx=5,pady=5,sticky=E)
e1=Entry(root)

e1.grid(row=2,rowspan=2,column=1)


Label(root, text="Enter Name: ",fg="#42A5F5",bg="#795548",font=("chiller",20)).grid(row=4,padx=5,pady=5,sticky=E)

e2=Entry(root)

e2.grid(row=3,rowspan=3,column=1)
#clear button
Button(root,text="CLEAR",bg="#00695C",font=("times new roman",25), command=root.quit).grid(row=5,columnspan=2,stick=E+W+N+S, pady=4)

#enter/submit button
Button(root,text="ENTER",bg="#00695C",font=("times new roman",25), command=enter_the_value).grid(row=6,columnspan=2,stick=W+E+N+S, pady=4)

root.mainloop()
