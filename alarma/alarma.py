from tkinter import *
from tkinter import ttk
from datetime import datetime
import time

class Aplicacion():
    def __init__(self):
        #Aqui creamos lo que va a contener la aplicacion
        #Seteamos tamaño de la ventana y el titulo
        self.root = Tk()
        self.root.title("Alarma")
        #Creamos un marco dentro de la ventana que
        #contiene todos los elementos, hora
        self.frame = ttk.Frame(self.root)
        self.frame.pack()
        #
        self.frame_bottom = ttk.Frame(self.root)
        self.frame_bottom.pack()
        #Creamos un marco para contener la hora
        #y la etiqueta que es la que muestra la hora
        self.label = ttk.Label(self.frame, text="", font=("times", 30, "bold"))
        self.label.pack()
        #llamamos la instancia que contiene la hora actual
        self.reloj()
        
        #el spinbox es para seleccionar horas, minutos y segundos de la alarma, el format=%02.0f
        #es para mostrar dos digitos siempre, estado=readonly evita poder colocar o modificar
        #de forma distinta a las flechas subir bajar
        
        self.spinbox_hora = Spinbox(self.frame, from_=0, to=23, format="%02.0f",
                                   width=4, font=('times', 15, 'bold'), state="readonly")
        self.spinbox_hora.pack(side=LEFT)
        self.spinbox_minuto = Spinbox(self.frame, from_=0, to=59, format="%02.0f",
                                     width=4, font=('times', 15, 'bold'), state="readonly")
        self.spinbox_minuto.pack(side=LEFT)
        self.spinbox_segundo = Spinbox(self.frame, from_=0, to=59, format="%02.0f",
                                   width=4, font=('times', 15, 'bold'), state="readonly")
        self.spinbox_segundo.pack(side=LEFT)
        self.checkbox_value = BooleanVar(False)
        self.check = ttk.Checkbutton(self.frame_bottom, variable=self.checkbox_value, command=self.activar_alarma)
        self.check.pack(side=LEFT)    
        self.labelcheck = ttk.Label(self.frame_bottom, text="Activar Alarma", font=("times",10))
        self.labelcheck.pack(side=LEFT)
        self.root.mainloop()
        
    #obtener la hora actual
    def reloj(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.reloj)

    #alarma activa, despues de seleccionar checkbox cuenta cada segundo hasta que llegue a la hora 
    def activar_alarma(self):
        while self.checkbox_value.get()==True:
            time.sleep(1)
            despertador = f"{self.spinbox_hora.get()}:{self.spinbox_minuto.get()}:00"
            hora_actual = datetime.now().strftime("%H:%M:%S")
            #print(despertador, hora_actual)
            if despertador == hora_actual:
                print("Hola vietnant")
                break

        

#inicializa la aplicacion
        
def main():
    mi_app = Aplicacion()
    return 0
    
if __name__ == '__main__':
    main()
