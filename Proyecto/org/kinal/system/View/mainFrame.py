import tkinter as tk
import sys
sys.path.append("C:\\Users\\Javier\\OneDrive - Fundación Kinal -Alumnos-\\Desktop\\Proyecto")
from org.kinal.system.Controller import convertidor

def on_enter_menu(event):
    menubar.config(relief=tk.SUNKEN)

def on_leave_menu(event):
    menubar.config(relief=tk.RAISED)

window = tk.Tk()
window.title("Convertidor de Sentencias")
window.geometry("750x500+300+100")
window.resizable(False,False)
window.config(background="gray")

font_path = "assets/Fonts/Poppins/Poppins-Regular.ttf"
window.tk.call('font', 'create', 'Poppins', '-family', 'Poppins', '-size', 12)

tittle1 = tk.Label(
    window, 
    font=("Poppins", 13), 
    text="Ingresa Texto a Convertir", 
    width=20, 
    height=2, 
    fg="black",
    background="gray"
    )
tittle1.place(x=100, y=25)

entrada1 = tk.Text(window, font=("Poppins", 11))
entrada1.place(x=25, y=75, height=275, anchor="nw", width=330)
entrada1.config(borderwidth=5)

tittle2 = tk.Label(
    window, 
    font=("Poppins", 13), 
    text="Pre-Visualización SQL", 
    width=20, 
    height=2, 
    fg="black",
    background="gray"
    )
tittle2.place(x=450, y=25)

entrada2 = tk.Text(
    window, 
    font=("Poppins", 11)
    )
entrada2.place(
    x=390,
    y=75,
    height=275,
    anchor="nw",
    width=330
    )
entrada2.config(borderwidth=5)

separator = tk.Frame(window, width=5, height=275, background="lightblue")
separator.place(x=370, y=75, anchor="nw")

buttonConvert = tk.Button(window, text="Convertir", height=3, width=15, command=convertidor.convertir_entry_to_db)
buttonConvert.place(x=320, y=390)

menubar = tk.Menu(window)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Abrir", command=convertidor.abrir)
file_menu.add_command(label="Guardar", command=convertidor.guardar)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=convertidor.salir)

menubar.add_cascade(label="Archivo", menu=file_menu)

window.config(menu=menubar)

for item in menubar.winfo_children():
    item.bind("<Enter>", on_enter_menu)
    item.bind("<Leave>", on_leave_menu)

window.mainloop()
