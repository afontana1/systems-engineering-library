"""One-sided upper Clopper-Pearson bound after zero failures. Teaching example."""
import math

def upper_zero_failures(n: int, confidence: float = 0.95) -> float:
    if type(n) is not int or n < 1: raise ValueError('n must be a positive integer')
    if not (0.0 < confidence < 1.0): raise ValueError('confidence must be in (0, 1)')
    return -math.expm1(math.log1p(-confidence) / n)

if __name__ == '__main__':
    for n in (30,100,300): print(n, f'{upper_zero_failures(n)*100:.3f}%')
