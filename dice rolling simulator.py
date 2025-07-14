import tkinter
from PIL import Image, ImageTk
import random
import os

root = tkinter.Tk()
root.geometry("400x400")
root.title("Dice Rolling Simulator")

l1 = tkinter.Label(root, text="Roll the Dice", fg="blue", bg="dark green", font="Helvetica 16 bold")
l1.pack()

# Dynamically load dice images from the 'images' directory
dice_dir = "images"
dice = [os.path.join(dice_dir, f"{i}dice.png") for i in range(1, 7)]

# Try to load the first dice image
try:
    image1 = ImageTk.PhotoImage(Image.open(dice[0]))
except Exception as e:
    print("Error loading image:", e)
    image1 = None

if image1 is not None:
    label1 = tkinter.Label(root, image=image1)
    label1.image = image1
else:
    label1 = tkinter.Label(root, text="Image not found", fg="red")
label1.pack(expand=True)

def rolling_dice():
    try:
        img_path = random.choice(dice)
        image1 = ImageTk.PhotoImage(Image.open(img_path))
        label1.configure(image=image1, text="")
        label1.image = image1
    except Exception as e:
        print("Error loading image:", e)
        label1.configure(image="", text="Image not found", fg="red")

button = tkinter.Button(root, text="Roll the Dice", fg='blue', command=rolling_dice)
button.pack(expand=True)

root.mainloop()

