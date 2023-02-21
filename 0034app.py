import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

def mandelbrot(h,w, maxit=20):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2            # who is diverging
        div_now = diverge & (divtime==maxit)  # who is diverging now
        divtime[div_now] = i                  # note when
        z[diverge] = 2                        # avoid diverging too much

    return divtime

def on_button_click():
    # Create the fractal image
    img = Image.fromarray(mandelbrot(400, 400))

    # Update the image displayed by the label
    image_label.configure(image=img)
    image_label.image = img

root = tk.Tk()