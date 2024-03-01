from tkinter import filedialog
from tkinter import *
from PIL import Image
from tkinter import messagebox
import tkinter.ttk as ttk
import os

def openFile():
    msg["text"] = 'Memproses...'
    image_formats= [("Imagens","*.jpg;*.jpeg;*.png;*.gif;*.apng;*.tiff;*.tif;*.bmp;*.xcf;.*webp")]
    k =  filedialog.askopenfilename(title = "Pilih gambar",filetypes=image_formats)
    try:
        pixels=[]    
        im = Image.open(k)
        for i in im.getdata():
            pixels.append(list(i))
        width, height = im.size
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        
        # Menyimpan matriks warna ke dalam file WarnaMatrix.txt di direktori ./hasil/
        output_dir = './hasil/'
        os.makedirs(output_dir, exist_ok=True)
        output_file_path = os.path.join(output_dir, 'WarnaMatrix.txt')
        with open(output_file_path, 'w') as w:
            w.writelines(str(pixels))
        
        messagebox.showinfo('OK','Matrix berhasil dibuat!\nPeriksa file WarnaMatrix.txt di direktori ./hasil/!')
        msg["text"] = ''
    except Exception as e:
        print(e)
        msg["text"] = ''

#main
window = Tk()
window.title("Gambar dalam Matriks 3D RGB/RGBA - Tugas PCD")
k = ttk.Button(window,text='Pilih gambar',command = openFile,cursor="hand2")
window.geometry('450x100+300+50')
k.pack()
msg = ttk.Label(window,text='')
msg.pack()
window.mainloop()
