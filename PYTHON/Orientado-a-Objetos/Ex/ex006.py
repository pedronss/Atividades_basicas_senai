import os
os.system('cls')

class FormaGeometrica:
    def area(self):raise NotImplementedError("Subclasse deve implementar método abstrato!")
class Retangulo(FormaGeometrica):
    def area(self):
        return self.largura*self.altura
class Circulo(FormaGeometrica):
    def area(self):
        return 3.14*self.raio**2
class Triangulo(FormaGeometrica):
    def area(self):
        return (self.largura*self.altura)/2
class Trapezio(FormaGeometrica):
    def area(self):
        return (self.base_maior + self.base_menor) * self.altura / 2

def calcularforma(forma):
    print(forma.area())

retangulo=Retangulo()
retangulo.largura=10
retangulo.altura=5
print(retangulo.area())

circle=Circulo()
circle.raio=15
print(circle.area())

triangulo=Triangulo()
triangulo.largura=10
triangulo.altura=5
print(triangulo.area())

trapezio=Trapezio()

