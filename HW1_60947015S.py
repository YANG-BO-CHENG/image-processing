import tkinter as tk 
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import Image,ImageTk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
#建立主視窗
window =tk.Tk()
canvas=tk.Canvas() 
filename = tk.StringVar()
filenewname = tk.StringVar()

#標題
window.title('AIP 60947015S')
#視窗大小
window.geometry("1000x500") #寬x高
window.resizable(0,0)


#顏色
window.config(background='skyblue')
#透明度
window.attributes("-alpha",0.9)#1-0
#cv2.waitKey(0)
#cv2.destroyAllWindows()

def upload():
   global images
   global img_1
  #讀取圖片路徑檔
   filename = askopenfilename(initialdir = "/",title = "Select file",filetypes = [("png files","*.png"),("jpeg files","*.jpg"),( "ppm files","*.ppm"),("BMP files","*.bmp"),("all files", "*.*")])
   images = Image.open(filename)
   itr=images.format
  #固定圖片寬高
   images = images.resize((360,360 ),Image.ANTIALIAS)
  #輸入圖片
   photo = ImageTk.PhotoImage(images)
   img= tk.Label(frame,image=photo)
   if not img:
     return
   img.images = photo
   img.place(x=0, y=0)
   messagebox.showinfo("tittle","圖片寬*高:"+(str(images.size))+ "圖片格式:"+(str(itr)))
  #輸出圖片    
   img_1= tk.Label(frame_R ,image=photo)
   img_1.images = photo
   img_1.place(x=0, y=0)
 

   
  


def download():
  
   files = [("jpeg files","*.jpg")]    
   filenewpath = asksaveasfilename(filetype=files,defaultextension='.jpg')  
   filenewname.set(filenewpath)  
   if not filenewpath:
    return
   images.save(str(filenewname.get()))
   messagebox.showinfo("tittle","已下載JPG檔案")

                     
#frame 框架
frame_top = tk.Frame(window,width=1000,height=400)
frame_top.place(x=20, y=50)
frame_p = tk.LabelFrame(frame_top,text="function",width=160,height=400)
frame_p.place(x=10, y=0)
#labelframe

frame=tk.LabelFrame(frame_top,text="input-image",width=400,height=400)
frame.place(x=170, y=0)

frame_R=tk.LabelFrame(frame_top,text="Output-image",width=400,height=400)
frame_R.place(x=570, y=0)


#button

btn= tk.Button(frame_p,text='uploadfile',command=upload)
btn.config(width=20,height=1)
btn.place(x=5, y=10)



btn1= tk.Button(frame_p,text='savefile',command=download)
btn1.config(width=20,height=1)
btn1.place(x=5, y=50)



#視窗持續存在
window.mainloop()