poblacion = {
    'anio': [2018, 2019, 2020, 2021, 2022],
    'Bogotá': [7830, 7900, 7970, 8050, 8120],
    'Antioquia': [6420, 6480, 6535, 6590, 6645],
    'Valle del Cauca': [4840, 4900, 4955, 5020, 5090]
}

def calcular_tasa_crecimiento(p_inicial, p_final, n):
    tasa = (p_final / p_inicial) ** (1 / n) - 1
    return tasa

n = 2022 - 2018

tasa_bogota = calcular_tasa_crecimiento(7830, 8120, n)
tasa_antioquia = calcular_tasa_crecimiento(6420, 6645, n)
tasa_valle = calcular_tasa_crecimiento(4840, 5090, n)

print(f"Tasa Bogotá: {tasa_bogota:.4f}")
print(f"Tasa Antioquia: {tasa_antioquia:.4f}")
print(f"Tasa Valle del Cauca: {tasa_valle:.4f}")

def proyectar_poblacion(p_actual, tasa, años):
    proyeccion = []
    for i in range(1, años + 1):
        poblacion_futura = p_actual * ((1 + tasa) ** i)
        proyeccion.append(round(poblacion_futura, 2))
    return proyeccion

años_futuros = [2023, 2024, 2025, 2026, 2027]

proy_bogota = proyectar_poblacion(8120, tasa_bogota, 5)
proy_antioquia = proyectar_poblacion(6645, tasa_antioquia, 5)
proy_valle = proyectar_poblacion(5090, tasa_valle, 5)

import matplotlib.pyplot as grafyqueishon

años_totales = poblacion['anio'] + años_futuros
poblacion_bogota = poblacion['Bogotá'] + proy_bogota
poblacion_antioquia = poblacion['Antioquia'] + proy_antioquia
poblacion_valle = poblacion['Valle del Cauca'] + proy_valle

grafyqueishon.figure(figsize=(10, 6))
grafyqueishon.plot(años_totales, poblacion_bogota, marker='o', label='Bogotá')
grafyqueishon.plot(años_totales, poblacion_antioquia, marker='s', label='Antioquia')
grafyqueishon.plot(años_totales, poblacion_valle, marker='^', label='Valle del Cauca')

grafyqueishon.title("Proyección de Población 2023-2027")
grafyqueishon.xlabel("anio")
grafyqueishon.ylabel("Población (miles)")
grafyqueishon.grid(True)
grafyqueishon.legend()
grafyqueishon.tight_layout()
grafyqueishon.show()