from p5 import *

mouse_x: sketch.events.builtins.mouse_x
mouse_y: sketch.events.builtins.mouse_y
mouse_is_pressed: sketch.events.builtins.mouse_is_pressed


def setup():
    size(640, 360)
    no_stroke()
    background(204)


def draw():
    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 15)

    circle_size = random_uniform(low=10, high=80)

    circle((mouse_x, mouse_y), circle_size)


def key_pressed(_event):
    background(204)


# p5 supports different backends to render sketches,
# "vispy" for both 2D and 3D sketches & "skia" for 2D sketches
# use "skia" for better 2D experience
# Default renderer is set to "vispy"
run(renderer="vispy")  # "skia" is still in beta
