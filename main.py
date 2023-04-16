import math

# Есть N фигур, среди них может быть:
# 1. Круг - у него будет задан радиус
# 2. Прямоугольник - у него будут заданы 2 стороны
# Задача: вывести суммарную площадь всех фигур.
# Пример данных:
FIGURES = [
  {'type': 'round', 'params': [3]},
  {'type': 'rectangle', 'params': [3, 4]},
  {'type': 'rectangle', 'params': [4, 10]},
  {'type': 'round', 'params': [9]},
]

result = 0

for f in FIGURES:
    if f['type'] == 'round':
        (r,) = f['params']
        result += math.pi * r * r
    if f['type'] == 'rectangle':
        a, b = f['params']
        result += a * b

print(result)

def get_square(f):
    if f['type'] == 'round':
        (r,) = f['params']
        return math.pi * r * r
    if f['type'] == 'rectangle':
        a, b = f['params']
        return a * b

print(
    sum(
        [get_square(f) for f in FIGURES]
    )
)
