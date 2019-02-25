from os.path import isfile, join, isdir
from os import listdir
import os
import sys

def getFiles(mypath):
    ret = []
    for f in listdir(mypath):
        current = join(mypath, f)
        if isdir(current):
            ret = ret + getFiles(current)
        elif isfile(current) and ".CAM" in current:
            ret.append(os.path.normpath(current))
    return ret

def getGradients(arr):
    print arr
    ret = []
    act = 0
    tend = "up"
    candidate = 0
    top = 10
    count = 0
    cc = 0
    print str(len(arr))
    for a in arr:
        if "up" in tend:
            if a < act:
                act = a
                count += 1
            else:
                candicate = cc
                act = a
                count = 0
            if count >= top:
                ret.append(candidate)
                count = 0
                tend = "down"
        elif "down" in tend:
            if a > act:
                act = a
                count += 1
            else:
                candidate = cc
                act = a
                count = 0
            if count >= top:
                ret.append(candicate)
                count = 0
                tend = "up"
        cc+=1
    print ret
    #sys.exit()
    return ret

def main():
    files =  getFiles("Data")
    for a in files:
        f = open(a, "r")
        print(f.read())


if __name__ == '__main__':
    main()
