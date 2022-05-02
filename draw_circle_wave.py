from PIL import Image, ImageDraw
import random

def draw_image_circle_wave(colors):
    # background
    width_bg = 4000
    height_bg = 4200
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color='grey')
    # draw = ImageDraw.Draw(im1)

    # pixel
    circle_radius = 400
    color_pixel = []
    for color in colors:
        color_pixel.append(color)

    # count
    count_width = width_bg // circle_radius
    count_height = height_bg // circle_radius
    count_circle = 15

    # draw pixel
    pixel_ = Image.new(mode='RGBA', size=(circle_radius, circle_radius), color=(0, 0, 0, 0))
    draw_px = ImageDraw.Draw(pixel_)
    color_circle_in = random.choice(color_pixel)
    color_pixel.remove(color_circle_in)
    color_circle_out = random.choice(color_pixel)
    for i in range(count_circle):
        if i % 2 == 0:
            draw_px.ellipse((circle_radius / count_circle * i, circle_radius / count_circle * i, circle_radius - circle_radius / count_circle * i, circle_radius - circle_radius / count_circle * i), fill=color_circle_in)
        else:
            draw_px.ellipse((circle_radius / count_circle * i, circle_radius / count_circle * i, circle_radius - circle_radius / count_circle * i, circle_radius - circle_radius / count_circle * i), fill=color_circle_out)
    # paste
    if count_width >= count_height:
        for i in range(count_height * 3):
            for j in range(count_width * 3):
                if i % 2 == 0:
                    im1.paste(pixel_, (circle_radius * j - circle_radius // 2, circle_radius * i // 2), pixel_)
                else:
                    im1.paste(pixel_, (circle_radius * j, circle_radius * i // 2), pixel_)
    else:
        pass
    im1_crop = im1.crop((0, 200, width_bg, height_bg))
    im1_crop.save('static/image_circle_wave.jpg', format='JPEG')
