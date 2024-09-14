from solarsystem import Solar_system, Sun

solar_system = Solar_system(width=1400, height=900)

sun = Sun(solar_system, mass=10_000)

sun.draw()

#

import turtle
turtle.done()