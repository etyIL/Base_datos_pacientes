# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:37:13 2023

@author: Estefania
"""

import pandas as pd
import openpyxl
from tkinter import *
from tkinter import messagebox
import os
import os.path as path
import time
import pathlib
from PIL import Image


os.chdir('.')

""" ventana principal """
ventana1 = Tk()
ventana1.config(bg= 'lightblue')
ventana1.geometry('500x100')
ventana1.resizable(1,1)
ventana1.title('Bienvenido a la base de datos de tus pacientes!')
paciente= Label(ventana1, text= 'Ingrese el apellido del paciente', width=30, bg= 'lightblue')
paciente.pack()


# define variables globales porque se usan en varias funciones """
global ingresa_paciente
ingresa_paciente = Entry(ventana1, width=20, font= ('Calibri',11))
ingresa_paciente.pack()

def guardar_datos():
    
    """ guarda los datos en un excel (a modo de base de datos) 
    en caso de que el paciente no exista """
    
    global fecha1,nombre1,apellido1,edad1,dni1,dirección1,telefono1,consulta1,tratamiento1,pago1,debe1,odontograma,obra_social1

    fecha1= ingresa_fecha.get()
    nombre1= ingresa_nombre.get() 
    apellido1= ingresa_apellido.get() 
    edad1= ingresa_edad.get()
    dni1= ingresa_dni.get() 
    dirección1= ingresa_dirección.get() 
    telefono1= ingresa_telefono.get()
    consulta1= ingresa_motivo_consulta.get(1.0,END)
    tratamiento1= ingresa_tratamiento_continuar.get(1.0,END)
    pago1= ingresa_pago_efectuado.get()
    debe1= ingresa_debe.get()
    obra_social1= ingresa_obra_social.get()
   
    datos= { 'Fecha':fecha1,'Nombres':nombre1, 'Apellidos':apellido1, 'Edad':edad1, 'DNI':dni1, 'Dirección':dirección1, 'Teléfono':telefono1, 'Motivo consulta':consulta1, 'Tratamiento a continuar':tratamiento1, 'Pago efectuado':pago1, 'Debe':debe1, 'Obra Social':obra_social1} 
    nom_excel= (str(apellido1) + '.xlsx') 

    df= pd.DataFrame.from_dict(datos,orient='index')#columns= ['Fecha', 'Nombres', 'Apellidos', 'Edad', 'DNI', 'Dirección', 'Teléfono', 'Motivo consulta', 'Tratamiento a continuar', 'Pago efectuado', 'Debe'], orient='index') 
    df= df.transpose()
    
    df.to_excel(nom_excel, index= False, engine= 'openpyxl')

    nom_archivo= StringVar(frame2)
    nom_archivo.set(apellido1)
    
    # se borra el fomrulario una vez presionado 'Guardar'
    
    archivo = Label(frame2, text= 'Nombre Archivo', width= 20, bg= 'lightblue').grid(column= 0, row= 0,  pady=10, padx= 10)
    archivo_n = Entry(frame2, width=20, textvariable=nom_archivo, font = ('Calibri',11), highlightbackground = "lightblue", highlightthickness=4)
    archivo_n.grid(column=0, row=1, pady=10, padx= 10)
    ingresa_fecha.delete(0,END)
    ingresa_nombre.delete(0,END)
    ingresa_apellido.delete(0,END)
    ingresa_edad.delete(0,END)
    ingresa_dni.delete(0,END)
    ingresa_dirección.delete(0,END)
    ingresa_telefono.delete(0,END)
    ingresa_motivo_consulta.delete(1.0,END)
    ingresa_tratamiento_continuar.delete(1.0,END)
    ingresa_pago_efectuado.delete(0,END)
    ingresa_debe.delete(0,END) 
    ingresa_obra_social.delete(0,END)
    
    
    
    def abrir_odonto():
        
        """ busca la imagen del odontograma en el directorio y la abre.
        Si no encuentra el archivo tira un error """
        
        directorio = pathlib.Path('.')
        imagen = 'odontograma.JPG'
        for archivo in directorio.iterdir():
            if path.exists(imagen):
        
               odontograma= Image.open(imagen)
               odonto_paciente= odontograma.save('odontograma_' + str(apellido1) + '.JPG')
               os.startfile('odontograma_' + str(apellido1) + '.JPG') 
               
            else: 
                messagebox.showerror(message= 'No existe. Agregue el archivo en el directorio', title= 'Error')
                break
            
    mensaje= Tk()
    mensaje.config(bg= 'lightblue')
    mensaje.geometry('500x100')
    mensaje.resizable(1,1)
    mensaje.title('Resultado')
    texto = Label(mensaje, text= '¡Listo!¿Desea abrir y guardar el odontograma?', bg= 'lightblue')
    texto.pack()
    
    def destruir():
        mensaje.destroy()
    def cerrar_mensaje():
        mensaje.destroy()
        
    boton_si= Button(mensaje, text= 'Sí', command= abrir_odonto)
    boton_si.pack()
    boton_no= Button(mensaje, text= 'No', command= destruir)
    boton_no.pack()
    boton_cerrar_mensaje= Button(mensaje, text= 'Cerrar', command= cerrar_mensaje)
    boton_cerrar_mensaje.pack()
    
