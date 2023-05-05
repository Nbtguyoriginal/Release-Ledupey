import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageDraw, ImageFont

# Default settings
FONT_SIZE = 24
FONT_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)

# Create a function to convert the text to an image
def create_image(text):
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    size = font.getsize(text)
    image = Image.new("RGB", size, color=BG_COLOR)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill=FONT_COLOR)
    return image

# Create a function to save the image to a file
def save_image(image):
    filename = fd.asksaveasfilename(defaultextension=".png")
    if filename:
        image.save(filename)

# Create a function to visualize the image
def visualize_image(image):
    image.show()

# Create a function to update the font size
def update_font_size(new_size):
    global FONT_SIZE
    FONT_SIZE = new_size

# Create a function to update the font color
def update_font_color(new_color):
    global FONT_COLOR
    FONT_COLOR = new_color

# Create a function to update the background color
def update_bg_color(new_color):
    global BG_COLOR
    BG_COLOR = new_color

# Create the GUI
root = tk.Tk()
root.title("Text to PNG Converter")

# Create a text box for user input
input_frame = tk.Frame(root)
input_frame.pack(side="top", padx=10, pady=10)
input_label = tk.Label(input_frame, text="Enter text:")
input_label.pack(side="left")
input_text = tk.Entry(input_frame)
input_text.pack(side="left")

# Create a save button
save_button = tk.Button(root, text="Save", command=lambda: save_image(create_image(input_text.get())))
save_button.pack(side="left", padx=10)

# Create a visualize button
visualize_button = tk.Button(root, text="Visualize", command=lambda: visualize_image(create_image(input_text.get())))
visualize_button.pack(side="left", padx=10)

# Create a settings section
settings_frame = tk.Frame(root)
settings_frame.pack(side="top", padx=10, pady=10)
font_size_label = tk.Label(settings_frame, text="Font size:")
font_size_label.pack(side="left")
font_size_entry = tk.Entry(settings_frame)
font_size_entry.pack(side="left")
font_size_entry.insert(0, FONT_SIZE)
font_size_button = tk.Button(settings_frame, text="Update", command=lambda: update_font_size(int(font_size_entry.get())))
font_size_button.pack(side="left", padx=10)
font_color_label = tk.Label(settings_frame, text="Font color (R,G,B):")
font_color_label.pack(side="left")
font_color_entry = tk.Entry(settings_frame)
font_color_entry.pack(side="left")
font_color_entry.insert(0, str(FONT_COLOR))
font_color_button = tk.Button(settings_frame, text="Update", command=lambda: update_font_color(eval(font_color_entry.get())))
font_color_button.pack(side="left", padx=10)
bg_color_label = tk.Label(settings_frame, text="Background color (R,G,B):")
bg_color_label.pack(side="left")
bg_color_entry = tk.Entry(settings_frame)
bg_color_entry.pack(side="left")
bg_color_entry.insert(0, str(BG_COLOR))
bg_color_button = tk.Button(settings_frame, text="Update", command=lambda: update_bg_color(eval(bg_color_entry.get())))
bg_color_button.pack(side="left", padx=10)

# Start the GUI
root.mainloop()

