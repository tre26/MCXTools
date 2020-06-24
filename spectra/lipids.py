import os
import pandas as pd
from scipy.interpolate import interp1d

def lipid_mu_a(wavelength):
    # [1] https://omlc.org/spectra/fat/
    # Units = m^(-1)
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lipids.txt")
    t = pd.read_csv(file, skiprows=6)
    ws = t[t.columns[0]]
    mu = t[t.columns[1]] * 1000
    mu_a = interp1d(ws, mu)
    return mu_a(wavelength*1e9)
