from graphics import Canvas
import time
import random
import math

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 700

HEART_COLORS = ["red", "#800020", "pink"]
SPARKLE_COLORS = ["gold", "silver", "brown"]

def generate_flipped_heart_points(center_x, center_y, scale, num_points=100):
    points = []
    for i in range(num_points):
        t = math.pi - (2 * math.pi * i / num_points)
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        screen_x = center_x + scale * x
        screen_y = center_y - scale * y  # flip y for canvas
        points.append((screen_x, screen_y))
    return points

def get_heart_polygon_coords(cx, cy, scale=1.5):
    pts = generate_flipped_heart_points(cx, cy, scale)
    flat = []
    for x, y in pts:
        flat.extend([x, y])
    return flat

class FloatingHeart:
    def __init__(self, canvas, x, y, color, has_sparkles):
        self.canvas = canvas
        self.init_x = x
        self.init_y = y
        self.color = color
        self.has_sparkles = has_sparkles
        self.angle = random.uniform(0, 2 * math.pi)
        self.offset = random.uniform(0, 2 * math.pi)
        self.amp = random.randint(10, 20)
        self.speed = random.uniform(1.5, 2.0)
        self.scale = 1.5

        coords = get_heart_polygon_coords(self.init_x, self.init_y, self.scale)
        self.shape = self.canvas.create_polygon(*coords, color=self.color)
        self.sparkles = self._draw_sparkles() if has_sparkles else []

    def _draw_sparkles(self):
        x, y = self.init_x, self.init_y
        sparkles = []
        for dx, dy, color in zip([0, 8, 5], [0, 0, 8], SPARKLE_COLORS):
            sparkles.append(self.canvas.create_oval(x + dx, y + dy, x + dx + 4, y + dy + 4, color=color))
        return sparkles

    def update(self, step):
        dx = math.sin(self.angle + self.offset + step * 0.1) * self.amp
        dy = self.speed * step
        self.canvas.moveto(self.shape, self.init_x + dx - 15, self.init_y + dy - 15)
        for sparkle in self.sparkles:
            self.canvas.moveto(sparkle, self.init_x + dx + 5, self.init_y + dy + 5)

def draw_static_puppy(canvas):
    shift_x = 100
    scale = 0.65
    def sx(x): return shift_x + int(x * scale)
    def sy(y): return int(y * scale)
    canvas.create_oval(sx(400), sy(300), sx(800), sy(700), color="#F5CBA7", outline="black")
    canvas.create_oval(sx(500), sy(400), sx(540), sy(440), color="white")
    canvas.create_oval(sx(660), sy(400), sx(700), sy(440), color="white")
    canvas.create_oval(sx(515), sy(415), sx(525), sy(425), color="black")
    canvas.create_oval(sx(675), sy(415), sx(685), sy(425), color="black")
    canvas.create_oval(sx(580), sy(460), sx(620), sy(500), color="black")
    canvas.create_line(sx(580), sy(500), sx(600), sy(510))
    canvas.create_line(sx(600), sy(510), sx(620), sy(500))
    canvas.create_oval(sx(350), sy(250), sx(450), sy(400), color="#A04000")
    canvas.create_oval(sx(750), sy(250), sx(850), sy(400), color="#A04000")
    canvas.create_oval(sx(440), sy(700), sx(560), sy(780), color="#F5CBA7", outline="black")
    for x in [455, 480, 505, 530]:
        canvas.create_oval(sx(x), sy(765), sx(x + 10), sy(775), color="black")
    canvas.create_oval(sx(640), sy(700), sx(760), sy(780), color="#F5CBA7", outline="black")
    for x in [655, 680, 705, 730]:
        canvas.create_oval(sx(x), sy(765), sx(x + 10), sy(775), color="black")
    canvas.create_oval(sx(790), sy(640), sx(870), sy(720), color="#A04000", outline="black")

def spawn_heart_wave(canvas, all_hearts, step):
    count = random.randint(3, 4)
    base_y = random.randint(0, 60)
    for _ in range(count):
        x = random.randint(100, 300)
        y = base_y + random.randint(-20, 40)
        color = random.choice(HEART_COLORS)
        has_sparkles = len(all_hearts) % 7 == 0
        heart = FloatingHeart(canvas, x, y, color, has_sparkles)
        all_hearts.append((heart, step))

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_static_puppy(canvas)

    all_hearts = []
    step = 0

    while True:
        if step % 20 == 0:
            spawn_heart_wave(canvas, all_hearts, step)

        for heart, created_at in all_hearts:
            heart.update(step - created_at)

        step += 1
        time.sleep(0.05)

if __name__ == '__main__':
    main()
