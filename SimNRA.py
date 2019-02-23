# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# From type library 'Simnra.tlb'
# On Tue Jan 16 13:28:30 2018
'Simnra Library'
makepy_version = '0.5.01'
python_version = 0x2070af0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{9F51F4E0-754F-11D5-B742-0040332FCEB4}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IApp(DispatchBaseClass):
	'Dispatch interface for App Object'
	CLSID = IID('{9F51F4E1-754F-11D5-B742-0040332FCEB4}')
	coclass_clsid = IID('{9F51F4E3-754F-11D5-B742-0040332FCEB4}')

	def BringToFront(self):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	def BringToRear(self):
		return self._oleobj_.InvokeTypes(205, LCID, 1, (24, 0), (),)

	def CalculateDualScatteringBackground(self, AddToSpectrum=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(221, LCID, 1, (11, 0), ((11, 1),),AddToSpectrum
			)

	def CalculatePileup(self):
		return self._oleobj_.InvokeTypes(220, LCID, 1, (11, 0), (),)

	def CalculateSpectrum(self):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	def CalculateSpectrumFast(self):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), (),)

	def CalculateSpectrumToDepth(self, Depth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), ((5, 1),),Depth
			)

	def CopySpectrumData(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def CreateListOfCrSecs(self):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), (),)

	def FitSpectrum(self):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), (),)

	def Hide(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def Maximize(self):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), (),)

	def Minimize(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	def Open(self, FileName=defaultNamedNotOptArg, FileType=-1):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((8, 1), (3, 33)),FileName
			, FileType)

	def OpenAs(self, FileName=defaultNamedNotOptArg, FileType=-1):
		return self._oleobj_.InvokeTypes(202, LCID, 1, (11, 0), ((8, 1), (3, 49)),FileName
			, FileType)

	def OpenStream(self, Stream=defaultNamedNotOptArg, FileType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(208, LCID, 1, (11, 0), ((13, 1), (3, 1)),Stream
			, FileType)

	def ReadSpectrumData(self, FileName=defaultNamedNotOptArg, Format=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((8, 1), (3, 1)),FileName
			, Format)

	def Reset(self):
		return self._oleobj_.InvokeTypes(211, LCID, 1, (24, 0), (),)

	def ResizeSpectrum(self, NumChannels=defaultNamedNotOptArg, ResizeCalibration=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(216, LCID, 1, (24, 0), ((3, 1), (11, 1)),NumChannels
			, ResizeCalibration)

	def Restore(self):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	def SaveAs(self, FileName=defaultNamedNotOptArg, FileType=2):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((8, 1), (3, 49)),FileName
			, FileType)

	def SaveThumbnailAs(self, FileName=defaultNamedNotOptArg, Width=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(201, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, Width)

	def Show(self):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

	def Standalone(self):
		return self._oleobj_.InvokeTypes(204, LCID, 1, (11, 0), (),)

	def WriteSpectrumData(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((8, 1),),FileName
			)

	_prop_map_get_ = {
		"Active": (10, 2, (11, 0), (), "Active", None),
		"BorderStyle": (217, 2, (3, 0), (), "BorderStyle", None),
		"CalculatingSpectrum": (19, 2, (11, 0), (), "CalculatingSpectrum", None),
		"DeleteSpectrumOnCalculate": (14, 2, (11, 0), (), "DeleteSpectrumOnCalculate", None),
		"FileName": (21, 2, (8, 0), (), "FileName", None),
		"Height": (26, 2, (3, 0), (), "Height", None),
		"IncidentIonEnergyIsZero": (209, 2, (11, 0), (), "IncidentIonEnergyIsZero", None),
		"LastMessage": (16, 2, (8, 0), (), "LastMessage", None),
		"Left": (23, 2, (3, 0), (), "Left", None),
		"LegendOutsideOfChart": (206, 2, (11, 0), (), "LegendOutsideOfChart", None),
		"LegendVisible": (203, 2, (11, 0), (), "LegendVisible", None),
		"MenuVisible": (213, 2, (11, 0), (), "MenuVisible", None),
		"OLEUser": (218, 2, (8, 0), (), "OLEUser", None),
		"SRIMDirectory": (219, 2, (8, 0), (), "SRIMDirectory", None),
		"ShowMessages": (15, 2, (11, 0), (), "ShowMessages", None),
		"SpectrumChanged": (20, 2, (11, 0), (), "SpectrumChanged", None),
		"StatusbarVisible": (214, 2, (11, 0), (), "StatusbarVisible", None),
		"ToolbarVisible": (212, 2, (11, 0), (), "ToolbarVisible", None),
		"Top": (25, 2, (3, 0), (), "Top", None),
		"TopAxisCaption": (207, 2, (8, 0), (), "TopAxisCaption", None),
		"Version": (27, 2, (8, 0), (), "Version", None),
		"Visible": (210, 2, (11, 0), (), "Visible", None),
		"Width": (24, 2, (3, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"BorderStyle": ((217, LCID, 4, 0),()),
		"CloseButtonEnabled": ((222, LCID, 4, 0),()),
		"ControlsVisible": ((215, LCID, 4, 0),()),
		"DeleteSpectrumOnCalculate": ((14, LCID, 4, 0),()),
		"Height": ((26, LCID, 4, 0),()),
		"IncidentIonEnergyIsZero": ((209, LCID, 4, 0),()),
		"Left": ((23, LCID, 4, 0),()),
		"LegendOutsideOfChart": ((206, LCID, 4, 0),()),
		"LegendVisible": ((203, LCID, 4, 0),()),
		"MenuVisible": ((213, LCID, 4, 0),()),
		"OLEUser": ((218, LCID, 4, 0),()),
		"SRIMDirectory": ((219, LCID, 4, 0),()),
		"ShowMessages": ((15, LCID, 4, 0),()),
		"SpectrumChanged": ((20, LCID, 4, 0),()),
		"StatusbarVisible": ((214, LCID, 4, 0),()),
		"ToolbarVisible": ((212, LCID, 4, 0),()),
		"Top": ((25, LCID, 4, 0),()),
		"TopAxisCaption": ((207, LCID, 4, 0),()),
		"Width": ((24, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ICalc(DispatchBaseClass):
	CLSID = IID('{9DD33B20-A8EC-11D5-B749-0040332FCEB4}')
	coclass_clsid = IID('{9DD33B22-A8EC-11D5-B749-0040332FCEB4}')

	_prop_map_get_ = {
		"Accuracy": (207, 2, (3, 0), (), "Accuracy", None),
		"AutoStepwidthIn": (8, 2, (11, 0), (), "AutoStepwidthIn", None),
		"AutoStepwidthOut": (9, 2, (11, 0), (), "AutoStepwidthOut", None),
		"CalculateToEMin": (208, 2, (11, 0), (), "CalculateToEMin", None),
		"CreateSpectrum": (21, 2, (11, 0), (), "CreateSpectrum", None),
		"CreateSpectrumFromLayerNr": (206, 2, (3, 0), (), "CreateSpectrumFromLayerNr", None),
		"CrossSecStraggling": (201, 2, (3, 0), (), "CrossSecStraggling", None),
		"DualScattering": (6, 2, (11, 0), (), "DualScattering", None),
		"DualScatteringRoughness": (203, 2, (3, 0), (), "DualScatteringRoughness", None),
		"ElementSpectra": (12, 2, (11, 0), (), "ElementSpectra", None),
		"Emin": (3, 2, (5, 0), (), "Emin", None),
		"HighEnergyStopping": (15, 2, (11, 0), (), "HighEnergyStopping", None),
		"IsotopeSpectra": (13, 2, (11, 0), (), "IsotopeSpectra", None),
		"Isotopes": (5, 2, (11, 0), (), "Isotopes", None),
		"LogFile": (20, 2, (11, 0), (), "LogFile", None),
		"MultipleScattering": (7, 2, (11, 0), (), "MultipleScattering", None),
		"NuclearStoppingModel": (205, 2, (3, 0), (), "NuclearStoppingModel", None),
		"NumberOfAngleVariations": (11, 2, (3, 0), (), "NumberOfAngleVariations", None),
		"NumberOfDVariations": (10, 2, (3, 0), (), "NumberOfDVariations", None),
		"PUModel": (19, 2, (3, 0), (), "PUModel", None),
		"ScreeningModel": (18, 2, (3, 0), (), "ScreeningModel", None),
		"StoppingModel": (204, 2, (3, 0), (), "StoppingModel", None),
		"Straggling": (4, 2, (11, 0), (), "Straggling", None),
		"StragglingModel": (17, 2, (3, 0), (), "StragglingModel", None),
		"StragglingShape": (202, 2, (3, 0), (), "StragglingShape", None),
		"SubstrateRoughnessDimension": (16, 2, (3, 0), (), "SubstrateRoughnessDimension", None),
		"ZBStopping": (14, 2, (11, 0), (), "ZBStopping", None),
		"dEin": (1, 2, (5, 0), (), "dEin", None),
		"dEout": (2, 2, (5, 0), (), "dEout", None),
	}
	_prop_map_put_ = {
		"AutoStepwidthIn": ((8, LCID, 4, 0),()),
		"AutoStepwidthOut": ((9, LCID, 4, 0),()),
		"CalculateToEMin": ((208, LCID, 4, 0),()),
		"CreateSpectrum": ((21, LCID, 4, 0),()),
		"CreateSpectrumFromLayerNr": ((206, LCID, 4, 0),()),
		"CrossSecStraggling": ((201, LCID, 4, 0),()),
		"DualScattering": ((6, LCID, 4, 0),()),
		"DualScatteringRoughness": ((203, LCID, 4, 0),()),
		"ElementSpectra": ((12, LCID, 4, 0),()),
		"Emin": ((3, LCID, 4, 0),()),
		"HighEnergyStopping": ((15, LCID, 4, 0),()),
		"IsotopeSpectra": ((13, LCID, 4, 0),()),
		"Isotopes": ((5, LCID, 4, 0),()),
		"LogFile": ((20, LCID, 4, 0),()),
		"MultipleScattering": ((7, LCID, 4, 0),()),
		"NuclearStoppingModel": ((205, LCID, 4, 0),()),
		"NumberOfAngleVariations": ((11, LCID, 4, 0),()),
		"NumberOfDVariations": ((10, LCID, 4, 0),()),
		"PUModel": ((19, LCID, 4, 0),()),
		"ScreeningModel": ((18, LCID, 4, 0),()),
		"StoppingModel": ((204, LCID, 4, 0),()),
		"Straggling": ((4, LCID, 4, 0),()),
		"StragglingModel": ((17, LCID, 4, 0),()),
		"StragglingShape": ((202, LCID, 4, 0),()),
		"SubstrateRoughnessDimension": ((16, LCID, 4, 0),()),
		"ZBStopping": ((14, LCID, 4, 0),()),
		"dEin": ((1, LCID, 4, 0),()),
		"dEout": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ICrossSec(DispatchBaseClass):
	CLSID = IID('{1C467EA5-494F-4FA4-A305-84183157CC48}')
	coclass_clsid = IID('{504EF515-68CF-495D-8D7C-C132E538D839}')

	# The method Choose is actually a property, but must be used as a method to correctly pass the arguments
	def Choose(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(208, LCID, 2, (11, 0), ((3, 1),),Index
			)

	# The method EMax is actually a property, but must be used as a method to correctly pass the arguments
	def EMax(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(211, LCID, 2, (5, 0), ((3, 1),),Index
			)

	def ERDRutherford(self, Z1=defaultNamedNotOptArg, M1=defaultNamedNotOptArg, Z2=defaultNamedNotOptArg, M2=defaultNamedNotOptArg
			, E=defaultNamedNotOptArg, Phi=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (5, 0), ((3, 1), (5, 1), (3, 1), (5, 1), (5, 1), (5, 1)),Z1
			, M1, Z2, M2, E, Phi
			)

	# The method Emin is actually a property, but must be used as a method to correctly pass the arguments
	def Emin(self, Index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(210, LCID, 2, (5, 0), ((3, 1),),Index
			)

	# The method FileName is actually a property, but must be used as a method to correctly pass the arguments
	def FileName(self, Index=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(207, LCID, 2, (8, 0), ((3, 1),),Index
			)

	# The method Info is actually a property, but must be used as a method to correctly pass the arguments
	def Info(self, Index=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(209, LCID, 2, (8, 0), ((3, 1),),Index
			)

	def RBSRutherford(self, Z1=defaultNamedNotOptArg, M1=defaultNamedNotOptArg, Z2=defaultNamedNotOptArg, M2=defaultNamedNotOptArg
			, E=defaultNamedNotOptArg, Theta=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (5, 0), ((3, 1), (5, 1), (3, 1), (5, 1), (5, 1), (5, 1)),Z1
			, M1, Z2, M2, E, Theta
			)

	def SelectReactions(self):
		return self._oleobj_.InvokeTypes(219, LCID, 1, (24, 0), (),)

	def SelectRutherford(self, Z=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(201, LCID, 1, (24, 0), ((3, 1),),Z
			)

	def SelectRutherfordAll(self):
		return self._oleobj_.InvokeTypes(202, LCID, 1, (24, 0), (),)

	def SelectSigmaCalc(self, Z=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(212, LCID, 1, (24, 0), ((3, 1),),Z
			)

	def SelectSigmaCalcAll(self):
		return self._oleobj_.InvokeTypes(213, LCID, 1, (24, 0), (),)

	# The method SetChoose is actually a property, but must be used as a method to correctly pass the arguments
	def SetChoose(self, Index=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(208, LCID, 4, (24, 0), ((3, 1), (11, 1)),Index
			, arg1)

	# The method SetEMax is actually a property, but must be used as a method to correctly pass the arguments
	def SetEMax(self, Index=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(211, LCID, 4, (24, 0), ((3, 1), (5, 1)),Index
			, arg1)

	# The method SetEmin is actually a property, but must be used as a method to correctly pass the arguments
	def SetEmin(self, Index=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(210, LCID, 4, (24, 0), ((3, 1), (5, 1)),Index
			, arg1)

	# The method Title is actually a property, but must be used as a method to correctly pass the arguments
	def Title(self, Index=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(206, LCID, 2, (8, 0), ((3, 1),),Index
			)

	def UniversalEMax(self, Z1=defaultNamedNotOptArg, M1=defaultNamedNotOptArg, Z2=defaultNamedNotOptArg, M2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (5, 0), ((3, 1), (5, 1), (3, 1), (5, 1)),Z1
			, M1, Z2, M2)

	def Unselect(self, Z=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(216, LCID, 1, (24, 0), ((3, 1),),Z
			)

	def UnselectAll(self):
		return self._oleobj_.InvokeTypes(217, LCID, 1, (24, 0), (),)

	def UnselectRutherford(self, Z=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(203, LCID, 1, (24, 0), ((3, 1),),Z
			)

	def UnselectRutherfordAll(self):
		return self._oleobj_.InvokeTypes(204, LCID, 1, (24, 0), (),)

	def UnselectSigmaCalc(self, Z=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(214, LCID, 1, (24, 0), ((3, 1),),Z
			)

	def UnselectSigmaCalcAll(self):
		return self._oleobj_.InvokeTypes(215, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Count": (205, 2, (3, 0), (), "Count", None),
		"ReactionsChoosen": (218, 2, (11, 0), (), "ReactionsChoosen", None),
	}
	_prop_map_put_ = {
		"ReactionsChoosen": ((218, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(205, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IFit(DispatchBaseClass):
	'Dispatch interface for Fit Object'
	CLSID = IID('{54207F20-9D23-11D5-B748-0040332FCEB4}')
	coclass_clsid = IID('{54207F22-9D23-11D5-B748-0040332FCEB4}')

	def Chi2(self):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (5, 0), (),)

	# The method RegionMaxChannel is actually a property, but must be used as a method to correctly pass the arguments
	def RegionMaxChannel(self, reg=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 2, (3, 0), ((3, 1),),reg
			)

	# The method RegionMinChannel is actually a property, but must be used as a method to correctly pass the arguments
	def RegionMinChannel(self, reg=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 2, (3, 0), ((3, 1),),reg
			)

	# The method SetRegionMaxChannel is actually a property, but must be used as a method to correctly pass the arguments
	def SetRegionMaxChannel(self, reg=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(9, LCID, 4, (24, 0), ((3, 1), (3, 1)),reg
			, arg1)

	# The method SetRegionMinChannel is actually a property, but must be used as a method to correctly pass the arguments
	def SetRegionMinChannel(self, reg=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(8, LCID, 4, (24, 0), ((3, 1), (3, 1)),reg
			, arg1)

	_prop_map_get_ = {
		"Accuracy": (11, 2, (5, 0), (), "Accuracy", None),
		"Chi2Evaluation": (13, 2, (3, 0), (), "Chi2Evaluation", None),
		"EnergyCalibration": (2, 2, (11, 0), (), "EnergyCalibration", None),
		"LayerComposition": (5, 2, (11, 0), (), "LayerComposition", None),
		"LayerNr": (6, 2, (3, 0), (), "LayerNr", None),
		"LayerRoughness": (12, 2, (11, 0), (), "LayerRoughness", None),
		"LayerThickness": (4, 2, (11, 0), (), "LayerThickness", None),
		"MaxIterations": (10, 2, (3, 0), (), "MaxIterations", None),
		"NumberOfRegions": (7, 2, (3, 0), (), "NumberOfRegions", None),
		"ParticlesSr": (3, 2, (11, 0), (), "ParticlesSr", None),
	}
	_prop_map_put_ = {
		"Accuracy": ((11, LCID, 4, 0),()),
		"Chi2Evaluation": ((13, LCID, 4, 0),()),
		"EnergyCalibration": ((2, LCID, 4, 0),()),
		"LayerComposition": ((5, LCID, 4, 0),()),
		"LayerNr": ((6, LCID, 4, 0),()),
		"LayerRoughness": ((12, LCID, 4, 0),()),
		"LayerThickness": ((4, LCID, 4, 0),()),
		"MaxIterations": ((10, LCID, 4, 0),()),
		"NumberOfRegions": ((7, LCID, 4, 0),()),
		"ParticlesSr": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IFoil(DispatchBaseClass):
	'Dispatch interface for Foil Object'
	CLSID = IID('{FF8D5AF3-63B8-42B5-B3EC-511F561E51F8}')
	coclass_clsid = IID('{F14C14DC-62BD-4C60-9710-A05CA0151546}')

	def AddElement(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((3, 1),),lay
			)

	def AddLayer(self):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), (),)

	def DeleteAllLayer(self):
		return self._oleobj_.InvokeTypes(205, LCID, 1, (11, 0), (),)

	def DeleteElement(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((3, 1), (3, 1)),lay
			, el)

	def DeleteLayer(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (11, 0), ((3, 1),),lay
			)

	# The method ElementAmount is actually a property, but must be used as a method to correctly pass the arguments
	def ElementAmount(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 2, (5, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method ElementConcentration is actually a property, but must be used as a method to correctly pass the arguments
	def ElementConcentration(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 2, (5, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method ElementName is actually a property, but must be used as a method to correctly pass the arguments
	def ElementName(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(12, LCID, 2, (8, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method HasLayerPorosity is actually a property, but must be used as a method to correctly pass the arguments
	def HasLayerPorosity(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(201, LCID, 2, (11, 0), ((3, 1),),lay
			)

	# The method HasLayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def HasLayerRoughness(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 2, (11, 0), ((3, 1),),lay
			)

	def InsertLayer(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (11, 0), ((3, 1),),lay
			)

	# The method LayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def LayerRoughness(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 2, (5, 0), ((3, 1),),lay
			)

	# The method LayerThickness is actually a property, but must be used as a method to correctly pass the arguments
	def LayerThickness(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 2, (5, 0), ((3, 1),),lay
			)

	# The method NumberOfElements is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfElements(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 2, (3, 0), ((3, 1),),lay
			)

	# The method PoreDiameter is actually a property, but must be used as a method to correctly pass the arguments
	def PoreDiameter(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(203, LCID, 2, (5, 0), ((3, 1),),lay
			)

	# The method PorosityFraction is actually a property, but must be used as a method to correctly pass the arguments
	def PorosityFraction(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(202, LCID, 2, (5, 0), ((3, 1),),lay
			)

	def ReadFoil(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def ReadLayer(self, FileName=defaultNamedNotOptArg, LayerNr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, LayerNr)

	def SaveFoilAs(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def SaveLayerAs(self, FileName=defaultNamedNotOptArg, LayerNr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, LayerNr)

	# The method SetElementAmount is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementAmount(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(13, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),lay
			, el, arg2)

	# The method SetElementConcentration is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementConcentration(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(6, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),lay
			, el, arg2)

	# The method SetElementName is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementName(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(12, LCID, 4, (24, 0), ((3, 1), (3, 1), (8, 1)),lay
			, el, arg2)

	# The method SetHasLayerPorosity is actually a property, but must be used as a method to correctly pass the arguments
	def SetHasLayerPorosity(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(201, LCID, 4, (24, 0), ((3, 1), (11, 1)),lay
			, arg1)

	# The method SetHasLayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def SetHasLayerRoughness(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(4, LCID, 4, (24, 0), ((3, 1), (11, 1)),lay
			, arg1)

	# The method SetLayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def SetLayerRoughness(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(3, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetLayerThickness is actually a property, but must be used as a method to correctly pass the arguments
	def SetLayerThickness(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(1, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetPoreDiameter is actually a property, but must be used as a method to correctly pass the arguments
	def SetPoreDiameter(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(203, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetPorosityFraction is actually a property, but must be used as a method to correctly pass the arguments
	def SetPorosityFraction(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(202, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetStoppingFactor is actually a property, but must be used as a method to correctly pass the arguments
	def SetStoppingFactor(self, lay=defaultNamedNotOptArg, Z=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(206, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),lay
			, Z, arg2)

	# The method StoppingFactor is actually a property, but must be used as a method to correctly pass the arguments
	def StoppingFactor(self, lay=defaultNamedNotOptArg, Z=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(206, LCID, 2, (5, 0), ((3, 1), (3, 1)),lay
			, Z)

	_prop_map_get_ = {
		"NumberOfLayers": (2, 2, (3, 0), (), "NumberOfLayers", None),
		"Thickness": (204, 2, (5, 0), (), "Thickness", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IForms(DispatchBaseClass):
	CLSID = IID('{A9E30D30-9792-4EF5-B5FE-81446FF50084}')
	coclass_clsid = IID('{E31D2D47-3E2E-418B-93E3-8A8C72A7E6C2}')

	def ShowReactions(self):
		return self._oleobj_.InvokeTypes(206, LCID, 1, (24, 0), (),)

	def ShowSetupCalculation(self):
		return self._oleobj_.InvokeTypes(202, LCID, 1, (24, 0), (),)

	def ShowSetupDetector(self):
		return self._oleobj_.InvokeTypes(204, LCID, 1, (24, 0), (),)

	def ShowSetupExperiment(self):
		return self._oleobj_.InvokeTypes(201, LCID, 1, (24, 0), (),)

	def ShowSetupGeometry(self):
		return self._oleobj_.InvokeTypes(203, LCID, 1, (24, 0), (),)

	def ShowSetupPileup(self):
		return self._oleobj_.InvokeTypes(205, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IProjectile(DispatchBaseClass):
	CLSID = IID('{2486C206-2AE3-4D27-8B96-F3384714119A}')
	coclass_clsid = IID('{AB9D3C37-2FA9-434A-8959-8C84A8F50C97}')

	_prop_map_get_ = {
		"Charge": (5, 2, (3, 0), (), "Charge", None),
		"Mass": (6, 2, (5, 0), (), "Mass", None),
		"Name": (4, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
		"Charge": ((5, LCID, 4, 0),()),
		"Mass": ((6, LCID, 4, 0),()),
		"Name": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISetup(DispatchBaseClass):
	'Dispatch interface for Setup Object'
	CLSID = IID('{C22A1430-9329-11D5-B743-0040332FCEB4}')
	coclass_clsid = IID('{C22A1432-9329-11D5-B743-0040332FCEB4}')

	def ReadDetectorSensitivity(self, FileName=defaultNamedNotOptArg, Format=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(201, LCID, 1, (11, 0), ((8, 1), (3, 1)),FileName
			, Format)

	def SetBeta(self, Geometry=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (5, 0), ((3, 1),),Geometry
			)

	_prop_map_get_ = {
		"Alpha": (3, 2, (5, 0), (), "Alpha", None),
		"Beamspread": (10, 2, (5, 0), (), "Beamspread", None),
		"Beta": (4, 2, (5, 0), (), "Beta", None),
		"CalibrationLinear": (7, 2, (5, 0), (), "CalibrationLinear", None),
		"CalibrationOffset": (6, 2, (5, 0), (), "CalibrationOffset", None),
		"CalibrationQuadratic": (8, 2, (5, 0), (), "CalibrationQuadratic", None),
		"DetectorResolution": (9, 2, (5, 0), (), "DetectorResolution", None),
		"DetectorSensitivity": (202, 2, (3, 0), (), "DetectorSensitivity", None),
		"DetectorSensitivityFileName": (203, 2, (8, 0), (), "DetectorSensitivityFileName", None),
		"DetectorType": (19, 2, (3, 0), (), "DetectorType", None),
		"Energy": (1, 2, (5, 0), (), "Energy", None),
		"LTCorrection": (16, 2, (11, 0), (), "LTCorrection", None),
		"LifeTime": (12, 2, (5, 0), (), "LifeTime", None),
		"LiveTime": (18, 2, (5, 0), (), "LiveTime", None),
		"PUCalculation": (17, 2, (11, 0), (), "PUCalculation", None),
		"PUROn": (15, 2, (11, 0), (), "PUROn", None),
		"PURResolution": (14, 2, (5, 0), (), "PURResolution", None),
		"ParticlesSr": (5, 2, (5, 0), (), "ParticlesSr", None),
		"RealTime": (11, 2, (5, 0), (), "RealTime", None),
		"RiseTime": (13, 2, (5, 0), (), "RiseTime", None),
		"TOFLength": (20, 2, (5, 0), (), "TOFLength", None),
		"TOFTimeResolution": (21, 2, (5, 0), (), "TOFTimeResolution", None),
		"Theta": (2, 2, (5, 0), (), "Theta", None),
	}
	_prop_map_put_ = {
		"Alpha": ((3, LCID, 4, 0),()),
		"Beamspread": ((10, LCID, 4, 0),()),
		"Beta": ((4, LCID, 4, 0),()),
		"CalibrationLinear": ((7, LCID, 4, 0),()),
		"CalibrationOffset": ((6, LCID, 4, 0),()),
		"CalibrationQuadratic": ((8, LCID, 4, 0),()),
		"DetectorResolution": ((9, LCID, 4, 0),()),
		"DetectorSensitivity": ((202, LCID, 4, 0),()),
		"DetectorType": ((19, LCID, 4, 0),()),
		"Energy": ((1, LCID, 4, 0),()),
		"LTCorrection": ((16, LCID, 4, 0),()),
		"LifeTime": ((12, LCID, 4, 0),()),
		"LiveTime": ((18, LCID, 4, 0),()),
		"PUCalculation": ((17, LCID, 4, 0),()),
		"PUROn": ((15, LCID, 4, 0),()),
		"PURResolution": ((14, LCID, 4, 0),()),
		"ParticlesSr": ((5, LCID, 4, 0),()),
		"RealTime": ((11, LCID, 4, 0),()),
		"RiseTime": ((13, LCID, 4, 0),()),
		"TOFLength": ((20, LCID, 4, 0),()),
		"TOFTimeResolution": ((21, LCID, 4, 0),()),
		"Theta": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpectrum(DispatchBaseClass):
	CLSID = IID('{DF418CC1-A5C6-11D5-B749-0040332FCEB4}')
	coclass_clsid = IID('{DF418CC3-A5C6-11D5-B749-0040332FCEB4}')

	def Data(self, spID=defaultNamedNotOptArg, chan=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (5, 0), ((3, 1), (3, 1)),spID
			, chan)

	def DataArray(self, spID=defaultNamedNotOptArg):
		return self._ApplyTypes_(201, 1, (12, 0), ((3, 1),), u'DataArray', None,spID
			)

	def Delete(self, spID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(204, LCID, 1, (24, 0), ((3, 1),),spID
			)

	def IDOfElement(self, Z=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(205, LCID, 1, (3, 0), ((3, 1),),Z
			)

	def IDOfIsotope(self, Z=defaultNamedNotOptArg, M=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(206, LCID, 1, (3, 0), ((3, 1), (5, 1)),Z
			, M)

	def Integrate(self, spID=defaultNamedNotOptArg, lowChannel=defaultNamedNotOptArg, upChannel=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (5, 0), ((3, 1), (3, 1), (3, 1)),spID
			, lowChannel, upChannel)

	# The method NumberOfChannels is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfChannels(self, spID=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 2, (3, 0), ((3, 1),),spID
			)

	_prop_map_get_ = {
		"AutoScale": (4, 2, (11, 0), (), "AutoScale", None),
		"BottomAxisMax": (6, 2, (5, 0), (), "BottomAxisMax", None),
		"BottomAxisMin": (5, 2, (5, 0), (), "BottomAxisMin", None),
		"EndAcquisition": (203, 2, (7, 0), (), "EndAcquisition", None),
		"LeftAxisMax": (8, 2, (5, 0), (), "LeftAxisMax", None),
		"LeftAxisMin": (7, 2, (5, 0), (), "LeftAxisMin", None),
		"StartAcquisition": (202, 2, (7, 0), (), "StartAcquisition", None),
	}
	_prop_map_put_ = {
		"AutoScale": ((4, LCID, 4, 0),()),
		"BottomAxisMax": ((6, LCID, 4, 0),()),
		"BottomAxisMin": ((5, LCID, 4, 0),()),
		"LeftAxisMax": ((8, LCID, 4, 0),()),
		"LeftAxisMin": ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IStopping(DispatchBaseClass):
	'Dispatch interface for Stopping Object'
	CLSID = IID('{0A40E4F1-D298-11D5-B752-0040332FCEB4}')
	coclass_clsid = IID('{0A40E4F3-D298-11D5-B752-0040332FCEB4}')

	def EnergylossInLayer(self, Z1=defaultNamedNotOptArg, M1=defaultNamedNotOptArg, E=defaultNamedNotOptArg, id=defaultNamedNotOptArg
			, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (5, 0), ((3, 1), (5, 1), (5, 1), (3, 1), (3, 1)),Z1
			, M1, E, id, lay)

	def StoppingInElement(self, Z1=defaultNamedNotOptArg, M1=defaultNamedNotOptArg, E=defaultNamedNotOptArg, Z2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (5, 0), ((3, 1), (5, 1), (5, 1), (3, 1)),Z1
			, M1, E, Z2)

	def StoppingInLayer(self, Z1=defaultNamedNotOptArg, M1=defaultNamedNotOptArg, E=defaultNamedNotOptArg, id=defaultNamedNotOptArg
			, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (5, 0), ((3, 1), (5, 1), (5, 1), (3, 1), (3, 1)),Z1
			, M1, E, id, lay)

	def StragglingInLayer(self, Z1=defaultNamedNotOptArg, M1=defaultNamedNotOptArg, E=defaultNamedNotOptArg, id=defaultNamedNotOptArg
			, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (5, 0), ((3, 1), (5, 1), (5, 1), (3, 1), (3, 1)),Z1
			, M1, E, id, lay)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITarget(DispatchBaseClass):
	'Dispatch interface for Target Object'
	CLSID = IID('{5978B7E1-9706-11D5-B747-0040332FCEB4}')
	coclass_clsid = IID('{5978B7E3-9706-11D5-B747-0040332FCEB4}')

	def AddElement(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((3, 1),),lay
			)

	def AddIsotope(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(211, LCID, 1, (11, 0), ((3, 1), (3, 1)),lay
			, el)

	def AddLayer(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def DeleteAllLayer(self):
		return self._oleobj_.InvokeTypes(205, LCID, 1, (11, 0), (),)

	def DeleteElement(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((3, 1), (3, 1)),lay
			, el)

	def DeleteIsotope(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, iso=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(212, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),lay
			, el, iso)

	def DeleteLayer(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((3, 1),),lay
			)

	# The method ElementAmount is actually a property, but must be used as a method to correctly pass the arguments
	def ElementAmount(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 2, (5, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method ElementConcentration is actually a property, but must be used as a method to correctly pass the arguments
	def ElementConcentration(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(9, LCID, 2, (5, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method ElementName is actually a property, but must be used as a method to correctly pass the arguments
	def ElementName(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(15, LCID, 2, (8, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method HasLayerPorosity is actually a property, but must be used as a method to correctly pass the arguments
	def HasLayerPorosity(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(201, LCID, 2, (11, 0), ((3, 1),),lay
			)

	# The method HasLayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def HasLayerRoughness(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 2, (11, 0), ((3, 1),),lay
			)

	def InsertLayer(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (11, 0), ((3, 1),),lay
			)

	# The method IsotopeConcentration is actually a property, but must be used as a method to correctly pass the arguments
	def IsotopeConcentration(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, iso=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(209, LCID, 2, (5, 0), ((3, 1), (3, 1), (3, 1)),lay
			, el, iso)

	# The method IsotopeMass is actually a property, but must be used as a method to correctly pass the arguments
	def IsotopeMass(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, iso=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(210, LCID, 2, (5, 0), ((3, 1), (3, 1), (3, 1)),lay
			, el, iso)

	# The method LayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def LayerRoughness(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 2, (5, 0), ((3, 1),),lay
			)

	# The method LayerThickness is actually a property, but must be used as a method to correctly pass the arguments
	def LayerThickness(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 2, (5, 0), ((3, 1),),lay
			)

	# The method NumberOfElements is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfElements(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 2, (3, 0), ((3, 1),),lay
			)

	# The method NumberOfIsotopes is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfIsotopes(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(208, LCID, 2, (3, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method PoreDiameter is actually a property, but must be used as a method to correctly pass the arguments
	def PoreDiameter(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(203, LCID, 2, (5, 0), ((3, 1),),lay
			)

	# The method PorosityFraction is actually a property, but must be used as a method to correctly pass the arguments
	def PorosityFraction(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(202, LCID, 2, (5, 0), ((3, 1),),lay
			)

	def ReadLayer(self, FileName=defaultNamedNotOptArg, LayerNr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, LayerNr)

	def ReadTarget(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def SaveLayerAs(self, FileName=defaultNamedNotOptArg, LayerNr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, LayerNr)

	def SaveTargetAs(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	# The method SetElementAmount is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementAmount(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(16, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),lay
			, el, arg2)

	# The method SetElementConcentration is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementConcentration(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(9, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),lay
			, el, arg2)

	# The method SetElementName is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementName(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(15, LCID, 4, (24, 0), ((3, 1), (3, 1), (8, 1)),lay
			, el, arg2)

	# The method SetHasLayerPorosity is actually a property, but must be used as a method to correctly pass the arguments
	def SetHasLayerPorosity(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(201, LCID, 4, (24, 0), ((3, 1), (11, 1)),lay
			, arg1)

	# The method SetHasLayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def SetHasLayerRoughness(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(4, LCID, 4, (24, 0), ((3, 1), (11, 1)),lay
			, arg1)

	# The method SetIsotopeConcentration is actually a property, but must be used as a method to correctly pass the arguments
	def SetIsotopeConcentration(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, iso=defaultNamedNotOptArg, arg3=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(209, LCID, 4, (24, 0), ((3, 1), (3, 1), (3, 1), (5, 1)),lay
			, el, iso, arg3)

	# The method SetIsotopeMass is actually a property, but must be used as a method to correctly pass the arguments
	def SetIsotopeMass(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, iso=defaultNamedNotOptArg, arg3=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(210, LCID, 4, (24, 0), ((3, 1), (3, 1), (3, 1), (5, 1)),lay
			, el, iso, arg3)

	# The method SetLayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def SetLayerRoughness(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(3, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetLayerThickness is actually a property, but must be used as a method to correctly pass the arguments
	def SetLayerThickness(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(1, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetPoreDiameter is actually a property, but must be used as a method to correctly pass the arguments
	def SetPoreDiameter(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(203, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetPorosityFraction is actually a property, but must be used as a method to correctly pass the arguments
	def SetPorosityFraction(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(202, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetStoppingFactor is actually a property, but must be used as a method to correctly pass the arguments
	def SetStoppingFactor(self, lay=defaultNamedNotOptArg, Z=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(207, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),lay
			, Z, arg2)

	# The method StoppingFactor is actually a property, but must be used as a method to correctly pass the arguments
	def StoppingFactor(self, lay=defaultNamedNotOptArg, Z=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(207, LCID, 2, (5, 0), ((3, 1), (3, 1)),lay
			, Z)

	_prop_map_get_ = {
		"HasSubstrateRoughness": (6, 2, (11, 0), (), "HasSubstrateRoughness", None),
		"NumberOfLayers": (2, 2, (3, 0), (), "NumberOfLayers", None),
		"SubstrateRoughness": (5, 2, (5, 0), (), "SubstrateRoughness", None),
		"SubstrateRoughnessDistribution": (8, 2, (3, 0), (), "SubstrateRoughnessDistribution", None),
		"Thickness": (206, 2, (5, 0), (), "Thickness", None),
		"TotalNumberOfElements": (204, 2, (3, 0), (), "TotalNumberOfElements", None),
	}
	_prop_map_put_ = {
		"HasSubstrateRoughness": ((6, LCID, 4, 0),()),
		"SubstrateRoughness": ((5, LCID, 4, 0),()),
		"SubstrateRoughnessDistribution": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITargetOut(DispatchBaseClass):
	CLSID = IID('{5DB47E27-5BA1-4FE3-8785-545F494FCBE2}')
	coclass_clsid = IID('{E45540BA-A7B0-4033-9E6F-B26230D41F69}')

	def AddElement(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(208, LCID, 1, (11, 0), ((3, 1),),lay
			)

	def AddLayer(self):
		return self._oleobj_.InvokeTypes(205, LCID, 1, (11, 0), (),)

	def CreateTargetOut(self):
		return self._oleobj_.InvokeTypes(211, LCID, 1, (24, 0), (),)

	def DeleteAllLayer(self):
		return self._oleobj_.InvokeTypes(215, LCID, 1, (11, 0), (),)

	def DeleteElement(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(209, LCID, 1, (11, 0), ((3, 1), (3, 1)),lay
			, el)

	def DeleteLayer(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(207, LCID, 1, (11, 0), ((3, 1),),lay
			)

	def DestroyTargetOut(self):
		return self._oleobj_.InvokeTypes(212, LCID, 1, (24, 0), (),)

	# The method ElementConcentration is actually a property, but must be used as a method to correctly pass the arguments
	def ElementConcentration(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(204, LCID, 2, (5, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method ElementName is actually a property, but must be used as a method to correctly pass the arguments
	def ElementName(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(210, LCID, 2, (8, 0), ((3, 1), (3, 1)),lay
			, el)

	def InsertLayer(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(206, LCID, 1, (11, 0), ((3, 1),),lay
			)

	# The method LayerThickness is actually a property, but must be used as a method to correctly pass the arguments
	def LayerThickness(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(201, LCID, 2, (5, 0), ((3, 1),),lay
			)

	# The method NumberOfElements is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfElements(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(203, LCID, 2, (3, 0), ((3, 1),),lay
			)

	# The method SetElementConcentration is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementConcentration(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(204, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),lay
			, el, arg2)

	# The method SetElementName is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementName(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(210, LCID, 4, (24, 0), ((3, 1), (3, 1), (8, 1)),lay
			, el, arg2)

	# The method SetLayerThickness is actually a property, but must be used as a method to correctly pass the arguments
	def SetLayerThickness(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(201, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	_prop_map_get_ = {
		"NumberOfLayers": (202, 2, (3, 0), (), "NumberOfLayers", None),
		"Shift": (213, 2, (5, 0), (), "Shift", None),
		"Thickness": (214, 2, (5, 0), (), "Thickness", None),
	}
	_prop_map_put_ = {
		"Shift": ((213, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWindow(DispatchBaseClass):
	CLSID = IID('{2C926AE5-0CDA-45F2-BD6B-70031EFFB199}')
	coclass_clsid = IID('{58312EB5-30F5-47D1-8E60-04634C214FBD}')

	def AddElement(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(210, LCID, 1, (11, 0), ((3, 1),),lay
			)

	def AddLayer(self):
		return self._oleobj_.InvokeTypes(207, LCID, 1, (11, 0), (),)

	def DeleteAllLayer(self):
		return self._oleobj_.InvokeTypes(222, LCID, 1, (11, 0), (),)

	def DeleteElement(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(211, LCID, 1, (11, 0), ((3, 1), (3, 1)),lay
			, el)

	def DeleteLayer(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(209, LCID, 1, (11, 0), ((3, 1),),lay
			)

	# The method ElementAmount is actually a property, but must be used as a method to correctly pass the arguments
	def ElementAmount(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(213, LCID, 2, (5, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method ElementConcentration is actually a property, but must be used as a method to correctly pass the arguments
	def ElementConcentration(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(206, LCID, 2, (5, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method ElementName is actually a property, but must be used as a method to correctly pass the arguments
	def ElementName(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(212, LCID, 2, (8, 0), ((3, 1), (3, 1)),lay
			, el)

	# The method HasLayerPorosity is actually a property, but must be used as a method to correctly pass the arguments
	def HasLayerPorosity(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(218, LCID, 2, (11, 0), ((3, 1),),lay
			)

	# The method HasLayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def HasLayerRoughness(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(204, LCID, 2, (11, 0), ((3, 1),),lay
			)

	def InsertLayer(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(208, LCID, 1, (11, 0), ((3, 1),),lay
			)

	# The method LayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def LayerRoughness(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(203, LCID, 2, (5, 0), ((3, 1),),lay
			)

	# The method LayerThickness is actually a property, but must be used as a method to correctly pass the arguments
	def LayerThickness(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(201, LCID, 2, (5, 0), ((3, 1),),lay
			)

	# The method NumberOfElements is actually a property, but must be used as a method to correctly pass the arguments
	def NumberOfElements(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(205, LCID, 2, (3, 0), ((3, 1),),lay
			)

	# The method PoreDiameter is actually a property, but must be used as a method to correctly pass the arguments
	def PoreDiameter(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(220, LCID, 2, (5, 0), ((3, 1),),lay
			)

	# The method PorosityFraction is actually a property, but must be used as a method to correctly pass the arguments
	def PorosityFraction(self, lay=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(219, LCID, 2, (5, 0), ((3, 1),),lay
			)

	def ReadLayer(self, FileName=defaultNamedNotOptArg, LayerNr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(214, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, LayerNr)

	def ReadWindow(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(216, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def SaveLayerAs(self, FileName=defaultNamedNotOptArg, LayerNr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(215, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, LayerNr)

	def SaveWindowAs(self, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(217, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	# The method SetElementAmount is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementAmount(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(213, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),lay
			, el, arg2)

	# The method SetElementConcentration is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementConcentration(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(206, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),lay
			, el, arg2)

	# The method SetElementName is actually a property, but must be used as a method to correctly pass the arguments
	def SetElementName(self, lay=defaultNamedNotOptArg, el=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(212, LCID, 4, (24, 0), ((3, 1), (3, 1), (8, 1)),lay
			, el, arg2)

	# The method SetHasLayerPorosity is actually a property, but must be used as a method to correctly pass the arguments
	def SetHasLayerPorosity(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(218, LCID, 4, (24, 0), ((3, 1), (11, 1)),lay
			, arg1)

	# The method SetHasLayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def SetHasLayerRoughness(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(204, LCID, 4, (24, 0), ((3, 1), (11, 1)),lay
			, arg1)

	# The method SetLayerRoughness is actually a property, but must be used as a method to correctly pass the arguments
	def SetLayerRoughness(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(203, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetLayerThickness is actually a property, but must be used as a method to correctly pass the arguments
	def SetLayerThickness(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(201, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetPoreDiameter is actually a property, but must be used as a method to correctly pass the arguments
	def SetPoreDiameter(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(220, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetPorosityFraction is actually a property, but must be used as a method to correctly pass the arguments
	def SetPorosityFraction(self, lay=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(219, LCID, 4, (24, 0), ((3, 1), (5, 1)),lay
			, arg1)

	# The method SetStoppingFactor is actually a property, but must be used as a method to correctly pass the arguments
	def SetStoppingFactor(self, lay=defaultNamedNotOptArg, Z=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(223, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),lay
			, Z, arg2)

	# The method StoppingFactor is actually a property, but must be used as a method to correctly pass the arguments
	def StoppingFactor(self, lay=defaultNamedNotOptArg, Z=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(223, LCID, 2, (5, 0), ((3, 1), (3, 1)),lay
			, Z)

	_prop_map_get_ = {
		"NumberOfLayers": (202, 2, (3, 0), (), "NumberOfLayers", None),
		"Thickness": (221, 2, (5, 0), (), "Thickness", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'Simnra.App'
class App(CoClassBaseClass): # A CoClass
	# App Object
	CLSID = IID('{9F51F4E3-754F-11D5-B742-0040332FCEB4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IApp,
	]
	default_interface = IApp

# This CoClass is known by the name 'Simnra.Calc'
class Calc(CoClassBaseClass): # A CoClass
	CLSID = IID('{9DD33B22-A8EC-11D5-B749-0040332FCEB4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICalc,
	]
	default_interface = ICalc

# This CoClass is known by the name 'Simnra.CrossSec'
class CrossSec(CoClassBaseClass): # A CoClass
	CLSID = IID('{504EF515-68CF-495D-8D7C-C132E538D839}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICrossSec,
	]
	default_interface = ICrossSec

# This CoClass is known by the name 'Simnra.Fit'
class Fit(CoClassBaseClass): # A CoClass
	CLSID = IID('{54207F22-9D23-11D5-B748-0040332FCEB4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFit,
	]
	default_interface = IFit

# This CoClass is known by the name 'Simnra.Foil'
class Foil(CoClassBaseClass): # A CoClass
	CLSID = IID('{F14C14DC-62BD-4C60-9710-A05CA0151546}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IFoil,
	]
	default_interface = IFoil

# This CoClass is known by the name 'Simnra.Forms'
class Forms(CoClassBaseClass): # A CoClass
	CLSID = IID('{E31D2D47-3E2E-418B-93E3-8A8C72A7E6C2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IForms,
	]
	default_interface = IForms

# This CoClass is known by the name 'Simnra.Projectile'
class Projectile(CoClassBaseClass): # A CoClass
	CLSID = IID('{AB9D3C37-2FA9-434A-8959-8C84A8F50C97}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IProjectile,
	]
	default_interface = IProjectile

# This CoClass is known by the name 'Simnra.Setup'
class Setup(CoClassBaseClass): # A CoClass
	# Setup Object
	CLSID = IID('{C22A1432-9329-11D5-B743-0040332FCEB4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISetup,
	]
	default_interface = ISetup

# This CoClass is known by the name 'Simnra.Spectrum'
class Spectrum(CoClassBaseClass): # A CoClass
	CLSID = IID('{DF418CC3-A5C6-11D5-B749-0040332FCEB4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpectrum,
	]
	default_interface = ISpectrum

# This CoClass is known by the name 'Simnra.Stopping'
class Stopping(CoClassBaseClass): # A CoClass
	CLSID = IID('{0A40E4F3-D298-11D5-B752-0040332FCEB4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IStopping,
	]
	default_interface = IStopping

# This CoClass is known by the name 'Simnra.Target'
class Target(CoClassBaseClass): # A CoClass
	# Target Object
	CLSID = IID('{5978B7E3-9706-11D5-B747-0040332FCEB4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ITarget,
	]
	default_interface = ITarget

# This CoClass is known by the name 'Simnra.TargetOut'
class TargetOut(CoClassBaseClass): # A CoClass
	CLSID = IID('{E45540BA-A7B0-4033-9E6F-B26230D41F69}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ITargetOut,
	]
	default_interface = ITargetOut

# This CoClass is known by the name 'Simnra.Window'
class Window(CoClassBaseClass): # A CoClass
	CLSID = IID('{58312EB5-30F5-47D1-8E60-04634C214FBD}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWindow,
	]
	default_interface = IWindow

IApp_vtables_dispatch_ = 1
IApp_vtables_ = [
	(( u'Open' , u'FileName' , u'FileType' , u'Value' , ), 1, (1, (), [ 
			(8, 1, None, None) , (3, 33, '-1', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'CalculateSpectrum' , u'Value' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'SaveAs' , u'FileName' , u'FileType' , u'Value' , ), 3, (3, (), [ 
			(8, 1, None, None) , (3, 49, '2', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'ReadSpectrumData' , u'FileName' , u'Format' , u'Value' , ), 4, (4, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Minimize' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Restore' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'BringToFront' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'WriteSpectrumData' , u'FileName' , u'Param2' , ), 8, (8, (), [ (8, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'CopySpectrumData' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'Active' , u'Value' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Hide' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'Show' , ), 12, (12, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'FitSpectrum' , u'Value' , ), 13, (13, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'DeleteSpectrumOnCalculate' , u'Value' , ), 14, (14, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'DeleteSpectrumOnCalculate' , u'Value' , ), 14, (14, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'ShowMessages' , u'Value' , ), 15, (15, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'ShowMessages' , u'Value' , ), 15, (15, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'LastMessage' , u'Value' , ), 16, (16, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Maximize' , ), 17, (17, (), [ ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'CalculateSpectrumFast' , u'Value' , ), 18, (18, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'CalculatingSpectrum' , u'Value' , ), 19, (19, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'SpectrumChanged' , u'Value' , ), 20, (20, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'SpectrumChanged' , u'Value' , ), 20, (20, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'FileName' , u'Value' , ), 21, (21, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'CalculateSpectrumToDepth' , u'Depth' , u'Value' , ), 22, (22, (), [ (5, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'Left' , u'Value' , ), 23, (23, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'Left' , u'Value' , ), 23, (23, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'Width' , u'Value' , ), 24, (24, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'Width' , u'Value' , ), 24, (24, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'Top' , u'Value' , ), 25, (25, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'Top' , u'Value' , ), 25, (25, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'Height' , u'Value' , ), 26, (26, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'Height' , u'Value' , ), 26, (26, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'Version' , u'Value' , ), 27, (27, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'CreateListOfCrSecs' , ), 28, (28, (), [ ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'SaveThumbnailAs' , u'FileName' , u'Width' , ), 201, (201, (), [ (8, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'Standalone' , u'Value' , ), 204, (204, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'BringToRear' , ), 205, (205, (), [ ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'OpenAs' , u'FileName' , u'FileType' , u'Value' , ), 202, (202, (), [ 
			(8, 1, None, None) , (3, 49, '-1', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'LegendVisible' , u'Value' , ), 203, (203, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'LegendVisible' , u'Value' , ), 203, (203, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'LegendOutsideOfChart' , u'Value' , ), 206, (206, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'LegendOutsideOfChart' , u'Value' , ), 206, (206, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( u'TopAxisCaption' , u'Value' , ), 207, (207, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'TopAxisCaption' , u'Value' , ), 207, (207, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( u'OpenStream' , u'Stream' , u'FileType' , u'Value' , ), 208, (208, (), [ 
			(13, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'IncidentIonEnergyIsZero' , u'Value' , ), 209, (209, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( u'IncidentIonEnergyIsZero' , u'Value' , ), 209, (209, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'Visible' , u'Value' , ), 210, (210, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( u'Reset' , ), 211, (211, (), [ ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'ToolbarVisible' , u'Value' , ), 212, (212, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( u'ToolbarVisible' , u'Value' , ), 212, (212, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'MenuVisible' , u'Value' , ), 213, (213, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( u'MenuVisible' , u'Value' , ), 213, (213, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'StatusbarVisible' , u'Value' , ), 214, (214, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( u'StatusbarVisible' , u'Value' , ), 214, (214, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( u'ControlsVisible' , ), 215, (215, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
	(( u'ResizeSpectrum' , u'NumChannels' , u'ResizeCalibration' , ), 216, (216, (), [ (3, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( u'BorderStyle' , u'Value' , ), 217, (217, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
	(( u'BorderStyle' , u'Value' , ), 217, (217, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( u'OLEUser' , u'Value' , ), 218, (218, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
	(( u'OLEUser' , u'Value' , ), 218, (218, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( u'SRIMDirectory' , u'Value' , ), 219, (219, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
	(( u'SRIMDirectory' , u'Value' , ), 219, (219, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( u'CalculatePileup' , u'Value' , ), 220, (220, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 284 , (3, 0, None, None) , 0 , )),
	(( u'CalculateDualScatteringBackground' , u'AddToSpectrum' , u'Value' , ), 221, (221, (), [ (11, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( u'CloseButtonEnabled' , ), 222, (222, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 292 , (3, 0, None, None) , 0 , )),
]

ICalc_vtables_dispatch_ = 1
ICalc_vtables_ = [
	(( u'dEin' , u'Value' , ), 1, (1, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'dEin' , u'Value' , ), 1, (1, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'dEout' , u'Value' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'dEout' , u'Value' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Emin' , u'Value' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Emin' , u'Value' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Straggling' , u'Value' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Straggling' , u'Value' , ), 4, (4, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Isotopes' , u'Value' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'Isotopes' , u'Value' , ), 5, (5, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'DualScattering' , u'Value' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'DualScattering' , u'Value' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'MultipleScattering' , u'Value' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'MultipleScattering' , u'Value' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'AutoStepwidthIn' , u'Value' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'AutoStepwidthIn' , u'Value' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'AutoStepwidthOut' , u'Value' , ), 9, (9, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'AutoStepwidthOut' , u'Value' , ), 9, (9, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfDVariations' , u'Value' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfDVariations' , u'Value' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfAngleVariations' , u'Value' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfAngleVariations' , u'Value' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'ElementSpectra' , u'Value' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'ElementSpectra' , u'Value' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'IsotopeSpectra' , u'Value' , ), 13, (13, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'IsotopeSpectra' , u'Value' , ), 13, (13, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'ZBStopping' , u'Value' , ), 14, (14, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'ZBStopping' , u'Value' , ), 14, (14, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'HighEnergyStopping' , u'Value' , ), 15, (15, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'HighEnergyStopping' , u'Value' , ), 15, (15, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'SubstrateRoughnessDimension' , u'Value' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'SubstrateRoughnessDimension' , u'Value' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'StragglingModel' , u'Value' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'StragglingModel' , u'Value' , ), 17, (17, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'ScreeningModel' , u'Value' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'ScreeningModel' , u'Value' , ), 18, (18, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'PUModel' , u'Value' , ), 19, (19, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'PUModel' , u'Value' , ), 19, (19, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'LogFile' , u'Value' , ), 20, (20, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'LogFile' , u'Value' , ), 20, (20, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'CreateSpectrum' , u'Value' , ), 21, (21, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'CreateSpectrum' , u'Value' , ), 21, (21, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'CrossSecStraggling' , u'Value' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( u'CrossSecStraggling' , u'Value' , ), 201, (201, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'StragglingShape' , u'Value' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( u'StragglingShape' , u'Value' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'DualScatteringRoughness' , u'Value' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( u'DualScatteringRoughness' , u'Value' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'StoppingModel' , u'Value' , ), 204, (204, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( u'StoppingModel' , u'Value' , ), 204, (204, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'NuclearStoppingModel' , u'Value' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( u'NuclearStoppingModel' , u'Value' , ), 205, (205, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'CreateSpectrumFromLayerNr' , u'Value' , ), 206, (206, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( u'CreateSpectrumFromLayerNr' , u'Value' , ), 206, (206, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'Accuracy' , u'Value' , ), 207, (207, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( u'CalculateToEMin' , u'Value' , ), 208, (208, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( u'CalculateToEMin' , u'Value' , ), 208, (208, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
]

ICrossSec_vtables_dispatch_ = 1
ICrossSec_vtables_ = [
	(( u'RBSRutherford' , u'Z1' , u'M1' , u'Z2' , u'M2' , 
			u'E' , u'Theta' , u'Value' , ), 1, (1, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'UniversalEMax' , u'Z1' , u'M1' , u'Z2' , u'M2' , 
			u'Value' , ), 2, (2, (), [ (3, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , 
			(5, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ERDRutherford' , u'Z1' , u'M1' , u'Z2' , u'M2' , 
			u'E' , u'Phi' , u'Value' , ), 3, (3, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'SelectRutherford' , u'Z' , ), 201, (201, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'SelectRutherfordAll' , ), 202, (202, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'UnselectRutherford' , u'Z' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'UnselectRutherfordAll' , ), 204, (204, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Count' , u'Value' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Title' , u'Index' , u'Value' , ), 206, (206, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'FileName' , u'Index' , u'Value' , ), 207, (207, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Choose' , u'Index' , u'Value' , ), 208, (208, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'Choose' , u'Index' , u'Value' , ), 208, (208, (), [ (3, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Info' , u'Index' , u'Value' , ), 209, (209, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'Emin' , u'Index' , u'Value' , ), 210, (210, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Emin' , u'Index' , u'Value' , ), 210, (210, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'EMax' , u'Index' , u'Value' , ), 211, (211, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'EMax' , u'Index' , u'Value' , ), 211, (211, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'SelectSigmaCalc' , u'Z' , ), 212, (212, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'SelectSigmaCalcAll' , ), 213, (213, (), [ ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'UnselectSigmaCalc' , u'Z' , ), 214, (214, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'UnselectSigmaCalcAll' , ), 215, (215, (), [ ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'Unselect' , u'Z' , ), 216, (216, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'UnselectAll' , ), 217, (217, (), [ ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'ReactionsChoosen' , u'Value' , ), 218, (218, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'ReactionsChoosen' , u'Value' , ), 218, (218, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'SelectReactions' , ), 219, (219, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IFit_vtables_dispatch_ = 1
IFit_vtables_ = [
	(( u'EnergyCalibration' , u'Value' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'EnergyCalibration' , u'Value' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ParticlesSr' , u'Value' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'ParticlesSr' , u'Value' , ), 3, (3, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'LayerThickness' , u'Value' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'LayerThickness' , u'Value' , ), 4, (4, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'LayerComposition' , u'Value' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'LayerComposition' , u'Value' , ), 5, (5, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'LayerNr' , u'Value' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'LayerNr' , u'Value' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfRegions' , u'Value' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfRegions' , u'Value' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'RegionMinChannel' , u'reg' , u'Value' , ), 8, (8, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'RegionMinChannel' , u'reg' , u'Value' , ), 8, (8, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'RegionMaxChannel' , u'reg' , u'Value' , ), 9, (9, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'RegionMaxChannel' , u'reg' , u'Value' , ), 9, (9, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'MaxIterations' , u'Value' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'MaxIterations' , u'Value' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Accuracy' , u'Value' , ), 11, (11, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'Accuracy' , u'Value' , ), 11, (11, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Chi2' , u'Value' , ), 1, (1, (), [ (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'LayerRoughness' , u'Value' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'LayerRoughness' , u'Value' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'Chi2Evaluation' , u'Value' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Chi2Evaluation' , u'Value' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
]

IFoil_vtables_dispatch_ = 1
IFoil_vtables_ = [
	(( u'LayerThickness' , u'lay' , u'Value' , ), 1, (1, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'LayerThickness' , u'lay' , u'Value' , ), 1, (1, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfLayers' , u'Value' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'LayerRoughness' , u'lay' , u'Value' , ), 3, (3, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'LayerRoughness' , u'lay' , u'Value' , ), 3, (3, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerRoughness' , u'lay' , u'Value' , ), 4, (4, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerRoughness' , u'lay' , u'Value' , ), 4, (4, (), [ (3, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfElements' , u'lay' , u'Value' , ), 5, (5, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'ElementConcentration' , u'lay' , u'el' , u'Value' , ), 6, (6, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'ElementConcentration' , u'lay' , u'el' , u'Value' , ), 6, (6, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AddLayer' , u'Value' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'InsertLayer' , u'lay' , u'Value' , ), 8, (8, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'DeleteLayer' , u'lay' , u'Value' , ), 9, (9, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'AddElement' , u'lay' , u'Value' , ), 10, (10, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'DeleteElement' , u'lay' , u'el' , u'Value' , ), 11, (11, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'ElementName' , u'lay' , u'el' , u'Value' , ), 12, (12, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'ElementName' , u'lay' , u'el' , u'Value' , ), 12, (12, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'ElementAmount' , u'lay' , u'el' , u'Value' , ), 13, (13, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'ElementAmount' , u'lay' , u'el' , u'Value' , ), 13, (13, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'ReadLayer' , u'FileName' , u'LayerNr' , ), 14, (14, (), [ (8, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'SaveLayerAs' , u'FileName' , u'LayerNr' , ), 15, (15, (), [ (8, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'ReadFoil' , u'FileName' , ), 16, (16, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'SaveFoilAs' , u'FileName' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerPorosity' , u'lay' , u'Value' , ), 201, (201, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerPorosity' , u'lay' , u'Value' , ), 201, (201, (), [ (3, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'PorosityFraction' , u'lay' , u'Value' , ), 202, (202, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'PorosityFraction' , u'lay' , u'Value' , ), 202, (202, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'PoreDiameter' , u'lay' , u'Value' , ), 203, (203, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'PoreDiameter' , u'lay' , u'Value' , ), 203, (203, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'Thickness' , u'Value' , ), 204, (204, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'DeleteAllLayer' , u'Value' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'StoppingFactor' , u'lay' , u'Z' , u'Value' , ), 206, (206, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'StoppingFactor' , u'lay' , u'Z' , u'Value' , ), 206, (206, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
]

IForms_vtables_dispatch_ = 1
IForms_vtables_ = [
	(( u'ShowSetupExperiment' , ), 201, (201, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'ShowSetupCalculation' , ), 202, (202, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ShowSetupGeometry' , ), 203, (203, (), [ ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'ShowSetupDetector' , ), 204, (204, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'ShowSetupPileup' , ), 205, (205, (), [ ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'ShowReactions' , ), 206, (206, (), [ ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

IProjectile_vtables_dispatch_ = 1
IProjectile_vtables_ = [
	(( u'Name' , u'Value' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Name' , u'Value' , ), 4, (4, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Charge' , u'Value' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Charge' , u'Value' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Mass' , u'Value' , ), 6, (6, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Mass' , u'Value' , ), 6, (6, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ISetup_vtables_dispatch_ = 1
ISetup_vtables_ = [
	(( u'Energy' , u'Value' , ), 1, (1, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Energy' , u'Value' , ), 1, (1, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Theta' , u'Value' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'Theta' , u'Value' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Alpha' , u'Value' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'Alpha' , u'Value' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Beta' , u'Value' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'Beta' , u'Value' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'ParticlesSr' , u'Value' , ), 5, (5, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'ParticlesSr' , u'Value' , ), 5, (5, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'CalibrationOffset' , u'Value' , ), 6, (6, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'CalibrationOffset' , u'Value' , ), 6, (6, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'CalibrationLinear' , u'Value' , ), 7, (7, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'CalibrationLinear' , u'Value' , ), 7, (7, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'CalibrationQuadratic' , u'Value' , ), 8, (8, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'CalibrationQuadratic' , u'Value' , ), 8, (8, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'DetectorResolution' , u'Value' , ), 9, (9, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'DetectorResolution' , u'Value' , ), 9, (9, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Beamspread' , u'Value' , ), 10, (10, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'Beamspread' , u'Value' , ), 10, (10, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'RealTime' , u'Value' , ), 11, (11, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'RealTime' , u'Value' , ), 11, (11, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'LifeTime' , u'Value' , ), 12, (12, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'LifeTime' , u'Value' , ), 12, (12, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'RiseTime' , u'Value' , ), 13, (13, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'RiseTime' , u'Value' , ), 13, (13, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'PURResolution' , u'Value' , ), 14, (14, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'PURResolution' , u'Value' , ), 14, (14, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'PUROn' , u'Value' , ), 15, (15, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'PUROn' , u'Value' , ), 15, (15, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'LTCorrection' , u'Value' , ), 16, (16, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'LTCorrection' , u'Value' , ), 16, (16, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'PUCalculation' , u'Value' , ), 17, (17, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'PUCalculation' , u'Value' , ), 17, (17, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'LiveTime' , u'Value' , ), 18, (18, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'LiveTime' , u'Value' , ), 18, (18, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'DetectorType' , u'Value' , ), 19, (19, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'DetectorType' , u'Value' , ), 19, (19, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'TOFLength' , u'Value' , ), 20, (20, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'TOFLength' , u'Value' , ), 20, (20, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'TOFTimeResolution' , u'Value' , ), 21, (21, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'TOFTimeResolution' , u'Value' , ), 21, (21, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'SetBeta' , u'Geometry' , u'Value' , ), 22, (22, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( u'ReadDetectorSensitivity' , u'FileName' , u'Format' , u'Value' , ), 201, (201, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'DetectorSensitivity' , u'Value' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( u'DetectorSensitivity' , u'Value' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'DetectorSensitivityFileName' , u'Value' , ), 203, (203, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
]

ISpectrum_vtables_dispatch_ = 1
ISpectrum_vtables_ = [
	(( u'Integrate' , u'spID' , u'lowChannel' , u'upChannel' , u'Value' , 
			), 1, (1, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'Data' , u'spID' , u'chan' , u'Value' , ), 2, (2, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfChannels' , u'spID' , u'Value' , ), 3, (3, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'AutoScale' , u'Value' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'AutoScale' , u'Value' , ), 4, (4, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'BottomAxisMin' , u'Value' , ), 5, (5, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'BottomAxisMin' , u'Value' , ), 5, (5, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'BottomAxisMax' , u'Value' , ), 6, (6, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'BottomAxisMax' , u'Value' , ), 6, (6, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'LeftAxisMin' , u'Value' , ), 7, (7, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'LeftAxisMin' , u'Value' , ), 7, (7, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'LeftAxisMax' , u'Value' , ), 8, (8, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'LeftAxisMax' , u'Value' , ), 8, (8, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'DataArray' , u'spID' , u'Value' , ), 201, (201, (), [ (3, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'StartAcquisition' , u'Value' , ), 202, (202, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'EndAcquisition' , u'Value' , ), 203, (203, (), [ (16391, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Delete' , u'spID' , ), 204, (204, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'IDOfElement' , u'Z' , u'Value' , ), 205, (205, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'IDOfIsotope' , u'Z' , u'M' , u'Value' , ), 206, (206, (), [ 
			(3, 1, None, None) , (5, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
]

IStopping_vtables_dispatch_ = 1
IStopping_vtables_ = [
	(( u'StoppingInElement' , u'Z1' , u'M1' , u'E' , u'Z2' , 
			u'Value' , ), 1, (1, (), [ (3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , 
			(3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'StoppingInLayer' , u'Z1' , u'M1' , u'E' , u'id' , 
			u'lay' , u'Value' , ), 2, (2, (), [ (3, 1, None, None) , (5, 1, None, None) , 
			(5, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'StragglingInLayer' , u'Z1' , u'M1' , u'E' , u'id' , 
			u'lay' , u'Value' , ), 4, (4, (), [ (3, 1, None, None) , (5, 1, None, None) , 
			(5, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'EnergylossInLayer' , u'Z1' , u'M1' , u'E' , u'id' , 
			u'lay' , u'Value' , ), 3, (3, (), [ (3, 1, None, None) , (5, 1, None, None) , 
			(5, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

ITarget_vtables_dispatch_ = 1
ITarget_vtables_ = [
	(( u'LayerThickness' , u'lay' , u'Value' , ), 1, (1, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'LayerThickness' , u'lay' , u'Value' , ), 1, (1, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfLayers' , u'Value' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'LayerRoughness' , u'lay' , u'Value' , ), 3, (3, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'LayerRoughness' , u'lay' , u'Value' , ), 3, (3, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerRoughness' , u'lay' , u'Value' , ), 4, (4, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerRoughness' , u'lay' , u'Value' , ), 4, (4, (), [ (3, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'SubstrateRoughness' , u'Value' , ), 5, (5, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'SubstrateRoughness' , u'Value' , ), 5, (5, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'HasSubstrateRoughness' , u'Value' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'HasSubstrateRoughness' , u'Value' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfElements' , u'lay' , u'Value' , ), 7, (7, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'ElementConcentration' , u'lay' , u'el' , u'Value' , ), 9, (9, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'ElementConcentration' , u'lay' , u'el' , u'Value' , ), 9, (9, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'AddLayer' , u'Value' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'InsertLayer' , u'lay' , u'Value' , ), 11, (11, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'DeleteLayer' , u'lay' , u'Value' , ), 12, (12, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'AddElement' , u'lay' , u'Value' , ), 13, (13, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'DeleteElement' , u'lay' , u'el' , u'Value' , ), 14, (14, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'ElementName' , u'lay' , u'el' , u'Value' , ), 15, (15, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'ElementName' , u'lay' , u'el' , u'Value' , ), 15, (15, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'SubstrateRoughnessDistribution' , u'Value' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'SubstrateRoughnessDistribution' , u'Value' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'ElementAmount' , u'lay' , u'el' , u'Value' , ), 16, (16, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'ElementAmount' , u'lay' , u'el' , u'Value' , ), 16, (16, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'ReadLayer' , u'FileName' , u'LayerNr' , ), 17, (17, (), [ (8, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'SaveLayerAs' , u'FileName' , u'LayerNr' , ), 18, (18, (), [ (8, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'ReadTarget' , u'FileName' , ), 19, (19, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'SaveTargetAs' , u'FileName' , ), 20, (20, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerPorosity' , u'lay' , u'Value' , ), 201, (201, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerPorosity' , u'lay' , u'Value' , ), 201, (201, (), [ (3, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 4 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'PorosityFraction' , u'lay' , u'Value' , ), 202, (202, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'PorosityFraction' , u'lay' , u'Value' , ), 202, (202, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( u'PoreDiameter' , u'lay' , u'Value' , ), 203, (203, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'PoreDiameter' , u'lay' , u'Value' , ), 203, (203, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( u'TotalNumberOfElements' , u'Value' , ), 204, (204, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'DeleteAllLayer' , u'Value' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( u'Thickness' , u'Value' , ), 206, (206, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'StoppingFactor' , u'lay' , u'Z' , u'Value' , ), 207, (207, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( u'StoppingFactor' , u'lay' , u'Z' , u'Value' , ), 207, (207, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfIsotopes' , u'lay' , u'el' , u'Value' , ), 208, (208, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( u'IsotopeConcentration' , u'lay' , u'el' , u'iso' , u'Value' , 
			), 209, (209, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'IsotopeConcentration' , u'lay' , u'el' , u'iso' , u'Value' , 
			), 209, (209, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( u'IsotopeMass' , u'lay' , u'el' , u'iso' , u'Value' , 
			), 210, (210, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'IsotopeMass' , u'lay' , u'el' , u'iso' , u'Value' , 
			), 210, (210, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( u'AddIsotope' , u'lay' , u'el' , u'Value' , ), 211, (211, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'DeleteIsotope' , u'lay' , u'el' , u'iso' , u'Value' , 
			), 212, (212, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
]

ITargetOut_vtables_dispatch_ = 1
ITargetOut_vtables_ = [
	(( u'LayerThickness' , u'lay' , u'Value' , ), 201, (201, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'LayerThickness' , u'lay' , u'Value' , ), 201, (201, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfLayers' , u'Value' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfElements' , u'lay' , u'Value' , ), 203, (203, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'ElementConcentration' , u'lay' , u'el' , u'Value' , ), 204, (204, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'ElementConcentration' , u'lay' , u'el' , u'Value' , ), 204, (204, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'AddLayer' , u'Value' , ), 205, (205, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'InsertLayer' , u'lay' , u'Value' , ), 206, (206, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'DeleteLayer' , u'lay' , u'Value' , ), 207, (207, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'AddElement' , u'lay' , u'Value' , ), 208, (208, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'DeleteElement' , u'lay' , u'el' , u'Value' , ), 209, (209, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'ElementName' , u'lay' , u'el' , u'Value' , ), 210, (210, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'ElementName' , u'lay' , u'el' , u'Value' , ), 210, (210, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'CreateTargetOut' , ), 211, (211, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'DestroyTargetOut' , ), 212, (212, (), [ ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'Shift' , u'Value' , ), 213, (213, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Shift' , u'Value' , ), 213, (213, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'Thickness' , u'Value' , ), 214, (214, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'DeleteAllLayer' , u'Value' , ), 215, (215, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
]

IWindow_vtables_dispatch_ = 1
IWindow_vtables_ = [
	(( u'LayerThickness' , u'lay' , u'Value' , ), 201, (201, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( u'LayerThickness' , u'lay' , u'Value' , ), 201, (201, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfLayers' , u'Value' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( u'LayerRoughness' , u'lay' , u'Value' , ), 203, (203, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'LayerRoughness' , u'lay' , u'Value' , ), 203, (203, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerRoughness' , u'lay' , u'Value' , ), 204, (204, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerRoughness' , u'lay' , u'Value' , ), 204, (204, (), [ (3, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 4 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfElements' , u'lay' , u'Value' , ), 205, (205, (), [ (3, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'ElementConcentration' , u'lay' , u'el' , u'Value' , ), 206, (206, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( u'ElementConcentration' , u'lay' , u'el' , u'Value' , ), 206, (206, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AddLayer' , u'Value' , ), 207, (207, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( u'InsertLayer' , u'lay' , u'Value' , ), 208, (208, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'DeleteLayer' , u'lay' , u'Value' , ), 209, (209, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( u'AddElement' , u'lay' , u'Value' , ), 210, (210, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'DeleteElement' , u'lay' , u'el' , u'Value' , ), 211, (211, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( u'ElementName' , u'lay' , u'el' , u'Value' , ), 212, (212, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'ElementName' , u'lay' , u'el' , u'Value' , ), 212, (212, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( u'ElementAmount' , u'lay' , u'el' , u'Value' , ), 213, (213, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'ElementAmount' , u'lay' , u'el' , u'Value' , ), 213, (213, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( u'ReadLayer' , u'FileName' , u'LayerNr' , ), 214, (214, (), [ (8, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'SaveLayerAs' , u'FileName' , u'LayerNr' , ), 215, (215, (), [ (8, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( u'ReadWindow' , u'FileName' , ), 216, (216, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'SaveWindowAs' , u'FileName' , ), 217, (217, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerPorosity' , u'lay' , u'Value' , ), 218, (218, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'HasLayerPorosity' , u'lay' , u'Value' , ), 218, (218, (), [ (3, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 4 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( u'PorosityFraction' , u'lay' , u'Value' , ), 219, (219, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'PorosityFraction' , u'lay' , u'Value' , ), 219, (219, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( u'PoreDiameter' , u'lay' , u'Value' , ), 220, (220, (), [ (3, 1, None, None) , 
			(16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'PoreDiameter' , u'lay' , u'Value' , ), 220, (220, (), [ (3, 1, None, None) , 
			(5, 1, None, None) , ], 1 , 4 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( u'Thickness' , u'Value' , ), 221, (221, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'DeleteAllLayer' , u'Valu' , ), 222, (222, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( u'StoppingFactor' , u'lay' , u'Z' , u'Value' , ), 223, (223, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'StoppingFactor' , u'lay' , u'Z' , u'Value' , ), 223, (223, (), [ 
			(3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{58312EB5-30F5-47D1-8E60-04634C214FBD}' : Window,
	'{AB9D3C37-2FA9-434A-8959-8C84A8F50C97}' : Projectile,
	'{5DB47E27-5BA1-4FE3-8785-545F494FCBE2}' : ITargetOut,
	'{9F51F4E1-754F-11D5-B742-0040332FCEB4}' : IApp,
	'{9F51F4E3-754F-11D5-B742-0040332FCEB4}' : App,
	'{2C926AE5-0CDA-45F2-BD6B-70031EFFB199}' : IWindow,
	'{54207F20-9D23-11D5-B748-0040332FCEB4}' : IFit,
	'{54207F22-9D23-11D5-B748-0040332FCEB4}' : Fit,
	'{DF418CC3-A5C6-11D5-B749-0040332FCEB4}' : Spectrum,
	'{FF8D5AF3-63B8-42B5-B3EC-511F561E51F8}' : IFoil,
	'{E45540BA-A7B0-4033-9E6F-B26230D41F69}' : TargetOut,
	'{2486C206-2AE3-4D27-8B96-F3384714119A}' : IProjectile,
	'{C22A1430-9329-11D5-B743-0040332FCEB4}' : ISetup,
	'{C22A1432-9329-11D5-B743-0040332FCEB4}' : Setup,
	'{1C467EA5-494F-4FA4-A305-84183157CC48}' : ICrossSec,
	'{F14C14DC-62BD-4C60-9710-A05CA0151546}' : Foil,
	'{5978B7E1-9706-11D5-B747-0040332FCEB4}' : ITarget,
	'{5978B7E3-9706-11D5-B747-0040332FCEB4}' : Target,
	'{504EF515-68CF-495D-8D7C-C132E538D839}' : CrossSec,
	'{A9E30D30-9792-4EF5-B5FE-81446FF50084}' : IForms,
	'{DF418CC1-A5C6-11D5-B749-0040332FCEB4}' : ISpectrum,
	'{0A40E4F1-D298-11D5-B752-0040332FCEB4}' : IStopping,
	'{0A40E4F3-D298-11D5-B752-0040332FCEB4}' : Stopping,
	'{9DD33B20-A8EC-11D5-B749-0040332FCEB4}' : ICalc,
	'{9DD33B22-A8EC-11D5-B749-0040332FCEB4}' : Calc,
	'{E31D2D47-3E2E-418B-93E3-8A8C72A7E6C2}' : Forms,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{C22A1430-9329-11D5-B743-0040332FCEB4}' : 'ISetup',
	'{A9E30D30-9792-4EF5-B5FE-81446FF50084}' : 'IForms',
	'{DF418CC1-A5C6-11D5-B749-0040332FCEB4}' : 'ISpectrum',
	'{1C467EA5-494F-4FA4-A305-84183157CC48}' : 'ICrossSec',
	'{54207F20-9D23-11D5-B748-0040332FCEB4}' : 'IFit',
	'{5978B7E1-9706-11D5-B747-0040332FCEB4}' : 'ITarget',
	'{0A40E4F1-D298-11D5-B752-0040332FCEB4}' : 'IStopping',
	'{FF8D5AF3-63B8-42B5-B3EC-511F561E51F8}' : 'IFoil',
	'{9DD33B20-A8EC-11D5-B749-0040332FCEB4}' : 'ICalc',
	'{5DB47E27-5BA1-4FE3-8785-545F494FCBE2}' : 'ITargetOut',
	'{9F51F4E1-754F-11D5-B742-0040332FCEB4}' : 'IApp',
	'{2486C206-2AE3-4D27-8B96-F3384714119A}' : 'IProjectile',
	'{2C926AE5-0CDA-45F2-BD6B-70031EFFB199}' : 'IWindow',
}


NamesToIIDMap = {
	'ISetup' : '{C22A1430-9329-11D5-B743-0040332FCEB4}',
	'ICalc' : '{9DD33B20-A8EC-11D5-B749-0040332FCEB4}',
	'IStopping' : '{0A40E4F1-D298-11D5-B752-0040332FCEB4}',
	'ISpectrum' : '{DF418CC1-A5C6-11D5-B749-0040332FCEB4}',
	'IWindow' : '{2C926AE5-0CDA-45F2-BD6B-70031EFFB199}',
	'IFoil' : '{FF8D5AF3-63B8-42B5-B3EC-511F561E51F8}',
	'ICrossSec' : '{1C467EA5-494F-4FA4-A305-84183157CC48}',
	'ITargetOut' : '{5DB47E27-5BA1-4FE3-8785-545F494FCBE2}',
	'ITarget' : '{5978B7E1-9706-11D5-B747-0040332FCEB4}',
	'IApp' : '{9F51F4E1-754F-11D5-B742-0040332FCEB4}',
	'IProjectile' : '{2486C206-2AE3-4D27-8B96-F3384714119A}',
	'IForms' : '{A9E30D30-9792-4EF5-B5FE-81446FF50084}',
	'IFit' : '{54207F20-9D23-11D5-B748-0040332FCEB4}',
}


