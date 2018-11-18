class FitNode:

    def __init__(self):
        self.params = []
        self.refFile = ""

    del createCommonParams():
        param = {}
        param['SelectRutherford'] = 42
        param['NumberOfRegions'] = 1
        param['SetRegionMinChannel'] = 400
        param['SetRegionMaxChannel'] = 600

        return param

    def getParams(self):
        return self.params
