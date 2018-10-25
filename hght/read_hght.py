import os
import struct

from .Hght import Hght


def read_hght(path: str, verbose=False, raw_height=False) -> list:
    height_array = []

    if os.path.exists(path):
        if verbose:
            print("Reading {}...".format(path))

        with open(path, 'rb') as infile:
            for _ in range(65536):
                height_data = struct.unpack('<H', infile.read(2))[0]

                if raw_height:
                    hght = Hght(height_data)
                else:
                    hght = Hght(Hght.to_float(height_data))

                height_array.append(hght)

    return height_array
