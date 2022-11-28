import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import *

# The objects that will be going down the tautochrone
# c is the constant of how far up up down the tautochrone the object's starting position is.
# c = 0.0 means the object is at the bottom, c=1.0 means the object is at the top.
# color is the color and shape of the object (circle).
objects = [{'c': 1.0, 'color': 'bo'},
           {'c': 0.7, 'color': 'go'},
           {'c': 0.4, 'color': 'ro'},
           {'c': 0.2, 'color': 'yo'}]


# define the curve() function which will be used to plot the curve and the points of the objects as they fall
def curve(phi):
    x = phi + sin(phi)
    y = 1 - cos(phi)
    return np.array([x, y])


# number of points to use when creating the graph and animation.
# Also the number of frames in the animation, and the frames per second to display at.
frames = 90
fps = 30


def animate(frame):
    t = frame / float(frames - 1.)

    # plot the ramp
    ramp_x = []
    ramp_y = []
    for i in range(frames):
        phi = i / (frames - 1.0) * pi - pi
        x, y = curve(phi)
        ramp_x.append(x)
        ramp_y.append(y)

    ramp_vertx = [min(ramp_x), min(ramp_x)]
    ramp_horizx = [min(ramp_x), min(ramp_y)]
    ramp_verty = [min(ramp_y), max(ramp_y)]
    ramp_horizy = [max(ramp_x), min(ramp_y)]

    plt.clf()
    plt.axis('off')
    plt.plot(ramp_x, ramp_y, 'k')
    plt.plot(ramp_vertx, ramp_verty, '.5')
    plt.plot(ramp_horizx, ramp_horizy, '.5')

    # plot the falling objects
    for obj in objects:
        phi_pendulum = obj['c'] * -cos(t * pi / 2)
        # the 2*asin(phi) is to "undo" the cos(t*pi/2) and and shift by 180 degrees
        phi_wheel = -abs(2 * asin(phi_pendulum))
        x, y = curve(phi_wheel)

        plt.plot(x, y, obj['color'])
    return


# plot the animation
fig = plt.figure()
anim = animation.FuncAnimation(fig, func=animate, frames=frames, repeat=False)
plt.show()

# saves the animation in the folder
anim.save('Tautochrone.mp4', writer = 'ffmpeg', fps = fps)
Writer = animation.PillowWriter(fps=fps)
anim.save('/*PATH HERE*/Tautochrone.gif', writer=Writer)
