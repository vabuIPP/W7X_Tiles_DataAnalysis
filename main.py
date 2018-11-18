from fitfactory import FitFactory


def doFitting(param):
    print("I'm working")

def fitSimFit(data):
    SimFit.SetRegionMinChannel('SetRegionMinChannel')

def main():

    for f in files:

        ffactory = FitFactory()
        ffactory.buildCriteria(f)
        node = ffactory.decideCase()
        for param in node.data:
            fitSimFit(data)
            SimApp.FitSpectrum()
            #TODO implement each fit process

if __name__ == '__main__':
    main()
