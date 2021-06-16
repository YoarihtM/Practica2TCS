from tkinter import *
import tkinter.filedialog
from PIL import Image,ImageTk
from scipy.io import wavfile
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import pyaudio
import wave
import threading
import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
from tkinter import messagebox

class GUI:
    def list2string(self, lista):
        datos = ''
        
        for dato in lista:
            datos += str(dato) + ', '
        
        return datos
    
    def updtGrafica(self, data):
        self.graf.clear()
        self.graf.plot(data)
        self.canvas_grafica.get_tk_widget().pack(side=RIGHT, fill=BOTH)
        self.canvas_grafica.draw()
    
    def updtGrafica2(self, data, axis):
        self.graf.clear()
        self.graf.plot(data, axis)
        self.canvas_grafica.get_tk_widget().pack(side=RIGHT, fill=BOTH)
        self.canvas_grafica.draw()

    def comparaGrafica(self, dato1, dato2):
        self.graf.clear()
        self.graf.plot(dato1)
        self.graf.plot(dato2)
        self.canvas_grafica.get_tk_widget().pack(side=RIGHT, fill=BOTH)
        self.canvas_grafica.draw()
    
    def Desplazamiento(self, serie, k):
        l_serie1 = serie.split(', ')
        num_serie1 = []
        res = []
        
        for valor in l_serie1:
            num_serie1.append(float(valor))
        
        for s in num_serie1:
            res.append(s + k)
        
        datos = self.list2string(res)
        self.comparaGrafica(num_serie1, res)
        messagebox.showinfo('Datos resultantes del desplazamiento', datos)

    def Amplifica(self, serie, factor):
        l_serie1 = serie.split(', ')
        num_serie1 = []
        res = []
        
        for valor in l_serie1:
            num_serie1.append(float(valor))
        
        for s in num_serie1:
            res.append(s*factor)
        
        datos = self.list2string(res)
        self.comparaGrafica(num_serie1, res)
        messagebox.showinfo('Datos resultantes de la amplificación', datos)

    def Atenua(self, serie, factor):
        l_serie1 = serie.split(', ')
        num_serie1 = []
        res = []
        
        for valor in l_serie1:
            num_serie1.append(float(valor))
        
        for s in num_serie1:
            res.append(s*(1/factor))
        
        datos = self.list2string(res)
        self.comparaGrafica(num_serie1, res)
        messagebox.showinfo('Datos resultantes de la amplificación', datos)
    
    def reflexion(self, serie):
        l_serie1 = serie.split(', ')
        num_serie1 = []
        
        for valor in l_serie1:
            num_serie1.append(float(valor))
        
        res = num_serie1[::-1]
        print(res)
        self.updtGrafica(res)
        
        datos = self.list2string(res)
        messagebox.showinfo('Datos resultantes de la convolución', datos)

    def Diezmacion(self, serie, k):
        l_serie1 = serie.split(', ')
        num_serie1 = []
        
        for valor in l_serie1:
            num_serie1.append(float(valor))
        
        np.asarray(num_serie1)
        res = num_serie1[:-k:k]
        
        datos = self.list2string(res)
        self.updtGrafica2(res, res)
        messagebox.showinfo('Datos resultantes de la diezmación', datos)

    def Interpolacion(self, serie, factor, tipo):
        l_serie = serie.split(', ')
        print(l_serie)
        num_serie = []
        res = []
        
        for valor in l_serie:
            num_serie.append(float(valor))
        
        np.asarray(num_serie)
        
        if(tipo == "linear"):
            for x in range(0,len(num_serie)-1):
                suma = abs((abs(num_serie[x]) - abs(num_serie[x+1])) / factor) 
                print("La suma es ", suma)
                acumulador = suma
                res.append(num_serie[x])
                for y in range(0,factor):
                    res.append(round((num_serie[x] + acumulador),1))
                    acumulador += suma
        elif(tipo == "escalon"):
            for x in range(0,len(num_serie)-1):
                res.append(num_serie[x])
                for y in range(0,factor):
                    res.append(num_serie[x])
            res.append(num_serie[len(num_serie)-1])
        elif(tipo == "zeros"):
            for x in range(0,len(num_serie)-1):
                res.append(num_serie[x])
                for y in range(0,factor):
                    res.append(0)
            res.append(num_serie[len(num_serie)-1])
            
        res_np = np.asarray(res)
        datos = self.list2string(res_np)
        self.updtGrafica(res_np)
        messagebox.showinfo('Datos resultantes de la convolución de tipo ' + tipo, datos)

    def convolucion(self, serie1, serie2):
        l_serie1 = serie1.split(', ')
        l_serie2 = serie2.split(', ')
        # print(l_serie1)
        # print(l_serie2)
        
        num_serie1 = []
        num_serie2 = []
        
        for valor in l_serie1:
            num_serie1.append(float(valor))
            
        for valor in l_serie2:
            num_serie2.append(float(valor))
        
        # print(num_serie1)
        # print(num_serie2)
        res = np.convolve(num_serie1,num_serie2,mode="same")
        
        datos = self.list2string(res)
        
        self.updtGrafica(res)
        messagebox.showinfo('Datos resultantes de la convolución', datos)
    
    def color(self):
        if self.color_base == '#24264F':
            self.color_base = '#FFFFFF'
            self.color_fuente = '#24264F'
            
            self.img_sol = Image.open('./img_interfaz/media-luna.png')
            self.img_sol = self.img_sol.resize((50,50), Image.ANTIALIAS)
            self.img_sol = ImageTk.PhotoImage(self.img_sol)
            self.btnSol = Button(self.frame1, image=self.img_sol, text='Abrir', bg=self.color_base, command=self.color)
            self.btnSol.place(x=755,y=55)   
            
            self.frame1.config(bg=self.color_base)
            self.frame2.config(bg=self.color_base)
            self.frame3.config(bg=self.color_base)
            
            self.lblTitulo.config(bg=self.color_base, fg=self.color_fuente)
            self.lblOperaciones.config(bg=self.color_base, fg=self.color_fuente)
            self.lblAbrir.config(bg=self.color_base, fg=self.color_fuente)
            self.lblEscribir.config(bg=self.color_base, fg=self.color_fuente)
            self.lblLeer.config(bg=self.color_base, fg=self.color_fuente)
            self.lblAmpl.config(bg=self.color_base, fg=self.color_fuente)
            self.lblAten.config(bg=self.color_base, fg=self.color_fuente)
            self.lblConv.config(bg=self.color_base, fg=self.color_fuente)
            self.lblDesp.config(bg=self.color_base, fg=self.color_fuente)
            self.lblDiez.config(bg=self.color_base, fg=self.color_fuente)
            self.lblInter.config(bg=self.color_base, fg=self.color_fuente)
            self.lblReflejo.config(bg=self.color_base, fg=self.color_fuente)
            self.lblResta.config(bg=self.color_base, fg=self.color_fuente)
            self.lblSuma.config(bg=self.color_base, fg=self.color_fuente)
            self.lblSerie1.config(bg=self.color_base, fg=self.color_fuente)
            self.lblSerie2.config(bg=self.color_base, fg=self.color_fuente)
            self.lblOrigen1.config(bg=self.color_base, fg=self.color_fuente)
            self.lblOrigen2.config(bg=self.color_base, fg=self.color_fuente)
            
            self.btnFile.config(bg=self.color_base)
            self.btnFile1.config(bg=self.color_base)
            self.btnFile2.config(bg=self.color_base)
            self.btnAmpl.config(bg=self.color_base)
            self.btnAten.config(bg=self.color_base)
            self.btnConv.config(bg=self.color_base)
            self.btnDesp.config(bg=self.color_base)
            self.btnDiez.config(bg=self.color_base)
            self.btnInter.config(bg=self.color_base)
            self.btnReflejo.config(bg=self.color_base)
            self.btnResta.config(bg=self.color_base)
            self.btnSuma.config(bg=self.color_base)
            
        else:
            self.color_base = '#24264F'
            self.color_fuente = '#FFFFFF'
            
            self.img_sol = Image.open('./img_interfaz/dom.png')
            self.img_sol = self.img_sol.resize((50,50), Image.ANTIALIAS)
            self.img_sol = ImageTk.PhotoImage(self.img_sol)
            self.btnSol = Button(self.frame1, image=self.img_sol, text='Abrir', bg=self.color_base, command=self.color)
            self.btnSol.place(x=755,y=55)
            
            self.frame1.config(bg=self.color_base)
            self.frame2.config(bg=self.color_base)
            self.frame3.config(bg=self.color_base)
            
            self.lblTitulo.config(bg=self.color_base, fg=self.color_fuente)
            self.lblOperaciones.config(bg=self.color_base, fg=self.color_fuente)
            self.lblAbrir.config(bg=self.color_base, fg=self.color_fuente)
            self.lblEscribir.config(bg=self.color_base, fg=self.color_fuente)
            self.lblLeer.config(bg=self.color_base, fg=self.color_fuente)
            self.lblAmpl.config(bg=self.color_base, fg=self.color_fuente)
            self.lblAten.config(bg=self.color_base, fg=self.color_fuente)
            self.lblConv.config(bg=self.color_base, fg=self.color_fuente)
            self.lblDesp.config(bg=self.color_base, fg=self.color_fuente)
            self.lblDiez.config(bg=self.color_base, fg=self.color_fuente)
            self.lblInter.config(bg=self.color_base, fg=self.color_fuente)
            self.lblReflejo.config(bg=self.color_base, fg=self.color_fuente)
            self.lblResta.config(bg=self.color_base, fg=self.color_fuente)
            self.lblSuma.config(bg=self.color_base, fg=self.color_fuente)
            self.lblSerie1.config(bg=self.color_base, fg=self.color_fuente)
            self.lblSerie2.config(bg=self.color_base, fg=self.color_fuente)
            self.lblOrigen1.config(bg=self.color_base, fg=self.color_fuente)
            self.lblOrigen2.config(bg=self.color_base, fg=self.color_fuente)
            
            self.btnFile.config(bg=self.color_base)
            self.btnFile1.config(bg=self.color_base)
            self.btnFile2.config(bg=self.color_base)
            self.btnAmpl.config(bg=self.color_base)
            self.btnAten.config(bg=self.color_base)
            self.btnConv.config(bg=self.color_base)
            self.btnDesp.config(bg=self.color_base)
            self.btnDiez.config(bg=self.color_base)
            self.btnInter.config(bg=self.color_base)
            self.btnReflejo.config(bg=self.color_base)
            self.btnResta.config(bg=self.color_base)
            self.btnSuma.config(bg=self.color_base)
    
    def reproducirAudio(self):
        chunk = 1024
        audio = wave.open(self.ruta_archivo, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format = p.get_format_from_width(audio.getsampwidth()),
                        channels = audio.getnchannels(),
                        rate = audio.getframerate(),
                        output = True)
        datos = audio.readframes(chunk)
        while datos:
            stream.write(datos)
            datos = audio.readframes(chunk)
    
    def abrirArchivo(self):
        reproduccion = threading.Thread(target=self.reproducirAudio)
        self.ruta_archivo = tkinter.filedialog.askopenfilename()
        print('Ruta del archivo ', self.ruta_archivo)
        samplerate, data = wavfile.read(self.ruta_archivo)
        print(data)
        print(samplerate)
        reproduccion.start()
        self.updtGrafica(data)
            
    def __init__(self):
        self.color_base = '#24264F'
        self.color_fuente = '#FFFFFF'
        self.root = Tk()
        self.root.iconbitmap('./img_interfaz/señales.ico')
        self.root.title('Practica 2 - Teoría de Comunicaciones y Señales')
        self.root.geometry('900x600')
        self.root.config()
        
        ###################### PRIMER FRAME ######################
        self.frame1 = Frame(bd=10, width='900', height='150', bg=self.color_base)
        self.frame1.pack(side='top')
        self.lblTitulo = Label(self.frame1, text='Operaciones Básicas', font=('Open Sans', 20), fg=self.color_fuente, bg=self.color_base)
        self.lblTitulo.place(x=330, y=0)
        
        self.img_file = Image.open('./file_n_folder/png/007-folder-8.png')
        self.img_file = self.img_file.resize((50,50), Image.ANTIALIAS)
        self.img_file = ImageTk.PhotoImage(self.img_file)
        self.btnFile = Button(self.frame1, image=self.img_file, text='Abrir', bg=self.color_base, command=self.abrirArchivo)
        self.btnFile.place(x=55,y=55)
        self.lblAbrir = Label(self.frame1, text='Abrir archivo', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblAbrir.place(x=40,y=115)
        
        # self.img_file1 = Image.open('./file_n_folder/png/010-add-file.png')
        # self.img_file1 = self.img_file1.resize((50,50), Image.ANTIALIAS)
        # self.img_file1 = ImageTk.PhotoImage(self.img_file1)
        # self.btnFile1 = Button(self.frame1, image=self.img_file1, text='Abrir', bg=self.color_base)
        # self.btnFile1.place(x=155,y=55)
        # self.lblEscribir = Label(self.frame1, text='Escribir señal', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        # self.lblEscribir.place(x=140,y=115)
        
        # self.img_file2 = Image.open('./file_n_folder/png/010-add-file.png')
        # self.img_file2 = self.img_file2.resize((50,50), Image.ANTIALIAS)
        # self.img_file2 = ImageTk.PhotoImage(self.img_file2)
        # self.btnFile2 = Button(self.frame1, image=self.img_file2, text='Abrir', bg=self.color_base)
        # self.btnFile2.place(x=255,y=55)
        # self.lblLeer = Label(self.frame1, text='Leer señal escrita', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        # self.lblLeer.place(x=240,y=115)
        
        self.lblSerie1 = Label(self.frame1, text='Serie 1', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblSerie1.place(x=200,y=45)
        self.serie1 = Entry(self.frame1, width = 30)
        self.serie1.place(x=200,y=65)
        
        self.lblSerie2 = Label(self.frame1, text='Serie 2', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblSerie2.place(x=500,y=45)
        self.serie2 = Entry(self.frame1, width = 30)
        self.serie2.place(x=500,y=65)
        
        self.lblOrigen1 = Label(self.frame1, text='Origen 1', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblOrigen1.place(x=200,y=85)
        self.origen1 = Entry(self.frame1, width = 10)
        self.origen1.place(x=200,y=105)
        
        self.lblOrigen2 = Label(self.frame1, text='Origen 2', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblOrigen2.place(x=500,y=85)
        self.origen2 = Entry(self.frame1, width = 10)
        self.origen2.place(x=500,y=105)
        
        self.img_sol = Image.open('./img_interfaz/dom.png')
        self.img_sol = self.img_sol.resize((50,50), Image.ANTIALIAS)
        self.img_sol = ImageTk.PhotoImage(self.img_sol)
        self.btnSol = Button(self.frame1, image=self.img_sol, text='Abrir', bg=self.color_base, command=self.color)
        self.btnSol.place(x=755,y=55)
        
        ###################### SEGUNDO FRAME ######################
        self.frame2 = Frame(bd=10, width='300', height='450', bg=self.color_base)
        self.frame2.pack(side='left')
        self.lblOperaciones = Label(self.frame2, text='Seleccinar Operación', font=('Open Sans', 12), fg=self.color_fuente, bg=self.color_base)
        self.lblOperaciones.place(x=80,y=20)
        
        self.img = Image.open('./math/png/020-plus.png')
        self.img = self.img.resize((50,50), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.btnSuma = Button(self.frame2, image=self.img, text='suma', bg=self.color_base)
        self.btnSuma.place(x=10,y=60)
        self.lblSuma = Label(self.frame2, text='Suma', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblSuma.place(x=17,y=118)
        
        self.img1 = Image.open('./math/png/015-minus.png')
        self.img1 = self.img1.resize((50,50), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.btnResta = Button(self.frame2, image=self.img1, text='resta', bg=self.color_base)
        self.btnResta.place(x=110,y=60)
        self.lblResta = Label(self.frame2, text='Resta', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblResta.place(x=118,y=118)
        
        self.img2 = Image.open('./math/png/017-multiply.png')
        self.img2 = self.img2.resize((50,50), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(self.img2)
        self.btnAmpl = Button(self.frame2, image=self.img2, text='amplificacion', bg=self.color_base, command = lambda: self.Amplifica(self.serie1.get(), int(self.serie2.get())))
        self.btnAmpl.place(x=210,y=60)
        self.lblAmpl = Label(self.frame2, text='Amplificación', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblAmpl.place(x=195,y=118)
        
        self.img3 = Image.open('./math/png/007-divided.png')
        self.img3 = self.img3.resize((50,50), Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(self.img3)
        self.btnAten = Button(self.frame2, image=self.img3, text='atenuacion', bg=self.color_base, command = lambda: self.Atenua(self.serie1.get(), int(self.serie2.get())))
        self.btnAten.place(x=10,y=160)
        self.lblAten = Label(self.frame2, text='Atenuación', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblAten.place(x=0,y=218)
        
        self.img4 = Image.open('./math_2/png/048-hyperbole.png')
        self.img4 = self.img4.resize((50,50), Image.ANTIALIAS)
        self.img4 = ImageTk.PhotoImage(self.img4)
        self.btnReflejo = Button(self.frame2, image=self.img4, text='reflejo', bg=self.color_base, command = lambda: self.reflexion(self.serie1.get()))
        self.btnReflejo.place(x=110,y=160)
        self.lblReflejo = Label(self.frame2, text='Reflejo', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblReflejo.place(x=115,y=218)
        
        self.img5 = Image.open('./math_2/png/013-line segment.png')
        self.img5 = self.img5.resize((50,50), Image.ANTIALIAS)
        self.img5 = ImageTk.PhotoImage(self.img5)
        self.btnDesp = Button(self.frame2, image=self.img5, text='desplazamiento', bg=self.color_base, command = lambda: self.Desplazamiento(self.serie1.get(), int(self.serie2.get())))
        self.btnDesp.place(x=210,y=160)
        self.lblDesp = Label(self.frame2, text='Desplazamiento', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblDesp.place(x=190,y=218)
        
        self.img6 = Image.open('./math_2/png/050-graphic.png')
        self.img6 = self.img6.resize((50,50), Image.ANTIALIAS)
        self.img6 = ImageTk.PhotoImage(self.img6)
        self.btnDiez = Button(self.frame2, image=self.img6, text='diezmacion', bg=self.color_base, command = lambda: self.Diezmacion(self.serie1.get(), int(self.serie2.get())))
        self.btnDiez.place(x=10,y=260)
        self.lblDiez = Label(self.frame2, text='Diezmación', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblDiez.place(x=0,y=318)
        
        self.img7 = Image.open('./math_2/png/049-graphic.png')
        self.img7 = self.img7.resize((50,50), Image.ANTIALIAS)
        self.img7 = ImageTk.PhotoImage(self.img7)
        self.btnInter = Button(self.frame2, image=self.img7, text='interpolacion', bg=self.color_base, command = lambda: self.Interpolacion(self.serie1.get(), int(self.origen1.get()), self.serie2.get()))
        self.btnInter.place(x=110,y=260)
        self.lblInter = Label(self.frame2, text='Interpolación', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblInter.place(x=95,y=318)
        
        self.img8 = Image.open('./math_2/png/002-cosine.png')
        self.img8 = self.img8.resize((50,50), Image.ANTIALIAS)
        self.img8 = ImageTk.PhotoImage(self.img8)
        self.btnConv = Button(self.frame2, image=self.img8, text='convolucion', bg=self.color_base, command = lambda: self.convolucion(self.serie1.get(), self.serie2.get()))
        self.btnConv.place(x=210,y=260)
        self.lblConv = Label(self.frame2, text='Convolución', font=('Open Sans', 10), fg=self.color_fuente, bg=self.color_base)
        self.lblConv.place(x=196,y=318)
        
        ###################### TERCER FRAME ######################
        self.frame3 = Frame(bd=10, width='600', height='450', bg=self.color_base)
        self.frame3.pack(side='right')
        self.grafico = plt.Figure(figsize=(6,6), dpi=100)
        self.graf = self.grafico.add_subplot(111)
        self.canvas_grafica = FigureCanvasTkAgg(self.grafico, self.frame3)
        
        self.root.resizable(0,0)
        self.root.mainloop()

gui = GUI()