from PIL import Image
import os
import random
import sys

TILES_PATH = "./BLUE"

def concatenate(im1, im2, im3, im4):
    dst = Image.new('RGB', (im1.width * 2, im1.height * 2))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.paste(im3, (0, im1.height))
    dst.paste(im4, (im1.width, im1.height))
    return dst

def random_rotation(im):
    angle = 90 * random.randint(0,3)
    return im.rotate(angle)

def get_tile_list():
    tiles = os.listdir(TILES_PATH)
    return tiles

def select_tiles(tiles):
    options = list(tiles)
    selection = []
    for i in range(0,4):
        sel = random.randint(0, len(options)-1)
        selection.append(options[sel])
        del options[sel]
    return selection

def load_images(names):
    images = []
    for name in names:
        path = os.path.join(TILES_PATH, name)
        img = Image.open(path)
        images.append(img)
    return images

def render_quarter(tiles):
    selection = select_tiles(tiles)
    images = load_images(selection)
    for i in range (0, len(selection)):
        images[i] = random_rotation(images[i])
    return concatenate(images[0], images[1], images[2], images[3])

def main():
    global TILES_PATH
    outputname = "mapa_generado.png"
    if len(sys.argv) == 3:
        TILES_PATH = os.path.join(".", sys.argv[1])
        outputname = sys.argv[2] + ".png"
    if len(sys.argv) == 2:
        outputname = sys.argv[1] + ".png"

    tiles = get_tile_list()
    quarters = []
    for i in range(0,4):
        print("Rendering quarter", i+1)
        quarters.append(render_quarter(tiles))

    print("Saving final level map")
    level = concatenate(quarters[0], quarters[1], quarters[2], quarters[3])
    level.save(outputname)
    for i in range(0,4):
        print("Saving quarter {0}".format(i+1))
        quarters[i].save("Q{0}_".format(i+1) + outputname)

if __name__ == "__main__":
    main()