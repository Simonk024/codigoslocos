import datetime

def calcular_dias_cumpleaños(nombre, dia_cumpleaños, mes_cumpleaños):
    hoy = datetime.date.today()
    cumpleaños = datetime.date(hoy.year, mes_cumpleaños, dia_cumpleaños)

    if cumpleaños < hoy:
        cumpleaños = datetime.date(hoy.year + 1, mes_cumpleaños, dia_cumpleaños)

    dias_restantes = (cumpleaños - hoy).days

    print(f"Feliz cumpleaños, {nombre}! Te quedan {dias_restantes} días para tu cumpleaños.")

nombre = input("Ingresa tu nombre: ")
dia_cumpleaños = int(input("Ingresa el día de tu cumpleaños (1-31): "))
mes_cumpleaños = int(input("Ingresa el mes de tu cumpleaños (1-12): "))

calcular_dias_cumpleaños(nombre, dia_cumpleaños, mes_cumpleaños)