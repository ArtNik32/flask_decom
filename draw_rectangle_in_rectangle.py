from PIL import Image, ImageDraw
import random

def draw_image_rectangle_diag_half(colors):
    # background
    width_bg = 4000
    height_bg = 4000
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color='grey')

    # pixel
    width_pixel = 400
    height_pixel = 400
    pixel_color = colors

    # count
    width_count = width_bg // width_pixel
    height_count = height_bg // height_pixel

    if width_count >= height_count:
        for i in range(height_count):
            for j in range(width_count):
                pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=(random.choice(pixel_color)))
                draw_ = ImageDraw.Draw(pixel_)
                draw_.regular_polygon(bounding_circle=(width_pixel // 2, height_pixel // 2, width_pixel // 2), n_sides=4, fill=random.choice(pixel_color))
                im1.paste(pixel_, (width_pixel * j, height_pixel * i))
    else:
        for i in range(width_count * 2):
            for j in range(height_count * 2):
                pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=(random.choice(pixel_color)))
                draw_ = ImageDraw.Draw(pixel_)
                draw_.regular_polygon(bounding_circle=(width_pixel // 2, height_pixel // 2, width_pixel // 2),
                                      n_sides=3, fill=random.choice(pixel_color))
                im1.paste(pixel_, (pixel_.size[0] // 2 * j, pixel_.size[1] // 2 * i))

    im1.save('static/image_rect_diag_half.jpg', format='JPEG')
