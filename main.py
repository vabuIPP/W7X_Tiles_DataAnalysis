from fitfactory import FitFactory
import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
from win32com.client import Dispatch
import scipy.optimize as sciopt
import scipy.stats as scistat
import filemanager as fm

def getFiles(path):
    aux = os.listdir(path)
    ret = []
    for c in aux:
        if (".CAM" in c):
            ret.append(os.path.normpath(path+"\\"+c))
    return ret

def fitSimFit(param):
	SimFit.SetRegionMinChannel('SetRegionMinChannel')

def fitSimFitFluence(file):
	SimApp = Dispatch("Simnra.App") #opening OLE object
	SimSpec = Dispatch("Simnra.Spectrum")
	SimSet = Dispatch("Simnra.Setup")
	SimFit = Dispatch("Simnra.Fit")
	SimTar = Dispatch("Simnra.Target")

	SimApp.OpenAs(file, 2)

	SimTar.ReadTarget('./fullC.xtarget')

	#set fit parameters
	SimFit.Chi2Evaluation = 1
	SimFit.Accuracy = 0.001
	SimFit.MaxIterations = 1000
	SimFit.ParticlesSr = 'true'
	SimFit.NumberOfRegions = 1
	SimFit.SetRegionMinChannel(1, 200)
	SimFit.SetRegionMaxChannel(1, 350)

	SimApp.FitSpectrum()
	newFile = os.path.normpath(file[0:-5]+'_fitted_fluence.xnra')
	SimApp.SaveAs(newFile)

	del SimApp, SimSpec, SimSet, SimFit, SimTar
	return newFile

def camToXnra(file, template):
	SimApp = Dispatch("Simnra.App") #opening OLE object
	#print file
	SimApp.Open(template, FileType = 2)
	SimApp.ReadSpectrumData(file,2)
	output_loc = str(os.path.normpath(file.replace('.CAM','')))
	newFile = output_loc + '.xnra'
	SimApp.SaveAs(newFile)

	del SimApp
	return newFile

def main():
	#files = [os.path.normpath('C:\Users\\vabu\Documents\GitHub\W7X_Tiles_DataAnalysis\Data\\2018-05-09.vabu\\BOM_165\\107#004.CAM')]
	files = fm.getFiles('\\\\AFS\\ipp\\home\\m\\mguitart\\HIWI\\fittings\\auto_test')
	template = os.path.normpath("C:\\Users\\mguitart\\Documents\\GitHub\\W7X_Tiles_DataAnalysis\\template.xnra")
	for f in files:
		xnraFile = camToXnra(f, template)
        fitFluenceFile = fitSimFitFluence(xnraFile)
        print "Break point"
        print fitFluenceFile
        ffactory = FitFactory()
        ffactory.buildCriteria(fitFluenceFile)
        node = ffactory.decideCase(f)
        print node
        for param in node.params:
			fitSimFit(param)
			#TODO implement each fit process

if __name__ == '__main__':
	main()
