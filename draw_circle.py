from PIL import Image, ImageDraw
import random

def draw_image_circle(colors):

    # background
    width_bg = 4000
    height_bg = 4000
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color='grey')

    draw = ImageDraw.Draw(im1)

    # pixel
    circle_radius = 50

    color_pixel = colors

    # count
    count_ = 0
    if width_bg >= height_bg:
        count_ = width_bg // circle_radius
    else:
        count_ = height_bg // circle_radius

    # draw circle centr
    for i in range(count_):
        draw.ellipse(((width_bg // 2) - circle_radius * (count_ - i), (height_bg // 2) - circle_radius * (count_ - i), (width_bg // 2) + circle_radius * (count_ - i), (height_bg // 2) + circle_radius * (count_ - i)), fill=(random.choice(color_pixel)))


    im1.save('static/image_circle.jpg', format='JPEG')
