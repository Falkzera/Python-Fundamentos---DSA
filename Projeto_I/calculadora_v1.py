# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

def calculator(operador, num1, num2):   
    if operador == "+":
        resultado = num1 + num2
        print(f'{num1} + {num2} = {resultado}')
    elif operador == "-":
        resultado = num1 - num2
        print(f'{num1} - {num2} = {resultado}')
    elif operador == "*":
        resultado = num1 * num2
        print(f'{num1} * {num2} = {resultado}')
    elif operador == "/":
        try:
            resultado = num1 / num2
            print(f's{num1} / {num2} = {resultado}')
        except ZeroDivisionError:
            print("Divisão por zero, gera uma indeterminação de +- infinito.")
    else:
        print("Você não digitou corretamente.")

pergunta = input('Escolha o Operador mátematico: \n' '[+] ; [-] ; [*] ; [/] ')
try:
    numero_1 = float(input('Escolha o primeiro número: '))
    numero_2 = float(input('Escolha o primeiro segundo: '))
except ValueError:
    print('Digite apenas números')

(calculator(pergunta, numero_1, numero_2))