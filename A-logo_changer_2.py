import os
import shutil
from PIL import Image, ImageTk
from tkinter import Tk, Listbox, Button, Label, Canvas, END

def get_png_files():
    png_files = [f for f in os.listdir("logos") if f.endswith(".png")]
    return png_files

def initialize_logo_name_txt():
    if not os.path.isfile("logo_name.txt"):
        png_files = get_png_files()
        if png_files:
            with open("logo_name.txt", "w") as f:
                f.write(png_files[0])

def swap_logo():
    selected_file = listbox.get(listbox.curselection())
    logo_path = "logo.png"
    selected_file_path = os.path.join("logos", selected_file)
    
    if os.path.isfile(logo_path):
        with open("logo_name.txt", "r") as f:
            original_name = f.read()
        original_path = os.path.join("logos", original_name)
        shutil.move(logo_path, original_path)
    
    with open("logo_name.txt", "w") as f:
        f.write(selected_file)
    
    shutil.move(selected_file_path, logo_path)
    update_listbox()

def update_listbox():
    listbox.delete(0, END)
    png_files = get_png_files()
    for file in png_files:
        listbox.insert(END, file)

def show_logo_preview(event):
    selected_file = listbox.get(listbox.curselection())
    image_path = os.path.join("logos", selected_file)
    preview_image = Image.open(image_path).resize((200, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(preview_image)
    preview_label.config(image=photo)
    preview_label.image = photo

def toggle_logo():
    logo_files = get_png_files()
    counter_file = "counter.txt"
    if not os.path.isfile(counter_file):
        with open(counter_file, "w") as f:
            f.write("0")
    
    with open(counter_file, "r+") as f:
        count = int(f.read())
        count += 1
        f.seek(0)
        f.write(str(count))
        f.truncate()

    selected_file = logo_files[count % len(logo_files)]
    listbox.selection_clear(0, END)
    listbox.selection_set(logo_files.index(selected_file))
    listbox.event_generate("<<ListboxSelect>>")

# Initialize logo_name.txt
initialize_logo_name_txt()

# Create the main window
root = Tk()
root.title("Logo Swapper")
root.configure(bg='lightblue')

# Create a list box and fill it with the PNG files
listbox = Listbox(root, bg='white', fg='black', font=("Arial", 12))
update_listbox()
listbox.bind("<<ListboxSelect>>", show_logo_preview)
listbox.pack(pady=10, padx=10)

# Create a preview label
preview_label = Label(root)
preview_label.pack(pady=10)

# Create a swap button
swap_button = Button(root, text="Swap Logo", command=swap_logo, bg='blue', fg='white')
swap_button.pack(pady=5)

# Create a toggle button
toggle_button = Button(root, text="Toggle Logo", command=toggle_logo, bg='purple', fg='white')
toggle_button.pack(pady=5)

# Start the main loop
root.mainloop()
