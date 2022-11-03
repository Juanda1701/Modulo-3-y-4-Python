from datetime import datetime

Mi_dato = datetime(2020, 11, 4, 14, 53)

print(Mi_dato.strftime("%Y/%m/%d  %H:%M:%S"))
print(Mi_dato.strftime("%Y/%m/%d  %H:%M:%S %p"))
print(Mi_dato.strftime("%a, %Y %b %d"))
print(Mi_dato.strftime("%A, %Y %B %d"))
print(Mi_dato.strftime("Dia de la semana : %w"))
print(Mi_dato.strftime("Día del año: %j"))
print(Mi_dato.strftime("Numero de semana en el año: %W"))
