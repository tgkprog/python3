import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageGrab
from ani import run_startup_animation
import os
import io
import sys

class PaintApp:
    def __init__(self, root, skip_animation=False):
        self.root = root
        self.root.title("Invert Crop!")
        self.root.geometry("850x650")

        # Load icon safely using absolute path
        self.res_path = os.path.join(os.path.dirname(__file__), "res")
        icon_image = tk.PhotoImage(file=os.path.join(self.res_path, "paint_logo2.png"))
        self.root.iconphoto(True, icon_image)

        self.image = None
        self.tk_image = None
        self.selection = None
        self.start_x = self.start_y = self.end_x = self.end_y = None
        self.selecting = False

        # UI - IMPORTANT ORDER!
        if skip_animation:
            self.create_toolbar(initial_blank=False)
        else:
            self.create_toolbar(initial_blank=True)

        self.create_canvas()
        self.root.update()

        if not skip_animation:
            # Run startup animation
            run_startup_animation(self.canvas, self.root, self.update_toolbar_icons_to_real)

        # Once animation done, show menu
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_image)
        filemenu.add_command(label="Save As", command=self.save_image)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)

    def create_toolbar(self, initial_blank=True):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)

        def icon(name):
            path = os.path.join(self.res_path, f"{name}.png")
            return ImageTk.PhotoImage(Image.open(path).resize((25, 25), Image.LANCZOS))

        if initial_blank:
            names = ["blank"] * 7
        else:
            names = ["open", "save", "paste", "select-region", "inverse-crop", "select-all", "copy"]

        commands = [
            self.open_image,
            self.save_image,
            self.paste_clipboard_image,
            self.enable_selection,
            self.inverse_crop,
            self.select_all,
            self.copy_to_clipboard
        ]

        self.toolbar_buttons = []

        for name, command in zip(names, commands):
            img = icon(name)
            btn = tk.Button(toolbar, image=img, command=command)
            btn.image = img
            btn.pack(side=tk.LEFT, padx=2, pady=2)
            self.toolbar_buttons.append(btn)

        toolbar.pack(side=tk.TOP, fill=tk.X)

    def update_toolbar_icons_to_real(self):
        names = ["open", "save", "paste", "select-region", "inverse-crop", "select-all", "copy"]

        for btn, name in zip(self.toolbar_buttons, names):
            img = ImageTk.PhotoImage(Image.open(os.path.join(self.res_path, f"{name}.png")).resize((25, 25), Image.LANCZOS))
            btn.configure(image=img)
            btn.image = img

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if path:
            self.image = Image.open(path).convert("RGBA")
            self.display_image()

    def save_image(self):
        if not self.image:
            messagebox.showerror("Error", "No image to save.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if path:
            self.image.save(path)

    def paste_clipboard_image(self):
        try:
            img = ImageGrab.grabclipboard()
            if img:
                self.image = img.convert("RGBA")
                self.display_image()
        except Exception as e:
            messagebox.showerror("Clipboard Error", str(e))

    def display_image(self):
        if not self.image:
            return
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def enable_selection(self):
        if not self.image:
            messagebox.showerror("Error", "Paste or open image first.")
            return
        self.selecting = True

    def on_mouse_down(self, event):
        if self.selecting:
            self.start_x, self.start_y = event.x, event.y
            self.selection = self.canvas.create_rectangle(event.x, event.y, event.x, event.y, outline='red')

    def on_mouse_drag(self, event):
        if self.selecting and self.selection:
            self.canvas.coords(self.selection, self.start_x, self.start_y, event.x, event.y)

    def on_mouse_up(self, event):
        if self.selecting:
            self.end_x, self.end_y = event.x, event.y
            self.selecting = False

    def inverse_crop(self):
        print("=== inverse_crop version 1.1 ===")

        if not self.image or None in [self.start_x, self.start_y, self.end_x, self.end_y]:
            messagebox.showerror("Error", "Select a region first.")
            return

        w, h = self.image.size

        # Convert canvas coords to image coords by clamping
        x0, x1 = sorted([max(0, min(self.start_x, w)), max(0, min(self.end_x, w))])
        y0, y1 = sorted([max(0, min(self.start_y, h)), max(0, min(self.end_y, h))])

        # Debug print
        print(f"Selection (canvas coords): ({self.start_x}, {self.start_y}) to ({self.end_x}, {self.end_y})")
        print(f"Selection (clamped image coords): ({x0}, {y0}) to ({x1}, {y1})")
        print(f"Image size: {w} x {h}")

        # If selection is invalid, abort
        if x0 == x1 or y0 == y1:
            messagebox.showerror("Error", "Selection too small or invalid.")
            print("Selection too small or invalid.")
            return

        # Correct direction detection:
        if (y1 - y0) < (x1 - x0):
            print("Performing vertical cut (cutting out horizontal band)")
            top = self.image.crop((0, 0, w, y0))
            bottom = self.image.crop((0, y1, w, h))
            new_img = Image.new("RGBA", (w, top.height + bottom.height), (255, 255, 255, 0))
            new_img.paste(top, (0, 0))
            new_img.paste(bottom, (0, top.height))
        else:
            print("Performing horizontal cut (cutting out vertical band)")
            left = self.image.crop((0, 0, x0, h))
            right = self.image.crop((x1, 0, w, h))
            new_img = Image.new("RGBA", (left.width + right.width, h), (255, 255, 255, 0))
            new_img.paste(left, (0, 0))
            new_img.paste(right, (left.width, 0))

        print(f"New image size: {new_img.size}")

        self.image = new_img
        self.display_image()


# end inv crop 

    def select_all(self):
        if self.image:
            w, h = self.image.size
            self.start_x, self.start_y = 0, 0
            self.end_x, self.end_y = w, h
            self.selection = self.canvas.create_rectangle(0, 0, w, h, outline='blue')

    def copy_to_clipboard(self):
        if not self.image:
            return
        try:
            import win32clipboard
            output = io.BytesIO()
            self.image.convert("RGB").save(output, "BMP")
            data = output.getvalue()[14:]
            output.close()

            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
            win32clipboard.CloseClipboard()
        except ImportError:
            messagebox.showerror("Clipboard Error", "Requires pywin32 on Windows")

if __name__ == "__main__":
    skip_animation = False
    if len(sys.argv) > 1 and sys.argv[1] == 'n':
        skip_animation = True

    root = tk.Tk()
    app = PaintApp(root, skip_animation=skip_animation)
    root.mainloop()