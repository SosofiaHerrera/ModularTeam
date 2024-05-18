import tkinter
from tkinter import *
import customtkinter as interfaz
from PIL import Image
import CTkMessagebox
from ClasesHumanoCompu import *
from CTkMenuBar import *
from tkinter import Menu

interfaz.set_appearance_mode("dark")
interfaz.set_default_color_theme("dark-blue")

mydb = database()
 
app = interfaz.CTk()
app.title("Modular Team")
app.geometry("1400x750")
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
        mydb.contraseña = contraseña
        mydb.correo = correo
        resultado = mydb.obtener_usuario(correo, contraseña)
        mydb.nombre = resultado[0][0]
        mydb.id = resultado[0][1]
        
def crear_cuenta():
    place_crear()
    


#---------------------------------INTERFAZ LOGIN--------------------------------#

loginImagen = interfaz.CTkImage(light_image=Image.open("01login.png"), size=(700, 750))
loginLabel = interfaz.CTkLabel(app, text="", image=loginImagen)

logoImage = interfaz.CTkImage(light_image=Image.open("02logo.png"), size=(270, 170))
logo = interfaz.CTkLabel(app, text="", image=logoImage)

textIngreso = interfaz.CTkLabel(app, text="INGRESO", font=("Yu gothic medium", 30))

correoLoginLabel = interfaz.CTkLabel(app, text="Correo", font=("Yu gothic medium", 20))
txCorreoLogin = interfaz.CTkEntry(app, width=300)
ContraseñaLoginLabel = interfaz.CTkLabel(app, text="Contraseña", font=("Yu gothic medium", 20))
txContraseñaLogin = interfaz.CTkEntry(app, width=300, show="*")

IniciarSesionButton = interfaz.CTkButton(app, text="Iniciar Sesión", font=("Yu gothic medium", 12), command=login, corner_radius=10, hover_color="#052C3F", fg_color="#001520")
creaCuentaHv = interfaz.CTkLabel(app, text="¿Nuevo usuario? Crea una cuenta nueva", font=("Yu gothic medium", 12, "underline"), cursor="hand2")
creaCuentaHv.bind("<Button-1>", lambda e: crear_cuenta())

def crearCuentaDB():
    correo = txCorreoRegistro.get()
    contraseña = txContraseñaRegistro.get()
    nombre = txNombreLogin.get()
    carrera = txCarrera.get()
    centro = txCentro.get()

    usuario = [correo, contraseña, nombre, carrera, centro]

    for n in usuario:
        if n == "":
            CTkMessagebox.CTkMessagebox(message="Los campos no están completos", title="Llenar todos los campos", icon="cancel")
            unlock_all()
            delete_all()
            txNombreLogin.wait_variable(var)
        else:
            continue

    idUsuarios = mydb.get_ids_usuarios()
    ID = len(idUsuarios) + 1
    for id in range(len(idUsuarios)):
        if id + 1 == idUsuarios[id]:
            continue
        else:
            ID = id + 1
            break
    
    usuarioNuevo = usuarios(ID, correo, contraseña, nombre, carrera, centro)
    mydb.insertar_usuario(usuarioNuevo)
    unlock_all()
    delete_all()
    forget_all()
    place_login()
    
def actualizar_usuario():
    # Get updated user data from entry widgets
    nuevo_nombre = txNombreLogin.get()
    nuevo_correo = txCorreoRegistro.get()
    nueva_contraseña = txContraseñaRegistro.get()
    nuevo_centro = txCentro.get()
    nueva_carrera = txCarrera.get()

    # Update user data in the database
    mydb.actualizar_usuario(mydb.id, nuevo_correo, nueva_contraseña,  nuevo_nombre, nueva_carrera, nuevo_centro)

    # Show a message box indicating successful update
    CTkMessagebox.CTkMessagebox(message="Los datos del usuario han sido actualizados exitosamente", title="Actualización exitosa", icon="info")

