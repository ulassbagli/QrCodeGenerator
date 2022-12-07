import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyqrcode
import qrcode
import sys
from tkinter import filedialog
import cv2
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import pyzbar.pyzbar as pyzbar
import webbrowser
import customtkinter
from typing import List
import tkinter.messagebox
import pyqrcode
from pyqrcode import create
import png
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def qrcode_okuyucu():
    img = cv2.imread('channel.png')
    cap = cv2.VideoCapture(0)


    while True:
        _, frame = cap.read()
        cv2.imshow("Kamera", frame)

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
        

            if len(obj) >= 1:
                import webbrowser
                webbrowser.open(obj.data.decode('utf-8'))
                exit()

        key = cv2.waitKey(1)
        
        if key == 27:
            break

def qr_code_olusturucu():
    my_w = tk.Tk()
    my_w.geometry("410x400")
    my_w.title("Qr Kod Oluşturucu")

    e1=tk.Entry(my_w,font=22,bg='white',width=15)
    e1.grid(row=0,column=0,padx=10,pady=4)
    b1=tk.Button(my_w,font=22,text='Qr Kodu Oluştur',
        command=lambda:my_generate())
    b1.grid(row=0,column=1,padx=5,pady=4)

    l1=tk.Label(my_w,text='Qr Oluşturmak İçin Buraya Yazınız.')
    l1.grid(row=1,column=0,columnspan=2)
    path=''

    def my_generate():
        global my_img
        my_qr = pyqrcode.QRCode(e1.get(),error = 'H') 
        my_qr.png(path, scale=10,module_color=[0, 0, 0, 128], 
            background=[0xff, 0xcc, 0xcc])
        im = Image.open(path)
        im = im.convert("RGBA")
        logo = Image.open("")
        box = (90,150,250,170)
        im.crop(box)
        region = logo
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        im.paste(region,box)
        im.show() 
        im.save("path","PNG")
        my_img = tk.PhotoImage(file = "path") 
        l1.config(image=my_img)  

    my_w.mainloop()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Qr Code Oluşturma Ve Okuma")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="QrCode", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Qr code okumak için tıklayınız.",command=qrcode_okuyucu)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Qr Code Oluşturmak İçin Tıklayınız",command=qr_code_olusturucu)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Sistem Teması:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Arayüz Ölçeklendirme:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


if __name__ == "__main__":
    app = App()
    app.mainloop()



