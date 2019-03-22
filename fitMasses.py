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

    # estimates the fit parameters for the given range to ensure good starting conditions
    def estimate_start_parameters(self, apply=True):
        intensity = np.amax(self.YDAT)
        x0 = np.amin(self.XDAT) + 0.5*(np.amax(self.XDAT) - np.amin(self.XDAT))
        constBkg = np.amin(self.YDAT)
        broadening = 0.33*np.abs(np.amax(self.XDAT) - np.amin(self.XDAT))
        params = self.FFDICT['start_parameters']
        intensity -= constBkg
        try:
            i_intensity = self.FFDICT['parameter_names'].index('intensity')
            params[i_intensity] = intensity
        except:
            print('no intensity parameter found')
        try:
            i_broadening = self.FFDICT['parameter_names'].index('broadening')
            params[i_broadening] = broadening
        except:
            print("No broadening parameter found")
        try:
            i_x0 = self.FFDICT['parameter_names'].index('x0')
            params[i_x0] = x0
        except:
            print("No x0 parameter found")
        try:
            i_constBkg = self.FFDICT['parameter_names'].index('const_background')
            params[i_constBkg] = constBkg
        except:
            print("No const_background parameter found")
        if apply:
            self.FFDICT['start_parameters'] = params
        return params

    # performs the fitting procedure
    def do_fit(self):
        function = self.FFDICT['function']
        start_parameters = self.FFDICT['start_parameters']
        boundaries = self.FFDICT['bounds']
        self.POPT, self.PCOV = curve_fit(function, self.XDAT, self.YDAT, p0=start_parameters, bounds=boundaries)
        return self.POPT, self.PCOV

    # gives the fit result for the x-values given in xdat
    def fitcurve(self, xdat):
        ydat = [self.FFDICT['function'](x, *self.POPT) for x in xdat]
        return np.array(ydat)



if __name__ == "__main__":
    pass