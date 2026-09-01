import random

class Games:

    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        opciones = ["piedra", "papel", "tijera"]

        if jugador1 not in opciones or jugador2 not in opciones:
            if jugador1 not in opciones:
                return "invalid"
            return "invalid"

        if jugador1 == jugador2:
            return "empate"

        if (
            (jugador1 == "piedra" and jugador2 == "tijera") or
            (jugador1 == "papel" and jugador2 == "piedra") or
            (jugador1 == "tijera" and jugador2 == "papel")
        ):
            return "jugador1"

        return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        for i in range(3):
            if tablero[i][0] != " " and tablero[i][0] == tablero[i][1] == tablero[i][2]:
                return tablero[i][0]

            if tablero[0][i] != " " and tablero[0][i] == tablero[1][i] == tablero[2][i]:
                return tablero[0][i]

        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            return tablero[0][0]

        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            return tablero[0][2]

        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        combinacion = []

        for _ in range(longitud):
            combinacion.append(random.choice(colores_disponibles))

        return combinacion

    def validar_movimiento_torre_ajedrez(
        self,
        desde_fila,
        desde_col,
        hasta_fila,
        hasta_col,
        tablero
    ):
        if desde_fila < 0 or desde_fila > 7:
            return False

        if desde_col < 0 or desde_col > 7:
            return False

        if hasta_fila < 0 or hasta_fila > 7:
            return False

        if hasta_col < 0 or hasta_col > 7:
            return False

        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        if desde_fila == hasta_fila:
            inicio = min(desde_col, hasta_col)
            fin = max(desde_col, hasta_col)

            for col in range(inicio + 1, fin):
                if tablero[desde_fila][col] != " ":
                    return False

        else:
            inicio = min(desde_fila, hasta_fila)
            fin = max(desde_fila, hasta_fila)

            for fila in range(inicio + 1, fin):
                if tablero[fila][desde_col] != " ":
                    return False

        return True