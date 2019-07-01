import numpy as np
import matplotlib.pyplot as plt


### --- DEFINE FITTING FUNCTIONS --- ###
def linear(x, a0, a1, a2):
    return a0 * (x - a1) + a2

def quadratic(x, a0, a1, a2):
    return a0 * (x - a1)**2 + a2

def lorentzian(x, a0, a1, a2, a3, a4):
    return a0*(np.pi*a1)**(-1)*(a1**2 / ((x - a2)**2 + a1**2)) + a3 * (x - a2) + a4

def gaussian(x, a0, a1, a2, a3, a4):
    return a0*(a1*np.sqrt(2.*np.pi))**(-1)*np.exp(-0.5*((x - a2)/a1)**2) + a3 * (x - a2) + a4
    
def mexican_hat(x, a0, a1, a2, a3):
    return a0*(-(x - a2)**2 + a1*(x-a2)**4) + a3


### --- COMBINE FITTING FUNCTIONS WITH DICTIONARIES FOR THEIR NAME, STARTING PARAMETERS, TEMPLATE, ETC. --- ###
linear_dict = {
    'function' : linear,
    'name' : 'linear',
    'function_template': 'a0*(x-a1) + a2',
    'start_parameters' : [1., 1., 1.],
    'parameter_names' : ['intensity', 'x0', 'const_background'],
    'bounds' : ([-np.inf, -np.inf, -np.inf], [np.inf, np.inf, np.inf])
}

quadratic_dict = {
    'function' : quadratic,
    'name' : 'quadratic',
    'function_template' : 'a0 * (x-a1)**2 + a2',
    'start_parameters' : [1., 1., 1.],
    'parameter_names' : ['intensity', 'x0', 'const_background'],
    'bounds' : ([-np.inf, -np.inf, -np.inf], [np.inf, np.inf, np.inf])
}

mexican_dict = {
    'function' : mexican_hat,
    'name' : 'mexican',
    'function_template' : 'a0 * [-(x-a2)**2 + a1 * (x-a2)**4] + a3',
    'start_parameters' : [1., 50., 0., 0.],
    'parameter_names' : ['intensity', 'fraction_mexican', 'x0', 'const_background'],
    'bounds' : ([-np.inf, -np.inf, -np.inf, -np.inf], [np.inf, np.inf, np.inf, np.inf])
}

lorentzian_dict = {
    'function' : lorentzian,
    'name' : 'lorentzian',
    'function_template' : 'a0*(1/(pi*a1))*(a1^2/((x-a2)^2+a1^2)) + a3*(x-a2) + a4',
    'start_parameters' : [1., 1., 1., 1., 1.],
    'parameter_names' : ['intensity', 'broadening', 'x0', 'slope_linear_background', 'const_background'],
    'bounds' : ([-np.inf, -np.inf, -np.inf, -np.inf, -np.inf], [np.inf, np.inf, np.inf, np.inf, np.inf])
}

gaussian_dict = {
    'function' : gaussian,
    'name' : 'gaussian',
    'function_template' : 'a0*(1/(a1*sqrt(2*pi)))*exp(-0.5*((x-a2)/a1)^2) + a3*(x-a2)+a4',
    'start_parameters' : [1., 1., 1., 1., 1.],
    'parameter_names' : ['intensity', 'broadening', 'x0', 'slope_linear_background', 'const_background'],
    'bounds' : ([-np.inf, -np.inf, -np.inf, -np.inf, -np.inf], [np.inf, np.inf, np.inf, np.inf, np.inf])
}


### --- PUT ALL FITTING FUNCTIONS INTO A LIST FOR LATER USE --- ###
fitfunc_dict = {
    'linear' : linear_dict,
    'quad' : quadratic_dict,
    'lorentz' : lorentzian_dict,
    'gauss' : gaussian_dict,
    'mexican' : mexican_dict
}