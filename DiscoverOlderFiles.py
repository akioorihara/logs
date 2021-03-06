import datetime, os, time, stat, glob
from math import log2

currentTime = datetime.datetime.now()

def modi_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def check_the_diff(filename):
    v = datetime.datetime(2020, 4, 10)
    if  (currentTime - modi_date(filename) >= currentTime-v):
        #print("This file is oder than", currentTime - modi_date(filename))
        return True
    else:  
        #print(currentTime - modi_date(filename))
        return False

def file_size(size):
    _suffixes = ['bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
    order = int(log2(size) / 10) if size else 0
    return '{:.4g} {}'.format(size / (1 << (order * 10)), _suffixes[order])

#glob to scan through files within the GitHub folder 
pathDir = r"C:\Users\aorihara\Documents\GitHub"
for root, dirs, files in os.walk(pathDir):
    for file in files:
        if not file.startswith(".") and file.endswith(".txt"):
            x = os.path.join(root, file)
            if check_the_diff(x): #check if file is older than x date(s)
                print(x,file_size(os.stat(x).st_size))    
            else:
                #print(x)
                continue