def crearCurriculum():
    # Obtener el ID del nuevo curriculum
    idCurriculum = mydb.get_ids_curriculums()
    ID = len(idCurriculum) + 1
    idUsuarios = mydb.id
    
    descripcion = descripcionLogin.get()
    experiencia = experienciaLogin.get()
    intereses = interesesLogin.get()
    habilidades = habilidadesLogin.get()

    # Crear un nuevo usuario con los datos obtenidos
    curriculum = [ID, idUsuarios, descripcion, experiencia, intereses, habilidades]

    # Verificar si todos los campos del formulario están completos
    for n in curriculum:
        if n == "":
            CTkMessagebox.CTkMessagebox(message="Los campos no están completos", title="Llenar todos los campos", icon="cancel")
            unlock_all()
            delete_all()
            txNombreLogin.wait_variable(var)
            return  # Salir de la función si falta algún campo

    # Crear el objeto de curriculum nuevo
    curriculumNuevo = curriculum(ID, idUsuarios, descripcion, experiencia, intereses, habilidades)

    # Insertar el nuevo curriculum en la base de datos
    mydb.insertarCurriculum(curriculumNuevo)

    # Mostrar un mensaje de éxito y volver a la pantalla de inicio de sesión
    CTkMessagebox.CTkMessagebox(message="El currículum ha sido creado exitosamente", title="Creación exitosa", icon="info")
    unlock_all()
    delete_all()
    forget_all()
    perfil()

   

#--------------------------------INTERFAZ CREAR CUENTA--------------------------#
registroImagen = interfaz.CTkImage(light_image=Image.open("01login.png"), size=(700, 750))
registroLabel = interfaz.CTkLabel(app, text="", image=registroImagen)

logoRegistroImage = interfaz.CTkImage(light_image=Image.open("02logo.png"), size=(270, 170))
logoRegistro = interfaz.CTkLabel(app, text="", image=logoRegistroImage)

textoRegistro = interfaz.CTkLabel(app, text="REGISTRO", font=("Yu gothic medium", 30))

nombreCompletoLabel = interfaz.CTkLabel(app, text="Nombre", font=("Yu gothic medium", 20))
txNombreLogin = interfaz.CTkEntry(app, width=300)

carreraLabel = interfaz.CTkLabel(app, text="Carrera", font=("Yu gothic medium", 20))
centros = ["Ingenieria en Computación", "Ingenieria en Fotónica"]
txCarrera = interfaz.CTkOptionMenu(app, values=centros, width=300)


centroLabel = interfaz.CTkLabel(app, text="Centro", font=("Yu gothic medium", 20))
centros = ["CUCEI"]
txCentro = interfaz.CTkOptionMenu(app, values=centros, width=300)

correoRegistroLabel = interfaz.CTkLabel(app, text="Correo", font=("Yu gothic medium", 20))
txCorreoRegistro = interfaz.CTkEntry(app, width=300)

ContraseñaRegistroLabel = interfaz.CTkLabel(app, text="Contraseña", font=("Yu gothic medium", 20))
txContraseñaRegistro = interfaz.CTkEntry(app, width=300, show="*")

RegistroButton = interfaz.CTkButton(app, text="Crear cuenta", command=crearCuentaDB, font=("Yu gothic medium", 12), corner_radius=10, hover_color="#052C3F", fg_color="#001520")
loginHv = interfaz.CTkLabel(app, text="¿Ya tienes cuenta? Inicia sesión", font=("Yu gothic medium", 12, "underline"), cursor="hand2")
loginHv.bind("<Button-1>", lambda e: place_login())

#--------------------------------INTERFAZ PERFIL --------------------------#
textoPerfil = interfaz.CTkLabel(app, text="PERFIL", font=("Yu gothic medium", 45))
EditarButton = interfaz.CTkButton(app, text="Editar", command=actualizar_usuario, width=430, font=("Yu gothic medium", 12), corner_radius=10, hover_color="#052C3F", fg_color="#001520")
proyectoButton = interfaz.CTkButton(app, text="Proyecto", width=200, height=150, font=("Yu gothic medium", 25), corner_radius=10, hover_color="#262626", fg_color="#262626")


