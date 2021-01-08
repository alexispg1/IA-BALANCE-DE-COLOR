import cv2
import numpy as np
import math
import tkinter.filedialog
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from matplotlib import pyplot as plt
import tkinter.filedialog
from tkinter import simpledialog
from tkinter import messagebox

def select_image():
    global panelA, panelB, image, panelC, panelD, btn2, btn3, btn4
    path = tk.filedialog.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        edged =  cv2.imread(path)
        image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        edged = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image2 = Image.fromarray(image2)
        edged = Image.fromarray(edged)
        
        image2 = ImageTk.PhotoImage(image2)
        edged = ImageTk.PhotoImage(edged)
        if panelA is None or panelB is None:
    	# 	# the first panel will store our original image
            panelA = tk.Label(image=image2)
            panelA.image = image2
            panelA.pack(side="left", padx=10, pady=10)
		# 	# while the second panel will store the edge map
            panelB = tk.Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)
		#     # otherwise, update the image panels

            panelC = tk.Label(image=image2)
            panelC.image = image2
            panelC.pack(side="left", padx=10, pady=10)

            panelD = tk.Label(image=image2)
            panelD.image = image2
            panelD.pack(side="left", padx=10, pady=10)
            btn2.config( state = 'active')
            btn3.config( state = 'active')
            btn4.config( state = 'active')
        else:
		# 	# update the pannels
            panelA.configure(image=image2)
            panelB.configure(image=edged)
            panelA.image = image2
            panelB.image = edged
            panelC.configure(image=image2)
            panelD.configure(image=edged)
            panelC.image = image2
            panelD.image = edged

def Grayworld():
    global image, panelB
    image2 = np.array(image)
    sumatoria_total_canal_R=np.sum(image[:,:,0])
    sumatoria_total_canal_G=np.sum(image[:,:,1])
    sumatoria_total_canal_B=np.sum(image[:,:,2])
    
    arreglo_sumatoria_de_canales=[]
    arreglo_sumatoria_de_canales.append(sumatoria_total_canal_R)
    arreglo_sumatoria_de_canales.append(sumatoria_total_canal_G)
    arreglo_sumatoria_de_canales.append(sumatoria_total_canal_B)
    sumatoria_minima=min(arreglo_sumatoria_de_canales)
    
    ksR=sumatoria_minima/sumatoria_total_canal_R
    ksG=sumatoria_minima/sumatoria_total_canal_G
    ksB=sumatoria_minima/sumatoria_total_canal_B

    image2[:,:,0]=image[:,:,0]*ksR
    image2[:,:,1]=image[:,:,1]*ksG
    image2[:,:,2]=image[:,:,2]*ksB
    
    imgaux = np.array(image2)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    image2 = Image.fromarray(image2)
    image2 = ImageTk.PhotoImage(image2)
    panelC.configure(image=image2)
    panelC.image = image2
    graphics(imgaux,image, "Grayworld")

def Scalebymax():
    global panelD
    image2 = np.array(image)
    maximo_R=np.amax(image[:,:,0])
    maximo_G=np.amax(image[:,:,1])
    maximo_B=np.amax(image[:,:,2])

    arreglo_de_maximos=[]
    arreglo_de_maximos.append(maximo_R)
    arreglo_de_maximos.append(maximo_G)
    arreglo_de_maximos.append(maximo_B)
    minimo_de_los_maximos=min(arreglo_de_maximos)

    kmR =minimo_de_los_maximos/maximo_R
    kmG =minimo_de_los_maximos/maximo_G
    kmB=minimo_de_los_maximos/maximo_B
   
    image2[:,:, 0]=image[:,:,0]*kmR
    image2[:,:, 1]=image[:,:,1]*kmG
    image2[:,:, 2]=image[:,:,2]*kmB

    imgaux = np.array(image2)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    image2 = Image.fromarray(image2)
    image2 = ImageTk.PhotoImage(image2)
    panelD.configure(image=image2)
    panelD.image = image2
    graphics(imgaux,image, "Scalebymax")
   
