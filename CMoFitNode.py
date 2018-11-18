from fitnode import FitNode

class CMoFitNode(FitNode):

    def __init__(self, Mo_estimator):
        self.refFile = 'C_Mo.xtarget'
        first = self.createCommonParams()
        first['SetElementAmount'] = Mo_estimator

    def doFit(self):
        SimTar.ReadTarget(self.refFile)
        ##--workaround
        SimApp.SaveAs(data_loc[0:-5]+'_fit_molay.xnra')
        SimApp.OpenAs(data_loc[0:-5]+'_fit_molay.xnra', 2)
        ##--workaround

        SimTar.SetElementAmount(1, 2, self.Mo_estimator)
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
