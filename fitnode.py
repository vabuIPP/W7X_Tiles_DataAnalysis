class FitNode:

    def __init__(self):
        self.params = []
        self.refFile = ""

    del createCommonParams():
        param = {}
        param['SetRegionMinChannel'] = 400
        param['SetRegionMaxChannel'] = 600
        return param

    def getParams(self):
        return self.params
