from fitnode import FitNode

class ExampleFitNode(FitNode):

    def __init__(self):
        self.params = []
        params1 = self.createCommonParams())
        self.params.append(params1)
        self.refFile = "file where is the reference"
