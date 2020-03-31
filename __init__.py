def gen_volume_file(array, filename):
    from numpy import uint8
    array = array.astype(uint8)
    bytes = array.tobytes("F")
    with open(filename, "wb") as f:
        f.write(bytes)


def read_output_file(filename, mcx_settings):
    pass
