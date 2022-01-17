import os.path

from PIL import Image


def add_watermark(in_file):
    photo = Image.open(in_file)
    watermark = Image.open(os.path.join(os.getcwd(), 'watermark/Watermark.png'))
    photo.paste(watermark, (0, 0), watermark)
    photo.save(in_file)

