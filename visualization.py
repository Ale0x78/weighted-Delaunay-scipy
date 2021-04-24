#!pip3 install pyglet
import pyglet, math, numpy as np
from pyglet.window import key, mouse, Window
from pyglet import shapes
from weighted_delaunay import WeightedDelaunay

# match inputs from the user
inputstack = []
# Keep track of all points added to the triangulation
pointstack = []
DEFAULT_RADIUS = 5


window = Window(width=1080, height=720)
label = pyglet.text.Label('Click and Drag to create points',
                          font_name='Times New Roman',
                          font_size=18,
                          x=10, y=10)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.U and len(pointstack) > 0:
        p = pointstack.pop()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        inputstack.append([x,y])

@window.event
def on_mouse_release(x,y, button, modifiers):
    if len(inputstack) == 0:
        return False
    center = inputstack.pop()
    # Calculate offsets
    radius = center[0]**2 + center[1]**2 - x**2 - y**2
    # Find radius length, as an integer (hacky but simpler)
    radius = int(math.sqrt(abs(radius))) // 4
    center.append(DEFAULT_RADIUS + radius)
    pointstack.append(center)

    print("POINTSTACK", pointstack)

@window.event
def on_draw():
    window.clear()
    label.draw()
    drawDelaunay()


def drawDelaunay():
    drawPoints()
    drawLines()

def drawLines():
    if len(pointstack) <= 2:
        return
    # xs, ys are center points; ws is weights of points
    xs, ys, ws = zip(*pointstack)
    # ps is center points zipped in NP Array
    ps = np.column_stack((xs, ys))
    ws = list(ws)
    ws = [100 * (x - DEFAULT_RADIUS) for x in ws]
    print("ps=", ps, "ws=", list(ws))

    wd = WeightedDelaunay(ps, list(ws))
    for s in wd.triangulation:
        p1 = pointstack[s[0]]
        p2 = pointstack[s[1]]
        p3 = pointstack[s[2]]
        shapes.Line(p1[0], p1[1], p2[0], p2[1]).draw()
        shapes.Line(p2[0], p2[1], p3[0], p3[1]).draw()
        shapes.Line(p1[0], p1[1], p3[0], p3[1]).draw()

def drawPoints():
    for p in pointstack:
        shapes.Circle(p[0], p[1], p[2]).draw()
pyglet.app.run()
