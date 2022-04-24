from PIL import Image
import random

def draw_image_vert_rect_45(colors):
    # background
    width_bg = 6000
    height_bg = 6000
    width_bg_45 = 4000
    height_bg_45 = 4000
    im_rotate45 = Image.new(mode='RGB', size=(width_bg_45, height_bg_45), color='grey')
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color='grey')

    # pixel
    width_pixel = 100
    height_pixel = 100
    color_pixel = colors

    # count
    width_count = width_bg // width_pixel
    height_count = height_bg // height_pixel

    # rotate
    angle_ = -45

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

    im1 = im1.rotate(angle_)
    crop_area = (1000, 1000, 5000, 5000)
    im1 = im1.crop(crop_area)
    im_rotate45.paste(im1)
    #im_rotate45 = im_rotate45.rotate(angle_)
    im_rotate45.save('static/image_vert_rect_45.jpg', format='JPEG')
