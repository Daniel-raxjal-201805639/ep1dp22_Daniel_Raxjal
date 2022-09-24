from cProfile import label
import tkinter
from tkinter import CENTER, END, ttk
from Mixtos import Mixtos


ventana = tkinter.Tk()
ventana.title("Parcial No.1")
ventana.geometry("700x550")
ventana.configure(bg="deep sky blue")

tabla = ttk.Treeview(ventana, columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"))

listaMixto = []

def aguardarDatos():
    mixto = Mixtos()

    mixto.codigo = int(txt_codigo.get())
    mixto.nombre = txt_nombre.get()
    mixto.direccion = txt_direccion.get()
    mixto.telefono = txt_telefono.get()
    mixto.director = txt_director.get()
    mixto.url = txt_url.get()
    mixto.fecha_creacion = txt_fecha.get()
    mixto.tipo = txt_tipo.get()
    mixto.descripcion = txt_descripcion.get()
    mixto.cantidad_hombres = txt_hombres.get()
    mixto.cantidad_mujeres = txt_mujeres.get()
   
    listaMixto.append(mixto)
    generarTabla()
    limpiarCajasTexto()

'''_______________________________
def verDatos():
    estudiantes.verDatosMixtos()
_______________________________'''

def generarTabla():

    for fila in tabla.get_children():
        tabla.delete(fila)

    tabla.column("#0", width=59)
    tabla.column("col1", width=59)
    tabla.column("col2", width=59)
    tabla.column("col3", width=59)
    tabla.column("col4", width=59)
    tabla.column("col5", width=59)
    tabla.column("col6", width=59)
    tabla.column("col7", width=59)
    tabla.column("col8", width=59)
    tabla.column("col9", width=59)
    tabla.column("col10", width=59)

    tabla.heading("#0", text="Codigo", anchor=CENTER)
    tabla.heading("col1", text="Nombre", anchor=CENTER)
    tabla.heading("col2", text="Direccion", anchor=CENTER)
    tabla.heading("col3", text="Teléfono", anchor=CENTER)
    tabla.heading("col4", text="Director", anchor=CENTER)
    tabla.heading("col5", text="URL", anchor=CENTER)
    tabla.heading("col6", text="Fecha creacion", anchor=CENTER)
    tabla.heading("col7", text="Tipo", anchor=CENTER)
    tabla.heading("col8", text="Descripcion", anchor=CENTER)
    tabla.heading("col9", text="Cantidad hombres", anchor=CENTER)
    tabla.heading("col10", text="Cantidad mujeres", anchor=CENTER)

    for registro in listaMixto:
        tabla.insert("", END, values=(registro.codigo,registro.nombre,registro.direccion,registro.telefono,registro.director,registro.url,registro.fecha_creacion,registro.tipo,registro.descripcion,registro.cantidad_hombres,registro.cantidad_mujeres))

    tabla.place(x=10,y=300)

def limpiarCajasTexto():
    
    txt_codigo.delete(0,"end")
    txt_nombre.delete(0,"end")
    txt_direccion.delete(0,"end")
    txt_telefono.delete(0,"end")
    txt_director.delete(0,"end")
    txt_url.delete(0,"end")
    txt_fecha.delete(0,"end")
    txt_tipo.delete(0,"end")
    txt_descripcion.delete(0,"end")
    txt_hombres.delete(0,"end")
    txt_mujeres.delete(0,"end")

    txt_codigo.focus_set()


tipo1=("Arial", 12)
tipo2=("Arial", 24)
color1="white"
color2="sky blue"

lbl_titulo=tkinter.Label(ventana, text="Centros Educativo", bg=color2, fg=color1, font=tipo2)
    

lbl_codigo=tkinter.Label(ventana,text="Código", bg=color2, fg=color1, font=tipo1)
txt_codigo=tkinter.Entry(ventana)

lbl_nombre=tkinter.Label(ventana,text="Nombre", bg=color2, fg=color1, font=tipo1)
txt_nombre=tkinter.Entry(ventana)

lbl_direccion=tkinter.Label(ventana,text="Dirección", bg=color2, fg=color1, font=tipo1)
txt_direccion=tkinter.Entry(ventana)

lbl_telefono=tkinter.Label(ventana,text="Teléfono", bg=color2, fg=color1, font=tipo1)
txt_telefono=tkinter.Entry(ventana)

lbl_director=tkinter.Label(ventana,text="Director", bg=color2, fg=color1, font=tipo1)
txt_director=tkinter.Entry(ventana)

lbl_url=tkinter.Label(ventana,text="URL", bg=color2, fg=color1, font=tipo1)
txt_url=tkinter.Entry(ventana)

lbl_fecha=tkinter.Label(ventana,text="Fecha creación", bg=color2, fg=color1, font=tipo1)
txt_fecha=tkinter.Entry(ventana)

lbl_tipo=tkinter.Label(ventana,text="Tipo", bg=color2, fg=color1, font=tipo1)
txt_tipo=tkinter.Entry(ventana)

lbl_descripcion=tkinter.Label(ventana,text="Descripcion", bg=color2, fg=color1, font=tipo1)
txt_descripcion=tkinter.Entry(ventana)

lbl_hombres=tkinter.Label(ventana,text="Cantidad de hombres", bg=color2, fg=color1, font=tipo1)
txt_hombres=tkinter.Entry(ventana)

lbl_mujeres=tkinter.Label(ventana,text="Cantidad de mujeres", bg=color2, fg=color1, font=tipo1)
txt_mujeres=tkinter.Entry(ventana)

btn_guardar=tkinter.Button(ventana, text="Aguardar Datos",  font= tipo1, command=aguardarDatos)

lbl_titulo.place(x=230, y=10)
lbl_codigo.place(x=10, y=70)
txt_codigo.place(x=145,y=70)

lbl_nombre.place(x=345, y=70)
txt_nombre.place(x=490, y=70)

lbl_direccion.place(x=10, y=100)
txt_direccion.place(x=145, y=100)

lbl_telefono.place(x=345, y=100)
txt_telefono.place(x=490,y=100)

lbl_director.place(x=10, y= 130)
txt_director.place(x=145, y=130)

lbl_url.place(x=345, y=130)
txt_url.place(x=490, y=130)

lbl_fecha.place(x=10, y=160)
txt_fecha.place(x=145, y=160)

lbl_tipo.place(x=345, y=160)
txt_tipo.place(x=490, y=160)

lbl_descripcion.place(x=10, y=190)
txt_descripcion.place(x=145, y=190)

lbl_hombres.place(x=345, y=190)
txt_hombres.place(x=505, y=190)

lbl_mujeres.place(x=10, y=220)
txt_mujeres.place(x=160, y=220)


btn_guardar.place(x=10, y=270)

ventana.mainloop()