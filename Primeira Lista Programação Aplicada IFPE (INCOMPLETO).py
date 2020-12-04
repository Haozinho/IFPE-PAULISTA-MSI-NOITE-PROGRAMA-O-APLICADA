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
numero1 = int(input("3.1º) Digite um número qualquer: "))
numero2 = int(input("3.2º) Digite outro número qualquer: "))
numero3 = int(input("3.3º) Digite mais um número qualquer: "))

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
print("A temperatura em Fahrenheit é igual a: ", temperaturaFahrenheit,"ºF")


#Atividade 7
temperaturaFahrenheit = float(input("7º) Digite a temperatura em graus Fahrenheit para saber em Celsius: "))
temperaturaCelsius = 5*(temperaturaFahrenheit - 32)/9
print("A temperatura em Celsius é igual a: ", temperaturaCelsius,"ºC")


#Atividade 8
temperaturaKelvin = float(input("8º) Digite a temperatura em graus Kelvin para saber em Celsius: "))
temperaturaCelsius = temperaturaKelvin - 273.15
print("A temperatura em Celsius é igual a: ", temperaturaCelsius,"ºC")


#Atividade 9
temperaturaCelsius = float(input("9º) Digite a temperatura em graus Celsius para saber em Kelvin: "))
temperaturaKelvin = temperaturaCelsius + 273.15
print("A temperatura em Kelvin é igual a: ", temperaturaKelvin,"K")


#Atividade 10
velocidadeKM = float(input("10º) Digite a velocidade do carro, sabendo que está em quilometros por hora: "))
velocidadeMS = velocidadeKM/3.6
print("A velocidade convertida para metros por segundo é igual a: ",velocidadeMS,"m/s")


#Atividade 11
velocidadeMS = float(input("11º) Digite a velocidade do carro, sabendo que está em metros por segundo: "))
velocidadeKM = velocidadeMS*3.6
print("A velocidade convertida para quilometros por hora é igual a: ",velocidadeKM,"km/h")


#Atividade 12
distanciaMilhas = float(input("12º) Digite uma distancia qualquer em milhas: "))
distanciaKM = 1.61*distanciaMilhas
print("A distancia convertida para quilometros é: ",distanciaKM,"km")


#Atividade 13
distanciaKM = float(input("13º) Digite uma distancia qualquer em quilometros: "))
distanciaMilhas = distanciaKM/1.61
print("A distancia convertida para milhas é: ", distanciaMilhas,"mi")


#Atividade 14
anguloGraus = float(input("14º) Digite um angulo qualquer para ser convertido em radianos: "))
pi = 3.14
anguloRadianos = (anguloGraus*pi)/180
print("O angulo em radianos é: ",anguloRadianos,"rad")


#Atividade 15
anguloRadianos = float(input("15º) Digite um angulo qualquer em radianos para ser convertido em graus: "))
pi = 3.14
anguloGraus = (anguloRadianos*180)/pi
print("O angulo em graus é: ",anguloGraus,"º")


#Atividade 16
comprimentoPolegadas = float(input("16º) Digite o valor do comprimento em polegadas para saber em centímetros: "))
comprimentoCentimetros = comprimentoPolegadas*2.54
print("O comprimento convertido é igual a:",comprimentoPolegadas,"cm")


#Atividade 17
comprimentoCentimetros = float(input("17º) Digite o valor do comprimento em polegadas para saber em centímetros: "))
comprimentoPolegadas = comprimentoCentimetros/2.54
print("O comprimento convertido é igual a:",comprimentoPolegadas,"″")


#Atividade 18
volume = float(input("18º) Digite o valor em m³ para saber o volume em litros: "))
litros = 1000*volume
print("Tem uma capacidade de ",litros,"litros")


#Atividade 19
litros = float(input("19º) Digite quantos litros tem para saber o volume: "))
volume = litros/1000
print("Tem um volume de",volume,"m³")


#Atividade 20
massaKG = float(input("20º) Digite o valor da massa em quilogramas para saber em libras: "))
massaLibras = massaKG/0.45
print("O valor em libras é:",massaLibras,"lb")


#Atividade 21
massaLibras = float(input("21º) Digite o valor da massa em libras para saber em quilogramas: "))
massaKG = massaLibras*0.45
print("O valor em quilogramas é:",massaKG,"Kg")


#Atividade 22
distanciaJardas = float(input("22º) Digite a distancia em jardas: "))
distanciaMetros = distanciaJardas*0.91
print("A convertida para metros e",distanciaMetros,"M")


