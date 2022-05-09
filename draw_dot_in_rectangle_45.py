from PIL import Image, ImageDraw
import random

def draw_dot_in_rct_45(colors):
    # background
    width_bg = 4000
    height_bg = 4200
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color='grey')

    # pixel
    width_pixel = 400
    height_pixel = 400
    pixel_color = colors
    color_1 = random.choice(pixel_color)
    pixel_color.remove(color_1)
    color_2 = random.choice(pixel_color)

    # count
    width_count = width_bg // width_pixel
    height_count = height_bg // height_pixel

    if width_count >= height_count:
        for i in range(height_count * 3):
            for j in range(width_count * 3):
                if i % 2 == 0:
                    pixel_ = Image.new(mode='RGBA', size=(width_pixel, height_pixel), color=(0, 0, 0, 0))
                    draw_ = ImageDraw.Draw(pixel_)
                    draw_.regular_polygon(bounding_circle=(width_pixel // 2, height_pixel // 2, width_pixel // 2), n_sides=4, rotation=45, fill=color_1)
                    draw_.ellipse((150, 150, 250, 250), fill=color_2)
                    im1.paste(pixel_, (width_pixel * j - width_pixel // 2, height_pixel * i // 2), pixel_)
                else:
                    pixel_ = Image.new(mode='RGBA', size=(width_pixel, height_pixel), color=(0, 0, 0, 0))
                    draw_ = ImageDraw.Draw(pixel_)
                    draw_.regular_polygon(bounding_circle=(width_pixel // 2, height_pixel // 2, width_pixel // 2), n_sides=4, rotation=45, fill=color_2)
                    draw_.ellipse((150, 150, 250, 250), fill=color_1)
                    im1.paste(pixel_, (width_pixel * j, height_pixel * i // 2), pixel_)

    else:
        for i in range(width_count * 2):
            for j in range(height_count * 2):
                pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=(random.choice(pixel_color)))
                draw_ = ImageDraw.Draw(pixel_)
                draw_.regular_polygon(bounding_circle=(width_pixel // 2, height_pixel // 2, width_pixel // 2),
                                      n_sides=3, fill=random.choice(pixel_color))
                im1.paste(pixel_, (pixel_.size[0] // 2 * j, pixel_.size[1] // 2 * i))

    im1_crop = im1.crop((0, 200, width_bg, height_bg))
    im1_crop.save('static/image_dot_in_rct_45.jpg', format='JPEG')
