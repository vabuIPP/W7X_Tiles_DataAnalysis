from os.path import isfile, join, isdir
from os import listdir

def getFiles(mypath):
    ret = []
    for f in listdir(mypath):
        current = join(mypath, f)
        if isdir(current):
            ret = ret + getFiles2(current)
        elif isfile(current) and ".CAM" in current:
            ret.append(current)
    return ret

def main():
    files =  getFiles2("Data")
    for a in files:
        f = open(a, "r")
        print(f.read())


if __name__ == '__main__':
    main()
