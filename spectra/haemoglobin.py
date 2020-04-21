import pandas as pd
import os.path
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
from spectra.melanin import *
from spectra.water import *


def blood_water_vol_frac(hmtcrit):
    f_plasma = 0.9
    f_rbc = 0.66
    return (1 - hmtcrit) * f_plasma + hmtcrit * f_rbc  # the volume fraction of water in blood.


def blood_mu_a(wavelength, so2=1, haematocrit=0.45, water=True):
    assert 1 >= so2 >= 0
    # Haematocrit = 45%
    # [1] N. Bosschaart, G. J. Edelman, M. C. G. Aalders, T. G. Van Leeuwen, and D. J. Faber,
    # “A literature review and novel theoretical approach on the optical properties of whole blood,”
    # Lasers Med. Sci., vol. 29, no. 2, pp. 453–479, Oct. 2014.
    # Units = m^(-1)
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "haemoglobin.csv")
    t = pd.read_csv(file, skiprows=2, thousands=",")
    ws = t[t.columns[0]]
    e_hb = t[t.columns[2]] * 1000
    mu_hb = interp1d(ws, e_hb)
    e_hbo2 = t[t.columns[1]] * 1000
    mu_hbo2 = interp1d(ws, e_hbo2)
    # The spectra above include the water content of the blood.
    mu_a = (1 - so2) * mu_hb(wavelength * 1e9) + so2 * mu_hbo2(wavelength * 1e9)
    mu_a_h2o = water_mu_a(wavelength)
    f = blood_water_vol_frac(0.45)
    f_h = blood_water_vol_frac(haematocrit)
    mu_a_corr = haematocrit * (mu_a - mu_a_h2o * f) / 0.45
    if water:
        mu_a_corr += mu_a_h2o * f_h
    return mu_a_corr


if __name__ == "__main__":
    wavelengths = np.linspace(500, 1500, num=100) * 1e-9
    for so2 in np.linspace(0, 1, num=4):
        plt.semilogy(1e9 * wavelengths, blood_mu_a(wavelengths, so2, water=False, haematocrit=1))
        #plt.semilogy(1e9 * wavelengths, blood_mu_a(wavelengths, so2, water=True))
    plt.semilogy(1e9 * wavelengths, melanosome_mu_a(wavelengths, 1))
    plt.semilogy(1e9 * wavelengths, water_mu_a(wavelengths))
    plt.xlabel("Wavelength / $nm$")
    plt.ylabel(r"Absorption coefficient / $m^{-1}$")
    plt.show()
