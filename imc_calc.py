# imc = peso / altura ^2

print("Vamos calcular seu IMC")
peso = input("Primeiro, digite seu peso: ")
altura = input("Agora digite sua altura em centimetros: ")

imc = round((int(peso) / int(altura) ** 2) *10000, 2)

print("Seu IMC é: ", imc)

if imc >= 18.5 and imc <= 24.9:
    print("Seu peso está normal, parabéns.")
elif imc <= 29.9:
    print("Você está com sobrepeso, cuidado.")
elif imc <= 34.9:
    print("Você está com Obesidade de grau 1, cuidado.")
elif imc <= 39.9:
    print("Você está com Obesidade de grau 2, cuidado.")
else:
    print("Você está com obesidade de grau 3, por favor, procure um médico.")
