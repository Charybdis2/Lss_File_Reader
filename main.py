from graph import generateGraph, generateSplitGraph, deleteGraphs
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from splits.category import category

# Initialize your category parser
c = category()

# Callback when file is dropped
def on_drop(event):
    file_path = event.data.strip('{').strip('}')
    if file_path.endswith(".lss"):
        print(f"Loading file: {file_path}")
        deleteGraphs()
        c.parseFile(file_path)
        generateGraph(c)
        generateSplitGraph(c)
        print("File loaded successfully.")
    else:
        print("Please drop a .lss file.")

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def show_all_pngs_in_folder(folder_path):
    root = tk.Tk()
    root.title("Generated Graphs")

    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    # Link scrolling
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Store image references to prevent garbage collection
    image_refs = []

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".png"):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            img = img.resize((800, int(img.height * (800 / img.width))), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)

            label = ttk.Label(scrollable_frame, image=img_tk, text=filename, compound="top")
            label.pack(pady=10)
            image_refs.append(img_tk)  # Prevent garbage collection

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()

# Usage:
 # Replace with your output folder



# Create a drag-and-drop window
root = TkinterDnD.Tk()
root.title("Drop your .lss file here")
root.geometry("400x200")

label = tk.Label(root, text="Drag and drop your .lss file here", bg="lightgray", font=("Arial", 14))
label.pack(expand=True, fill="both", padx=10, pady=10)

# Bind drop event
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
show_all_pngs_in_folder("graph") 
