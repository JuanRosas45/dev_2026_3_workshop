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
        """
        Calcula el monto final de un capital a interés compuesto.

        Args:
            capital (float): Capital inicial
            tasa (float): Tasa de interés anual (en decimal, ej. 0.05 para 5%)
            tiempo (float): Tiempo en años
            n (int): Número de capitalizaciones por año, por defecto 1

        Returns:
            float: Monto final

        Fórmula: M = C * (1 + r/n)^(n*t)

        Ejemplo:
            interes_compuesto(1000, 0.05, 2) -> 1102.5
        """
        pass

    def discriminante(self, a, b, c):
        """
        Calcula el discriminante de una ecuación cuadrática ax^2 + bx + c = 0.

        Args:
            a (float): Coeficiente cuadrático
            b (float): Coeficiente lineal
            c (float): Término independiente

        Returns:
            float: Discriminante

        Fórmula: D = b^2 - 4*a*c

        Ejemplo:
            discriminante(1, -3, 2) -> 1
        """
        pass

    def raices_cuadraticas(self, a, b, c):
        """
        Calcula las raíces reales de una ecuación cuadrática ax^2 + bx + c = 0
        usando la fórmula general. Si el discriminante es negativo, lanza ValueError.

        Args:
            a (float): Coeficiente cuadrático (distinto de cero)
            b (float): Coeficiente lineal
            c (float): Término independiente

        Returns:
            tuple: (raiz1, raiz2) las dos raíces reales

        Fórmula: x = (-b ± sqrt(b^2 - 4ac)) / (2a)

        Ejemplo:
            raices_cuadraticas(1, -3, 2) -> (2.0, 1.0)
        """
        pass

    def imc(self, peso, altura):
        """
        Calcula el Índice de Masa Corporal (IMC).

        Args:
            peso (float): Peso en kilogramos
            altura (float): Altura en metros

        Returns:
            float: Índice de Masa Corporal

        Fórmula: IMC = peso / altura^2

        Ejemplo:
            imc(70, 1.75) -> 22.86
        """
        pass

    def hipotenusa_pitagoras(self, cateto1, cateto2):
        """
        Calcula la longitud de la hipotenusa de un triángulo rectángulo.

        Args:
            cateto1 (float): Longitud del primer cateto
            cateto2 (float): Longitud del segundo cateto

        Returns:
            float: Longitud de la hipotenusa

        Fórmula: h = sqrt(cateto1^2 + cateto2^2)

        Ejemplo:
            hipotenusa_pitagoras(3, 4) -> 5.0
        """
        pass
