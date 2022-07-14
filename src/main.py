from threading import local
from parinya import LINE
from datetime import date
import json
import time
import calendar
import cv2



class LineNotification:
    
    def __init__(self, token):
        self.token = token

    def sendText(self,text):
        user = LINE(self.token)
        user.sendtext("คาบนี้เรียน " + str(text))

    def findClass(self,day,time):
        for i in data[day]:
            if (i['time'] == time):
                self.sendText(i['name'])
            
        
    




##curr_date = date.today()
##print(calendar.day_name[curr_date.weekday()])

seconds = time.time()
local_time = time.ctime(seconds).split(' ')
Line = LineNotification("QY5wu14gVNJwHRFzDAytp47YkLw98GeuJ5jwkeeFwci")

with open('classes.json', 'r') as f:
    data = json.load(f)



while True:
    epochSeconds = time.time()
    local_time = time.ctime(epochSeconds).split(' ')
    print(local_time[3])
    Line.findClass(local_time[0],local_time[3])
    time.sleep(1)
       




#ink QY5wu14gVNJwHRFzDAytp47YkLw98GeuJ5jwkeeFwci
#smill UP6z8gDv4NBO9mVUfvKgJafRwVN9MpxwJTxw3VtaGZN