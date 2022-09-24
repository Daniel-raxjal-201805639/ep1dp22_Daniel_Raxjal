import tkinter

def promedio():
    suma=int(valor1.get())+int(valor2.get())+int(valor3.get())+int(valor4.get())+int(valor5.get())
    promedio=suma/5

    lbl_resultado["text"] = promedio

def mayor():
    num1 = int(valor1.get())
    num2 = int(valor2.get())
    num3 = int(valor3.get())
    num4 = int(valor4.get())
    num5 = int(valor5.get())

    if (num1!=num2) and (num1!=num3) and (num1!=num4) and (num1!=num5) and (num2!=num3) and (num2!=num4) and (num2!=num5) and (num3!=num4) and (num3!=num5) and (num4!=num5) :
        if (num1>num2) and (num1>num3) and (num1>num4) and (num1>num5):
            lbl_resultado["text"]="El ",num1," es mayor"
        else:
                if(num2>num1) and (num2>num3) and (num2>num4) and (num2>num5):
                     lbl_resultado["text"]="El ",num2," es mayor"
                else:
                    if(num3>num1) and (num3>num2) and (num3>num4) and (num3>num5):
                        lbl_resultado["text"]="El ",num3," es mayor"
                    else:
                        if(num4>num1) and (num4>num2) and (num4>num3) and (num4>num5):
                             lbl_resultado["text"]="El ",num4," es mayor"
                        else:
                            if(num5>num1) and (num5>num2) and (num5>num3) and (num5>num4):
                                lbl_resultado["text"]="El ",num5," es mayor"
    else:       

         lbl_resultado["text"]="Valide que los valores sean distintos"

def sumayor():
    num1 = int(valor1.get())
    num2 = int(valor2.get())
    num3 = int(valor3.get())
    num4 = int(valor4.get())
    num5 = int(valor5.get())

    suma = num1+num2+num3+num4+num5
    multiplicacion = num1*num5

    if suma==multiplicacion:
        lbl_resultado["text"]="La suma ",suma," y la ",multiplicacion," multiplicacín del valor 1 y valor 5 es igual "
    else:
            if suma>multiplicacion:
                lbl_resultado["text"]="La suma ",suma," es mayor que la ",multiplicacion," multiplicacín del valor 1 y valor 5"
            else:
                if suma<multiplicacion:
                    lbl_resultado["text"]="La suma ",suma," es menor que la ",multiplicacion," multiplicacín del valor 1 y valor 5"



ventana=tkinter.Tk()
ventana.title("Actividad No.1")
ventana.geometry("650x470")
ventana.config(bg="slate blue")

tipo1=("Arial", 24)
tipo2=("Arial", 12)

titulo=tkinter.Label(ventana, text="Actividad No.1", bg="royal blue", fg="white", font=tipo1)
titulo.grid(row=0, column=0, padx=200, pady=15,columnspan=2, sticky=(tkinter.W,tkinter.E))

lbl_valor1=tkinter.Label(ventana, text="Ingrese un valor:", bg="royal blue", fg="white", font=tipo2)
lbl_valor1.grid(row=1, column=0, padx= 5, pady=3, sticky=(tkinter.W, tkinter.E))

valor1=tkinter.Entry(ventana)
valor1.grid(row=1, column=1, padx=5, pady=3)

lbl_valor2=tkinter.Label(ventana, text="Ingrese un valor:", bg="royal blue", fg="white", font=tipo2)
lbl_valor2.grid(row=2, column=0, padx= 5, pady=3, sticky=(tkinter.W, tkinter.E))

valor2=tkinter.Entry(ventana)
valor2.grid(row=2, column=1, padx=5, pady=3)

lbl_valor3=tkinter.Label(ventana, text="Ingrese un valor:", bg="royal blue", fg="white", font=tipo2)
lbl_valor3.grid(row=3, column=0, padx= 5, pady=3, sticky=(tkinter.W, tkinter.E))

valor3=tkinter.Entry(ventana)
valor3.grid(row=3, column=1, padx=5, pady=3)

lbl_valor4=tkinter.Label(ventana, text="Ingrese un valor:", bg="royal blue", fg="white", font=tipo2)
lbl_valor4.grid(row=4, column=0, padx= 5, pady=3, sticky=(tkinter.W, tkinter.E))

valor4=tkinter.Entry(ventana)
valor4.grid(row=4, column=1, padx=5, pady=3)

lbl_valor5=tkinter.Label(ventana, text="Ingrese un valor:", bg="royal blue", fg="white", font=tipo2)
lbl_valor5.grid(row=5, column=0, padx= 5, pady=3, sticky=(tkinter.W, tkinter.E))

valor5=tkinter.Entry(ventana)
valor5.grid(row=5, column=1, padx=5, pady=3)

btn_promedio=tkinter.Button(ventana, text="Calcular el promedio", font=tipo2, bg="royal blue", fg="white", command=promedio)
btn_promedio.grid(row=6, column=0, sticky=(tkinter.W, tkinter.E), padx= 50, pady=3)

btn_mayor=tkinter.Button(ventana, text="Calcular el mayor", font=tipo2, bg="royal blue", fg="white", command=mayor)
btn_mayor.grid(row=7, column=0, sticky=(tkinter.W, tkinter.E), padx= 50, pady=3)

btn_calcular=tkinter.Button(ventana, text="Calcular el mayor, menor , igual", font=tipo2, bg="royal blue", fg="white", command=sumayor)
btn_calcular.grid(row=8, column=0, sticky=(tkinter.W, tkinter.E), padx= 50, pady=3)

lbl_resultado=tkinter.Label(ventana, text="Resultado", font=tipo2)
lbl_resultado.grid(row=9, column=0, columnspan=2, pady=5, padx=5)

ventana.mainloop()