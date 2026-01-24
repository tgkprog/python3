from graphics import Canvas
import time
import random
import math

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

GameState = {
    'x': random.randint(61, CANVAS_WIDTH - 110),
    'y': random.randint(70, CANVAS_HEIGHT - 110),
    'directionX': 1,
    'directionY': 1,
    'hits': [],
    'ogre_health': 8,
    'ogre_parts': None,
    'start_time': None,
    'moveX': random.choice([7, 9, 11]),
    'moveY':  random.choice([6, 8, 10]),
    'cnt': random.randint(5, 9)
}

def draw_ogre():
    scale = 0.3
    origin_x = GameState['x']
    origin_y = GameState['y']

    def s(x): return int(x * scale)

    parts = []
    offsets = []

    def add(part, x_offset, y_offset):
        parts.append(part)
        offsets.append((x_offset, y_offset))

    body = canvas.create_polygon(
        origin_x + s(60), origin_y + s(50),
        origin_x + s(80), origin_y + s(50),
        origin_x + s(95), origin_y + s(65),
        origin_x + s(100), origin_y + s(85),
        origin_x + s(90), origin_y + s(115),
        origin_x + s(75), origin_y + s(125),
        origin_x + s(60), origin_y + s(125),
        origin_x + s(45), origin_y + s(115),
        origin_x + s(35), origin_y + s(90),
        origin_x + s(40), origin_y + s(65),
        origin_x + s(55), origin_y + s(50)
    )
    canvas.set_color(body, 'coral')
    add(body, 0, 0)

    joint_radius = s(5)
    joint_points = [
        (60, 50), (80, 50), (95, 65), (100, 85), (90, 115),
        (75, 125), (60, 125), (45, 115), (35, 90), (40, 65), (55, 50)
    ]

    for x0, y0 in joint_points:
        oval = canvas.create_oval(
            origin_x + s(x0 - joint_radius),
            origin_y + s(y0 - joint_radius),
            origin_x + s(x0 + joint_radius),
            origin_y + s(y0 + joint_radius),
            'coral'
        )
        add(oval, s(x0 - joint_radius) - s(60), s(y0 - joint_radius) - s(50))

    eye1 = canvas.create_polygon(
        origin_x + s(60), origin_y + s(60),
        origin_x + s(62), origin_y + s(58),
        origin_x + s(65), origin_y + s(60),
        origin_x + s(62), origin_y + s(63))
    canvas.set_color(eye1, 'white')
    add(eye1, s(60) - s(60), s(60) - s(50))

    eye2 = canvas.create_polygon(
        origin_x + s(85), origin_y + s(60),
        origin_x + s(87), origin_y + s(58),
        origin_x + s(90), origin_y + s(60),
        origin_x + s(87), origin_y + s(63))
    canvas.set_color(eye2, 'white')
    add(eye2, s(85) - s(60), s(60) - s(50))

    mouth = canvas.create_polygon(
        origin_x + s(70), origin_y + s(85),
        origin_x + s(81), origin_y + s(83),
        origin_x + s(77), origin_y + s(91))
    canvas.set_color(mouth, 'red')
    add(mouth, s(70) - s(60), s(85) - s(50))

    blood1 = canvas.create_oval(
        origin_x + s(55), origin_y + s(80),
        origin_x + s(58), origin_y + s(83))
    canvas.set_color(blood1, 'coral1')
    add(blood1, s(55) - s(60), s(80) - s(50))

    blood2 = canvas.create_oval(
        origin_x + s(53), origin_y + s(85),
        origin_x + s(56), origin_y + s(88))
    canvas.set_color(blood2, 'coral2')
    add(blood2, s(53) - s(60), s(85) - s(50))

    blood3 = canvas.create_oval(
        origin_x + s(50), origin_y + s(90),
        origin_x + s(53), origin_y + s(93))
    canvas.set_color(blood3, 'coral3')
    add(blood3, s(50) - s(60), s(90) - s(50))

    return {
        'main': body,
        'parts': parts,
        'offsets': offsets
    }

