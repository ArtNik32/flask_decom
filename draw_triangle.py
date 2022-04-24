from PIL import Image, ImageDraw
import random

def draw_image_triangle(colors):

    # background
    width_bg = 4000
    height_bg = 4000
    im1 = Image.new(mode='RGB', size=(width_bg, height_bg), color='grey')

    draw = ImageDraw.Draw(im1)

    # pixel
    circle_radius = 100

    # count
    height_count = height_bg // circle_radius
    width_count = width_bg // circle_radius

    # draw

    if width_count >= height_count:
        for i in range(width_count * 2 + 1):
            for j in range(height_count * 2 + 1):
                draw.regular_polygon(bounding_circle=(j * circle_radius // 2, i * circle_radius // 2, circle_radius // 2), n_sides=4, rotation=45, fill=random.choice(colors))
    else:
        for i in range(width_count * 2 + 1):
            for j in range(height_count * 2 + 1):
                draw.regular_polygon(bounding_circle=(j * circle_radius // 2, i * circle_radius // 2, circle_radius // 2), n_sides=4, rotation=45, fill=random.choice(colors))

    im1.save('static/image_triang.jpg', format='JPEG')
