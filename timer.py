import time 
import os
import datetime as dt 


ReunionDate = dt.datetime(2021,5,12, 20,00,00,0000000)
for i in range (20):    
    dateNow = dt.datetime.now()
    Reunionday = ReunionDate - dateNow
    print("Hey my beautiful baby it is only :")
    print(str(Reunionday) + " Until i get to hold my Beautiful Princess")
    print("I love you so so much \n")
    time.sleep(2)