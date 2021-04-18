radio = ""
altura = ""

class circulo:
    def __init__ (self, radio, altura ):
        self.radio = radio
        self.altura = altura
    
    def area(self):
        self.radio ** 2

    def prisma(self):
        self.area * altura
    
    def piramide(self):
        self.area * altura / 3

radio = input("Dime el radio: ")
altura = input("Dime la altura: ")

print ("El area es: ", radio )
print ("El prisma es: ", radio * altura)
print ("La piramide es: ", radio * altura / 3)