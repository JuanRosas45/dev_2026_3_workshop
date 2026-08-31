import math
class Formulas:
    """
    Clase con ejercicios de fórmulas de física, finanzas y álgebra.
    """

    def velocidad_media(self, distancia, tiempo):
        return distancia / tiempo

    def mruv_posicion(self, posicion_inicial, velocidad_inicial, aceleracion, tiempo):
        return posicion_inicial + velocidad_inicial * tiempo + (aceleracion * tiempo ** 2) / 2

    def mruv_velocidad(self, velocidad_inicial, aceleracion, tiempo):
        return velocidad_inicial + aceleracion * tiempo

    def fuerza_newton(self, masa, aceleracion):
        return masa * aceleracion

    def energia_cinetica(self, masa, velocidad):
        return (1 / 2) * masa * velocidad ** 2
    def energia_potencial(self, masa, altura, gravedad=9.8):
        return masa * gravedad * altura
    def ley_ohm_voltaje(self, corriente, resistencia):
        return corriente * resistencia


    def ley_ohm_corriente(self, voltaje, resistencia):
        return voltaje / resistencia

    def interes_simple(self, capital, tasa, tiempo):
        return capital * tasa * tiempo

    def interes_compuesto(self, capital, tasa, tiempo, n=1):
        return capital * (1 + tasa / n) ** (n * tiempo)


    def discriminante(self, a, b, c):
        return b ** 2 - 4 * a * c

    def raices_cuadraticas(self, a, b, c):
        discriminante = self.discriminante(a, b, c)

    def raices_cuadraticas(self, a, b, c):
        discriminante = self.discriminante(a, b, c)

        if discriminante < 0:
            raise ValueError("No hay raíces reales")

        raiz = math.sqrt(discriminante)

        raiz1 = (-b + raiz) / (2 * a)
        raiz2 = (-b - raiz) / (2 * a)

        return (raiz1, raiz2)
    
    def imc(self, peso, altura):
        return peso / altura ** 2

    def hipotenusa_pitagoras(self, cateto1, cateto2):
        return math.sqrt(cateto1 ** 2 + cateto2 ** 2)