def agregar_datos():
    
    """ se crean los frames para agregar los datos en el formulario """
            
    ventana = Tk()
    ventana.config(bg='lightblue')
    #ventana.geometry('978x450')
    ventana.resizable(1,1)
    ventana.title('Guardar datos de paciente')
    global fecha1,nombre1,apellido1,edad1,dni1,dirección1,telefono1,consulta1,tratamiento1,pago1,debe1,obra_social1
    global ingresa_fecha, ingresa_nombre, ingresa_apellido, ingresa_motivo_consulta, ingresa_tratamiento_continuar, ingresa_edad, ingresa_dni, ingresa_dirección, ingresa_telefono, ingresa_pago_efectuado, ingresa_debe, ingresa_obra_social
    global frame2
    global nombre_archivo
    
    frame1= Frame(ventana, width= 300, height= 1500, bg='lightblue')
    frame1.grid(column=0, row=0, sticky='nsew')
    
   
    frame2= Frame(ventana, width= 200, height= 1500, bg='lightblue')
    frame2.grid(column=1, row=0, sticky='nsew')
    

    fecha= Label(frame1, text= 'Fecha', width=10).grid(column=0, row=0, pady=20, padx=10)
    ingresa_fecha = Entry(frame1, width=20, font= ('Calibri',11))
    ingresa_fecha.grid(column=1, row=0)

    nombre = Label(frame1, text ='Nombre', width=10).grid(column=0, row=1, pady=20, padx= 10)
    ingresa_nombre = Entry(frame1, width=20, font= ('Calibri',11))
    ingresa_nombre.grid(column=1, row=1)

    apellido = Label(frame1, text ='Apellido', width=10).grid(column=0, row=2, pady=20, padx= 10)
    ingresa_apellido = Entry(frame1, width=20, font = ('Calibri',11))
    ingresa_apellido.grid(column=1, row=2)

    edad = Label(frame1, text ='Edad', width=10).grid(column=0, row=3, pady=20, padx= 10)
    ingresa_edad = Entry(frame1,  width=20, font = ('Calibri',11))
    ingresa_edad.grid(column=1, row=3)
    
    obra_social= Label(frame1, text= 'Obra Social', width= 20).grid(column=0, row=4, pady=20, padx=10)
    ingresa_obra_social= Entry(frame1, width=20, font= ('Calibri', 11))
    ingresa_obra_social.grid(column=1, row=4)
    
    consulta= Label(frame1, text= 'Motivo consulta', width=20).grid(column=0, row=5, pady=20, padx=10)
    ingresa_motivo_consulta= Text(frame1, width=20, height=5, font= ('Calibri', 11), wrap='word')
    ingresa_motivo_consulta.grid(column=1, row=5)
    
    dni= Label(frame1, text= 'DNI', width=10).grid(column=2, row=0, pady=20, padx= 10)
    ingresa_dni= Entry(frame1, width=20, font= ('Calibri', 11))
    ingresa_dni.grid(column=3, row=0)

    dirección = Label(frame1, text ='Dirección', width=10).grid(column=2, row=1, pady=20, padx= 10)
    ingresa_dirección = Entry(frame1,  width=20, font = ('Calibri',11))
    ingresa_dirección.grid(column=3, row=1)

    telefono = Label(frame1, text ='Telefono', width=10).grid(column=2, row=2, pady=20, padx= 10)
    ingresa_telefono = Entry(frame1, width=20, font = ('Calibri',11))
    ingresa_telefono.grid(column=3, row=2)

    pago= Label(frame1, text= 'Pago efectuado', width=20).grid(column=2, row=3, pady=20, padx=10)
    ingresa_pago_efectuado= Entry(frame1, width=20, font= ('Calibri', 11))
    ingresa_pago_efectuado.grid(column=3, row=3)

    debe= Label(frame1, text= 'Monto adeudado', width=20).grid(column=2, row=4, pady=20, padx=10)
    ingresa_debe= Entry(frame1, width=20, font= ('Calibri', 11))
    ingresa_debe.grid(column=3, row=4)
    
    tratamiento= Label(frame1, text= 'Tratamiento a continuar', width=20).grid(column=2, row=5, pady=20, padx=10)
    ingresa_tratamiento_continuar= Text(frame1, width=20, height=5, font= ('Calibri', 11), wrap='word')
    ingresa_tratamiento_continuar.grid(column=3, row=5)
    
    guardar = Button(frame2, width=20, font=('Calibri',12, 'bold'), text='Guardar', bg='pink',bd=5, command =guardar_datos)
    guardar.grid(column=0, row=2, pady=20, padx= 10)
    
    def cerrar():
       ventana.destroy()
            
    cerrar = Button(frame2, width=20, font = ('Calibri',12, 'bold'), text='Cerrar', bg='pink',bd=5, command =cerrar)
    cerrar.grid(column=0, row=3, pady=20, padx= 10)

