import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageFont


def add_watermark():
    file_path = askopenfilename(title="Select Image", filetypes=[('Image Files', '*.jpg')])
    file_name = file_path.split("/")[-1]
    img = Image.open(file_path)
    img_height = int(img.height/2)
    img_width = int(img.width/10)

    I1 = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf", 40)

    I1.text((img_width, img_height), "your custom watermark here", fill=(147, 179, 199, 0), font=font)

    img.show()

    if not os.path.isdir("C:/Users/jack/Desktop/watermarked"):
        os.makedirs("C:/Users/jack/Desktop/watermarked")
        img.save(f"C:/Users/jack/Desktop/watermarked/{file_name}")
    else:
        img.save(f"C:/Users/jack/Desktop/watermarked/{file_name}")


def quit():
    window.destroy()


window = Tk()
window.title("Photo Watermark App")

canvas = Canvas(window, width=600, height=500)
canvas.grid(columnspan=5, rowspan=4)

instruction_label = Label(window, text="Select photo to watermark.", font="Ariel")
instruction_label.grid(columnspan=5, column=0, row=1)

browse_btn = Button(window, command=add_watermark, text="Browse", font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
browse_btn.grid(column=2, row=2)

quit_btn = Button(window, command=quit, text="Quit", font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
quit_btn.grid(column=3, row=2)

window.mainloop()

