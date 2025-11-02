from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("🎨 Nehal Paint")
root.geometry("1200x700")
root.config(bg="#dcdcdc")


brush_color = "black"
brush_size = 5
tool = "brush"


canvas = Canvas(root, bg="white", width=1200, height=600, bd=2, relief=RIDGE)
canvas.pack(pady=10)


def choose_color():
    global brush_color
    color = colorchooser.askcolor(title="Pick a color")[1]
    if color:
        brush_color = color

def change_size(val):
    global brush_size
    brush_size = int(val)

def use_tool(selected):
    global tool
    tool = selected

def paint(event):
    if tool == "brush":
        x1, y1 = (event.x - brush_size), (event.y - brush_size)
        x2, y2 = (event.x + brush_size), (event.y + brush_size)
        canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)
    elif tool == "eraser":
        x1, y1 = (event.x - brush_size), (event.y - brush_size)
        x2, y2 = (event.x + brush_size), (event.y + brush_size)
        canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")

start_x, start_y = None, None
def start_shape(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def end_shape(event):
    if tool == "rectangle":
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline=brush_color, width=brush_size)
    elif tool == "oval":
        canvas.create_oval(start_x, start_y, event.x, event.y, outline=brush_color, width=brush_size)
    elif tool == "line":
        canvas.create_line(start_x, start_y, event.x, event.y, fill=brush_color, width=brush_size)


def clear_canvas():
    canvas.delete("all")


canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-1>", start_shape)
canvas.bind("<ButtonRelease-1>", end_shape)


toolbar = Frame(root, bg="#c0c0c0", height=50, relief=RAISED, bd=2)
toolbar.pack(fill=X)


Button(toolbar, text="🖌️ Brush", command=lambda: use_tool("brush"), width=10).pack(side=LEFT, padx=5, pady=5)
Button(toolbar, text="🧽 Eraser", command=lambda: use_tool("eraser"), width=10).pack(side=LEFT, padx=5)
Button(toolbar, text="⬛ Rectangle", command=lambda: use_tool("rectangle"), width=10).pack(side=LEFT, padx=5)
Button(toolbar, text="⚪ Oval", command=lambda: use_tool("oval"), width=10).pack(side=LEFT, padx=5)
Button(toolbar, text="📏 Line", command=lambda: use_tool("line"), width=10).pack(side=LEFT, padx=5)
Button(toolbar, text="🎨 Color", command=choose_color, width=10).pack(side=LEFT, padx=5)
Button(toolbar, text="🧹 Clear", command=clear_canvas, width=10).pack(side=LEFT, padx=5)


Label(toolbar, text="Brush Size:", bg="#c0c0c0").pack(side=LEFT, padx=10)
size_slider = Scale(toolbar, from_=1, to=20, orient=HORIZONTAL, command=change_size, bg="#c0c0c0")
size_slider.set(5)
size_slider.pack(side=LEFT, padx=5)

root.mainloop()
