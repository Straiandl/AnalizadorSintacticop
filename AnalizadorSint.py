#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analizador Sintáctico
"""

class Lexico:
    """Clase para realizar el análisis léxico de la cadena de entrada."""
    def __init__(self, cadena: str):
        self.cadena = cadena.replace(" ", "")
        self.pos = 0
        self.simbolo = ""
        self.tipo = -1  

    def sigSimbolo(self):
        """Avanza al siguiente símbolo de la entrada."""
        if self.pos >= len(self.cadena):
            self.simbolo = "$"
            self.tipo = 2  
            return

        c = self.cadena[self.pos]
        self.pos += 1

        if c.isalpha():
            self.simbolo = c
            self.tipo = 0 
        elif c == '+':
            self.simbolo = '+'
            self.tipo = 1 
        elif c == '$':
            self.simbolo = '$'
            self.tipo = 2  
        else:
            self.simbolo = c
            self.tipo = -1  

    def terminado(self):
        return self.tipo == 2 and self.pos >= len(self.cadena)



def ejemplo1():
    print("=" * 50)
    print("EJEMPLO 1: Operaciones con la Pila")
    print("=" * 50)
    
    pila = []
    pila.append(2)
    pila.append(3)
    pila.append(4)
    pila.append(5)
    
    print(f"Estado de la pila: {pila}")
    print(f"Top element: {pila[-1]}")
    print(f"Top element: {pila[-1]}")
    print(f"Pop: {pila.pop()}")
    print(f"Pop: {pila.pop()}")
    print(f"Pila resultante: {pila}\n")



def ejemplo2():
    print("=" * 50)
    print("EJEMPLO 2: Lectura de símbolos léxicos")
    print("=" * 50)
    
    lexico = Lexico("a")
    lexico.sigSimbolo()
    print(f"Símbolo: {lexico.simbolo} | Tipo: {lexico.tipo}\n")



def ejercicio1(cadena="a+b"):
    print("=" * 50)
    print(f"EJERCICIO 1: Gramática E -> <id> + <id>")
    print(f"Cadena a analizar: '{cadena}'")
    print("=" * 50)

   
    tablaLR = [
        [2, 0,  0, 1], 
        [0, 0, -1, 0],  
        [0, 3,  0, 0],  
        [4, 0,  0, 0],  
        [0, 0, -2, 0]   
    ]


    id_reglas = [3]
    lon_reglas = [3]

    pila = [2, 0] 
    lexico = Lexico(cadena)
    lexico.sigSimbolo()

    paso = 1
    while True:
        estado_actual = pila[-1]
        columna = lexico.tipo

        if columna == -1:
            print(f"Error Léxico: Carácter no válido '{lexico.simbolo}'")
            break

        accion = tablaLR[estado_actual][columna]

        print(f"Paso {paso}:")
        print(f"  Pila: {pila}")
        print(f"  Entrada actual: '{lexico.simbolo}' (tipo {lexico.tipo})")
        print(f"  Acción: {accion}")

        if accion == -1:
            print("\n>>> ¡CADENA ACEPTADA EXITOSAMENTE! <<<\n")
            break

        elif accion > 0:
            
            print(f"  -> Desplazamiento al estado {accion}")
            pila.append(lexico.tipo)
            pila.append(accion)
            lexico.sigSimbolo()

        elif accion < 0:
           
            num_regla = abs(accion) - 2  
            longitud = lon_reglas[num_regla]
            no_terminal = id_reglas[num_regla]

            print(f"  -> Reducción por Regla {num_regla + 1} (Longitud: {longitud})")

          
            for _ in range(longitud * 2):
                pila.pop()

        
            estado_anterior = pila[-1]
            transicion = tablaLR[estado_anterior][no_terminal]

            pila.append(no_terminal)
            pila.append(transicion)

        else:
            print("\n>>> ERROR SINTÁCTICO: Cadena no válida <<<\n")
            break

        paso += 1


def ejercicio2(cadena="a+b"):
    print("=" * 50)
    print(f"EJERCICIO 2: Gramática E -> <id> + E | <id>")
    print(f"Cadena a analizar: '{cadena}'")
    print("=" * 50)

    
    tablaLR = [
        [2, 0,  0, 1],  
        [0, 0, -1, 0], 
        [0, 3, -3, 0],
        [2, 0,  0, 4],  
        [0, 0, -2, 0]  
    ]


    id_reglas = [3, 3]
    lon_reglas = [3, 1]

    pila = [2, 0]
    lexico = Lexico(cadena)
    lexico.sigSimbolo()

    paso = 1
    while True:
        estado_actual = pila[-1]
        columna = lexico.tipo

        if columna == -1:
            print(f"Error Léxico: Carácter no reconocido '{lexico.simbolo}'")
            break

        accion = tablaLR[estado_actual][columna]

        print(f"Paso {paso}:")
        print(f"  Pila: {pila}")
        print(f"  Entrada actual: '{lexico.simbolo}' (tipo {lexico.tipo})")

        if accion > 0:
            print(f"  Acción: {accion} (Desplazamiento al estado {accion})")
            pila.append(lexico.tipo)
            pila.append(accion)
            lexico.sigSimbolo()

        elif accion < 0:
            if accion == -1:
                print(f"  Acción: {accion} (Aceptación)")
                print("\n>>> ¡CADENA ACEPTADA EXITOSAMENTE! <<<\n")
                break
            else:
                num_regla = abs(accion) - 2 
                longitud = lon_reglas[num_regla]
                no_terminal = id_reglas[num_regla]

                print(f"  Acción: {accion} (Reducción por Regla {num_regla + 1}, sacar {longitud} símbolo(s))")

            
                for _ in range(longitud * 2):
                    pila.pop()

                estado_anterior = pila[-1]
                transicion = tablaLR[estado_anterior][no_terminal]

                pila.append(no_terminal)
                pila.append(transicion)

        else:
            print(f"  Acción: 0 (Error)")
            print("\n>>> ERROR SINTÁCTICO: La cadena no pertenece al lenguaje <<<\n")
            break

        paso += 1



def main():
    ejemplo1()
    ejemplo2()
    
    #Ejercicio 1
    ejercicio1("a+b")
    
    #Ejercicio 2
    ejercicio2("a")
    ejercicio2("a+b")
    ejercicio2("a+b+c")


if __name__ == "__main__":
    main()