#Atividade 23
distanciaMetros = float(input("23º) Digite a distancia em metros: "))
distanciaJardas = distanciaMetros/0.91
print("A convertida para jardas e",distanciaJardas,"yd")


#Atividade 24
areaMetrosQuadrados = float(input("24º) Digite o valor da area que será em m²: "))
areaAcres = areaMetrosQuadrados*0.000247
print("A area convertida para acres é",areaAcres,"acres")


#Atividade 25
areaAcres = float(input("25º) Digite o valor da area que será em acres: "))
areaMetrosQuadrados = areaAcres*4048.58
print("A area convertida",areaMetrosQuadrados,"m²")


#Atividade 26
areaMetrosQuadrados = float(input("26º) Digite a área em m²: "))
areaHectares = areaMetrosQuadrados*0.0001
print("A área convertida para hectares é",areaHectares,"ha")


#Atividade 27
areaHectares = float(input("27º) Digite o valor da área em hectares: "))
areaMetrosQuadrados = areaHectares*10000
print("A área em metros quadrados é",areaMetrosQuadrados,"m²")


#Atividade 28
numero1 = float(input("28.1º) Digite um número qualquer: "))
numero2 = float(input("28.2º) Digite outro número qualquer: "))
numero3 = float(input("28.3º) Digite mais um número qualquer: "))
quadradoTres = (numero1**2)+(numero2**2)+(numero3**2)
print("Essa é a soma do quadrado dos números digitados:",quadradoTres)


#Atividade 29
nota1 = float(input("29.1º) Digite a primeira nota: "))
nota2 = float(input("29.2º) Digite a segunda nota: "))
nota3 = float(input("29.3º) Digite a terceira nota: "))
nota4 = float(input("29.4º) Digite a quarta nota: "))
mediaAritmetica = (nota1+nota2+nota3+nota4) / 4
print("A média aritmética é igual a: ",mediaAritmetica)


#Atividade 30
moedaReal = float(input("30.1º) Digite a quantia de dinheiro em reais: "))
cotacaoDolar = float(input("30.2º) Digite o valor da cotação do dolar: "))
moedaDolar = moedaReal * cotacaoDolar
print("Esse é o montante em dolares ",moedaDolar,"$")


#Atividade 31
numeroQualquer = int(input("31º) Digite um numero para saber qual é seu antecessor e seu sucessor: "))
numeroAntecessor = numeroQualquer - 1
numeroSucessor = numeroQualquer + 1
print("O antecessor e sucessor do numero digitado é",numeroAntecessor,numeroSucessor,"respectivivamente")


#Atividade 32
numeroQualquer = int(input("32º) Digite um numero: "))
calculo = ((numeroQualquer*3)+1)+((numeroQualquer*2)-1)
print("Essa é a soma do sucessor de seu triplo com o antecessor de seu dobro",calculo)


#Atividade 33
ladoQuadrado = float(input("33º) Digite o valor de um dos lados do quadrado: "))
area = ladoQuadrado**2
print("A área desse quadrado é de, ",area,"m²")


#Atividade 34
raioCirculo = float(input("34º) Digite o valor do raio do circulo: "))
pi = 3.141592
areaCirculo = pi * (raioCirculo**2)
print("A área do circulo é igual a: ",areaCirculo)


#Atividade 35
catetoA = float(input("35.1º) Qual o valor do cateto oposto: "))
catetoB = float(input("35.2º) Qual o valor do cateto adjacente: "))
hipotenusa = ((catetoA**2) + (catetoB**2))**(1/2)
print("Esse é o valor da hipotenusa: ",hipotenusa)


#Atividade 36
alturaCilindro = float(input("36.1º) Digite a altura do cilindro: "))
raioCilindro = float(input("36.2º) Digite o raio do cilindro: "))
pi = 3.141592
volumeCilindro = pi * (raioCilindro**2) * alturaCilindro
print("O volume do cilindro é de:", volumeCilindro)


#Atividade 37
valorDesconto = float(input("37º) Digite o valor do produto para saber quando fica com o desconto de 12%: "))
valorFinal = valorDesconto * 0.88
print("O valor final com desconto é de R$",valorFinal)


#Atividade 38
salario = float(input("38º) Digite o valor do seu salario: "))
salarioNovo = salario * 1.25
print("Seu salario com o aumento de 25% é igual a R$",salarioNovo)


