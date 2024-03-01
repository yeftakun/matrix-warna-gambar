from tkinter import filedialog
from tkinter import *
from PIL import Image
from tkinter import messagebox
import tkinter.ttk as ttk
import ast
import os

def openFile():
    msg["text"] = 'Memproses...'
    filename = filedialog.askopenfilename(title="Pilih file teks", filetypes=[("Teks Files", "*.txt")])
    try:
        with open(filename, 'r') as file:
            data = file.read()
            pixels = ast.literal_eval(data)

        width = len(pixels[0])
        height = len(pixels)
        im = Image.new("RGB", (width, height))
        for y in range(height):
            for x in range(width):
                im.putpixel((x, y), tuple(pixels[y][x]))

        # Menyimpan hasil gambar di direktori ./hasil/
        output_dir = './hasil/'
        os.makedirs(output_dir, exist_ok=True)
        output_file_path = os.path.join(output_dir, 'hasil_gambar.png')
        im.save(output_file_path)
        
        messagebox.showinfo('OK', 'Gambar berhasil dibuat!\nPeriksa file hasil_gambar.png di direktori ./hasil/!')
        msg["text"] = ''
    except Exception as e:
        print(e)
        msg["text"] = ''

#main
window = Tk()
window.title("Matriks Warna ke Gambar - Tugas PCD")
k = ttk.Button(window, text='Buka file teks', command=openFile, cursor="hand2")
window.geometry('450x100+300+50')
k.pack()
msg = ttk.Label(window, text='')
msg.pack()
window.mainloop()
