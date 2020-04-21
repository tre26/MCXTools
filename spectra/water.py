# https://omlc.org/spectra/melanin/opticaldepth.html
# G. M. Hale and M. R. Querry, "Optical constants of water in the 200nm to
# 200 micron wavelength region," Appl. Opt., 12, 555--563, (1973).

import pandas as pd
import os.path
from scipy.interpolate import interp1d


def water_mu_a(wavelength):
    # Units = m^(-1)
    # G. M. Hale and M. R. Querry, "Optical constants of water in the 200nm to
    # 200 micron wavelength region," Appl. Opt., 12, 555--563, (1973).
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "water.csv")
    t = pd.read_csv(file)
    ws = t[t.columns[0]]
    e_h2o = t[t.columns[1]] * 100
    mu_h2o = interp1d(ws, e_h2o)
    return mu_h2o(wavelength * 1e9)
