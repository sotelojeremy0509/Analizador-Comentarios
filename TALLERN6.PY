"""
Analizador de comentarios - Taller 6 (Cadenas y tuplas)
Lógica de Programación - Python

Programa de consola para registrar comentarios de estudiantes y analizarlos
con operaciones básicas de texto. Solo usa listas, tuplas y cadenas
(sin diccionarios, clases, archivos ni librerías externas).
"""

comentarios = []

SIGNOS = ".,;:!?¡¿()\"'-"

def normalizar(texto):
    texto = texto.strip().lower()
    for signo in SIGNOS:
        texto = texto.replace(signo, " ")
    return texto


def palabras_de(texto):
    return normalizar(texto).split()


def hay_comentarios():
    if len(comentarios) == 0:
        print("Todavía no hay comentarios registrados.")
        return False
    return True


def pedir_palabra():
    entrada = input("Escriba la palabra: ")
    partes = palabras_de(entrada)
    if len(partes) != 1:
        print("Debe ingresar una sola palabra.")
        return ""
    return partes[0]


def seleccionar_comentario():
    mostrar_comentarios()
    opcion = input("Número del comentario: ").strip()
    if not opcion.isdigit():
        print("Debe ingresar un número.")
        return -1
    indice = int(opcion) - 1
    if indice < 0 or indice >= len(comentarios):
        print("Ese comentario no existe.")
        return -1
    return indice


def contar_palabra_en_comentario(texto, palabra):
    return palabras_de(texto).count(palabra)


def generar_resumen(texto, palabra):
    caracteres = len(texto)
    cantidad_palabras = len(palabras_de(texto))
    apariciones = contar_palabra_en_comentario(texto, palabra)
    return (caracteres, cantidad_palabras, apariciones)

def registrar_comentario():
    texto = input("Escriba el comentario: ").strip()
    if texto != "":
        comentarios.append(texto)
        print("Comentario registrado.")
    else:
        print("El comentario no puede estar vacío.")


def mostrar_comentarios():
    if not hay_comentarios():
        return
    print("\n--- COMENTARIOS REGISTRADOS ---")
    for i in range(len(comentarios)):
        print(i + 1, comentarios[i])


def buscar_comentarios():
    if not hay_comentarios():
        return
    palabra = pedir_palabra()
    if palabra == "":
        return

    encontrados = []
    for i in range(len(comentarios)):
        if palabra in palabras_de(comentarios[i]):
            encontrados.append((i + 1, comentarios[i]))

    if len(encontrados) == 0:
        print(f'Sin coincidencias: ningún comentario contiene "{palabra}".')
    else:
        print(f'Búsqueda exitosa: {len(encontrados)} comentario(s) '
              f'contienen "{palabra}":')
        for encontrado in encontrados:
            print(f"  {encontrado[0]}. {encontrado[1]}")


def mostrar_cantidad_palabras():
    if not hay_comentarios():
        return
    print("\n--- PALABRAS POR COMENTARIO ---")
    for i in range(len(comentarios)):
        cantidad = len(palabras_de(comentarios[i]))
        print(f"Comentario {i + 1}: {cantidad} palabras")


def contar_palabra():
    if not hay_comentarios():
        return
    indice = seleccionar_comentario()
    if indice == -1:
        return
    palabra = pedir_palabra()
    if palabra == "":
        return

    veces = contar_palabra_en_comentario(comentarios[indice], palabra)
    if veces == 0:
        print(f'La palabra "{palabra}" no aparece en el comentario '
              f'{indice + 1}.')
    else:
        print(f'La palabra "{palabra}" aparece {veces} vez/veces en el '
              f'comentario {indice + 1}.')


def mostrar_resumen():
    if not hay_comentarios():
        return
    indice = seleccionar_comentario()
    if indice == -1:
        return
    palabra = pedir_palabra()
    if palabra == "":
        return

    resumen = generar_resumen(comentarios[indice], palabra)
    print(f"\n--- RESUMEN DEL COMENTARIO {indice + 1} ---")
    print("Tupla:", resumen)
    print("Caracteres:", resumen[0])
    print("Palabras:", resumen[1])
    print(f'Apariciones de "{palabra}":', resumen[2])


# Menú principal
def mostrar_menu():
    print("\n===== ANALIZADOR DE COMENTARIOS =====")
    print("1. Registrar un comentario")
    print("2. Mostrar todos los comentarios")
    print("3. Buscar comentarios por palabra")
    print("4. Mostrar cantidad de palabras de cada comentario")
    print("5. Contar una palabra en un comentario")
    print("6. Mostrar resumen de un comentario")
    print("7. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            registrar_comentario()
        elif opcion == "2":
            mostrar_comentarios()
        elif opcion == "3":
            buscar_comentarios()
        elif opcion == "4":
            mostrar_cantidad_palabras()
        elif opcion == "5":
            contar_palabra()
        elif opcion == "6":
            mostrar_resumen()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Elija un número del 1 al 7.")


if __name__ == "__main__":
    main()