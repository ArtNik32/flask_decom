from PIL import Image, ImageDraw
import random

def draw_wave_horizontal_lines(colors):
    # background
    width_bg = 4000
    height_bg = 4000
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color='grey')

    # pixel
    width_pixel = 200
    height_pixel = 200
    pixel_color = []
    for color in colors:
        pixel_color.append(color)
    color_1 = random.choice(pixel_color)
    pixel_color.remove(color_1)
    color_2 = random.choice(pixel_color)

    width_outline_ellipse = 10

    # count
    width_count = width_bg // width_pixel
    height_count = height_bg // height_pixel

    if width_count >= height_count:
        for i in range(height_count):
            for j in range(width_count):
                if i % 2 == 0:
                    pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=color_1)
                    draw_ = ImageDraw.Draw(pixel_)
                    if j % 2 == 0:
                        draw_.ellipse((- width_outline_ellipse // 2, - height_pixel // 2 - width_outline_ellipse, width_pixel + width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                        # Part of the circle from the bottom left
                        draw_.ellipse((width_pixel - width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse, width_pixel * 2 + width_outline_ellipse // 2, height_pixel + height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                        # Part of the circle from the bottom right
                        draw_.ellipse((- width_pixel - width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse, width_outline_ellipse // 2, height_pixel + height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                    else:
                        draw_.ellipse((- width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse, width_pixel + width_outline_ellipse // 2, height_pixel + height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                        # Part of the circle from the top left
                        draw_.ellipse((width_pixel - width_outline_ellipse // 2, - height_pixel // 2 - width_outline_ellipse, width_pixel * 2 + width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                        # Part of the circle from the top right
                        draw_.ellipse((- width_pixel - width_outline_ellipse // 2, - height_pixel // 2 - width_outline_ellipse, width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                    im1.paste(pixel_, (width_pixel * j, height_pixel * i))
                else:
                    pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=color_1)
                    draw_ = ImageDraw.Draw(pixel_)
                    if j % 2 == 0:
                        draw_.ellipse((- width_outline_ellipse // 2, - height_pixel // 2 - width_outline_ellipse, width_pixel + width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                        # Part of the circle from the bottom left
                        draw_.ellipse((width_pixel - width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse, width_pixel * 2 + width_outline_ellipse // 2, height_pixel + height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                        # Part of the circle from the bottom right
                        draw_.ellipse((- width_pixel - width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse, width_outline_ellipse // 2, height_pixel + height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                    else:
                        draw_.ellipse((- width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse, width_pixel + width_outline_ellipse // 2, height_pixel + height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                        # Part of the circle from the top left
                        draw_.ellipse((width_pixel - width_outline_ellipse // 2, - height_pixel // 2 - width_outline_ellipse, width_pixel * 2 + width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                        # Part of the circle from the top right
                        draw_.ellipse((- width_pixel - width_outline_ellipse // 2, - height_pixel // 2 - width_outline_ellipse, width_outline_ellipse // 2, height_pixel // 2 - width_outline_ellipse), fill=color_1, outline=color_2, width=width_outline_ellipse)
                    im1.paste(pixel_, (width_pixel * j, height_pixel * i))

    else:
        for i in range(width_count * 2):
            for j in range(height_count * 2):
                pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=(random.choice(pixel_color)))
                draw_ = ImageDraw.Draw(pixel_)
                draw_.regular_polygon(bounding_circle=(width_pixel // 2, height_pixel // 2, width_pixel // 2),
                                      n_sides=3, fill=random.choice(pixel_color))
                im1.paste(pixel_, (pixel_.size[0] // 2 * j, pixel_.size[1] // 2 * i))

    im1.save('static/image_wave_horizontal_lines.jpg', format='JPEG')
