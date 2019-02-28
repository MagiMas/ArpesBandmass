from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as pyplot


class FitClass:
    def __init__(self, xdata, ydata, fitdictionary):
        self.XDAT = xdata
        self.YDAT = ydata
        self.FFDICT = fitdictionary
        self.XFIT = []
        self.YFIT = []
        self.POPT, self.PCOV = None, None

    def do_fit(self):
        function = self.FFDICT['function']
        start_parameters = self.FFDICT['start_parameters']
        boundaries = self.FFDICT['bounds']
        self.POPT, self.PCOV = curve_fit(function, self.XDAT, self.YDAT, p0=start_parameters, bounds=boundaries)
        return self.POPT, self.PCOV

    def fitcurve(self, xdat):
        ydat = [self.FFDICT['function'](x, *self.POPT) for x in xdat]
        return np.array(ydat)



if __name__ == "__main__":
    pass