#--------------------------------INTERFAZ CURRICULUM --------------------------#
textoCurriculum = interfaz.CTkLabel(app, text="CURRICULUM", font=("Yu gothic medium", 30))

nombreLabel = interfaz.CTkLabel(app, text="Nombre", font=("Yu gothic medium", 20))
nombreLogin = interfaz.CTkEntry(app, width=300)
descripcionLabel = interfaz.CTkLabel(app, text="Descripción", font=("Yu gothic medium", 20))
descripcionLogin = interfaz.CTkEntry(app, width=300)
experienciaLabel = interfaz.CTkLabel(app, text="Experiencia", font=("Yu gothic medium", 20))
experienciaLogin = interfaz.CTkEntry(app, width=300)
interesesLabel = interfaz.CTkLabel(app, text="Intereses", font=("Yu gothic medium", 20))
interesesLogin = interfaz.CTkEntry(app, width=300)
habilidadesLabel = interfaz.CTkLabel(app, text="Habilidades", font=("Yu gothic medium", 20))
habilidadesLogin = interfaz.CTkEntry(app, width=300)
guardarButton = interfaz.CTkButton(app, text="Guardar", command=crearCurriculum, width=430, font=("Yu gothic medium", 12), corner_radius=10, hover_color="#052C3F", fg_color="#001520")


#--------------------------------INTERFAZ PROYECTO --------------------------#
textoProyecto = interfaz.CTkLabel(app, text="PROYECTO", font=("Yu gothic medium", 30))

#--------------------------------INTERFAZ BUSCAR PROYECTO --------------------------#
textoProyectos = interfaz.CTkLabel(app, text="BUSCAR PROYECTOS", font=("Yu gothic medium", 30))


#-------------------------------------INTERFAZ PROYECTO------------------------------#
menu = CTkMenuBar(app)
def place_menu():
    menu.add_cascade("Perfil", command=perfil)
    menu.add_cascade("Curriculum")
    menu.add_cascade("Mi proyecto")
    menu.add_cascade("Buscar proyectos", command=perfil)
    menu.add_cascade("Salir", command=app.quit)
    

def place_login():
    forget_all()
    loginLabel.pack(anchor=tkinter.W)
    logo.place(x=910, y=100)
    textIngreso.place(x=1050, y=350, anchor=tkinter.CENTER)
    correoLoginLabel.place(x=850, y=400)
    txCorreoLogin.place(x=975, y=400)
    ContraseñaLoginLabel.place(x=850, y=450)
    txContraseñaLogin.place(x=975, y=450)
    IniciarSesionButton.place(x=1050, y=550, anchor=tkinter.CENTER)
    creaCuentaHv.place(x=1050, y=580, anchor=tkinter.CENTER)
    
def place_crear():
    forget_all()
    registroLabel.pack(anchor=tkinter.W)
    logoRegistro.place(x=910, y=80)
    textoRegistro.place(x=1050, y=300, anchor=tkinter.CENTER)
    nombreCompletoLabel.place(x=850, y=350)
    txNombreLogin.place(x=975, y=350)
    correoRegistroLabel.place(x=850, y=400)
    txCorreoRegistro.place(x=975, y=400)
    ContraseñaRegistroLabel.place(x=850, y=450)
    txContraseñaRegistro.place(x=975, y=450)
    carreraLabel.place(x=850, y=500)
    txCarrera.place(x=975, y=500)
    centroLabel.place(x=850, y=550)
    txCentro.place(x=975, y=550)
    RegistroButton.place(x=1050, y=650, anchor=tkinter.CENTER)
    loginHv.place(x=1050, y=680, anchor=tkinter.CENTER)
    
