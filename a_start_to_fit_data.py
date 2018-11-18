import SimNRA
import sys
import os
#import raw_input

def getSpectra(path):
    aux = os.listdir(path)
    ret = []
    for c in aux:
        if (".CAM" in c):
            ret.append(path+"\\"+c)
    return ret

def getSpectrumFile(path):
    return [path]

def applyFit(app, fit, cspect, params):

    app.ReadSpectrumData(cspect, 2)

    fit.ParticlesSr = params["particles"]
    fit.LayerThickness = params["thickness"]
    fit.LayerRoughness = params["roughness"]
    
    fit.LayerNr = params["layer"]
    
    fit.NumberOfRegions = params["number_regions"]
    
    for i in range(len(params["regions_values"])):
        reg = params["regions_values"][i]
        fit.SetRegionMaxChannel(i+1, reg["max"])
        fit.SetRegionMinChannel(i+1, reg["min"])

    app.FitSpectrum()

def main():
    print "Parameters:"
    print "First parameter is the file where the fit is defined"
    print "Second parameter is the spectra folder, or spectrum file depending on what you have commented into the code"
    
    app = SimNRA.App() # The SimNRA app instance
    target = SimNRA.Target() # The SimNRA target instance
    spectrum = SimNRA.Spectrum() # The current SimNRA calculated/experimental spectrum
    setup = SimNRA.Setup()
    fit = SimNRA.Fit()
    app.Show()

    fit_file = str(raw_input("Enter the fit file .xnra"))
    spec_data = str(raw_input("Enter the spectrum data .CAM"))
    
    # Load template
    app.Open(fit_file, FileType = 2) # File format 2 is format .xnra

    # If you want to apply the fit to a set .CAM into a folder, use getSpectra functions. In the other hand, if you only want to apply
    # to a single .CAM file, use getSpectrum file. To change it, just comment one function and use the other.
    #spects = getSpectra(spec_data)
    spects = getSpectrumFile(spec_data)
    
    for spec in spects:

        print spec

        print "Write the minimum value of the region and the maximum for the fit particles. In this case, the width of the first Carbon layer."
        min = int(raw_input("Enter the minimum"))
        max = int(raw_input("Enter the maximum"))
        applyFit(app, fit, spec, { "particles": True, "thickness": False, "roughness": False, "layer": 1, "number_regions": 1, "regions_values": [{"min": min, "max":max}]})

        print "Layer Thickness of Carbon layer. Min and max value for the first carbon layer and min and max also for the tungsten platform"
        min1 = int(raw_input("Enter the minimum of first region"))
        max1 = int(raw_input("Enter the maximum of first region"))
        min2 = int(raw_input("Enter the minimum of second region"))
        max2 = int(raw_input("Enter the maximum of second region"))
        applyFit(app, fit, spec, { "particles": False, "thickness": True, "roughness": False, "layer": 1, "number_regions": 2, "regions_values": [{"min": min1, "max":max1},{"min": min2, "max": max2}]})

        print "Layer Thickness of Molibdenium. Min and max value for left and right hand side of peak"
        min = int(raw_input("Enter the minimum"))
        max = int(raw_input("Enter the maximum"))
        applyFit(app, fit, spec, { "particles": False, "thickness": True, "roughness": False, "layer": 2, "number_regions": 1, "regions_values": [{"min": min, "max": max}]})
        
        print "Layer Thickness and roughness of Carbon layer. Min and max value for the first carbon layer and min and max also for the tungsten platform, including the molibdenium right peak"
        min1 = int(raw_input("Enter the minimum of first region"))
        max1 = int(raw_input("Enter the maximum of first region"))
        min2 = int(raw_input("Enter the minimum of second region"))
        max2 = int(raw_input("Enter the maximum of second region"))
        applyFit(app, fit, spec, { "particles": False, "thickness": True, "roughness": True, "layer": 1, "number_regions": 2, "regions_values": [{"min": min1, "max":max1},{"min": min2, "max": max2}]})
        
        print "Layer Roughness of Molibdenium. Min and max value for left and right hand side of peak"
        min1 = int(raw_input("Enter the minimum of first region"))
        max1 = int(raw_input("Enter the maximum of first region"))
        min2 = int(raw_input("Enter the minimum of second region"))
        max2 = int(raw_input("Enter the maximum of second region"))
        applyFit(app, fit, spec, { "particles": False, "thickness": True, "roughness": True, "layer": 2, "number_regions": 2, "regions_values": [{"min": min1, "max":max1},{"min": min2, "max": max2}]})

        print "Particles * sr. Platform of first peak of Carbon"
        min = int(raw_input("Enter the minimum"))
        max = int(raw_input("Enter the maximum"))
        applyFit(app, fit, spec, { "particles": True, "thickness": False, "roughness": False, "layer": 1, "number_regions": 1, "regions_values": [{"min": min, "max": max}]})
        #applyFit(app, fit, spec, { "particles": False, "thickness": False, "roughness": True, "layer": 1, "number_regions": 2, "regions_values": []})
        #applyFit(app, fit, spec, { "particles": False, "thickness": True, "roughness": True, "layer": 1, "number_regions": 2, "regions_values": []})

        app.SaveAs(spec[0:-4]+".xnra") # spec is a string, i.e. array of chars, and tells it to save it with the same name form position 0 to position n-1 (so it removes the xnra)

if __name__== "__main__": #sentence to apply the code. Mo more relevance

  main()