def paciente():
    
    """ Busca la base de datos del paciente y si existe la abre junto con su odontograma.
    Si no existe, pregunta si quiere ingresarlo """
    
    directorio = pathlib.Path('.')
    paciente_ = ingresa_paciente.get() 
    paciente = str(paciente_) + '.xlsx'
    odonto= ('odontograma_' + paciente_ + '.JPG')
    
    for archivo in directorio.iterdir():
        if path.exists(paciente) and path.exists(odonto):
            ventana2= Tk()
            ventana2.config(bg= 'lightblue')
            ventana2.geometry('500x100')
            ventana2.resizable(1,1)
            ventana2.title('Resultado de la búsqueda')
            texto = Label(ventana2, text= 'Genial! Aquí está el historial de su paciente y su odontograma!', bg= 'lightblue')
            texto.pack()
            os.startfile(paciente)
            os.startfile('odontograma_' + paciente_ + '.JPG')
            def cerrar3():
                ventana2.destroy()
                
            botoncerrar = Button(ventana2, text= 'Cerrar', command= cerrar3) 
            botoncerrar.pack() 
            break
        
        elif path.exists(paciente) and not path.exists(odonto):
            ventana2= Tk()
            ventana2.config(bg= 'lightblue')
            ventana2.geometry('500x150')
            ventana2.resizable(1,1)
            ventana2.title('Resultado de la búsqueda')
            texto = Label(ventana2, text= 'Ok, aquí está el historial de su paciente pero no existe odontograma!', bg= 'lightblue')
            texto2= Label(ventana2, text= '¿Desea agregar odontograma al historial?', bg= 'lightblue')
            texto.pack()
            texto2.pack()
            
            # acá vuelvo a definir la función para crear el odontograma. 
            # Esto seguramente se podría haber evitado...
            
            def abrir_odonto():
                directorio = pathlib.Path('.')
                imagen = 'odontograma.JPG'
                for archivo in directorio.iterdir():
                    if path.exists(imagen):
                
                       odontograma= Image.open(imagen)
                       odonto_paciente= odontograma.save('odontograma_' + paciente_ + '.JPG')
                       os.startfile('odontograma_' + str(paciente_) + '.JPG') 
                       break

            def cerrar3():
                ventana2.destroy()
            
            boton_si_odonto= Button(ventana2, text= 'Sí', command= abrir_odonto)
            boton_si_odonto.pack()
            boton_no_odonto= Button(ventana2, text= 'No', command= cerrar3)
            boton_no_odonto.pack()
            botoncerrar = Button(ventana2, text= 'Cerrar', command= cerrar3) 
            botoncerrar.pack() 
            os.startfile(paciente)
            break
        
        else:
            ventana2= Tk()
            ventana2.config(bg= 'lightblue')
            ventana2.geometry('500x100')
            ventana2.resizable(1,1)
            ventana2.title('Resultado de la búsqueda')
            texto = Label(ventana2, text= 'No se encuentra el paciente en la base de datos, ¿desea agregarlo?', bg= 'lightblue')
            texto.pack()
            botonsi = Button(ventana2, text= 'Sí', command= agregar_datos)
            botonsi.pack()
            

            def cerrar2():
                ventana2.destroy()
            
            botonno = Button(ventana2, text= 'No', command= cerrar2)
            botonno.pack() 
            boton_cerrar= Button(ventana2, text='Cerrar', command= cerrar2).pack()
            break
            

def cerrar4():
    ventana1. destroy()
    
Enviar= Button(ventana1, text='Enviar', command=paciente)
Enviar.pack()
Cerrar= Button(ventana1, text= 'Cerrar', command= cerrar4)
Cerrar.pack()

ventana1.mainloop()