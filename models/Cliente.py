class Cliente(object):
    estado_cuenta = None

    def __init__(self,nombre,apellidos,edad):
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad

    def __len__(self):
        return self.edad

    def __str__(self):
        #no es eficiente
        #return self.nombre+' '+self.apellidos

        #dato = ' Cliente: %s %s' % (self.nombre,self.apellidos)
        #return dato

        return self.getNombres()

    def getNombres(self):
        return ' '.join((self.nombre, self.apellidos), )

    @property
    def nombres(self):
        return ' '.join((self.nombre, self.apellidos), )

    """
    Comentario de bloque
    """

#Probando codigo dentro de la misma clase
 
if __file__ == '__main__':
    c = Cliente('Jose','Ramirez',edad=28)
    print(c.edad)
    print(c.nombres, len(c))
    c.edad=27
