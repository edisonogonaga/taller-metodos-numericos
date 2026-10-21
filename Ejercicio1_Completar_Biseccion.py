import numpy as np


def biseccion(f, a, b, TOL=1e-6, N0=100):
    """Devuelve (p, historia), con historia = [(a, b, p) por iteración]."""
    FA = f(a)
    historia = []
    i = 1

    while i <= N0:
        p = (a + b) / 2
        FP = f(p)
        historia.append((a, b, p))

        if FP == 0 or (b - a) / 2 < TOL:
            return p, historia

        i += 1

        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p

    raise RuntimeError(f"Fracaso después de {N0} iteraciones.")


def f(x: float) -> float:
    return x**3 + 4 * x**2 - 10


if __name__ == "__main__":
    p, historia = biseccion(f, 1.0, 2.0, TOL=1e-2)
    print(f"La solución es: {p:.6f}")
    print(f"Número de iteraciones: {len(historia)}")
