print("Bienvenido a la calculadora de IMC :)")
peso = float(input("Ingresa tu peso actual"))
altura = float(input("Ingresa tu altura actual"))
edad = int(input("Ingresa tu edad actual"))
imc = peso / altura ** 2
print("Tu IMC actual es de {}".format(imc))
if imc >= 18.5 and imc <= 25.0:
    print("Tu imc es normal")
elif imc >= 25 and imc <= 30 :
    print("Estas en sobrepeso")
elif imc >= 30 and imc <= 35:
    print("Tienes obesidad grado 1")
elif imc >= 35 and imc <= 40:
    print("Tienes obesidad grado 2")