#Atividade 39
print("39º) Iremos dividir o prêmio de 780.000,00 entre três ganhadores do concurso.")
premioConcurso = 780.000
primeiroLugar = premioConcurso * 0.54
segundoLugar = premioConcurso * 0.68
terceiroLugar = (primeiroLugar+segundoLugar)-premioConcurso
print("O primeiro lugar fica com R$", primeiroLugar)
print("O segundo lugar fica com R$", segundoLugar)
print("O terceiro lugar fica com R$", terceiroLugar)


#Atividade 40
diariaEncanador = int(input("40º) Diga por quantos dias o encanador trabalhou? "))
diaria = 30
SalarioLiquido = diariaEncanador*diaria * 0.92
print("O salario do encanador é de R$ ",SalarioLiquido)


#Atividade 41
horaPaga = float(input("Qual o valor em reais da sua hora trabalhada: "))
horaTrabalhada = int(input("Digite quantas horas você trabalha pro dia: "))
salarioPago = horaPaga*horaTrabalhada * 1.10
print("O seu salario é de R$",salarioPago)


#Atividade 42
salarioBase = float(input("Informe o seu salario: "))
salarioGratificado = salarioBase * 1.05
impostoSalario = salarioGratificado * 0.93
print("Seu salario com a gratificação de 5% mais o desconto de 7% de imposto é de R$",impostoSalario)


#Atividade43
valorProduto = float(input("Digite o valor do produto para saber as opções: "))
valorAvista = valorProduto * 0.90
valorParcelado = valorProduto / 3
comissaoAvista = valorAvista * 0.05
comissaoParcelado = (valorParcelado * 3) * 0.05
print("O valor do produto avista fica de R$",valorAvista)
print("O valor do produto parcelado fica 3 parcelas de R$", valorParcelado)
print("Comissão do vendedor caso a venda seja avista é de R$", comissaoAvista)
print("Comissao do vendedor caso a venda seja parcelada é de R$",comissaoParcelado)


#Atividade 44
alturaDegrau = float(input("Digite a altura do degrau em centimetros: "))
alturaAlcancar = float(input("Digite a altura que deseja alcançar em centimetros: "))
quantidadeDegrau = alturaDegrau/alturaAlcancar
quantidadeInteira = int(quantidadeDegrau)
print("Você deve subir",quantidadeInteira,"degraus")


#Atividade 45
numeroLido = int(input("Digite um numero inteiro de três digitos, de 100 a 999: "))
unidadeNumero = numeroLido // 1 % 10
dezenaNumero = numeroLido // 10 % 10
centenaNumero = numeroLido // 100 % 10
print("A ordem inversa dos numeros é:", unidadeNumero,dezenaNumero,centenaNumero)


#Atividade 46
numeroLido = int(input("Digite um numero inteiro de quatro digitos, de 1000 a 9999: "))
unidadeNumero = numeroLido // 1 % 10
dezenaNumero = numeroLido // 10 % 10
centenaNumero = numeroLido // 100 % 10
milharNumero = numeroLido // 1000 % 10
print("Primeiro numero:",milharNumero)
print("Segundo numero:",centenaNumero)
print("Terceiro numero:",dezenaNumero)
print("Quarto numero:",unidadeNumero)


#Atividade 47
segundos = int(input("Digite a quantidade de segundos a ser convertida: "))
horas = segundos // 3600
segundosRestante = segundos % 3600
minutos = segundosRestante // 60
segundosRestante = segundosRestante % 60
print(horas,"horas",minutos,"minutos",segundosRestante,"segundos")


#Atividade 48 *** OBSERVAÇÃO ***
horaInicio = int(input("Diga que horas são valores de 1 a 12:"))
minutoInicio = int(input("Diga quantos minutos tem a hora valores de 0 a 59: "))
segundoInicio = int(input("Diga quantos segundos tem a hora valores de 0 a 60: "))
duracaoEventoBiologico = 7200
horas = duracaoEventoBiologico / 3600
minutos = (duracaoEventoBiologico-(horas*3600)) // 60
segundos = duracaoEventoBiologico - (horas*3600) - (minutos*60)
horaFinal = horaInicio + horas
minutoFinal = minutoInicio + minutos
segundoFinal = segundoInicio + segundos
print("O evento termina às", int(horaFinal),"horas", int(minutoFinal), "minutos", int(segundoFinal),"segundos")


#Atividade 49





















