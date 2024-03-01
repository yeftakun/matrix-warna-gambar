'''
pip install Pillow
'''
from tkinter import filedialog
from tkinter import *
from PIL import Image
from tkinter import messagebox
import tkinter.ttk as ttk

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
        ##continuar para pegar os pixels e ler como img
        
        w = open('WarnaMatrix.txt','w')
        w.writelines(str(pixels))
        w.close()
        messagebox.showinfo('OK','Matrix berhasil dibuat!\nPeriksa file WarnaMatrix.txt di direktori saat ini!')
        msg["text"] = ''
    except:
        msg["text"] = ''
        pass

#main
window = Tk()
window.title("Gambar dalam Matriks 3D RGB/RGBA - Tugas PCD")
k = ttk.Button(window,text='Pilih gambar',command = openFile,cursor="hand2")
window.geometry('450x100+300+50')
k.pack()
msg = ttk.Label(window,text='')
msg.pack()
window.mainloop()   



#salva matrix 3D de cores da imagem no txt