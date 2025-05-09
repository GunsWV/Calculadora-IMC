#1.Receber a variável peso  [float]
#2. Receber a variável altura [float]
#3. Realizar o calculo do IMC = (peso / altura²) 
#4. Imrprimir o resultado do IMC
 
#Operações usadas: divisão e potência (**)

Peso = float(input("Digite o peso:"))

Altura = float(input("Digite a altura:"))

imc = Peso / (Altura ** 2)
print(f'o seu imc é: {imc}')

