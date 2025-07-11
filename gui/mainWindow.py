import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

'''
Yeah I need to make this nicer. 
'''
def mainWindow(folder_path):
    root = tk.Tk()
    root.title("Generated Graphs")
    root.geometry("1600x800") 

    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollFrame = ttk.Frame(canvas)

    # Link scrolling
    scrollFrame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollFrame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Store image references to prevent garbage collection
    imageRef = []

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".png"):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            img = img.resize((800, int(img.height * (800 / img.width))), Image.LANCZOS)
            imgTK = ImageTk.PhotoImage(img)

            label = ttk.Label(scrollFrame, image=imgTK, text=filename, compound="top")
            label.pack(pady=10)
            imageRef.append(imgTK)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()
