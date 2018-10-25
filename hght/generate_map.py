from PIL import Image


def generate_map(data: list, outfile: str, image_base_color=(0, 0, 0)):
    if len(data) != 65536:
        if len(data) < 65536:
            print("Error 2001: Data list is not long enough. Expected 65536 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 65536 but saw {}".format(len(data)))
        exit(2002)

    height_map_image = Image.new("RGB", (256, 256), image_base_color)

    for index in range(65536):
        x = index % 256
        y = index // 256

        color_value = round(data[index].height / 800.0 * 255)
        color = (color_value, color_value, color_value)

        height_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    height_map_image.save(outfile)
