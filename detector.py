import cv2,os
import numpy as np
from PIL import Image
import pickle
import sqlite3

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainer/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

def attent(Id):
    conn=sqlite3.connect("attendance.db")
    cmd="SELECT * FROM attend WHERE ID="+str(Id);
    cursor1=conn.execute(cmd)
    add=None
    for row in cursor1:
        add=1
    if add==1 :
      alredy=0
    else :
        cmd="INSERT INTO attend(id) values("+str(Id)+")"
        conn.execute(cmd)
        conn.commit()
        conn.close()
    return profile

def getProfile(id):
    conn=sqlite3.connect("facebase.db")
    cmd="SELECT * FROM people WHERE ID="+str(id);
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
        #img=cv2.imread('C:/Python27/faceRegconition-master/attendance-management-using-face-recognition/face/temp/4.jpg')
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
      
             cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
             Id,conf =recognizer.predict(gray[y:y+h,x:x+w])
             if conf<60 :
              profile=getProfile(Id)
              if(profile!=None):
                  attent(Id)
                  cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[0]),(x,y+h+30),font,255)
                  cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[1]),(x,y+h+60),font,255)       
             cv2.imshow('im',im)
        
             if cv2.waitKey(10) & 0xFF==ord('q'):
               break
cam.release()
cv2.destroyAllWindows()

Label(root,text="Enter Student detail", font=("helvatica",40),bg="#F44336", fg="#0a0800").grid(rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="Enter USN: ",fg="#42A5F5",bg="#795548",font=("chiller",20)).grid(row=3,padx=5,pady=5,sticky=E)

e1=Entry(root)

e1.grid(row=3,rowspan=2,column=1)

Label(root, text="Enter Time: ",fg="#42A5F5",bg="#795548",font=("chiller",20)).grid(row=3,padx=5,pady=5,sticky=E)

e2=Entry(root)

e2.grid(row=3,rowspan=2,column=1)
#clear button
Button(root,text="CLEAR",bg="#00695C",font=("times new roman",25), command=root.quit).grid(row=5,columnspan=2,stick=E+W+N+S, pady=4)

#enter/submit button
Button(root,text="ENTER",bg="#00695C",font=("times new roman",25), command=enter_the_value).grid(row=6,columnspan=2,stick=W+E+N+S, pady=4)

root.mainloop()

