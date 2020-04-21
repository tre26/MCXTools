def melanosome_mu_a(wavelength, pigment="tanned"):
    # Pigment is the melanosome volume fraction
    # m^(-1)
    # [1] S. L. Jacques, “Optical properties of biological tissues:
    # A review,” Physics in Medicine and Biology, vol. 58, no. 11. pp. R37–R61, 07-Jun-2013.
    scales = {"light": 0.02, "tanned": 0.13, "dark": 0.3}
    if pigment in scales:
        scale = scales[pigment]
    else:
        scale = pigment
    return scale * 519 * (wavelength*1e9/500)**(-3) * 100
