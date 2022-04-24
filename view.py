import time

from app import app
from flask import render_template, request, send_file, url_for
from draw_vert import draw_image_vert
from draw_horiz import draw_image_horiz
from draw_circle import draw_image_circle
from draw_triangle import draw_image_triangle
from draw_vert_rect_45 import draw_image_vert_rect_45

@app.route('/')
def index():
    name = 'Art'
    return render_template('index.html', n = name)

@app.route('/result', methods=['POST'])
def result_vert():
    colors = []
    colors.append(request.form.get('color_1'))
    colors.append(request.form.get('color_2'))
    colors.append(request.form.get('color_3'))
    colors.append(request.form.get('color_4'))
    colors.append(request.form.get('color_5'))
    draw_image_vert(colors)
    draw_image_horiz(colors)
    draw_image_circle(colors)
    draw_image_triangle(colors)
    draw_image_vert_rect_45(colors)
    #time.sleep(5)
    return render_template('result.html', color_1=colors[0], color_2=colors[1], color_3=colors[2], color_4=colors[3], color_5=colors[4])