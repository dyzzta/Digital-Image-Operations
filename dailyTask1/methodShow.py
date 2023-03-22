import cv2
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import filedialog


def process_image():
    
    filename = filedialog.askopenfilename(initialdir="/", title="Select the image",
                                          filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")))
    
    
    img = cv2.imread(filename)

    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    kernel_size = int(e1.get())

    
    kernel_mean = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size*kernel_size)
    filtered_mean = cv2.filter2D(gray,-1,kernel_mean)

    filtered_median = cv2.medianBlur(gray, kernel_size)

    filtered_gaussian = cv2.GaussianBlur(gray, (kernel_size,kernel_size), 0)

    filtered_bilateral = cv2.bilateralFilter(gray, kernel_size, 75, 75)

    
    plt.subplot(2,3,1),plt.
window = Tk()
window.title("4 filter method")


btn_browse = Button(window, text="Gozat", command=process_image)
btn_browse.pack(pady=10)


lbl1 = Label(window, text="Kernel Boyutu:")
lbl1.pack(pady=5)
e1 = Entry(window)
e1.insert(END,'3')
e1.pack(pady=5)


btn_exit = Button(window, text="Cikis", command=exit_program)
btn_exit.pack(padx=200,pady=100)


window.mainloop()