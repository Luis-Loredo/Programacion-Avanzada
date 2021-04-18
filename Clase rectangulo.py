class rectangulo:
    def __init__ (self, base , alturax , altura ):
        self.base = base
        self.alturax = alturax
        self.altura = altura
    
    def area(self):
        self.base * self.altura
    
    def prisma(self):
        self.area * self.altura

    def piramide(self):
        self.area * self.altura / 3

base = input("Dime la base: ")
alturax = input("Dime la altura rectangulo: ")
altura = input("Dime la altura del prisma: ")

print("El area es: ", base * altura)
print("El prisma mide: ", base *alturax)
print("La piramide mide: ", base * altura / 3)
