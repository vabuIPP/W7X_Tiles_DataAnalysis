from fitnode import FitNode

class ExampleFitNode(FitNode):

    def __init__(self):
        self.data = []
        self.data.append(self.createCommonData())
