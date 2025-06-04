# ani.py

import math
import time
import os
from PIL import Image, ImageTk
import tkinter as tk

lightning_image = None  # Global cache for lightning image

def run_startup_animation(canvas, root, update_toolbar_icons_func):
    global lightning_image

    stick_x = -50
    stick_y = 300

    # Walk in
    for step in range(30):
        canvas.delete("all")
        draw_stick_figure(canvas, stick_x + step * 10, stick_y, 0)
        root.update()
        time.sleep(0.05)

    # Raise arms to 75 degrees
    for angle in range(0, 76, 5):
        canvas.delete("all")
        draw_stick_figure(canvas, stick_x + 300, stick_y, angle)
        root.update()
        time.sleep(0.05)

    # Final stickman pose — do NOT clear
    final_x = stick_x + 300
    final_angle = 75
    canvas.delete("all")
    draw_stick_figure(canvas, final_x, stick_y, final_angle)

    # Update toolbar icons
    update_toolbar_icons_func()

    # Show lightning bolts from hands
    show_lightning_bolts_from_hands(canvas, root, final_x, stick_y, final_angle)

    # Wait 4 seconds
    time.sleep(4)

    # Optional: if you want, clear:
    # canvas.delete("all")

def draw_stick_figure(canvas, x, y, arm_angle):
    # Head
    canvas.create_oval(x, y - 50, x + 30, y - 20, fill="white", outline="black", width=2)
    # Eyes
    canvas.create_oval(x + 8, y - 43, x + 12, y - 39, fill="black")
    canvas.create_oval(x + 18, y - 43, x + 22, y - 39, fill="black")

    # Body (green)
    canvas.create_line(x + 15, y - 20, x + 15, y + 50, fill="green", width=4)

    # Arms (red), angled up
    arm_length = 40
    angle_rad = arm_angle * math.pi / 180
    dx = arm_length * math.cos(angle_rad)
    dy = -arm_length * math.sin(angle_rad)

    canvas.create_line(x + 15, y, x + 15 + dx, y + dy, fill="red", width=3)
    canvas.create_line(x + 15, y, x + 15 - dx, y + dy, fill="red", width=3)

    # Legs (blue)
    canvas.create_line(x + 15, y + 50, x + 5, y + 100, fill="blue", width=4)
    canvas.create_line(x + 15, y + 50, x + 25, y + 100, fill="blue", width=4)

def show_lightning_bolts_from_hands(canvas, root, stick_x, stick_y, arm_angle):
    global lightning_image

    # Load lightning image once
    if lightning_image is None:
        img_path = os.path.join(os.path.dirname(__file__), "res", "ligthining-bolt.png")
        img = Image.open(img_path).resize((40, 100), Image.LANCZOS)
        img = img.rotate(-90, expand=True)  # Point upwards
        lightning_image = ImageTk.PhotoImage(img)

    # Compute hand positions
    arm_length = 40
    angle_rad = arm_angle * math.pi / 180
    dx = arm_length * math.cos(angle_rad)
    dy = -arm_length * math.sin(angle_rad)

    left_hand_x = stick_x + 15 - dx
    left_hand_y = stick_y + dy

    right_hand_x = stick_x + 15 + dx
    right_hand_y = stick_y + dy

    # Target positions
    canvas_width = canvas.winfo_width()

    left_target = (20, 20)
    middle_target = (canvas_width // 2, 20)
    right_target = (canvas_width - 20, 20)

    # Function to animate one bolt
    def animate_bolt(start_x, start_y, target_x, target_y):
        steps = 20
        delta_x = (target_x - start_x) / steps
        delta_y = (target_y - start_y) / steps

        x = start_x
        y = start_y

        for _ in range(steps):
            bolt = canvas.create_image(x, y, image=lightning_image, anchor=tk.CENTER)
            root.update()
            time.sleep(0.02)
            canvas.delete(bolt)
            x += delta_x
            y += delta_y

        # Final draw at target
        canvas.create_image(target_x, target_y, image=lightning_image, anchor=tk.CENTER)
        root.update()

    # LEFT hand → one to left, one to middle
    animate_bolt(left_hand_x, left_hand_y, left_target[0], left_target[1])
    animate_bolt(left_hand_x, left_hand_y, middle_target[0], middle_target[1])

    # RIGHT hand → one to right
    animate_bolt(right_hand_x, right_hand_y, right_target[0], right_target[1])

    # After bolts → draw message below stickman
    text_x = canvas_width // 2
    text_y = stick_y + 150

    canvas.create_text(
        text_x,
        text_y,
        text="Open image to edit",
        fill="dark blue",
        font=("Courier", 30)
    )

    root.update()
