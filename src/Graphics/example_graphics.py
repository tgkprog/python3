"""
File: example_graphics.py
------------------
This is a file with an example graphics program that creates rectangles
and other shapes on a canvas. 
"""

from graphics import Canvas

WIDTH = 600
HEIGHT = 600

def main():
    # create the canvas
    canvas = Canvas(WIDTH, HEIGHT)

    # create a rectangle
    canvas.create_rectangle(0, 0, 400, HEIGHT, color="blue")

    # create an oval
    canvas.create_oval(100, 100, 300, 300, color="green")

    # create a line
    canvas.create_line(0, 0, WIDTH, HEIGHT, "red", 5)

    # create a triangle
    points = [150, 100, 250, 100, 200, 50]
    canvas.create_polygon(points, outline='black', fill='yellow', width=2)

    # write some text
    # text = canvas.create_text(20, 20, text="Hello, world!", anchor='nw', font_size=30, font="Times New Roman")

    # get some properties
    print(canvas.get_obj_width(text))

    # create an image
    canvas.create_image(300, 300, "karel.png", width=100, height=100)

    # wait for the user to close the window
    canvas.mainloop()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
