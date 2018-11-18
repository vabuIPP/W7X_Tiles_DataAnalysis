import subprocess as subp
import numpy as np
import os
import sys
import struct
from win32com.client import Dispatch

def spline_bayesian(x,y):
    ''' Bayesian Spline - takes x vs y plot and smoothes it.
    Uses a c code provided by Udo v.T. '''

    ## prepare input files 
    # pointer file

    fileID = open('input.dat','w')
    fileID.write('feedingUdosSpline1.dat \n '+ str(x[0]) +' '+str(x[-1])+'\n feedingUdosSpline2.dat')
    fileID.close()

    # x y Deltay to be fitted
    Dy = []
    for y_i in y:
        if y_i < 1: 
            Dy.append(1)
        else:
            Dy.append(np.sqrt(y_i))

    f = open('feedingUdosSpline1.dat','w')
    i = 0
    while i < len(x):
        f.write(str(x[i]) +' '+ str(y[i]) +' '+ str(Dy[i])+'\n')
        i += 1
    f.close()


    # desired x points
    f = open('feedingUdosSpline2.dat','w')
    for x_i in x:
        f.write(str(x_i)+'\n')
    f.close()
	# hide output
    FNULL = open(os.devnull, 'w')
    # calling udos code
    subp.call('temperature_calibration_03.exe', stdout=FNULL, stderr=subp.STDOUT)
    
	#reimporting the result
    f_cal  = open('calibrated_data.dat','r')
    data = f_cal.readlines()
    
    x_smooth = []
    y_smooth = []
    for line in data:
        values = line.split(' ')
        
        x_smooth.append(float(values[0]))
        y_smooth.append(float(values[1]))
		
    f_cal.close()

    return y_smooth
	

def read_coordinates(path):

	#variables
    ErrorOccured = False
    emptyString = ' '*63
    FileName = path

	#begin
    CAMReadObject = Dispatch("CanberraReadObject.CAMReadObject") #opening OLE object
    if CAMReadObject == None:
        ErrorOccured = True

    #{ Open the file }
    if CAMReadObject.OpenFileDataSource(FileName) != True:
       ErrorOccured = True

    StringToRead = 536936472 # insert in as hexadecimal
    test = CAMReadObject.GetParam_String(StringToRead, emptyString, len(emptyString))

    if test == None:
        ErrorOccured = True

    temp = str(test[1:])
    s = temp[3:-3]
    #print s
    coordinates = s.split(' ')
    coord_x = float(coordinates[0])
    coord_y = float(coordinates[1])
    coord_rot = float(coordinates[2])
    temp_z = coordinates[3]
    end_z = temp_z.find('\\')
    coord_z = float(coordinates[3][0:end_z])

    #{ Close data source and dispose libraries }
    CAMReadObject.CloseFileDataSource();

    #{ Delete CAMReadObject }
    del CAMReadObject

    return coord_x, coord_y, coord_z, coord_rot, ErrorOccured