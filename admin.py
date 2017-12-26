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
def function1():
    
    os.system("python info2.py")
    
def function2():
    
    os.system("python trainer.py")


Button(root,text="REGISTER",font=("times new roman",30),bg="#3F51B5",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="TRAIN_IMAGES",font=("times new roman",30),bg="#3F51B5",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
