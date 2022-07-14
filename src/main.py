from lib2to3.pgen2 import token
from threading import local
from parinya import LINE # LINE API module Line "parinya"
import json # database
import time # import เวลา
#import calendar ไม่ต้องใช้
import cv2
import keyboard
import sys





class LineNotification:
    
    def __init__(self,token):
        self.token = token
        
    def sendText(self,text):
        user = LINE(self.token)
        user.sendtext("คาบนี้เรียน " + str(text))

    def findClass(self,day,time):
        for i in data[day]:
            if (i['time'] == time):
                self.sendText(i['name'])

    def setToken(self, token):
        self.token = token

    def clear(self):
        self.token = None
        


tokenin = input("Enter your Line token : ")

Line = LineNotification(tokenin)


with open('classes.json', 'r') as classes:
    data = json.load(classes)




#main program
while True:
    epochSeconds = time.time()
    local_time = time.ctime(epochSeconds).split(' ')
    print(local_time[3])
    Line.findClass(local_time[0],local_time[3])
    time.sleep(1)
    if keyboard.is_pressed('j'):
        while True:
            if keyboard.is_pressed('k'):
                time.sleep(1)
                break;
    
    if keyboard.is_pressed('esc'):
        sys.exit("Execute program")
    
       




#ink QY5wu14gVNJwHRFzDAytp47YkLw98GeuJ5jwkeeFwci
#smill UP6z8gDv4NBO9mVUfvKgJafRwVN9MpxwJTxw3VtaGZN