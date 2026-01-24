import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Ensure PyPDF2 is installed
try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    import subprocess
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
        from PyPDF2 import PdfReader, PdfWriter
    except Exception as e:
        print(f"Failed to install PyPDF2: {e}")
        sys.exit(1)

def run_gui():
    root = tk.Tk()
    root.title("PDF Password Remover")
    root.geometry("500x350")

    # Variables
    file_path_var = tk.StringVar()
    password_var = tk.StringVar()
    status_var = tk.StringVar()

    def select_file():
        filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if filename:
            file_path_var.set(filename)
            status_var.set("") # Clear error on new file

    def process_pdf():
        input_path = file_path_var.get()
        password = password_var.get()

        if not input_path:
            status_var.set("Error: Please select a PDF file.")
            return
        
        if not os.path.exists(input_path):
             status_var.set(f"Error: File not found: {input_path}")
             return

        try:
            reader = PdfReader(input_path)
            
            if reader.is_encrypted:
                if not reader.decrypt(password):
                    status_var.set("Error: Incorrect password or decryption failed.")
                    return
            else:
                # If not encrypted, we can proceed or warn. 
                # Request implies putting password in text box, but if not needed, we just copy.
                pass

            writer = PdfWriter()
            # Copy all pages
            for page in reader.pages:
                writer.add_page(page)

            # Construct output filename
            base_dir = os.path.dirname(input_path)
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            output_filename = f"{base_name}-no-p.pdf"
            output_path = os.path.join(base_dir, output_filename)

            with open(output_path, "wb") as f:
                writer.write(f)
            
            status_var.set(f"Success! Saved to:\n{output_filename}")

        except Exception as e:
            status_var.set(f"Error: {str(e)}")

    # UI Layout
    # Padding
    padx = 10
    pady = 5

    # File Chooser Row
    file_frame = tk.Frame(root)
    file_frame.pack(fill=tk.X, padx=padx, pady=pady)
    
    btn_browse = tk.Button(file_frame, text="Select PDF", command=select_file)
    btn_browse.pack(side=tk.LEFT)
    
    lbl_file = tk.Label(file_frame, textvariable=file_path_var, anchor="w", relief=tk.SUNKEN)
    lbl_file.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))

    # Password Row
    pass_frame = tk.Frame(root)
    pass_frame.pack(fill=tk.X, padx=padx, pady=pady)
    
    lbl_pass = tk.Label(pass_frame, text="Password:")
    lbl_pass.pack(side=tk.LEFT)
    
    entry_pass = tk.Entry(pass_frame, textvariable=password_var) # Plain text box as requested
    entry_pass.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))

    # Action Button
    btn_run = tk.Button(root, text="Remove Password", command=process_pdf, bg="#dddddd")
    btn_run.pack(pady=pady * 2)

    # Error Label (Multi-row, full width)
    lbl_error = tk.Label(
        root, 
        textvariable=status_var, 
        fg="red", 
        wraplength=480, # Assuming 500 width minus padding
        justify=tk.CENTER
    )
    lbl_error.pack(fill=tk.X, padx=padx, pady=(0, pady))

    root.mainloop()

if __name__ == "__main__":
    run_gui()
