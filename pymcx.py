import numpy


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
    dimension = mcx_settings["Domain"]["Dim"]
    return numpy.fromfile(filename, dtype="single").reshape(dimension + (-1,), order="F")
