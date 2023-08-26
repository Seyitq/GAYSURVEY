from tkinter import * # tkinter kütüphanesini dahil ediyoruz
from tkinter import messagebox
import random

def no():
    messagebox.showinfo('BAŞARDIN', 'ADAMSIN') # messagebox ile kullanıcıya mesaj gösteriyoruz
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500)) # 0 ile 500 arasında rastgele x ve y değerleri alıp butonu o konuma yerleştiriyoruz

root = Tk() # tkinter penceresi oluşturuyoruz
root.geometry('600x600') # pencerenin boyutunu ayarlıyoruz
root.title('anket') # pencerenin başlığını ayarlıyoruz
root.resizable(False, False) # pencerenin boyutunun değiştirilmesini engelliyoruz
root['bg'] = 'white' # pencerenin arkaplan rengini ayarlıyoruz

label = Label(root, text='Gaymisin', font='Arial 20 bold', bg='white').pack() # label oluşturuyoruz
btnYes = Button(root, text='Hayır', font='Arial 20 bold') # buton oluşturuyoruz
btnYes.place(x=170, y=100) # butonu konumlandırıyoruz
btnYes.bind('<Enter>', motionMouse) # butona fare ile tıklandığında motionMouse fonksiyonunu çalıştırıyoruz
btnNo = Button(root, text='Evet', font='Arial 20 bold', command=no).place(x=350, y=100) # buton oluşturuyoruz ve butona tıklandığında no fonksiyonunu çalıştırıyoruz
root.mainloop() # pencereyi açıyoruz