def perfil():
    forget_all()
    textoPerfil.place(x=200, y=150, anchor=tkinter.CENTER)
    canvas = Canvas(app, width=900, height=2, bg="#1c1c1c", highlightthickness=0)  # Asegúrate de que el canvas tenga un fondo que coincida con la interfaz
    canvas.create_line(0, 0, 900, 0, fill="white")  # Aquí dibujamos la línea desde (0, 0) hasta (300, 0)
    canvas.place(x=150, y=250, anchor=tkinter.W)
    
    nombreCompletoLabel.place(x=130, y=250)
    txNombreLogin.place(x=250, y=250)
    correoRegistroLabel.place(x=130, y=300)
    txCorreoRegistro.place(x=250, y=300)
    ContraseñaRegistroLabel.place(x=130, y=350)
    txContraseñaRegistro.place(x=250, y=350)
    carreraLabel.place(x=130, y=400)
    txCarrera.place(x=250, y=400)
    centroLabel.place(x=130, y=450)
    txCentro.place(x=250, y=450)
    EditarButton.place(x=340, y=530, anchor=tkinter.CENTER)
    
    canvas2 = Canvas(app, width=900, height=2, bg="#1c1c1c", highlightthickness=0)  # Asegúrate de que el canvas tenga un fondo que coincida con la interfaz
    canvas2.create_line(0, 0, 900, 0, fill="white")  # Aquí dibujamos la línea desde (0, 0) hasta (300, 0)
    canvas2.place(x=150, y=750, anchor=tkinter.W)
    
    curriculumButton = interfaz.CTkButton(app, text="Curriculum", command=curriculum, width=200, height=150, font=("Yu gothic medium", 25), corner_radius=10, hover_color="#000000", fg_color="#262626")
    curriculumButton.place(x=1100, y=300, anchor=tkinter.CENTER)
    proyectoButton.place(x=1100, y=500, anchor=tkinter.CENTER)
    
def curriculum():
    forget_all()
    textoCurriculum.place(x=200, y=150, anchor=tkinter.CENTER)
    canvas = Canvas(app, width=900, height=2, bg="#1c1c1c", highlightthickness=0)  # Asegúrate de que el canvas tenga un fondo que coincida con la interfaz
    canvas.create_line(0, 0, 900, 0, fill="white")  # Aquí dibujamos la línea desde (0, 0) hasta (300, 0)
    canvas.place(x=150, y=250, anchor=tkinter.W)
    
    nombre_usuario = mydb.nombre
    nombreLabel.place(x=130, y=250)
    nombreLogin.place(x=250, y=250)
    nombreLogin.insert(tkinter.END, nombre_usuario)
    descripcionLabel.place(x=130, y=300)
    descripcionLogin.place(x=250, y=300)
    experienciaLabel.place(x=130, y=350)
    experienciaLogin.place(x=250, y=350)
    interesesLabel.place(x=130, y=400)
    interesesLogin.place(x=250, y=400)
    habilidadesLabel.place(x=130, y=450)
    habilidadesLogin.place(x=250, y=450)
    guardarButton.place(x=340, y=530, anchor=tkinter.CENTER)
    
    canvas2 = Canvas(app, width=900, height=2, bg="#1c1c1c", highlightthickness=0)  # Asegúrate de que el canvas tenga un fondo que coincida con la interfaz
    canvas2.create_line(0, 0, 900, 0, fill="white")  # Aquí dibujamos la línea desde (0, 0) hasta (300, 0)
    canvas2.place(x=150, y=750, anchor=tkinter.W)    
    
    
def proyecto():
    forget_all()
    textoProyecto.place(x=1050, y=300, anchor=tkinter.CENTER)
    
def buscarProyecto():
    forget_all()
    textoProyectos.place(x=1050, y=300, anchor=tkinter.CENTER)

place_login()
app.mainloop()