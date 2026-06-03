# `def main()` y `if __name__ == "__main__":` en Python

> Patrón profesional para organizar cualquier archivo Python ejecutable.

---

## La idea central

Tu archivo de Python es como una **caja de herramientas**:

- **Las funciones de arriba** son las herramientas (cosas que calculan y retornan).
- **`def main()`** es el director de orquesta: usa las herramientas, pide inputs, muestra resultados.
- **`if __name__ == "__main__":`** es el interruptor que decide si se ejecuta `main()` o no.

---

## Estructura profesional de un archivo Python

```python
# 1. Imports (si los hay)
from datetime import datetime

# 2. Constantes (si las hay)
PI = 3.14159

# 3. Funciones / herramientas
def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    # ...

# 4. main() — el director de orquesta
def main():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    operacion = input("Ingrese una operacion (+, -, *, /): ")
    resultado = calcular(num1, num2, operacion)
    print(f"El resultado es: {resultado}")

# 5. Interruptor
if __name__ == "__main__":
    main()
```

**Tres bloques claros:** herramientas arriba, instrucciones en `main()`, interruptor al final.

---

## ¿Qué es `__name__`?

Es una **variable mágica** que Python le pone a cada archivo automáticamente. Vos no la creás, ya está.

| Cómo se usa el archivo | Valor de `__name__` |
| ---------------------- | ------------------- |
| Lo ejecutás directo con `python archivo.py` | `"__main__"` |
| Lo importás desde otro archivo (`from archivo import ...`) | `"archivo"` (el nombre del módulo) |

Por eso:

```python
if __name__ == "__main__":
    main()
```

se traduce a: **"Si me están ejecutando directamente, corré `main()`. Si me están importando, no hagas nada."**

---

## ¿Por qué hace falta el interruptor?

Porque Python, al importar un archivo, **ejecuta todo el código que no esté adentro de una función**, de arriba a abajo.

### Sin guarda (la versión peligrosa)

```python
# nivel2.py
def calcular(a, b):
    return a + b

# código suelto
num1 = float(input("Numero: "))
num2 = float(input("Otro: "))
print(calcular(num1, num2))
```

Desde otro archivo:

```python
# nivel3.py
from nivel2 import calcular  # solo quiero la funcion
print("hola desde nivel 3")
```

Al ejecutar `python nivel3.py`:

```
Numero:                ← Python te pide input aunque no quisieras
Otro:                  ← te pide otro
3.0                    ← imprime el resultado
hola desde nivel 3     ← recien aca tu codigo
```

**Locura.** Solo querías importar una funcion y se te ejecutó todo.

### Con guarda (la versión correcta)

```python
# nivel2.py
def calcular(a, b):
    return a + b

def main():
    num1 = float(input("Numero: "))
    num2 = float(input("Otro: "))
    print(calcular(num1, num2))

if __name__ == "__main__":
    main()
```

Desde `nivel3.py`:

```python
from nivel2 import calcular
print("hola desde nivel 3")
print(calcular(2, 3))
```

Al ejecutar `python nivel3.py`:

```
hola desde nivel 3
5
```

Python al importar `nivel2`:

1. Lee las definiciones de `calcular` y `main` (las guarda en memoria, no las ejecuta).
2. Llega al `if __name__ == "__main__":` y pregunta: "¿`__name__` vale `"__main__"`?"
3. **NO**, vale `"nivel2"` porque estoy siendo importado.
4. **Salta `main()`, no lo ejecuta.**

---

## Regla de oro

> **Todo código que esté FUERA de una función, en el nivel más exterior del archivo, se ejecuta cuando el archivo es importado.**

Por eso:

- TODO el código ejecutable lo metés adentro de funciones.
- La **única** cosa "suelta" abajo es el `if __name__ == "__main__":` que actúa como interruptor.
- Eso es lo que hace que Python sea **modular**: podés armar archivos que sirven como herramientas reutilizables, sin efectos colaterales al importarlos.

---

## Errores comunes (los que ya cometiste)

```python
if_name__== "__main__":      # MAL — sin espacios, falta __ al principio de name
if __name__== "__main__":     # MAL — falta espacio antes de ==
if __name__ == "__main__":    # MAL si no llamas a main() abajo
```

La forma correcta, completa:

```python
if __name__ == "__main__":
    main()
```

Fijate bien:

- `if` espacio `__name__` (dos guiones bajos a cada lado de `name`)
- espacio `==` espacio
- `"__main__"` (también dos guiones bajos a cada lado)
- `:` al final
- En la siguiente linea, **indentado**, `main()` para realmente llamarla

---

## Checklist mental al escribir un script Python

- [ ] ¿Las funciones SOLO calculan y retornan? (no imprimen, no piden input)
- [ ] ¿Los `input()` y `print()` estan dentro de `main()`, no sueltos?
- [ ] ¿Llamo a `main()` desde `if __name__ == "__main__":`?
- [ ] ¿El archivo podria importarse desde otro lado sin efectos colaterales?

Si las cuatro respuestas son SI, está profesional.

---

## Analogía para recordar

`main()` es el **director de orquesta**. Las funciones son los **músicos**. El `if __name__ == "__main__":` es el **botón de encendido** del escenario.

- Si abrís el teatro (`python archivo.py`) → se prende el escenario → arranca el director → empieza el concierto.
- Si alguien viene solo a llevarse un músico para tocar en otro lado (`from archivo import calcular`) → el teatro queda apagado, el director no aparece, solo se lleva al músico que necesitaba.

**Es así de facil.**
