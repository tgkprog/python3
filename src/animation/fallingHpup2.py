
"""
File: fallingHpup2.py
---------------------
This program displays a puppy with floating animated hearts on a graphical canvas.
Uses a simplified graphics library (graphics.py) based on Tkinter.
Designed for local execution with a relative path to the graphics library.
"""

import time
import random
import math
import sys
import os

# Add relative path to graphics.py
current_dir = os.path.dirname(__file__)
graphics_path = os.path.join(current_dir, '..', 'Graphics')
sys.path.append(os.path.abspath(graphics_path))
from graphics import Canvas

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 1200
HEART_COLORS = ["red", "#800020", "pink"]
SPARKLE_COLORS = ["gold", "silver", "brown"]

def generate_heart_points(center_x, center_y, scale, num_points=100):
    points = []
    for i in range(num_points):
        t = math.pi - (2 * math.pi * i / num_points)
        x = 16 * math.sin(t)**3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        screen_x = center_x + scale * x
        screen_y = center_y - scale * y  # flip Y to match screen coordinates
        points.append((screen_x, screen_y))
    return points


def get_heart_polygon_coords(cx, cy, scale=2.5):
    pts = generate_heart_points(cx, cy, scale)
    flat = []
    for x, y in pts:
        flat.extend([x, y])
    return flat

class FloatingHeart:
    def __init__(self, canvas, x, y, color, has_sparkles):
        self.canvas = canvas
        self.base_x = x
        self.base_y = y
        self.color = color
        self.has_sparkles = has_sparkles
        self.angle = random.uniform(0, 2 * math.pi)
        self.amp = random.randint(15, 30)
        self.speed = random.uniform(1.5, 2.5)
        self.offset = random.uniform(0, 2 * math.pi)
        self.scale = 2.5
        coords = get_heart_polygon_coords(x, y, self.scale)
        self.shape = self.canvas.create_polygon(*coords, fill=self.color)
        self.sparkles = self._draw_sparkles() if has_sparkles else []

    def _draw_sparkles(self):
        x, y = self.base_x, self.base_y
        sparkles = []
        for dx, dy, color in zip([0, 10, 6], [0, 0, 10], SPARKLE_COLORS):
            sparkles.append(self.canvas.create_oval(x + dx, y + dy, x + dx + 5, y + dy + 5, fill=color))
        return sparkles

    def update(self, step):
        y = self.speed * step
        dx = math.sin(self.angle + self.offset + step * 0.1) * self.amp

        dy = y - self.base_y
        self.canvas.moveto(self.shape, self.base_x + dx - 20, self.base_y + dy - 20)
        for sparkle in self.sparkles:
            self.canvas.moveto(sparkle, self.base_x + dx + 5, self.base_y + dy + 5)

def draw_puppy(canvas):
    shift_x = 100
    canvas.create_oval(400 + shift_x, 300, 800 + shift_x, 700, fill="#F5CBA7", outline="black")
    canvas.create_oval(500 + shift_x, 400, 540 + shift_x, 440, fill="white")
    canvas.create_oval(660 + shift_x, 400, 700 + shift_x, 440, fill="white")
    canvas.create_oval(515 + shift_x, 415, 525 + shift_x, 425, fill="black")
    canvas.create_oval(675 + shift_x, 415, 685 + shift_x, 425, fill="black")
    canvas.create_oval(580 + shift_x, 460, 620 + shift_x, 500, fill="black")
    canvas.create_line(580 + shift_x, 500, 600 + shift_x, 510)
    canvas.create_line(600 + shift_x, 510, 620 + shift_x, 500)
    canvas.create_oval(350 + shift_x, 250, 450 + shift_x, 400, fill="#A04000")
    canvas.create_oval(750 + shift_x, 250, 850 + shift_x, 400, fill="#A04000")
    canvas.create_oval(440 + shift_x, 700, 560 + shift_x, 780, fill="#F5CBA7", outline="black")
    for x in [455, 480, 505, 530]:
        canvas.create_oval(x + shift_x, 765, x + 10 + shift_x, 775, fill="black")
    canvas.create_oval(640 + shift_x, 700, 760 + shift_x, 780, fill="#F5CBA7", outline="black")
    for x in [655, 680, 705, 730]:
        canvas.create_oval(x + shift_x, 765, x + 10 + shift_x, 775, fill="black")
    canvas.create_oval(790 + shift_x, 640, 870 + shift_x, 720, fill="#A04000", outline="black")

def spawn_heart_wave(canvas, all_hearts, wave_step):
    count = random.randint(3, 4)
    base_y = random.randint(0, 60)
    for _ in range(count):
        y = base_y + random.randint(-30, 50)
        x = random.randint(250, 550)
        color = random.choice(HEART_COLORS)
        has_sparkles = len(all_hearts) % 7 == 0
        heart = FloatingHeart(canvas, x, y, color, has_sparkles)
        all_hearts.append((heart, wave_step))

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_puppy(canvas)
    all_hearts = []
    step = 0

    while True:
        if step % 20 == 0:
            spawn_heart_wave(canvas, all_hearts, step)

        for heart, created_at in all_hearts:
            heart.update(step - created_at)

        canvas.update()
        step += 1
        time.sleep(0.05)

if __name__ == '__main__':
    main()
