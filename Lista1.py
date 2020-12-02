'''

IFPE CAMPUS PAULISTA - MSI NOITE 2º PERÍODO
ALUNO: Pedro Hao Tavares
INSTAGRAM: @sr.hao

'''


#Atividade 1
numeroInteiro = int(input("1º) Digite um numero que faça parte do conjunto dos inteiros: "))
print("Esse foi o numero inteiro que você digitou:",numeroInteiro)


#Atividade 2
numeroReal = float(input("2º) Digite um numero que faça parte do conjunto dos reais: "))
print("Esse foi o numero real que você digitou:", numeroReal)


#Atividade 3
numero1 = int(input("3.1º) Digite um numero qualquer: "))
numero2 = int(input("3.2º) Digite outro numero qualquer: "))
numero3 = int(input("3.3º) Digite mais um numero qualquer: "))

soma = numero1+numero2+numero3 # Não preciso criar uma variavel soma para guardar o valor da soma se eu não for usar ela posteriormente posso simplesmente jogar a seguinte fução:
#print("A soma dos numeros digitados é igual a:", numero1+numero2+numero3)
print("A soma dos numeros digitados é igual a:", soma)


#Atividade 4
numeroRealQuadrado = float(input("4º) Digite um número qualquer que faça parte do conjunto dos reais: "))
print("O quadrado do número digitado é igual a:", numeroRealQuadrado**2) # Ao contrario da questão anterior eu posso criar uma váriavel para salvar o valor da potência da seguinte maneira:
#potencia = NumeroRealQuadrado**2
#print("O quadrado do numero digitado é igual a:", potencia)


#Atividade 5
numeroQuintaParte = float(input("5º) Digite um número qualquer pertencente ao conjunto dos reais: "))
print("A quinta parte desse número é: ",numeroQuintaParte* 1/5)


#Atividade 6
temperaturaCelsius = float(input("6º) Digite a temperatura em graus Celsius para saber em Fahrenheit: "))
temperaturaFahrenheit = temperaturaCelsius*(9/5)+32
print("A temperatura em Fahrenheit é igual a: ", temperaturaFahrenheit)


#Atividade 7
temperaturaFahrenheit = float(input("7º) Digite a temperatura em graus Fahrenheit para saber em Celsius: "))
temperaturaCelsius = 5*(temperaturaFahrenheit - 32)/9
print("A temperatura em Celsius é igual a: ", temperaturaCelsius)


#Atividade 8
temperaturaKelvin = float(input("8º) Digite a temperatura em graus Kelvin para saber em Celsius: "))
temperaturaCelsius = temperaturaKelvin - 273.15
print("A temperatura em Celsius é igual a: ", temperaturaCelsius)


#Atividade 9
temperaturaCelsius = float(input("9º) Digite a temperatura em graus Celsius para saber em Kelvin: "))
temperaturaKelvin = temperaturaCelsius + 273.15
print("A temperatura em Kelvin é igual a: ", temperaturaKelvin)


#Atividade 10
velocidadeKM = float(input("10º) Digite a velocidade do carro, sabendo que está em quilometros por hora: "))
velocidadeMS = velocidadeKM/3.6
print("A velocidade convertida para metros por segundo é igual a: ", velocidadeMS)