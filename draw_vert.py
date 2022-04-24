from PIL import Image
import random

def draw_image_vert(colors):
    # background
    width_bg = 4000
    height_bg = 4000
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color='grey')

    # pixel
    width_pixel = 100
    height_pixel = 100
    color_pixel = colors

    # count
    width_count = width_bg // width_pixel
    height_count = height_bg // height_pixel

    if width_count >= height_count:
        for i in range(width_count * 2):
            pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=(random.choice(color_pixel)))
            for j in range(height_count * 2):
                im1.paste(pixel_, (int(pixel_.size[0] / 2) * i, int(pixel_.size[1] / 2) * j))
    else:
        for i in range(width_count * 2):
            pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=(random.choice(color_pixel)))
            for j in range(height_count * 2):
                im1.paste(pixel_, (int(pixel_.size[0] / 2) * i, int(pixel_.size[1] / 2) * j))

    im1.save('static/image_vert.jpg', format='JPEG')
