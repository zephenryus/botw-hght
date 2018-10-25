import struct

from .Hght import Hght


def write_hght(data: list, outfile_name: str) -> None:
    hght_binary = compile_hght(data)

    with open(outfile_name, 'wb+') as outfile:
        outfile.write(hght_binary)


def compile_hght(data: list) -> bytes:
    if len(data) != 65536:
        if len(data) < 65536:
            print("Error 2001: Data list is not long enough. Expected 65536 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 65536 but saw {}".format(len(data)))
        exit(2002)

    hght_binary = b''
    for index in range(65536):
        height = Hght.to_int(data[index].height)
        hght_binary += struct.pack('>H', height)

    return hght_binary