def move_ogre(_):
    if not GameState['ogre_parts']:
        return

    GameState['cnt'] += 1
    cnt = GameState['cnt']
    dirx = GameState['directionX']
    diry = GameState['directionY']

    GameState['x'] += GameState['moveX'] * dirx
    GameState['y'] += GameState['moveY'] * diry

    width = 50
    height = 50

    if (cnt == 13 and dirx == -1):
        GameState['directionX'] *= -1
        GameState['moveX'] = random.choice([9, 11, 13, 16])
    elif GameState['x'] <= 20:
        GameState['x'] = 22
        GameState['directionX'] = 1
        GameState['moveX'] = random.choice([18, 11, 13, 16])
    elif (GameState['x'] + width) >= (CANVAS_WIDTH - 50):
        GameState['x'] = CANVAS_WIDTH - width - 11
        GameState['directionX'] = -1
        GameState['moveX'] = random.choice([18, 11, 13, 16])

    if (cnt == 13):
        GameState['directionY'] *= -1
        GameState['moveY'] = random.choice([15, 17, 9, 12])
    elif GameState['y'] <= 20:
        GameState['y'] = 26
        GameState['directionY'] = 1
        GameState['moveY'] = random.choice([17, 13, 9, 15])
    elif GameState['y'] + height >= CANVAS_HEIGHT - 50:
        GameState['y'] = CANVAS_HEIGHT - height - 51
        GameState['directionY'] = -1
        GameState['moveY'] = random.choice([17, 13, 9, 11])

    if cnt > 14:
        GameState['cnt'] = random.randint(6, 11)

    x = GameState['x']
    y = GameState['y']
    parts = GameState['ogre_parts']['parts']
    offsets = GameState['ogre_parts']['offsets']

    for part, (dx, dy) in zip(parts, offsets):
        canvas.moveto(part, x + dx, y + dy)

def click_attack(x, y):
    dot = canvas.create_oval(x - 5, y - 5, x + 5, y + 5)
    canvas.set_color(dot, 'red')
    GameState['hits'].append({'dot': dot, 'timestamp': time.time(), 'x': x, 'y': y})

def check_hits():
    if not GameState['ogre_parts']:
        return

    ogre_left = GameState['x'] - 5
    ogre_top = GameState['y'] - 5
    w1 = 70
    h1 = 90
    ogre_right = ogre_left + w1
    ogre_bottom = ogre_top + h1

    for hit in GameState['hits'][:]:
        x = hit['x']
        y = hit['y']
        if ogre_left <= x <= ogre_right and ogre_top <= y <= ogre_bottom:
            GameState['ogre_health'] -= 1
            canvas.delete(hit['dot'])
            GameState['hits'].remove(hit)

def lifeLeft():
    x, y = 20, 300
    t = GameState['ogre_health'] + 2
    for i in range(t + 3):
        bar_y = y + (5 - i) * 15
        bar = canvas.create_rectangle(x, bar_y, x + 5, bar_y + 10)
        cc = "#A30B0A" if i < t else "#FFFFFF"
        canvas.set_color(bar, cc)

    # Ugly red-black heart
    canvas.create_oval(10, 365, 20, 375, color='red', outline='black')  # left lobe
    canvas.create_oval(20, 365, 30, 375, color='red', outline='black')  # right lobe
    canvas.create_polygon(13, 372, 27, 372, 20, 390, color='red', outline='black')  # point

def end(s):
    print(s)
    y = 60
    x = 30
    clr = ['blue', 'orange', 'teal', 'violet', '#00fa00', '#A2A3FA']
    for c, color in enumerate(clr):
        canvas.create_text(x, y, s, font_size=50, color=color)
        x += 25 + c * 9
        y += 30 + (c * 6)

    canvas.create_text(x + 15, y + 50, "    - tushar kapila", font_size=50, color=color)
    canvas.create_text(x + 15, y + 120, "       github/tgkprog", font_size=50, color=color)
                

def game_loop():
    GameState['start_time'] = time.time()
    if GameState['ogre_parts'] is None:
        GameState['ogre_parts'] = draw_ogre()

    while True:
        now = time.time()
        if now - GameState['start_time'] > 13:
            end("Ogre wins! You lose")
            break
        if GameState['ogre_health'] <= 0:
            end("Ogre lost! You WON")
            break

        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            x, y = click
            click_attack(x, y)

        for hit in GameState['hits'][:]:
            if now - hit['timestamp'] > 3:
                canvas.delete(hit['dot'])
                GameState['hits'].remove(hit)

        move_ogre(GameState['ogre_parts']['parts'])
        check_hits()
        lifeLeft()
        time.sleep(0.13)

def main():
    GameState['ogre_parts'] = draw_ogre()
    game_loop()

if __name__ == '__main__':
    main()
