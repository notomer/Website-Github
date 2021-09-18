import tkinter as tk
import os
root = tk.Tk()
root.mainloop()

myLabel1 = label(root, text="Heart Attack ID")
myLabel2 = label(root, text="Made with love by")


window = tk.Tk()
canvas = tk.Canvas(root, height=900, width=1000, bg="#FFBEBC")

canvas.pack()
frame=tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=0.1, relx=0.1, rely=0.1)

openFile=tk.Button(root, text="Open File", padx=10, 
                   pady=5, fg="white", bg="#FFBEBC" )
openFile.pack()

root.mainloop()


