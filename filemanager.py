from os.path import isfile, join, isdir
from os import listdir
import os

def getFiles(mypath):
    ret = []
    for f in listdir(mypath):
        current = join(mypath, f)
        if isdir(current):
            ret = ret + getFiles(current)
        elif isfile(current) and ".CAM" in current:
            ret.append(os.path.normpath(current))
    return ret

def main():
    files =  getFiles("Data")
    for a in files:
        f = open(a, "r")
        print(f.read())


if __name__ == '__main__':
    main()
