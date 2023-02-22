import numpy as np

# Eingabe der Funktionsgleichung als Text
equation = input("Geben Sie die Funktionsgleichung ein (mit 'x' als unabhängige Variable): ")

# Definition der Funktion
def function(x):
    return eval(equation)

# Eingabe der Intervallgrenzen und der Schrittweite
a = float(input("Geben Sie den Startwert a ein: "))
b = float(input("Geben Sie den Endwert b ein: "))
step = float(input("Geben Sie die Schrittweite ein: "))

# Berechnung der Wertetabelle
x_values = np.arange(a, b + step, step)
y_values = function(x_values)

# Ausgabe der Wertetabelle
print("      x  |       f(x)")
print("---------+------------")
for x, y in zip(x_values, y_values):
    print(f"{x:>7.3f}  | {y:>10.3f}")
