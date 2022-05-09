from PIL import Image, ImageDraw
import random

def draw_half_crc_in_rct(colors):
    # background
    width_bg = 4000
    height_bg = 4000
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color='grey')

    # pixel
    width_pixel = 200
    height_pixel = 200
    pixel_color = colors

    # count
    width_count = width_bg // width_pixel
    height_count = height_bg // height_pixel

    if width_count >= height_count:
        for i in range(height_count):
            for j in range(width_count):
                pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=(random.choice(pixel_color)))
                draw_ = ImageDraw.Draw(pixel_)
                rotation_ = random.choice([0, 1, 2, 3])
                draw_.ellipse((- width_pixel, - height_pixel, width_pixel, height_pixel), fill=random.choice(pixel_color))
                if rotation_ == 0:
                    pixel_ = pixel_.rotate(angle=90)
                elif rotation_ == 1:
                    pixel_ = pixel_.rotate(angle=180)
                elif rotation_ == 2:
                    pixel_ = pixel_.rotate(angle=270)
                else:
                    pass
                im1.paste(pixel_, (width_pixel * j, height_pixel * i))
    else:
        for i in range(width_count * 2):
            for j in range(height_count * 2):
                pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=(random.choice(pixel_color)))
                draw_ = ImageDraw.Draw(pixel_)
                draw_.regular_polygon(bounding_circle=(width_pixel // 2, height_pixel // 2, width_pixel // 2),
                                      n_sides=3, fill=random.choice(pixel_color))
                im1.paste(pixel_, (pixel_.size[0] // 2 * j, pixel_.size[1] // 2 * i))

    im1.save('static/image_half_crc_in_rct.jpg', format='JPEG')
