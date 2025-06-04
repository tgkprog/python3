import math
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
from ani import run_startup_animation
import os
import time

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Invert Crop!")
        # Load icon safely using absolute path
        res_path = os.path.join(os.path.dirname(__file__), "res")
        icon_image = tk.PhotoImage(file=os.path.join(res_path, "paint_logo2.png"))
        self.root.iconphoto(True, icon_image)
        self.root.geometry("850x650")

        # Variables
        self.image = None
        self.tk_image = None
        self.draw = None
        self.res_path = res_path

        # UI - IMPORTANT ORDER!
        self.create_toolbar(initial_blank=True)   # First create toolbar
        self.create_canvas()                      # Then canvas below it
        self.root.update()

        # Run startup animation
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

        if initial_blank:
            icon_file = os.path.join(self.res_path, "blank.png")
            open_img = Image.open(icon_file).resize((25, 25), Image.LANCZOS)
            save_img = Image.open(icon_file).resize((25, 25), Image.LANCZOS)
            reverse_crop_img = Image.open(icon_file).resize((25, 25), Image.LANCZOS)
        else:
            open_img = Image.open(os.path.join(self.res_path, "open.png")).resize((25, 25), Image.LANCZOS)
            save_img = Image.open(os.path.join(self.res_path, "save.png")).resize((25, 25), Image.LANCZOS)
            reverse_crop_img = Image.open(os.path.join(self.res_path, "reverse-crop.png")).resize((25, 25), Image.LANCZOS)

        open_img_tk = ImageTk.PhotoImage(open_img)
        save_img_tk = ImageTk.PhotoImage(save_img)
        reverse_crop_img_tk = ImageTk.PhotoImage(reverse_crop_img)

        self.open_btn = tk.Button(toolbar, image=open_img_tk, command=self.open_image)
        self.open_btn.image = open_img_tk
        self.open_btn.pack(side=tk.LEFT, padx=2, pady=2)

        self.save_btn = tk.Button(toolbar, image=save_img_tk, command=self.save_image)
        self.save_btn.image = save_img_tk
        self.save_btn.pack(side=tk.LEFT, padx=2, pady=2)

        self.inverse_crop_btn = tk.Button(toolbar, image=reverse_crop_img_tk, command=self.inverse_crop)
        self.inverse_crop_btn.image = reverse_crop_img_tk
        self.inverse_crop_btn.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)

    def update_toolbar_icons_to_real(self):
        open_img = Image.open(os.path.join(self.res_path, "open.png")).resize((25, 25), Image.LANCZOS)
        save_img = Image.open(os.path.join(self.res_path, "save.png")).resize((25, 25), Image.LANCZOS)
        reverse_crop_img = Image.open(os.path.join(self.res_path, "reverse-crop.png")).resize((25, 25), Image.LANCZOS)

        open_img_tk = ImageTk.PhotoImage(open_img)
        save_img_tk = ImageTk.PhotoImage(save_img)
        reverse_crop_img_tk = ImageTk.PhotoImage(reverse_crop_img)

        self.open_btn.configure(image=open_img_tk)
        self.open_btn.image = open_img_tk

        self.save_btn.configure(image=save_img_tk)
        self.save_btn.image = save_img_tk

        self.inverse_crop_btn.configure(image=reverse_crop_img_tk)
        self.inverse_crop_btn.image = reverse_crop_img_tk

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)



    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
        )
        if file_path:
            self.image = Image.open(file_path).convert("RGBA")
            self.display_image()

    def save_image(self):
        if not self.image:
            messagebox.showerror("Error", "No image to save.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg;*.jpeg")]
        )
        if file_path:
            self.image.save(file_path)

    def display_image(self):
        if not self.image:
            return
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def inverse_crop(self):
        if not self.image:
            messagebox.showerror("Error", "Open an image first.")
            return

        w, h = self.image.size
        crop_margin = 100

        left = self.image.crop((0, 0, w, crop_margin))
        right = self.image.crop((0, h - crop_margin, w, h))

        new_height = left.height + right.height
        new_img = Image.new("RGBA", (w, new_height), (255, 255, 255, 0))
        new_img.paste(left, (0, 0))
        new_img.paste(right, (0, left.height))

        self.image = new_img
        self.display_image()

    def zoom_in(self):
        if not self.image:
            messagebox.showerror("Error", "Open an image first.")
            return

        scale_factor = 1.10
        w, h = self.image.size
        new_size = (int(w * scale_factor), int(h * scale_factor))
        self.image = self.image.resize(new_size, Image.LANCZOS)
        self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
