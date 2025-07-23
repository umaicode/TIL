temps = [0, 20, 30, 37, 100]


def celsius(temps):
    celsius_temps = list(map(lambda x: x * 9 / 5 + 32, temps))
    return celsius_temps


print(*celsius(temps))

"""
temps = [0, 20, 30, 37, 100]

result = map(lambda c: c * 9 / 5 + 32, temps)
print(*result)
"""
