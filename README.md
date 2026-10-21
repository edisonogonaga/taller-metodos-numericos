# Taller 2 — Métodos Numéricos (Método de Bisección)

Autor: **Edison Ogonaga**

Resolución del **Taller 2** con los dos ejercicios separados e identificados y el script que los une:

## Archivos del Repositorio

- [`Ejercicio1_Completar_Biseccion.py`](./Ejercicio1_Completar_Biseccion.py): **Ejercicio 1. Completar la bisección** — Uso de `biseccion` con $f(x) = x^3 + 4x^2 - 10 = 0$ en $[1, 2]$ y $TOL = 10^{-2}$.
- [`Ejercicio2_Caida_Resistencia_Aire.py`](./Ejercicio2_Caida_Resistencia_Aire.py): **Ejercicio 2. Caída con resistencia del aire** — Definición de $s(t)$, resolución con `biseccion` en $[0, 20]$ con $TOL = 10^{-4}$ y generación de la gráfica con `graficar(..., k_iteracion=3)`.
- [`Taller2_Completo.py`](./Taller2_Completo.py): Script completo que une el Ejercicio 1 y el Ejercicio 2.
- [`caida.png`](./caida.png): Gráfica generada en el Ejercicio 2 resaltando la iteración 3.

---

## Ejercicio 1. Completar la bisección

Se resuelve la ecuación:

$$f(x) = x^3 + 4x^2 - 10 = 0, \quad x \in [1, 2], \quad TOL = 10^{-2}$$

- **Solución final ($p$):** `1.367188`
- **Número de iteraciones:** `7`

---

## Ejercicio 2. Caída con resistencia del aire

La posición $s(t)$ está dada por:

$$s(t) = s_0 - \frac{mg}{k}t + \frac{m^2 g}{k^2}\left(1 - e^{-kt/m}\right)$$

Con $g = 9.81$, $s_0 = 300.0$, $m = 0.25$ y $k = 0.1$, resolviendo en $[0, 20]$ con $TOL = 10^{-4}$:

- **Cambio de signo en $[0, 20]$:** $s(0) = 300.00 > 0$ y $s(20) = -129.21 < 0$
- **Tiempo de caída ($t^*$):** `14.725571 s`
- **Número de iteraciones:** `18`
- **Iteración 3 (`k_iteracion=3`):** Intervalo $[10, 15]$, punto medio $p = 12.5$


