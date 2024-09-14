import itertools
import math
import time
import turtle

class Solar_system_body(turtle.Turtle):
    min_display_size = 20
    display_log_base = 1.1
    def __init__(self, solar_system, mass, position = (0, 0), velocity = (0, 0)):
        super().__init__()
        self.mass = mass
        self.setposition(position)  # turtle method
        self.velocity = velocity
        self.display_size = max(math.log(self.mass, self.display_log_base), self.min_display_size)

        self.penup()
        self.hideturtle()

        solar_system.add_body(self)

    def draw(self):
        self.clear()
        self.dot(self.display_size)

    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])
class Sun(Solar_system_body):
    def __init__(self, solar_system, mass, position = (0, 0), velocity = (0, 0)):
        super().__init__(solar_system, mass, position, velocity)
        self.color("yellow")

class Planet(Solar_system_body):
    colors = itertools.cycle(["#FFB3BA", "#B2FFB3", "#BAE1FF"])  # Pastel shades
    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_system, mass, position, velocity)
        self.color(next(Planet.colors))

class Solar_system:
    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")

        self.bodies = []

        self.fps_display = turtle.Turtle()
        self.fps_display.hideturtle()
        self.fps_display.penup()
        self.fps_display.color("white")

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        body.clear()
        self.bodies.remove(body)

    def update_all(self):
        start_time = time.time()

        for body in self.bodies:
            body.move()
            body.draw()

        self.solar_system.update()

        end_time = time.time()
        frame_time = end_time - start_time
        fps = 1/frame_time if frame_time > 0 else 0

        self.display_fps(fps)

    def display_fps(self, fps):
        self.fps_display.clear()
        self.fps_display.goto(-self.solar_system.window_width() // 2 + 50, self.solar_system.window_height() // 2 - 50)
        self.fps_display.write(f"FPS: {fps:.2f}", font=("Arial", 16, "normal"))

    @staticmethod
    def accelerate_due_to_gravity(
            first: Solar_system_body,
            second: Solar_system_body,
            time_step=0.01,
    ):
        distance = max(first.distance(second), 1)  # Prevent division by zero
        force = first.mass * second.mass / distance ** 2
        angle = first.towards(second)
        reverse = 1
        for body in first, second:
            acceleration = force/body.mass
            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.sin(math.radians(angle))
            body.velocity = (
                body.velocity[0] + (reverse * acc_x * time_step),
                body.velocity[1] + (reverse * acc_y * time_step)
            )
            reverse = -1
    def check_collision(self, first, second):
        if isinstance(first, Planet) and isinstance(second, Planet):
            return
        if first.distance(second) < first.display_size/2 + second.display_size/2:
            for body in first, second:
                if isinstance(body, Planet):
                    self.remove_body(body)

    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                self.accelerate_due_to_gravity(first, second)
                self.check_collision(first, second)