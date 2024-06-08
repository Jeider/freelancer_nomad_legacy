import sys
import glob
from PIL import Image

THE_PATH = 'E:/FL/IMG_OUT/BOLT/*.png'
OUT_IMAGE = 'E:/FL/IMG_OUT/VID_RESULT/merged_image_bolt_{index}.png'

FRAME_SIZE = 1024
FRAMES_PER_LINE = 8
TOTAL_SIDE = FRAME_SIZE * FRAMES_PER_LINE
FRAMES_PER_FILE = 128
MAX_FRAMES = 64


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
    frames_count = 0
    file_index = 0

    for image in images:
        frames_count += 1
        print(frames_count)
        if frames_count > FRAMES_PER_FILE:
            new_image.save(OUT_IMAGE.format(index=file_index))
            new_image = Image.new('RGB', (TOTAL_SIDE, TOTAL_SIDE))
            pos_x = 0
            pos_y = 0
            file_index += 1
            print(file_index)
            frames_count = 1

        if pos_y >= TOTAL_SIDE:
            pos_y = 0
            pos_x += FRAME_SIZE
        new_image.paste(image, (pos_y, pos_x))
        pos_y += FRAME_SIZE

    new_image.save(OUT_IMAGE.format(index=file_index))


def get_frames():
    step = 0.125

    startU = 0.0
    startV = 1.0
    endU = step
    endV = 1 - step

    frames_count = 0
    total_frames_count = 0
    file_index = 0.0

    results = []

    for _ in get_images():

        frames_count += 1
        total_frames_count += 1
        if total_frames_count > MAX_FRAMES:
            break
        if frames_count > FRAMES_PER_FILE:
            startU = 0
            startV = 1
            endU = step
            endV = 1 - step
            file_index += 1
            frames_count = 1

        results += [file_index, startU, startV, endU, endV]

        startU += step
        endU += step

        if startU >= 1:
            startU = 0
            endU = step
            startV -= step
            endV -= step

    return results

def get_frames_ints():
    data = [
        '0',
        '0',
        '1065353216',
        '1048576000',
        '1061158912',
        '0',
        '1048576000',
        '1065353216',
        '1056964608',
        '1061158912',
        '0',
        '1056964608',
        '1065353216',
        '1061158912',
        '1061158912',
        '0',
        '1061158912',
        '1065353216',
        '1065353216',
        '1061158912',
        '0',
        '0',
        '1061158912',
        '1048576000',
        '1056964608',
        '0',
        '1048576000',
        '1061158912',
        '1056964608',
        '1056964608',
        '0',
        '1056964608',
        '1061158912',
        '1061158912',
        '1056964608',
        '0',
        '1061158912',
        '1061158912',
        '1065353216',
        '1056964608',
        '0',
        '0',
        '1056964608',
        '1048576000',
        '1048576000',
        '0',
        '1048576000',
        '1056964608',
        '1056964608',
        '1048576000',
        '0',
        '1056964608',
        '1056964608',
        '1061158912',
        '1048576000',
        '0',
        '1061158912',
        '1056964608',
        '1065353216',
        '1048576000',
        '0',
        '0',
        '1048576000',
        '1048576000',
        '0',
        '0',
        '1048576000',
        '1048576000',
        '1056964608',
        '0',
        '0',
        '1056964608',
        '1048576000',
        '1061158912',
        '0',
        '0',
        '1061158912',
        '1048576000',
        '1065353216',
        '0',
        '1065353216',
        '0',
        '1065353216',
        '1048576000',
        '1061158912',
        '1065353216',
        '1048576000',
        '1065353216',
        '1056964608',
        '1061158912',
        '1065353216',
        '1056964608',
        '1065353216',
        '1061158912',
        '1061158912',
        '1065353216',
        '1061158912',
        '1065353216',
        '1065353216',
        '1061158912',
        '1065353216',
        '0',
        '1061158912',
        '1048576000',
        '1056964608',
        '1065353216',
        '1048576000',
        '1061158912',
        '1056964608',
        '1056964608',
        '1065353216',
        '1056964608',
        '1061158912',
        '1061158912',
        '1056964608',
        '1065353216',
        '1061158912',
        '1061158912',
        '1065353216',
        '1056964608',
        '1065353216',
        '0',
        '1056964608',
        '1048576000',
        '1048576000',
        '1065353216',
        '1048576000',
        '1056964608',
        '1056964608',
        '1048576000',
        '1065353216',
        '1056964608',
        '1056964608',
        '1061158912',
        '1048576000',
        '1065353216',
        '1061158912',
        '1056964608',
        '1065353216',
        '1048576000',
        '1065353216',
        '0',
        '1048576000',
        '1048576000',
        '0',
        '1065353216',
        '1048576000',
        '1048576000',
        '1056964608',
        '0',
        '1065353216',
        '1056964608',
        '1048576000',
        '1061158912',
        '0',
        '1065353216',
        '1061158912',
        '1048576000',
        '1065353216',
        '0',
    ]

    float_indices = {
        '0': '0',
        '1065353216': '1',
        '1073741824': '2',
    }

    new_data = []

    index = 1
    max_index = 5
    for item in data:
        new_data.append(
            item if index != 1 else float_indices[item]
        )

        index += 1
        if index > max_index:
            index = 1

    return new_data

