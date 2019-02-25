import sys
import os
#import raw_input
import numpy as np
import custom as cs
from win32com.client import Dispatch
import filemanager as fm


def getSpectra(path):
	aux = os.listdir(path)
	ret = []
	for c in aux:
		if (".CAM" in c):
			ret.append(path+"\\"+c)
	return ret

def getSpectrumFile(path):
	return fm.getFiles(path)

def applyFit(app, fit, cspect, params):

	app.ReadSpectrumData(cspect, 2)

	fit.ParticlesSr = params["particles"]
	fit.LayerThickness = params["thickness"]
	fit.LayerRoughness = params["roughness"]

	fit.LayerNr = params["layer"]

	fit.NumberOfRegions = params["number_regions"]

	for i in range(len(params["regions_values"])):
		reg = params["regions_values"][i]
		#print reg
		fit.SetRegionMaxChannel(i+1, reg["max"])
		fit.SetRegionMinChannel(i+1, reg["min"])

	print app.FileName
	a = app.FitSpectrum()
	print a

def camToXnra(file, template):
	SimApp = Dispatch("Simnra.App") #opening OLE object
	#print file
	SimApp.Open(template, FileType = 2)
	SimApp.ReadSpectrumData(file,2)
	output_loc = str(os.path.normpath(file.replace('.CAM','')))
	newFile = output_loc + '_template.xnra'
	SimApp.SaveAs(newFile)

	del SimApp
	return newFile

def buildCriteria(app, spectrum, file, lowC, upC):
	print file
	a = app.OpenAs(file, 2)
	print a
	experimental_spectrum = np.asarray(spectrum.DataArray(1))
	#grads = fm.getNPGradients(experimental_spectrum)
	x = np.linspace(1,len(experimental_spectrum),len(experimental_spectrum))
	experimental_spectrum_segment = cs.spline_bayesian(x,experimental_spectrum)
	min_val = np.argmin(experimental_spectrum[lowC:upC])
	max_val = np.argmax(experimental_spectrum[lowC:upC])
	channel_dip = lowC + min_val
	channel_max = lowC + max_val
	## Classification
	surface_Mo = np.sum(experimental_spectrum[805:810])
	# Has C layer been fully sputtered (Y/N)
	min = lowC+25
	max = upC

	Int_Exp = spectrum.Integrate(1,min,max)
	Int_Sim = spectrum.Integrate(2,min,max)
	#print Int_Exp
	#print Int_Sim
	decision_coeff = Int_Exp / Int_Sim

	return surface_Mo, decision_coeff, channel_dip, channel_max

def MoEstimator(spec, minMo,maxMo):
	integratedExperimentalMoSpectrum = spec.Integrate(1,minMo,maxMo)
	print integratedExperimentalMoSpectrum
	m = 0.092
	c = 20
	Mo_estimator = integratedExperimentalMoSpectrum * m - c
	return Mo_estimator

def buildTest(path):
	arr = path.split("\\")[0:-1]
	return '\\'.join([str(x) for x in arr])+"\\test.xnra"

