import numpy as np
import matplotlib.pyplot as plt

def build_fitfunction_from_dict(func_dict):
    # build the def part of the method
    def_part = "def general_function(x"
    number_of_parameters = len(func_dict['start-values'])

    for val,num in zip(func_dict['start-values'], range(number_of_parameters)):
        def_part += ', a%i = %f' % (num, val)
    def_part += "):\n\t"
    func = def_part + "return " + func_dict['function']
    print("generating function:\n", func)
    d = {}
    exec(func) in d
    print(d)
    print(d['general_function'](5.))

if __name__ == "__main__":
    dict_example = {
        'function' : "a0 * x + a1",
        'start-values' : [1., 1.]
        }
    build_fitfunction_from_dict(dict_example)