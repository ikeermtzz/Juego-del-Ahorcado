# 🎯 Juego del Ahorcado (CLI, Python)

Un ahorcado clásico por consola: el programa elige una palabra al azar y tú la adivinas letra por letra. Tienes **6 vidas**. Cada fallo resta una vida; si completas todas las letras antes de quedarte sin intentos, ganas. 🏆

---

## 🚀 Requisitos
- Python 3.8+ (no requiere librerías externas)

---

## ▶️ Ejecución
Guarda tu script (por ejemplo `ahorcado.py`) y ejecútalo:

bash
python ahorcado.py
🧠 ¿Cómo funciona?
Se elige una palabra secreta con choice() desde lista_palabras.

Se piden letras validando que sean una sola letra y no se repitan.

Si la letra está en la palabra → se agrega a letras_correctas.

Si no está → se agrega a letras_incorrectas y se resta una vida.

El progreso se muestra reemplazando letras no adivinadas por _.

Condición de victoria: set(palabra).issubset(letras_correctas).

🧩 Estructura del código (funciones)
elegir_palabra(lista): retorna una palabra al azar.

pedir_letra(usadas): pide y valida una letra (una sola, a–z, no repetida).

chequear_letra(palabra, letra, correctas, incorrectas): actualiza acierto/error.

progreso_palabra(palabra, correctas): devuelve el estado tipo p _ _ o _.


🛠️ Personaliza
Palabras: edita lista_palabras.

Vidas: cambia vidas = 6.

Formato del progreso: usa "" en lugar de " " dentro de join para quitar espacios.

💡 Ideas de mejora
Contador de partidas ganadas/perdidas.

Dificultad (vidas/palabras por longitud).

Historial de letras en una sola línea con colores (si usas colorama).

Cargar palabras desde un archivo (.txt).

¡Listo para jugar y seguir mejorándolo! 🎉