def Shadesofgray():
    exponente=input_dialog("ingrese el exponente")
    alto, ancho = image.shape[0:2]
    image2 = np.array(image)
    #print("el exponentes es ",exponente)
    p=exponente
    cuadrado_R = 0
    cuadrado_G = 0
    cuadrado_B = 0
    
    for y in range(alto):
        for x in range(ancho):
            cuadrado_R =np.uint64(cuadrado_R+np.power(image[y,x,0],p))
            cuadrado_G =np.uint64(cuadrado_G+np.power(image[y,x,1],p))
            cuadrado_B =np.uint64(cuadrado_B+np.power(image[y,x,2],p))

    print("cuadrado R",cuadrado_R)
    print("cuadrado G",cuadrado_G)
    print("cuadrado B",cuadrado_B)
    raiz_R=math.sqrt(cuadrado_R)
    raiz_G=math.sqrt(cuadrado_G)
    raiz_B=math.sqrt(cuadrado_B)
    
    arreglo_de_raizes=[]
    arreglo_de_raizes.append(raiz_R)
    arreglo_de_raizes.append(raiz_G)
    arreglo_de_raizes.append(raiz_B)
    raiz_minima=min(arreglo_de_raizes)
    
    cksR=raiz_minima/raiz_R
    cksG=raiz_minima/raiz_G
    cksB=raiz_minima/raiz_B
    
    image2[:,:,0] = image[:,:,0] * cksR
    image2[:,:,1] = image[:,:,1] * cksG
    image2[:,:,2] = image[:,:,2] * cksB
   
    imgaux = np.array(image2)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    image2 = Image.fromarray(image2)
    image2 = ImageTk.PhotoImage(image2)
    panelB.configure(image=image2)
    panelB.image = image2
    graphics(imgaux,image,"Shadesofgray")

def graphics(imgaux,image, metodo):
    hist = cv2.calcHist([imgaux], [2], None, [256], [0, 256])  
    plt.subplot(221)
    plt.plot(hist, color = 'r', label=metodo)
    hist = cv2.calcHist([image], [2], None, [256], [0, 256])
    plt.plot(hist, color = '#d11367',label="Original")
    plt.xlim([0,256])
    plt.title('Comparacion canal Red')
    plt.legend()
    

    hist = cv2.calcHist([imgaux], [1], None, [256], [0, 256])
    plt.subplot(222)
    plt.plot(hist, color = 'g', label=metodo)
    hist = cv2.calcHist([image], [1], None, [256], [0, 256])
    plt.plot(hist, color = '#17c556',label="Original")
    plt.xlim([0,256])
    plt.title('Comparacion canal Green')
    plt.legend()
    

    hist = cv2.calcHist([imgaux], [0], None, [256], [0, 256])
    plt.subplot(223)
    plt.plot(hist, color = '#3390FF', label=metodo)
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist, color = '#256CC1',label="Original")
    plt.xlim([0,256])
    plt.title('Comparacion canal Blue')
    plt.legend()
    plt.show()

def input_dialog(text):
    try:
        root=tk.Tk()
        root.withdraw()
        value=simpledialog.askstring(title="grados",prompt=text)
        number=int(value)
        return number
    except:
        if value is None:
            print("algo malo a ocurrido")  
        else:
            messagebox.showinfo("informacion ","ingrese un valor entero") 
              
image = None
panelA = None
panelB = None
panelC = None
panelD = None
visual = tk.Tk()
visual.title("Mundo de grises")

btn4 = tk.Button(visual, text="Shades-of-gray", command=Shadesofgray, state = 'disabled')
btn4.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

btn3 = tk.Button(visual, text="Scale-by-max", command=Scalebymax, state = 'disabled')
btn3.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

btn2 = tk.Button(visual, text="Gray-world", command=Grayworld, state = 'disabled')
btn2.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

btn = tk.Button(visual, text="Seleccionar imagen", command=select_image)
btn.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

visual.mainloop()
