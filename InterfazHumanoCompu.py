import tkinter
from tkinter import *
import customtkinter as interfaz
from PIL import Image
import CTkMessagebox
from ClasesHumanoCompu import *
from CTkMenuBar import *

interfaz.set_appearance_mode("dark")
interfaz.set_default_color_theme("dark-blue")

mydb = database()
 
app = interfaz.CTk()
app.title("Modular Team")
app.geometry("1400x800")
app.resizable(0, 0)
app.configure()
var = IntVar()


def validar_entero(n):
    try:
        if n == int(n):
            return 0
    except:
        CTkMessagebox.CTkMessagebox(message="Ingresar un número entero", title="Error", icon="cancel")
        return ValueError

def forget_all_widgets(parent):
    for widget in parent.winfo_children():
        widget.place_forget()

def forget_all():
    forget_all_widgets(app)
    loginLabel.pack_forget()

def delete_all_widgets(parent):
    for widget in parent.winfo_children():
        try:
            try:
                widget.delete(0, "end")
            except:
                widget.set("")
        except:
            continue

def delete_all():
    delete_all_widgets(app)

def unlock_all_widgets(parent):

    for widget in parent.winfo_children():
        try:
            widget.configure(state="normal")
        except:
            continue

def unlock_all():
    unlock_all_widgets(app)

def lock_all_widgets(parent):
    for widget in parent.winfo_children():
        widget.configure(state="disabled")

def lock_all():
    lock_all_widgets(app)

def login():
    correo = txCorreoLogin.get()
    contraseña = txContraseñaLogin.get()
    usuarioexistente = mydb.validar_login(correo, contraseña)
    if len(usuarioexistente) == 0:
        CTkMessagebox.CTkMessagebox(message="No se encontró el usuario", title="Registrar usuario", icon="info")
        unlock_all()
        delete_all()
        txCorreoLogin.wait_variable(var)
    else:
        forget_all()
        place_menu()
        place_logo()
        mydb.contraseña = contraseña
        mydb.correo = correo
        resultado = mydb.obtener_usuario(correo, contraseña)
        mydb.nombre = resultado[0][0]
        mydb.id = resultado[0][1]

def crear_cuenta():
    place_crear()

#---------------------------------INTERFAZ LOGIN--------------------------------#

loginImagen = interfaz.CTkImage(light_image=Image.open("Login.jpg"), size=(700, 800))
loginLabel = interfaz.CTkLabel(app, text="", image=loginImagen)

logoLoginImage = interfaz.CTkImage(light_image=Image.open("LogoLogin.png"), size=(400, 400))
loginLogo = interfaz.CTkLabel(app, text="", image=logoLoginImage)

IniciarSesionButton = interfaz.CTkButton(app, text="Iniciar Sesión", font=("Yu gothic medium", 12), command=login, corner_radius=15, hover_color="#9E9786", fg_color="#615B4C")
createAccountButton = interfaz.CTkButton(app, text="Crear Cuenta", font=("Yu gothic medium", 12), corner_radius=10, command=crear_cuenta, hover_color="#9E9786", fg_color="#615B4C")

txCorreoLogin = interfaz.CTkEntry(app, width=300)
correoLoginLabel = interfaz.CTkLabel(app, text="Ingrese un correo", font=("Yu gothic medium", 20))

ContraseñaLoginLabel = interfaz.CTkLabel(app, text="Ingrese la contraseña", font=("Yu gothic medium", 20))
txContraseñaLogin = interfaz.CTkEntry(app, width=300, show="*")


def crearCuentaDB():
    correo = txCorreoLogin.get()
    contraseña = txContraseñaLogin.get()
    nombre = txNombreLogin.get()

    usuario = [correo, contraseña, nombre]

    for n in usuario:
        if n == "":
            CTkMessagebox.CTkMessagebox(message="Los campos no están completos", title="Llenar todos los campos", icon="cancel")
            unlock_all()
            delete_all()
            txNombreLogin.wait_variable(var)
        else:
            continue

    idUsuarios = mydb.get_ids_usuarios()
    ID = len(idUsuarios)+1
    for id in range(len(idUsuarios)):
        if id+1 == idUsuarios[id]:
            continue
        else:
            ID = id+1
            break
    
    usuarioNuevo = usuarios(ID, correo, contraseña, nombre)
    mydb.insertar_usuario(usuarioNuevo)
    unlock_all()
    delete_all()
    place_login()

#--------------------------------INTERFAZ CREAR CUENTA--------------------------#

LogoModularTeam = interfaz.CTkImage(light_image=Image.open("Modular Team.jpeg"), size=(597, 425))
LogoModularTeamLabel = interfaz.CTkLabel(app, text="", image=LogoModularTeam)

LabelCrearCuenta = interfaz.CTkLabel(app, text="Crear una nueva cuenta", font=("Yu gothic medium", 30))

crearCuentaImagen = interfaz.CTkImage(light_image=Image.open("Crear Cuenta.png"), size=(200, 200))
crearCuentaImagenLabel = interfaz.CTkLabel(app, text="", image=crearCuentaImagen)

nombreCompletoLabel = interfaz.CTkLabel(app, text="Ingresa tu nombre completo", font=("Yu gothic medium", 20))
txNombreLogin = interfaz.CTkEntry(app, width=300)

crearCuentaBoton = interfaz.CTkButton(app, text="Crear Cuenta", command=crearCuentaDB, font=("Yu gothic medium", 16), corner_radius=10, hover_color="#9E9786", fg_color="#615B4C")

menu = CTkMenuBar(app)

#-------------------------------------INTERFAZ PROYECTO------------------------------#



def place_menu():
    menu.add_cascade("Perfil")
    menu.add_cascade("Curriculum")
    menu.add_cascade("Mi proyecto")
    menu.add_cascade("Buscar proyectos")
    menu.add_cascade("Salir", command=app.quit)

def place_login():
    forget_all()
    loginLabel.pack(anchor=tkinter.W)
    loginLogo.place(x=850, y=10)
    IniciarSesionButton.place(x=952, y=600, anchor=tkinter.CENTER)
    createAccountButton.place(x=1148, y=600, anchor=tkinter.CENTER)
    correoLoginLabel.place(x=975, y=360)
    txCorreoLogin.place(x=900, y=400)
    ContraseñaLoginLabel.place(x=965, y=460)
    txContraseñaLogin.place(x=900, y=500)

def place_crear():
    forget_all()
    LabelCrearCuenta.place(x=500, y=20)
    crearCuentaImagenLabel.place(x=570, y=90)
    correoLoginLabel.place(x=565, y=340)
    txCorreoLogin.place(x=500, y=400)
    ContraseñaLoginLabel.place(x=555, y=460)
    txContraseñaLogin.place(x=500, y=500)
    nombreCompletoLabel.place(x=520, y=560)
    txNombreLogin.place(x=500, y=620)
    crearCuentaBoton.place(x=580, y=680)

def place_logo():
    LogoModularTeamLabel.place(x=400, y=187)

place_login()

app.mainloop()