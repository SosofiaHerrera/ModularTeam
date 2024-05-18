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
        usuario = self.result  # Asignar los resultados a la lista usuario
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
    
    def actualizar_usuario(self, usuario_id, nuevo_correo, nueva_contraseña, nuevo_nombre, nueva_carrera, nuevo_centro):
        self.open()
        query = "UPDATE usuarios SET correo=%s, contraseña=%s, nombre=%s, carrera=%s, centro=%s WHERE id=%s"
        data = (nuevo_correo, nueva_contraseña, nuevo_nombre, nueva_carrera, nuevo_centro, usuario_id)
        self.cursor.execute(query, data)
        self.conn.commit()
        self.close()

    def insertarCurriculum(self, curriculum):
        self.open()
        self.sql = "INSERT INTO curriculum (id, idusuarios, descripcion, experiencia, intereses, habilidades) VALUES (%s,%s,%s,%s,%s,%s)"
        self.data = (
            curriculum.getid(),
            curriculum.getidusuarios(),
            curriculum.getdescripcion(),
            curriculum.getexperiencia(),
            curriculum.getintereses(),
            curriculum.gethabilidades()
        )
        self.cursor.execute(self.sql, self.data)
        self.conn.commit()
        self.close()
        
    def actualizarCurriculum(self, idUsuario, nuevo_descripcion, nuevo_experiencia, nuevo_intereses, nuevo_habilidades):
        self.open()
        query = "UPDATE curriculum SET descripcion=%s, experiencia=%s, intereses=%s, habilidades=%s WHERE idusuarios=%s"
        data = (nuevo_descripcion, nuevo_experiencia, nuevo_intereses, nuevo_habilidades, idUsuario)
        self.cursor.execute(query, data)
        self.conn.commit()        
        self.close()

        
    def obtener_curriculum(self, idUsuarios):
        self.open()
        self.sql = "SELECT * FROM curriculum WHERE idusuarios = %s"
        self.data = (idUsuarios,)
        self.cursor.execute(self.sql, self.data)
        self.result = self.cursor.fetchall()
        self.conn.commit()
        self.close()
        return self.result
    
    def obtener_nombre_usuario_por_id(self, usuario_id):
        self.open()
        self.sql = "SELECT nombre FROM usuarios WHERE id=%s"
        self.data = (usuario_id,)
        self.cursor.execute(self.sql, self.data)
        result = self.cursor.fetchone()
        self.close()
        return result[0] if result else None
    
    def get_ids_curriculums(self):
        self.open()
        idCurriculum = []
        self.sql = "SELECT id FROM curriculum"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        for x in self.result:
            idCurriculum.append(int(x[0]))
        idCurriculum.sort()
        self.conn.commit()
        self.close()
        return idCurriculum
    
    def insertar_proyecto(self, proyecto):
        self.open()
        self.sql = "INSERT INTO proyecto (id, nombre, descripcion, objetivo, area) VALUES (%s, %s, %s, %s, %s)"
        self.data = (
            proyecto.getid(),
            proyecto.getnombre(),
            proyecto.getdescripcion(),
            proyecto.getobjetivo(),
            proyecto.getarea(),
        )
        self.cursor.execute(self.sql, self.data)
        self.conn.commit()
        self.close()

        
    def get_ids_proyectos(self):
        self.open()
        idProyecto = []
        self.sql = "SELECT id FROM proyecto"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        for x in self.result:
            idProyecto.append(int(x[0]))
        idProyecto.sort()
        self.conn.commit()
        self.close()
        return idProyecto
    
    def buscar_proyectos(self, nombre):
        self.open()
        self.cursor.execute("SELECT * FROM proyecto WHERE nombre LIKE %s", (f"%{nombre}%",))
        proyectos = self.cursor.fetchall()
        self.conn.commit()
        self.close()
        return proyectos
    
    def obtener_curriculum(self, idUsuarios):
        self.open()
        self.sql = "SELECT * FROM curriculum WHERE idusuarios = %s"
        self.data = (idUsuarios,)
        self.cursor.execute(self.sql, self.data)
        self.result = self.cursor.fetchall()
        self.conn.commit()
        self.close()
        return self.result


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
    
class curriculum:
    def __init__(self, id, idusuarios, descripcion, experiencia, intereses, habilidades):
        self.id = id
        self.idusuarios = idusuarios
        self.descripcion = descripcion
        self.experiencia = experiencia  # Corregido el nombre de la variable
        self.intereses = intereses
        self.habilidades = habilidades

    def getid(self):
        return self.id
    def getidusuarios(self):
        return self.idusuarios
    def getdescripcion(self):
        return self.descripcion
    def getexperiencia(self):
        return self.experiencia
    def getintereses(self):
        return self.intereses
    def gethabilidades(self):
        return self.habilidades 

class proyecto:
    def __init__(self, id, nombre, descripcion, objetivo, area):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetivo = objetivo  # Corregido el nombre de la variable
        self.area = area

    def getid(self):
        return self.id
    def getnombre(self):
        return self.nombre
    def getdescripcion(self):
        return self.descripcion
    def getobjetivo(self):
        return self.objetivo
    def getarea(self):
        return self.area