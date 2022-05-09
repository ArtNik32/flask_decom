import time

from app import app
from flask import render_template, request, send_file, url_for
from draw_vert import draw_image_vert
from draw_horiz import draw_image_horiz
from draw_circle import draw_image_circle
from draw_triangle import draw_image_triangle
from draw_vert_rect_45 import draw_image_vert_rect_45
from draw_pixel import draw_image_pixel
from draw_polka_dot import draw_image_polka_dot
from draw_rectangle_diag_half import draw_image_rct_diag_half
from draw_rectangle_in_rectangle import draw_image_rct_in_rct
from draw_circle_wave import draw_image_circle_wave
from draw_circle_triangle_in_rectangle import draw_image_crc_trn_in_rct
from draw_half_circle_in_rectangle import draw_half_crc_in_rct
from draw_dot_in_rectangle_45 import draw_dot_in_rct_45

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result_vert():
    colors = []
    try:
        if request.form.get('color_1'):
            colors.append(request.form.get('color_1'))
        else:
            pass
        if request.form.get('color_2'):
            colors.append(request.form.get('color_2'))
        else:
            pass
        if request.form.get('color_3'):
            colors.append(request.form.get('color_3'))
        else:
            pass
        if request.form.get('color_4'):
            colors.append(request.form.get('color_4'))
        else:
            pass
        if request.form.get('color_5'):
            colors.append(request.form.get('color_5'))
        else:
            pass
        if len(colors) >= 2:
            draw_image_vert(colors)
            draw_image_horiz(colors)
            draw_image_circle(colors)
            draw_image_triangle(colors)
            draw_image_vert_rect_45(colors)
            draw_image_pixel(colors)
            draw_image_polka_dot(colors)
            draw_image_rct_diag_half(colors)
            draw_image_rct_in_rct(colors)
            draw_image_circle_wave(colors)
            draw_image_crc_trn_in_rct(colors)
            draw_half_crc_in_rct(colors)
            draw_dot_in_rct_45(colors)
            return render_template('result.html')
        else:
            return render_template('index.html')
    except:
        return render_template('index.html')