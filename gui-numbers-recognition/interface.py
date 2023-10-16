import tkinter as tk
from PIL import Image, ImageTk
import io

import numpy as np


def capture_canvas_content(canvas):
    # Capture le contenu du canevas sous forme de fichier PostScript
    ps = canvas.postscript(colormode='color')

    # Convertit le fichier PostScript en une image PIL
    image = Image.open(io.BytesIO(ps.encode('utf-8')))

    # Retourne l'image PIL
    return image


window = tk.Tk()

window.title("Numbers Recognition")
window.geometry("500x500")


def draw(event):
    x = event.x
    y = event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")


canvas = tk.Canvas(window, width=200, height=200)
canvas.create_rectangle(1, 1, 199, 199, outline="black")
canvas.pack()
canvas.bind("<B1-Motion>", draw)


def buttonClick():
    # Chargez votre image
    image = capture_canvas_content(canvas)
    image = image.resize((28, 28))
    image = image.convert('L')

    # Préparez votre image pour l'entrée du modèle
    image_array = np.array(image)  # Convertir l'image en tableau numpy
    image_array = image_array / 255.0  # Normaliser les valeurs de pixel entre 0 et 1
    image_array = image_array.reshape(1, 28, 28, 1)
    print(image_array.shape)


btn = tk.Button(window, text="Predict", command=buttonClick)
btn.pack()


window.mainloop()
