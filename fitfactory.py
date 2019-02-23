from win32com.client import Dispatch
import numpy as np
import custom as cs

class FitFactory:

	def __init__(self):
		# physical constraints
		self.maxC = 615
		self.minMo = 675
		self.maxMo = 825
		# human induced constraints
		self.lowC = 400
		self.upC = 600
		self.surfaceMoLow = 805
		self.surfaceMoUp = 810
		self.decisionParameterIntegratedMo = 3000
		# variable iniciations
		self.decision_coeff = 0
		self.surface_Mo = 0

	## Builds the criteria to choose the fitting that will be dona
	def buildCriteria(self, file):
		SimApp = Dispatch("Simnra.App")
		SimSpec = Dispatch("Simnra.Spectrum")

		a = SimApp.OpenAs(file, 2)
		print a
		experimental_spectrum = np.asarray(SimSpec.DataArray(1))

		x = np.linspace(1,len(experimental_spectrum),len(experimental_spectrum))
		experimental_spectrum_segment = cs.spline_bayesian(x,experimental_spectrum)
		min_val = np.argmin(experimental_spectrum[self.lowC:self.upC])
		self.channel_dip = self.lowC + min_val

		## Classification
		self.surface_Mo = np.sum(experimental_spectrum[self.surfaceMoLow:self.surfaceMoUp])

		# Has C layer been fully sputtered (Y/N)
		min = self.lowC+25
		max = self.upC

		Int_Exp = SimSpec.Integrate(1,min,max)
		Int_Sim = SimSpec.Integrate(2,min,max)
		print Int_Exp
		print Int_Sim
		self.decision_coeff = Int_Exp / Int_Sim

		del SimApp, SimSpec
		return self.surface_Mo, self.decision_coeff, self.channel_dip

	## Returns the FitNode with the data that will be performed
	def decideCase(self, data_loc):
		SimSpec = Dispatch("Simnra.Spectrum")
		SimTar = Dispatch("Simnra.Target")
		SimApp = Dispatch("Simnra.App")
		if (self.decision_coeff > 0.95) or (self.channel_dip > 570) or (self.channel_dip < 410) or (self.surface_Mo > 100) or ((self.channel_dip < 420) and (self.surface_Mo > 50)): # Y, it has been full sputtered

			integratedExperimentalMoSpectrum = SimSpec.Integrate(1,self.minMo,self.maxMo)

			m = 0.092
			if integratedExperimentalMoSpectrum < self.decisionParameterIntegratedMo:
				print("This is C_Mo_thin case")
				SimTar.ReadTarget('.\\C_Mo_thin.xtarget')
				c = 20
				Mo_estimator = integratedExperimentalMoSpectrum * m - c

				self.fit_type = "C_Mo_thin"
			else:
				print("This is C_Mo case")
				SimTar.ReadTarget('.\\C_Mo.xtarget')
				Mo_estimator = integratedExperimentalMoSpectrum * m

				self.fit_type = "C_Mo"

			##--workaround
			SimApp.SaveAs(data_loc[0:-5]+'_fit_molay.xnra')
			SimApp.OpenAs(data_loc[0:-5]+'_fit_molay.xnra', 2)
			##--workaround

			SimTar.SetElementAmount(1, 2, Mo_estimator)
			SimCr.SelectRutherford(42)

			SimFit.NumberOfRegions = 1
			SimFit.SetRegionMinChannel(1, self.lowMo)
			SimFit.SetRegionMaxChannel(1, self.maxMo)
			SimFit.LayerNr = 1
			fit_success_caseA_1 = SimApp.FitSpectrum()
			fit_success = fit_success_caseA_1
			step.append(fit_success_caseA_1)

			SimFit.NumberOfRegions = 2
			SimFit.SetRegionMinChannel(1, self.lowC)
			SimFit.SetRegionMaxChannel(1, self.maxC)
			SimFit.SetRegionMinChannel(2, self.lowMo)
			SimFit.SetRegionMaxChannel(2, self.maxMo)
			SimFit.LayerNr = 1
			fit_success_caseA_2 = SimApp.FitSpectrum()
			fit_success = fit_success and fit_success_caseA_2
			step.append(fit_success_caseA_2)

		else:
			print("This is C_Mo_C case")
			self.fit_type = "C_Mo_C"
			SimTar.ReadTarget('.\\C_Mo_C.xtarget')

			##--workaround
			SimApp.SaveAs(data_loc[0:-5]+'_fit_molay.xnra')
			SimApp.OpenAs(data_loc[0:-5]+'_fit_molay.xnra', 2)
			##--workaround

			SimCr.SelectRutherford(42)
			SimTar.SetLayerThickness(3,0.0)
			#set fit parameters
			lowC_cover = self.channel_dip

			layerthickness = abs((lowC_cover - maxC)) * 530.0 - 5500.0

			SimTar.SetLayerThickness(1,layerthickness)
			lowMo = 665
			SimApp.CalculateSpectrum()

			for fit_accuracy in list_fit_accuracy:
				SimFit.Accuracy = fit_accuracy

				#fit Mo-layer thickness
				SimFit.NumberOfRegions = 1
				SimFit.SetRegionMinChannel(1, lowMo)
				SimFit.SetRegionMaxChannel(1, maxMo)
				SimFit.LayerNr = 2
				fit_success_caseB_1 = SimApp.FitSpectrum()
				fit_success = fit_success_caseB_1
				#step.append(fit_success_caseB_1)

				#fit C-layer thickness
				SimFit.NumberOfRegions = 1
				SimFit.SetRegionMinChannel(1, lowC_cover)
				SimFit.SetRegionMaxChannel(1, maxC)
				SimFit.LayerNr = 1
				fit_success_caseB_2 = SimApp.FitSpectrum()
				fit_success = fit_success and fit_success_caseB_2

				#fit Mo/C-layer thickness
				SimFit.Chi2Evaluation = 1
				SimFit.NumberOfRegions = 1
				SimFit.SetRegionMinChannel(1, lowMo)
				SimFit.SetRegionMaxChannel(1, maxMo)
				SimFit.LayerNr = 2

			SimTar.SetLayerThickness(3,1e7)
			SimApp.CalculateSpectrum()

		SimApp.SaveAs(data_loc[0:-5]+'_fit_molay.xnra')
		SimApp.LastMessage

		if fit_success != True:
			number_of_errors += 1
			print "The fit of "+ file +" failed to converge. Fit Class " + self.fit_type

		del SimSpec, SimTar, SimApp
		return self.self.fit_type
