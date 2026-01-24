

import time
import random
import math
import sys
import os

current_dir = os.path.dirname(__file__)
graphics_path = os.path.join(current_dir, '..', 'Graphics')
sys.path.append(os.path.abspath(graphics_path))
from graphics import Canvas

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 1200
HEART_COLORS = ["red", "#800020", "pink"]
SPARKLE_COLORS = ["gold", "silver", "brown"]
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
shift_x = 100
while True:
    canvas.create_oval(400 + shift_x, 300, 800 + shift_x, 700, color="#F5CBA7", outline="black")
    canvas.update()
    time.sleep(0.5)
