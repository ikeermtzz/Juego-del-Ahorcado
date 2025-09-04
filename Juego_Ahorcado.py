from random import *
lista_palabras = ["python", "programacion", "juego", "ahorcado",
                  "computadora","teclado", "pantalla", "internet",
                  "algoritmo", "variable", "funcion", "bucle",
                  "condicional", "clase", "objeto", "matriz",
                  "diccionario", "modulo", "cadena", "lista"]
letras_incorrectas = set()
letras_correctas = set()
letras_usadas = set()

#Funcion para elegir palabra alazar
def elegir_palabra(lista):
    return choice(lista)

#Funcion pedir letra
def pedir_letra(usadas):
    while True:
        intento = input("Ingresa una letra: ").lower().strip()
        if len(intento) != 1 or not(intento.isalpha()):
            print("Debes ingresar UNA sola letra")
            continue
        if intento in usadas:
            print("Ya usaste esa letra. Elige otra.")
            continue
        usadas.add(intento)  #marca como usada
        return intento

#Funcion chequear letra
def chequear_letra(palabra, letra, correctas, incorrectas):
    if letra in palabra:
        correctas.add(letra)
        return True
    else:
        incorrectas.add(letra)
        return False

#Funcion Progreso
def progreso_palabra(palabra, correctas):
    """[c if c in correctas else "_" for c in palabra]
        Esto es una comprension de listas.
        Recorre cada carácter l en la palabra secreta.
        Si esa letra ya está en el conjunto correctas, la pone tal cual (l).
        Si no, la reemplaza con "_"."""
    return " ".join([l if l in correctas else "_" for l in palabra])

print("Bienvenido al juego del ahorcado\nHe elegido la palabra\nEs hora de adivinar")
palabra_secreta = elegir_palabra(lista_palabras)
vidas = 6
while vidas > 0:
    print("\nPalabra:", progreso_palabra(palabra_secreta, letras_correctas))
    print("Letras incorrectas:", " ".join(sorted(letras_incorrectas)) or "-")
    print("Vidas:", vidas)
    letra_pedida = pedir_letra(letras_usadas)
    if chequear_letra(palabra_secreta, letra_pedida, letras_correctas, letras_incorrectas):
        # ¿Ganó?
        """set(palabra_secreta).issubset(letras_correctas): set(palabra_secreta) - Convierte la palabra secreta 
        (que es un string) en un conjunto de letras únicas. .issubset(otro_conjunto) - Este método responde 
        con True si todos los elementos del primer set están dentro del segundo. Si todas las letras de la palabra 
        secreta ya están dentro de las letras correctas que el jugador ha adivinado, entonces el jugador gana."""
        if set(palabra_secreta).issubset(letras_correctas):
            print("\n¡Ganaste! La palabra era:", palabra_secreta)
            break
    else:
        vidas -= 1

if vidas == 0:
    print("\nPerdiste. La palabra era:", palabra_secreta)

