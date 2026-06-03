  NIVEL 1 — Variables y tipos de datos

  1. Conversor de temperatura: pedile al usuario una temperatura en Celsius y mostrala en Fahrenheit. Fórmula: F = C *
  9/5 + 32.
  2. Cálculo de edad: pedile al usuario su año de nacimiento y calculá cuántos años tiene (o tendrá) en 2026.
  3. Intercambio de variables: tenés a = 5 y b = 10. Intercambialos sin usar una tercera variable.(Pista: Python tiene
  una forma elegante de hacerlo).

  NIVEL 2 — Operadores

  4. Par o impar: pedile un número al usuario y decile si es par o impar. (Usá el operador módulo %).
  <!-- 5. Calculadora simple: pedile dos números y una operación (+, -, *, /) y mostrá el resultado. -->


  <!-- `` -->
  6. Año bisiesto: dado un año, determiná si es bisiesto. (Regla: divisible por 4, EXCEPTO si es divisible por 100 PERO
  sí divisible por 400).

  NIVEL 3 — Strings

  7. Contador de vocales: dada una palabra, contá cuántas vocales tiene.
  8. Palíndromo: pedile una palabra y decile si se lee igual al derecho y al revés (ej: "neuquen","reconocer").
  9. Iniciales: dado un nombre completo ("Juan Pablo Pérez"), devolvé las iniciales: "J.P.P."
  10. Reemplazo manual: dado un texto, reemplazá todos los espacios por guiones bajos SIN usar .replace(). (Tenés que
  pensar con un loop).

  NIVEL 4 — Condicionales

  11. Categorizador de edad: dado una edad, decí si es: bebé (0-2), niño (3-12), adolescente (13-17), adulto (18-64),
  adulto mayor (65+).
  12. Triángulo válido: dados 3 lados, determiná si forman un triángulo. (Regla: cada lado debe ser menor a la suma de
  los otros dos).
  13. Sistema de notas: dado un puntaje 0-100, devolvé la nota: A (90+), B (80-89), C (70-79), D (60-69), F (menos
  de 60).

  NIVEL 5 — Loops (for, while)

  14. Tabla de multiplicar: pedile un número y mostrá su tabla del 1 al 10.
  15. Suma de pares: sumá todos los números pares del 1 al 100.
  16. Factorial: calculá el factorial de un número (5! = 5*4*3*2*1 = 120).
  17. Fibonacci: imprimí los primeros N números de Fibonacci (0, 1, 1, 2, 3, 5, 8...).
  18. Adivinanza: el programa genera un número aleatorio entre 1 y 100. El usuario va adivinando. Le decís "más alto" o
  "más bajo" hasta que acierte. (Usá random.randint()).

  NIVEL 6 — Listas

  19. Máximo y mínimo: dada una lista de números, encontrá el mayor y el menor SIN usar max() ni min().
  20. Promedio: calculá el promedio de una lista de números.
  21. Sin duplicados: dada una lista con elementos repetidos, devolvé una nueva sin duplicados (mantené el orden).
  22. Invertir: invertí una lista SIN usar .reverse() ni [::-1].
  23. Ordenar: ordená una lista de menor a mayor SIN usar .sort() ni sorted(). (Bubble sort o selection sort).

  NIVEL 7 — Diccionarios

  24. Contador de palabras: dado un texto, devolvé un diccionario con cada palabra y cuántas vecesaparece.
  25. Agenda: hacé un programa que permita agregar contactos (nombre → teléfono), buscar por nombre, listar todos, y
  eliminar.
  26. Inventario: gestioná un stock de productos: agregar, restar, consultar stock disponible.

  NIVEL 8 — Tuplas y Sets

  27. Coordenadas: representá un punto en 2D con una tupla (x, y) y calculá la distancia entre dospuntos.
  28. Elementos comunes: dados dos listas, devolvé los elementos que están en AMBAS (usá sets, vasa entender por qué
  son tan útiles).

  NIVEL 9 — Funciones (más serio)

  29. Refactor del calcular_propina: agarrá tu ejercicio actual y separá el cálculo del print. La función SOLO calcula y
   devuelve. Otra función muestra.
  30. Validador de email: hacé una función que reciba un string y devuelva True si parece un emailválido (tiene @,
  tiene un . después del @, etc.).
  31. Función con kwargs: hacé una función crear_usuario que reciba nombre obligatorio y opcionalmente edad, email,
  pais. Devolvé un diccionario.

  NIVEL 10 — Manejo de errores

  32. División segura: hacé una función que divida dos números. Si el divisor es 0, manejá el error con try/except y
  devolvé un mensaje claro.
  33. Lectura de input: pedile un número al usuario. Si escribe letras, capturá el ValueError y volvele a pedir hasta
  que ingrese un número válido.

  NIVEL 11 — Archivos

  34. Escribir y leer: escribí una lista de nombres a un archivo nombres.txt. Después leelo y mostralo.
  35. Contador de líneas: dado un archivo de texto, contá cuántas líneas tiene.

  NIVEL 12 — List comprehensions (PYTHONICO de verdad)

  36. Cuadrados: dada una lista [1,2,3,4,5], generá [1,4,9,16,25] en UNA LÍNEA con list comprehension.
  37. Filtrar pares: dada una lista de números, devolvé solo los pares en una línea.
  38. Transformar diccionario: dado {"a":1, "b":2, "c":3}, devolvé {"a":2, "b":4, "c":6} con dict comprehension.