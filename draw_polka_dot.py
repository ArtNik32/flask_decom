from PIL import Image, ImageDraw
import random

def draw_image_polka_dot(colors):
    # pixel
    circle_radius = 100

    # background
    width_bg = 4000
    height_bg = 4000
    color_pixel = colors
    bg_color = random.choice(color_pixel)
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color=bg_color)

    draw = ImageDraw.Draw(im1)

    # count
    count_width = width_bg // circle_radius
    count_height = height_bg // circle_radius

    color_pixel.remove(bg_color)

    # draw circle
    if count_width >= count_height:
        color_dot = random.choice(color_pixel)
        for i in range(count_height):
            for j in range(count_width):
                if i % 2 == 0:
                    draw.ellipse((circle_radius // 2 + circle_radius * j, circle_radius // 2 + circle_radius * i, circle_radius + circle_radius * j, circle_radius + circle_radius * i), fill=color_dot)
                else:
                    draw.ellipse((circle_radius // 2 + circle_radius * j + circle_radius // 2, circle_radius // 2 + circle_radius * i, circle_radius + circle_radius * j + circle_radius // 2, circle_radius + circle_radius * i), fill=color_dot)
    else:
        color_dot = random.choice(color_pixel)
        for i in range(count_height):
            for j in range(count_width):
                draw.ellipse(((circle_radius // 2) * j, (circle_radius // 2) * i, circle_radius * j, circle_radius * i), fill=color_dot)

    im1.save('static/image_polka_dot.jpg', format='JPEG')
