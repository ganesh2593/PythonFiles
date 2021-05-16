from datetime import datetime

currentTime = datetime.now()
print(currentTime)
print(type(currentTime))

modifiedTime = currentTime.replace(microsecond = 0)
print(modifiedTime)

#2021-05-05 19:23:38
#%Y-%m-%d %H:%M:%S

myFormat = "%y_%m_%d_%H_%M_%S"

convertedTime=datetime.strftime(modifiedTime,myFormat)
print(convertedTime)

import tkinter
from tkinter import filedialog
import os
root = tkinter.Tk()
root.withdraw()
path = filedialog.askdirectory()
print(path)
fileName ="project2" + convertedTime + ".txt"
finalPath = os.path.join(path,"project2.txt")
with open(finalPath,"a") as fileObj:
    fileObj.write("welcome to my page")
