# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:36:47 2022

@author: Zaid
"""

import NeuroPy
from threading import Thread
from time import time, sleep
from multiprocessing import Process
import csv
from itertools import zip_longest
from time import sleep
import pyautogui
import threading

#creating empty lists
attentionV = []
rawV = []
meditationV = []
lowalphaV = []
lowbetaV = []
lowgammaV = []
highalphaV = []
highbetaV = []
blinkV = []
X = []
Y = []
delta_x = []
delta_y = []
label = []

#headset socket connection
N=NeuroPy.NeuroPy.NeuroPy("COM7",57600)

#mouse movement function in 8 directions
def mouse():
    w = (pyautogui.size().width/2)-11
    h = (pyautogui.size().height/2)-11
    pyautogui.moveTo((pyautogui.size().width/2),(pyautogui.size().height/2))
    
    
    # up
    pyautogui.moveRel(0, -h, duration = 10)
    pyautogui.moveRel(0, h, duration = 10)
    # up-right
    pyautogui.moveRel(w, -h, duration = 10)
    pyautogui.moveRel(-w, h, duration = 10)
    # right
    pyautogui.moveRel(w, 0, duration = 10)
    pyautogui.moveRel(-w, 0, duration = 10)
    # down-right
    pyautogui.moveRel(w, h, duration = 10)
    pyautogui.moveRel(-w, -h, duration = 10)
    # down
    pyautogui.moveRel(0, h, duration = 10)
    pyautogui.moveRel(0, -h, duration = 10)
    # down-left
    pyautogui.moveRel(-w, h, duration = 10)
    pyautogui.moveRel(w, -h, duration = 10)
    # left
    pyautogui.moveRel(-w, 0, duration = 10)
    pyautogui.moveRel(w, 0, duration = 10)
    # up-right
    pyautogui.moveRel(-w, -h, duration = 10)
    pyautogui.moveRel(w, h, duration = 10)
    
def dataset_write():
    sleep(1.4)
    while t1.is_alive():
        sleep(0.8)
        
        #adding headset readings to the empty lists
        attentionV.append(N.attention)
        meditationV.append(N.meditation)
        lowalphaV.append(N.lowAlpha)
        lowbetaV.append(N.lowBeta)
        lowgammaV.append(N.lowAlpha)
        highalphaV.append(N.highAlpha)
        highbetaV.append(N.highBeta)
        blinkV.append(N.blinkStrength)
        x = pyautogui.position().x
        y = pyautogui.position().y
        X.append(x)
        Y.append(y)
        print (N.attention)

    #assigning directions (label) by comparing the coordinates of the next move            
    for i in range(1,len(X)):
        if X[i] > X[i-1] and Y[i] == Y[i-1]:
            label.append("Right")
        elif X[i] < X[i-1] and Y[i] == Y[i-1]:
            label.append("Left")
        elif Y[i] < Y[i-1] and X[i] == X[i-1]:
            label.append("Up")
        elif Y[i] > Y[i-1] and X[i] == X[i-1]:
            label.append("Down")
        elif Y[i] < Y[i-1] and X[i] > X[i-1]:
            label.append("Up-Right")
        elif Y[i] < Y[i-1] and X[i] < X[i-1]:
            label.append("Up-Left")
        elif Y[i] > Y[i-1] and X[i] > X[i-1]:
            label.append("Down-Right")
        elif Y[i] > Y[i-1] and X[i] < X[i-1]:
            label.append("Down-Left")
        elif Y[i] == Y[i-1] and X[i] == X[i-1]:
            label.append("No-Change")
            
            #adding list data to another list to be written in a csv file 
    data = [attentionV, meditationV,lowalphaV,lowbetaV,lowgammaV,highbetaV,highbetaV,X,Y,label]
    exp = zip_longest(*data, fillvalue='')
    with open(r'C:/Python39/Dataset1.csv', 'w', encoding='UTF8', newline='') as f:
         writer = csv.writer(f, quoting=csv.QUOTE_ALL)
         writer.writerow(("attention","meditation","lowAlpha","lowBeta","lowGamma","highAlpha","highBeta","X","Y","Direction"))
         writer.writerows(exp)
    f.close() 

#creating multi thread to call mouse function while taking the data from headset and adding it to the csv file
t1 = threading.Thread(target=mouse)
t2 = threading.Thread(target=dataset_write)

#starting both threads
t1.start()
t2.start()

#starting headset connection
N.start()






#print(len(meditationV))

    

#while True:
 #   print(x.attention)
#call start method

