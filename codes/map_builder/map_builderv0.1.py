# 使用gpt生成，地图绘制器。
# 仅适用于简单地图的绘制。

import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageDraw

# Default settings
CELL_SIZE = 20  # Cell size


class MapEditor:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.scale = 1.0  # Zoom scale
        self.offset_x = 0  # X-axis offset
        self.offset_y = 0  # Y-axis offset

        self.is_drawing = False  # Flag for drawing
        self.obstacles = set()  # Set of obstacle coordinates

        self.create_ui()

    def create_ui(self):
        self.root = tk.Tk()
        self.root.title("Map Editor")

        # Create canvas
        canvas_width = self.width * CELL_SIZE
        canvas_height = self.height * CELL_SIZE
        self.canvas = tk.Canvas(
            self.root, width=canvas_width, height=canvas_height, bg="white"
        )
        self.canvas.pack()

        # Bind events
        self.canvas.bind("<Button-1>", self.place_obstacle)
        self.canvas.bind("<B1-Motion>", self.place_obstacle)
        self.canvas.bind("<Button-3>", self.remove_obstacle)
        self.canvas.bind("<B3-Motion>", self.remove_obstacle)
        self.canvas.bind("<Button-2>", self.start_drag)
        self.canvas.bind("<B2-Motion>", self.drag_map)
        self.canvas.bind("<Configure>", self.resize_map)

        # Create menu
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save Map", command=self.save_map)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

        # Initialize map
        self.draw_map()

    def draw_map(self):
        self.canvas.delete("all")
        for x in range(self.width):
            for y in range(self.height):
                x1 = x * CELL_SIZE
                y1 = y * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                if (x, y) in self.obstacles:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")

    def place_obstacle(self, event):
        x = int(event.x / CELL_SIZE)
        y = int(event.y / CELL_SIZE)
        if 0 <= x < self.width and 0 <= y < self.height:
            self.obstacles.add((x, y))
            self.draw_map()

    def remove_obstacle(self, event):
        x = int(event.x / CELL_SIZE)
        y = int(event.y / CELL_SIZE)
        if (x, y) in self.obstacles:
            self.obstacles.remove((x, y))
            self.draw_map()

    def start_drag(self, event):
        self.last_drag_x = event.x
        self.last_drag_y = event.y

    def drag_map(self, event):
        delta_x = event.x - self.last_drag_x
        delta_y = event.y - self.last_drag_y
        self.canvas.scan_dragto(delta_x, delta_y, gain=1)
        self.offset_x += delta_x
        self.offset_y += delta_y
        self.last_drag_x = event.x
        self.last_drag_y = event.y

    def resize_map(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def save_map(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Images", "*.png"), ("All Files", "*.*")],
        )
        if file_path:
            image = Image.new("RGB", (self.width, self.height), color="white")
            draw = ImageDraw.Draw(image)
            for x in range(self.width):
                for y in range(self.height):
                    if (x, y) in self.obstacles:
                        draw.point((x, y), fill="black")
            image.save(file_path)
            messagebox.showinfo("Save Successful", "Map saved successfully!")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    width = int(input("Enter the width of the map: "))
    height = int(input("Enter the height of the map: "))

    editor = MapEditor(width, height)
    editor.run()
