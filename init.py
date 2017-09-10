from models.Cliente import  Cliente
c = Cliente('Jose','Ramirez',edad=28)
print(c.edad)
print(c.nombres, len(c))
c.edad=27