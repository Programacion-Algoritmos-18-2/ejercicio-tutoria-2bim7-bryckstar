class Persona(object):

    # Se crea el init con los valores iniailes del metodo
    def __init__(self, n, a, e):
        self.nombre = n
        self.apellido = a
        self.edad = e

    # Se crean los metodos get y set para todas la variables
    def setNombre(self, n):
        self.nombre = n

    def setApellido(self, n):
        self.apellido = n

    def setEdad(self, n):
        self.edad = n

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getEdad(self):
        return self.edad

    # Metodo para presentar los datos
    def __str__(self):

        return "%s %s %d\n" % (self.getNombre(), self.getApellido(), self.getEdad())