def doFit(template, spec_data):
	app = Dispatch("Simnra.App") # The SimNRA app instance
	target = Dispatch("Simnra.Target") # The SimNRA target instance
	spectrum = Dispatch("Simnra.Spectrum") # The current SimNRA calculated/experimental spectrum
	setup = Dispatch("Simnra.Setup")
	fit = Dispatch("Simnra.Fit")
	app.Show()

	# If you want to apply the fit to a set .CAM into a folder, use getSpectra functions. In the other hand, if you only want to apply
	# to a single .CAM file, use getSpectrum file. To change it, just comment one function and use the other.
	#spects = getSpectra(spec_data)
	spects = getSpectrumFile(spec_data)

	for spec in spects:
		print "New fitting at "+spec
		if fm.checkFile(buildTest(spec)):
			ctemplate = buildTest(spec)
		else:
			ctemplate = template
		print "Using: "+ctemplate
		fit_file = camToXnra(spec, ctemplate)
		# Load template
		r = app.Open(fit_file, FileType = 2) # File format 2 is format .xnra
		#print spec

		print "Fitting 1"
		min= 200
		#max = int(raw_input("Enter the maximum"))
		max = 350

		applyFit(app, fit, spec, { "particles": True, "thickness": False, "roughness": False, "layer": 1, "number_regions": 1, "regions_values": [{"min": min, "max":max}]})

		minimum = buildCriteria(app, spectrum, fit_file, 400, 600)

		#print "Layer Thickness of Carbon layer. Min and max value for the first carbon layer and min and max also for the tungsten platform"
		print "Fitting 2"
		min1 = minimum[2]+45 #int(raw_input("Enter the minimum of first region"))
		if min1 > 600:
			min1 = 550
		max1 = 600 #nt(raw_input("Enter the maximum of first region"))

		applyFit(app, fit, spec, { "particles": True, "thickness": False, "roughness": False, "layer": 1, "number_regions": 1, "regions_values": [{"min": min1, "max":max1}]})
		#print minimum
		#print "Layer Thickness of Carbon layer. Min and max value for the first carbon layer and min and max also for the tungsten platform"
		print "Fitting 3"
		tu = buildCriteria(app, spectrum, fit_file, 650, 800)
		min1 = minimum[2] #int(raw_input("Enter the minimum of first region"))
		max1 = 650 #nt(raw_input("Enter the maximum of first region"))
		min2 = tu[3]
		max2 = 830
		print "Max "+str(min2)
		applyFit(app, fit, spec, { "particles": False, "thickness": True, "roughness": False, "layer": 1, "number_regions": 2, "regions_values": [{"min": min1, "max":max1}, {"min":min2,"max":max2}]})

		print "Fitting 4"
		min1 = 650
		max1 = 750
		applyFit(app, fit, spec, { "particles": False, "thickness": True, "roughness": False, "layer": 2, "number_regions": 1, "regions_values": [{"min": min1, "max":max1}]})

		print "Fitting 5"
		min1 = minimum[2]
		max1 = minimum[2] + 45
		min2 = tu[3]
		max2 = 760
		applyFit(app, fit, spec, { "particles": False, "thickness": True, "roughness": True, "layer": 1, "number_regions": 2, "regions_values": [{"min": min1, "max":max1}, {"min":min2,"max":max2}]})

		print "Fitting 6"
		min1 = minimum[2] - 45
		max1 = minimum[2]
		min2 = 650
		max2 = 800
		applyFit(app, fit, spec, { "particles": False, "thickness": True, "roughness": True, "layer": 2, "number_regions": 2, "regions_values": [{"min": min1, "max":max1}, {"min":min2,"max":max2}]})

		print "Fitting 2: to be pretty"
		min1 = minimum[2]+45 #int(raw_input("Enter the minimum of first region"))
		if min1 > 600:
			min1 = 550
		max1 = 600 #nt(raw_input("Enter the maximum of first region"))

		applyFit(app, fit, spec, { "particles": True, "thickness": False, "roughness": False, "layer": 1, "number_regions": 1, "regions_values": [{"min": min1, "max":max1}]})
		#Mo_estimator = MoEstimator(spectrum, 620, 780)
		#caca = target.SetElementAmount(1, 2, Mo_estimator)
		#print caca
		#print "Mo_estimator: "+str(Mo_estimator)
		#print "Layer Thickness of Molibdenium. Min and max value for left and right hand side of peak"
		#min = 650 #int(raw_input("Enter the minimum"))
		#max = 750 #int(raw_input("Enter the maximum"))
		#applyFit(app, fit, spec, { "particles": False, "thickness": True, "roughness": False, "layer": 2, "number_regions": 1, "regions_values": [{"min": min, "max": max}]})

		app.SaveAs(spec[0:-4]+"_auto.xnra") # spec is a string, i.e. array of chars, and tells it to save it with the same name form position 0 to position n-1 (so it removes the xnra)

def main():

	fit_file = "C:\\Users\\mguitart\\Documents\\GitHub\\W7X_Tiles_DataAnalysis\\template1.xnra"

	#spec_data =  os.path.normpath('\\\\AFS\\ipp\\home\\m\\mguitart\\HIWI\\fittings\\')
	spec_data =  os.path.normpath('\\\\AFS\\ipp\\home\\m\\mguitart\\HIWI\\test_fittings\\single_test\\')
	doFit(fit_file, spec_data)


if __name__== "__main__": #sentence to apply the code. Mo more relevance

  main()
