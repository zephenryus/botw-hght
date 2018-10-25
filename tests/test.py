import filecmp
import hashlib
import json

import hght


def hght_to_json():
    """
    Tests reading of hght file and exports data as a json file
    """
    data = hght.read_hght("assets/5000000000.hght")

    print("Saving file output/5000000000.hght.json...")
    with open("output/5000000000.hght.json", "w+") as outfile:
        out_obj = []
        for entry in data:
            out_obj.append(entry.height)

        outfile.write(json.dumps(out_obj, indent=4, separators=(',', ': ')))


def hght_to_binary_string():
    """
        Tests that data is recompiled correctly and matches the original file
        """
    data = hght.read_hght("assets/5000000000.hght")
    binary_data = hght.compile_hght(data)

    hash_md5 = hashlib.md5()
    with open("assets/5000000000.hght", "rb") as infile:
        for chunk in iter(lambda: infile.read(4096), b""):
            hash_md5.update(chunk)

    file_hash = hash_md5.hexdigest()

    hash_md5 = hashlib.md5()
    pos = 0
    for chunk in iter(lambda: binary_data[pos:pos + 4096], b""):
        pos += 4096
        hash_md5.update(chunk)

    string_hash = hash_md5.hexdigest()

    print("The file and binary string are the same: {0}".format(file_hash == string_hash))


def hght_to_binary_file():
    """
    Tests reading data from mate file then writes the same data back as a binary
    """
    data = hght.read_hght("assets/5000000000.hght")
    hght.write_hght(data, "output/5000000000.hght")
    print("The files are the same: {0}".format(filecmp.cmp("assets/5000000000.hght", "output/5000000000.hght")))


def hght_to_image():
    """
    Tests reading data from hght file then generating height map images
    """
    data = hght.read_hght("assets/5000000000.hght")
    hght.generate_map(data, 'output/5000000000.hght.tiff')


def main():
    # hght_to_json()
    # hght_to_binary_string()
    # hght_to_binary_file()
    hght_to_image()


if __name__ == "__main__":
    main()
