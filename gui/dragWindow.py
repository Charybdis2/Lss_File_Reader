import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from splits.category import category
from .mainWindow import mainWindow
from graph import generateGraph, generateSplitGraph, deleteGraphs



c = category()

def onDrop(event):
    filePath = event.data.strip('{').strip('}')
    if filePath.endswith(".lss"):
        deleteGraphs()
        c.parseFile(filePath)
        generateGraph(c)
        generateSplitGraph(c)
        root.destroy()  
        mainWindow("graph")  
    else:
        #Error handling to do later
        pass


def dragWindow():
    global root
    root = TkinterDnD.Tk()
    root.title(".Lss File Reader")
    root.geometry("400x200")

    label = tk.Label(root, text="Drag and drop your .lss file here", bg="lightgray", font=("Arial", 14))
    label.pack(expand=True, fill="both", padx=10, pady=10)

    label.drop_target_register(DND_FILES)
    label.dnd_bind('<<Drop>>', onDrop)

    root.mainloop()
  


