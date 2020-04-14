import numpy
import json


def modify_settings_ms(settings, ms_media, wavelength):
    for i, __ in enumerate(settings["Domain"]["Media"]):
        settings["Domain"]["Media"][i]["mua"] = ms_media[i](wavelength)
    return settings


def load_mcx_settings(filename: str) -> dict:
    with open(filename, "r") as f:
        return json.load(f)


def write_mcx_settings(settings: dict, filename: str):
    with open(filename, "w") as f:
        return json.dump(settings, f)


def gen_volume_file(array: numpy.ndarray, filename: str, dtype: str = "uint8"):
    """

    Parameters
    ----------
    array : numpy.ndarray
    filename : str
    dtype : str
    """
    array = array.astype(dtype)
    array_bytes = array.tobytes("F")
    with open(filename, "wb") as f:
        f.write(array_bytes)


def read_output_file(filename: str, mcx_settings: dict) -> numpy.ndarray:
    """

    Parameters
    ----------
    filename : str
    mcx_settings : dict

    Returns
    -------
    numpy.ndarray
    """
    dimension = tuple(mcx_settings["Domain"]["Dim"])
    return numpy.fromfile(filename, dtype="single").reshape(dimension + (-1,), order="F")
