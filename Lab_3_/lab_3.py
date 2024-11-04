import cv2
from PIL import Image as Img
from PIL import ImageTk as ImgTk
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter.messagebox import showerror

def sharpness(img):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel)
    return img

def global_thresholdingOtsu(img):
    blur = cv2.GaussianBlur(img,(5,5),0)

    hist = cv2.calcHist([blur],[0],None,[256],[0,256])
    hist_norm = hist.ravel()/hist.sum()
    Q = hist_norm.cumsum()

    bins = np.arange(256)

    fn_min = np.inf
    thresh = -1

    for i in range(1,256):
        p1,p2 = np.hsplit(hist_norm,[i])
        q1,q2 = Q[i],Q[255]-Q[i]
        if q1 < 1.e-6 or q2 < 1.e-6:
            continue
        b1,b2 = np.hsplit(bins,[i])

        m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
        v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2

        fn = v1*q1 + v2*q2
        if fn < fn_min:
            fn_min = fn
    thresh = i

    return thresh

def global_thresholding_Otsu(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return th3

def adaptive1(img):
    mean_img = Img.fromarray(img).convert('L')
    arr2 = cv2.adaptiveThreshold(np.array(mean_img), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 20)
    return arr2.astype(np.uint8)

def adaptive2(img):
    mean_img = Img.fromarray(img).convert('L')
    arr2 = cv2.adaptiveThreshold(np.array(mean_img), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 20)
    return arr2.astype(np.uint8)

filepath = ''
def get_image():
    global filepath
    filepath = ''
    filepath = filedialog.askopenfilename()
    if filepath == '':
        return
    file_path.delete(0, END)
    file_path.insert(INSERT, filepath)
    image = Img.open(filepath)
    global photo
    photo = ImgTk.PhotoImage(image.resize((720,480)))
    image = canvas.create_image(0, 0, anchor='nw',image=photo)
      
def original():
    image = canvas.create_image(0, 0, anchor='nw',image=photo)
    
def sharpening_filter():
    img = cv2.imread(filepath)
    sharpened_img = sharpness(img)
    sharpened_image = Img.fromarray(sharpened_img)
    global final1
    final1 = ImgTk.PhotoImage(sharpened_image.resize((720,480)))
    image = canvas.create_image(0, 0, anchor='nw',image=final1)
    
def global_thresholding_1():
    img = cv2.imread(filepath)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    user_threshold = simpledialog.askinteger('Input', 'Input threshold value', parent=root, initialvalue=0)
    ret, thresh1 = cv2.threshold(gray_img, user_threshold, 255, cv2.THRESH_BINARY)
    new_img = thresh1
    new_image = Img.fromarray(new_img)
    global final2
    final2 = ImgTk.PhotoImage(new_image.resize((720,480)))
    image = canvas.create_image(0, 0, anchor='nw',image=final2)
    
def global_thresholding_2():
    img = cv2.imread(filepath)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    user_threshold = simpledialog.askinteger('Input', 'Input threshold value', parent=root, initialvalue=0)
    ret, thresh1 = cv2.threshold(gray_img, user_threshold, 255, cv2.THRESH_TRUNC)
    new_img = thresh1
    new_image = Img.fromarray(new_img)
    global final3
    final3 = ImgTk.PhotoImage(new_image.resize((720,480)))
    image = canvas.create_image(0, 0, anchor='nw',image=final3)
    
def adaptive_thresholding_1():
    img = cv2.imread(filepath)
    sharpened_img = adaptive1(img)
    sharpened_image = Img.fromarray(sharpened_img)
    global final5
    final5 = ImgTk.PhotoImage(sharpened_image.resize((720,480)))
    image = canvas.create_image(0, 0, anchor='nw',image=final5)
    
def adaptive_thresholding_2():
    img = cv2.imread(filepath)
    sharpened_img = adaptive2(img)
    sharpened_image = Img.fromarray(sharpened_img)
    global final6
    final6 = ImgTk.PhotoImage(sharpened_image.resize((720,480)))
    image = canvas.create_image(0, 0, anchor='nw',image=final6) 
    
def otsu():
    img = cv2.imread(filepath)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    new_img = global_thresholding_Otsu(gray_img)
    new_image = Img.fromarray(new_img)
    global final7
    final7 = ImgTk.PhotoImage(new_image.resize((720,480)))
    image = canvas.create_image(0, 0, anchor='nw',image=final7)
    
root = Tk()
root.title("Digital image processing")
root.geometry('1000x600')
root.configure(bg='#323332')

# Кнопка выбора папки
btn_file_path = Button(root, text="Browse", command=get_image, width=10, bg='#5f615f', font=('Times New Roman', 12, 'bold'), foreground='#FFFFFF')  # Цвета Barbie
btn_file_path.grid(row=0, column=0, padx=20, pady=20, sticky=(W, E))

# Поле ввода папки
file_path = Entry(root, width=70, bg='#5f615f', font=('Times New Roman', 12, 'bold'), foreground='#FFFFFF')
file_path.grid(row=0, column=1, padx=20, pady=20, sticky=(W, E))
file_path.insert(INSERT, "Select an image...")

original_button = Button(root, text="Original", command=original, width=15, bg='#5f615f', font=('Times New Roman', 12, 'bold'), foreground='#FFFFFF')
sharpening_filter_button = Button(root, text="Sharpening filter", command=sharpening_filter, width=15, bg='#5f615f', font=('Times New Roman', 12, 'bold'), foreground='#FFFFFF')
global_thresholding_1_button = Button(root, text="Global thresholding 1", command=global_thresholding_1, width=15, bg='#5f615f', font=('Times New Roman', 12, 'bold'), foreground='#FFFFFF')
global_thresholding_2_button = Button(root, text="Global thresholding 2", command=global_thresholding_2, width=15, bg='#5f615f', font=('Times New Roman', 12, 'bold'), foreground='#FFFFFF')
adaptive_thresholding_1_button = Button(root, text="Adaptive thresholding 1", command=adaptive_thresholding_1, width=15, bg='#5f615f', font=('Times New Roman', 12, 'bold'), foreground='#FFFFFF')
adaptive_thresholding_2_button = Button(root, text="Adaptive thresholding 2", command=adaptive_thresholding_2, width=15, bg='#5f615f', font=('Times New Roman', 12, 'bold'), foreground='#FFFFFF')
otsu_button = Button(root, text="Otsu", command=otsu, width=15, bg='#5f615f', font=('Times New Roman', 12, 'bold'), foreground='#FFFFFF')

original_button.place(x=25, y=95)
sharpening_filter_button.place(x=25, y=170)
global_thresholding_1_button.place(x=25, y=245)
global_thresholding_2_button.place(x=25, y=310)
adaptive_thresholding_1_button.place(x=25, y=395)
adaptive_thresholding_2_button.place(x=25, y=470)
otsu_button.place(x=25, y=545)

style = ttk.Style()
style.theme_use("default")

root.grid_rowconfigure(1, weight=1)

root.grid_columnconfigure(1, weight=1)

canvas = Canvas(root, height=480, width=720)
canvas.grid(row=1, column=1)

root.resizable(False, False)
root.mainloop()