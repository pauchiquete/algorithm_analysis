def encontrar_subconjuntos_contiguos_maximos(conjunto):
    def encontrar_maximo_cruzado(conjunto, izquierda, medio, derecha):
        max_izquierda = float('-inf')
        suma_izquierda = 0
        for i in range(medio, izquierda - 1, -1):
            suma_izquierda += conjunto[i]
            if suma_izquierda > max_izquierda:
                max_izquierda = suma_izquierda

        max_derecha = float('-inf')
        suma_derecha = 0
        for i in range(medio + 1, derecha + 1):
            suma_derecha += conjunto[i]
            if suma_derecha > max_derecha:
                max_derecha = suma_derecha

        return max_izquierda + max_derecha

    def encontrar_maximo_subconjunto(conjunto, izquierda, derecha):
        if izquierda == derecha:
            return conjunto[izquierda]

        medio = (izquierda + derecha) // 2

        max_izquierda = encontrar_maximo_subconjunto(conjunto, izquierda, medio)
        max_derecha = encontrar_maximo_subconjunto(conjunto, medio + 1, derecha)
        max_cruzado = encontrar_maximo_cruzado(conjunto, izquierda, medio, derecha)

        return max(max_izquierda, max_derecha, max_cruzado)

    return encontrar_maximo_subconjunto(conjunto, 0, len(conjunto) - 1)

# Ejemplo de uso
conjunto = [1, -2, 3, 10, -4, 7, 2, -5]
maximo_contiguo = encontrar_subconjuntos_contiguos_maximos(conjunto)
print("Máxima suma de subconjuntos contiguos:", maximo_contiguo)