import sys
import glob
from PIL import Image

THE_PATH = 'E:/FL/IMG_OUT/VID_EXP/*.png'
OUT_IMAGE = 'E:/FL/IMG_OUT/merged_image.png'

FRAME_SIZE = 512
FRAMES_PER_LINE = 16
TOTAL_SIDE = FRAME_SIZE * FRAMES_PER_LINE


def get_images():
    images = []
    for filename in glob.glob(THE_PATH):
        images.append(Image.open(filename))
    return images


def build_image():
    images = get_images()

    new_image = Image.new('RGB', (TOTAL_SIDE, TOTAL_SIDE))

    pos_x = 0
    pos_y = 0

    for image in images:
        if pos_y >= TOTAL_SIDE:
            pos_y = 0
            pos_x += FRAME_SIZE
        new_image.paste(image, (pos_y, pos_x))
        pos_y += FRAME_SIZE

    new_image.save(OUT_IMAGE)


def get_frames():
    step = 0.0625

    startU = 0
    startV = 1
    endU = step
    endV = 1 - step

    results = []

    for _ in get_images():
        results += [0, startU, startV, endU, endV]

        startU += step
        endU += step

        if startU >= 1:
            startU = 0
            endU = step
            startV -= step
            endV -= step

    return results
