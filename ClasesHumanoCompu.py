import mysql.connector as mysql

class database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "modularteam"
        self.correo = ""
        self.contraseña = ""
        self.nombre = ""
        self.id = ""
    
    def open(self):
        self.conn = mysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.conn.cursor()
    
    def close(self):
        self.conn.close()
    
    def validar_login(self, correo, contraseña):
        self.open()
        usuario = []
        self.sql = "SELECT * FROM usuarios WHERE correo=%s AND contraseña=%s"
        self.data = (correo, contraseña)
        self.cursor.execute(self.sql, self.data)
        self.result = self.cursor.fetchall()
        for x in self.result:
            usuario.append(x)
        self.conn.commit()
        self.close()
        return usuario
    
    def obtener_usuario(self, correo, contraseña):
        self.open()
        usuario = []
        self.sql = "SELECT nombre, id FROM usuarios WHERE correo=%s AND contraseña=%s"
        self.data = (correo, contraseña)
        self.cursor.execute(self.sql, self.data)
        self.result = self.cursor.fetchall()
        self.conn.commit()
        self.close()
        return usuario

    def get_ids_usuarios(self):
        self.open()
        IDUsuarios = []
        self.sql = "SELECT id FROM usuarios"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        for x in self.result:
            IDUsuarios.append(int(x[0]))
        IDUsuarios.sort()
        self.conn.commit()
        self.close()
        return IDUsuarios
    
    def insertar_usuario(self, usuario):
        self.open()
        self.sql = "INSERT INTO usuarios (id, correo, contraseña, nombre, carrera, centro) VALUES (%s,%s,%s,%s,%s,%s)"
        self.data = (
            usuario.getid(),
            usuario.getcorreo(),
            usuario.getcontraseña(),
            usuario.getnombre(),
            usuario.getcarrera(),
            usuario.getcentro()
        )
        self.cursor.execute(self.sql, self.data)
        self.conn.commit()
        self.close()


class usuarios:
    def __init__(self, id, correo, contraseña, nombre, carrera="", centro=""):
        self.id = id
        self.correo = correo
        self.contraseña = contraseña
        self.nombre = nombre
        self.carrera = carrera
        self.centro = centro

    def getid(self):
        return self.id
    def getcorreo(self):
        return self.correo
    def getcontraseña(self):
        return self.contraseña
    def getnombre(self):
        return self.nombre
    def getcarrera(self):
        return self.carrera
    def getcentro(self):
        return self.centro 