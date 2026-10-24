# Analizador de comentarios

Proyecto del **Taller 6 – Manipulación de texto, cadenas y tuplas** (Lógica de Programación, Python).

Programa de consola que permite registrar comentarios de estudiantes sobre sus cursos y analizarlos con operaciones básicas de texto. Usa únicamente **cadenas, listas y tuplas**: sin diccionarios, clases, archivos, bases de datos ni librerías externas.

## Autor

Jeremy Antoine Sotelo Scarpeta – Ingeniería de Software, Universidad de La Salle.

## Requisitos

- Python 3.8 o superior (no necesita instalar nada más).

## Cómo ejecutarlo

```bash
python TALLERN6.py
```

## Menú

| Opción | Qué hace |
|--------|----------|
| 1 | Registra un comentario (no acepta comentarios vacíos). |
| 2 | Muestra todos los comentarios registrados. |
| 3 | Busca los comentarios que contienen una palabra e informa si hubo o no coincidencias. |
| 4 | Muestra la cantidad de palabras de cada comentario. |
| 5 | Cuenta cuántas veces aparece una palabra en un comentario elegido. |
| 6 | Genera el resumen de un comentario elegido en una tupla `(caracteres, palabras, apariciones)`. |
| 7 | Sale del programa. |

Si todavía no hay comentarios, las opciones 2 a 6 avisan: *"Todavía no hay comentarios registrados."*

## Estructura del código

- `comentarios`: lista global donde se guardan los textos.
- `normalizar(texto)`: pasa a minúsculas, quita espacios extremos y reemplaza signos de puntuación por espacios.
- `palabras_de(texto)`: devuelve la lista de palabras del texto normalizado.
- `contar_palabra_en_comentario(texto, palabra)`: cuenta apariciones de la palabra completa.
- `generar_resumen(texto, palabra)`: devuelve la tupla de resumen.
- Funciones de menú: `registrar_comentario`, `mostrar_comentarios`, `buscar_comentarios`, `mostrar_cantidad_palabras`, `contar_palabra`, `mostrar_resumen` y `main`.

Métodos de cadenas usados: `strip()`, `lower()`, `replace()`, `split()`, `count()` e `isdigit()`, además del operador `in`.

## Detalles de diseño

- La búsqueda y el conteo trabajan con **palabras completas** e ignoran mayúsculas y signos de puntuación. Por ejemplo, buscar `curso` encuentra "Curso," pero no "cursos".
- Las coincidencias de la búsqueda se guardan como tuplas `(número, texto)`.
- El resumen se guarda en una tupla porque son tres datos fijos que no se modifican después de calcularse.

## Ejemplo de uso

```text
===== ANALIZADOR DE COMENTARIOS =====
Elija una opción: 1
Escriba el comentario: El curso de Python es muy bueno y el profesor explica muy bien
Comentario registrado.

Elija una opción: 3
Escriba la palabra: profesor
Búsqueda exitosa: 1 comentario(s) contienen "profesor":
  1. El curso de Python es muy bueno y el profesor explica muy bien

Elija una opción: 3
Escriba la palabra: examen
Sin coincidencias: ningún comentario contiene "examen".

Elija una opción: 6
Número del comentario: 1
Escriba la palabra: muy

--- RESUMEN DEL COMENTARIO 1 ---
Tupla: (62, 13, 2)
Caracteres: 62
Palabras: 13
Apariciones de "muy": 2
```

## Casos de prueba cubiertos

1. Registrar tres comentarios diferentes.
2. Intentar registrar un comentario vacío.
3. Mostrar todos los comentarios.
4. Buscar una palabra que aparece en dos comentarios.
5. Buscar una palabra que no aparece en ninguno.
6. Contar las apariciones de una palabra en un comentario.
7. Generar el resumen de un comentario.
8. Probar todas las opciones con la lista vacía.
