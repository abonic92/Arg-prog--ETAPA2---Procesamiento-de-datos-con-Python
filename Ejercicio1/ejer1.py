sueldos_por_mes = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]


sueldo_promedio = sum(sueldos_por_mes) / len(sueldos_por_mes)


if sueldo_promedio < 300:
    categoria = "Sueldo bajo"
elif sueldo_promedio >= 300 and sueldo_promedio <= 900:
    categoria = "Sueldo normal"
else:
    categoria = "Sueldo mejor de lo normal"


print(f"El sueldo promedio de Juan es: {sueldo_promedio:.2f} dólares")
print(f"Categoría de sueldo: {categoria}")