import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Invert Del!")
        icon_image = tk.PhotoImage(file="res/paint_logo2.png")
        self.root.iconphoto(True, icon_image)
        self.root.geometry("800x600")

        # Variables
        self.image = None
        self.tk_image = None
        self.draw = None

        # Setup UI
        self.create_menu()
        self.create_toolbar()
        self.create_canvas()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_image)
        filemenu.add_command(label="Save As", command=self.save_image)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)

        open_btn = tk.Button(toolbar, text="Open", command=self.open_image)
        open_btn.pack(side=tk.LEFT, padx=2, pady=2)

        save_btn = tk.Button(toolbar, text="Save", command=self.save_image)
        save_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Example placeholders for your future tools
        inverse_crop_btn = tk.Button(toolbar, text="Inverse Crop", command=self.inverse_crop)
        inverse_crop_btn.pack(side=tk.LEFT, padx=2, pady=2)

        zoom_btn = tk.Button(toolbar, text="Zoom +10%", command=self.zoom_in)
        zoom_btn.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)

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

        # Delete inner rectangle and shrink outer image to fit
        w, h = self.image.size
        crop_margin = 100  # You can replace this with user selection later
        
        # Crop outer parts and merge them
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

        scale_factor = 1.10  # 10% zoom in
        w, h = self.image.size
        new_size = (int(w * scale_factor), int(h * scale_factor))
        self.image = self.image.resize(new_size, Image.LANCZOS)
        self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
