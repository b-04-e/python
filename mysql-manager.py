import pymysql

class conectarbase:
    def __init__(self):
      self.host1 = input("Nombre Host o IP: ")
      self.usuario1 = input("Nombre de usuario de la DB:" )
      self.password1 = input("Password: ")
      self.base1 = input("Nombre de la base: ")
      try:
          conexion = pymysql.connect(host=self.host1, user=self.usuario1, password=self.password1, db=self.base1)
          print("Conexion OK a ", self.host1)
          MenuOpciones()
      except (pymysql.err.OperationalError) as e:
          print("Error al conectar ", e)
          MenuOpciones()

class VerTablas:
    def __init__(self):
        self.host1 = input("Nombre Host o IP: ")
        self.usuario1 = input("Nombre de usuario de la DB:")
        self.password1 = input("Password: ")
        self.base1 = input("Nombre de la base: ")
        self.tabla1 = input("Nombre de la tabla: ")

        try:
            conexion = pymysql.connect(host=self.host1, user=self.usuario1, password=self.password1, db=self.base1)
            cursor = conexion.cursor()
            consulta = "select * from " + self.tabla1
            print (consulta)
            cursor.execute(consulta)
            vuelta = cursor.fetchall()
            print(vuelta)
            MenuOpciones()
        except (pymysql.err.OperationalError) as e:
            print("Error al conectar ", e)
            MenuOpciones()

class MenuOpciones:
    def __init__(self):
        self.opcion=0
        #print ("Server definido", conectarbase.__init__(self).self.host1)
        print("1 Definir y probar datos de conexion a la base")
        print("2 Ver tablas de la base")
        self.opcion=int(input("Elija una opcion: "))
        print ("eligio ", self.opcion)
        if self.opcion == 1:
            print ("OK ejecuto clase")
            self.opcion = 0
            print("self", self.opcion)
            conectarbase()
        if self.opcion == 2:
            print("Ejecuto VerTablas")
            self.opcion = 0
            VerTablas()

MenuOpciones()
