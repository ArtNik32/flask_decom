from PIL import Image, ImageDraw
import random

def draw_image_rct_diag_half(colors):
    # background
    width_bg = 4000
    height_bg = 4000
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color='grey')

    # pixel
    width_pixel = 400
    height_pixel = 400

    # count
    width_count = width_bg // width_pixel
    height_count = height_bg // height_pixel

    if width_count >= height_count:
        for i in range(height_count):
            for j in range(width_count):
                pixel_color = []
                for color in colors:
                    pixel_color.append(color)
                bg_pixel_color = random.choice(pixel_color)
                pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=bg_pixel_color)
                draw_ = ImageDraw.Draw(pixel_)
                pixel_color.remove(bg_pixel_color)
                draw_.regular_polygon(bounding_circle=(width_pixel, height_pixel, width_pixel * 1.43), n_sides=3, rotation=105, fill=random.choice(pixel_color))
                im1.paste(pixel_, (width_pixel * j, height_pixel * i))
    else:
        for i in range(width_count * 2):
            for j in range(height_count * 2):
                pixel_color = []
                for color in colors:
                    pixel_color.append(color)
                bg_pixel_color = random.choice(pixel_color)
                pixel_ = Image.new(mode='RGB', size=(width_pixel, height_pixel), color=bg_pixel_color)
                draw_ = ImageDraw.Draw(pixel_)
                pixel_color.remove(bg_pixel_color)
                draw_.regular_polygon(bounding_circle=(width_pixel, height_pixel, width_pixel * 1.43), n_sides=3,
                                      rotation=105, fill=random.choice(pixel_color))
                im1.paste(pixel_, (width_pixel * j, height_pixel * i))

    im1.save('static/image_rect_diag_half.jpg', format='JPEG')
