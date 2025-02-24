class Persona:
    def __init__(self, nombre, edad, direccion):
        self._nombre = nombre
        self._edad = edad
        self._direccion = direccion

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad
        

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Dirección: {self._direccion}"

















