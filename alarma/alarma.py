from tkinter import *
from tkinter import ttk
import time

class Aplicacion():
    def __init__(self):
        #Aqui creamos lo que va a contener la aplicacion
        #Seteamos tamaño de la ventana y el titulo
        self.root = Tk()
        self.root.geometry('300x300')
        self.root.title("Alarma")

        
        
        #Creamos un marco dentro de la ventana que
        #contiene todos los elementos, hora, botones
        self.frame = ttk.Frame(self.root, borderwidth=2, relief="raised",
                               padding = (10,10))
        self.frame.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        
        #Creamos un marco para contener la hora
        #y la etiqueta que es la que muestra la hora
        self.fm_hora = ttk.Frame(self.frame, borderwidth=2, padding=(10,10))
        self.fm_hora.grid(column=1, row=0, sticky="nsew")
        self.label = ttk.Label(self.fm_hora, text="", font=("times", 30, "bold"))
        self.label.pack()
        #llamamos la instancia que contiene la hora actual
        self.reloj()
        #
        
        #
        self.bt_set = ttk.Button(self.frame, text="Set Alarma", command=self.set_alarma)
        self.bt_set.grid(column=1, row=6, padx=10, sticky="s")
        self.bt_out = ttk.Button(self.frame, text="Salir", command=self.root.destroy)
        self.bt_out.grid(column=1, row=8, pady=10, sticky="s")
        #
        self.separador = ttk.Separator(self.frame, orient=HORIZONTAL)
        
        self.separador.grid(column=0, row=7, pady=10, columnspan=6, sticky="nsew")
        
        #
        self.root.mainloop()

    def reloj(self):
        now = time.strftime("%H:%M:%S %p")
        self.label.configure(text=now)
        self.root.after(1000, self.reloj)

    def set_alarma(self):
        self.ventana = Toplevel(self.root)
        self.ventana.geometry("200x100")
        self.ventana.title("Set Alarma")
        self.fm_set_alarma = ttk.Frame(self.ventana, borderwidth=2, padding=(10,10))
        self.fm_set_alarma.grid(column=1, row=0, sticky="nsew")
        
        self.spinbox_hora = Spinbox(self.fm_set_alarma, from_=1, to=12, format="%02.0f",
                                   width=4, font=('times', 20, 'bold'), state="readonly")
        self.spinbox_hora.grid(column=1, row=2, padx=10, sticky="w")
        self.spinbox_minuto = Spinbox(self.fm_set_alarma, from_=0, to=59, format="%02.0f",
                                     width=4,font=('times', 20, 'bold'), state="readonly")
        self.spinbox_minuto.grid(column=2, row=2, padx=10, sticky="e")
        self.bt_alarma = ttk.Button(self.fm_set_alarma, text= "Set")
        self.bt_alarma.grid(column=1, row=6, padx=10, pady=10, sticky="s")
        self.bt_cancelar = ttk.Button(self.fm_set_alarma, text="Cancelar",
                                     command=self.ventana.destroy)
        self.bt_cancelar.grid(column=2, row=6, padx=10, pady=10, sticky="s")

    
def main():
    mi_app = Aplicacion()
    return 0
    
if __name__ == '__main__':
    main()
