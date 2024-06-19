# Este é um programa que converte bases numéricas. Com um menu onde o usuário escolhe a base origem (binário, octal, decimal, hexadecimal)e a base de destino (binário, octal, decimal, hexadecimal). Após entrar com as configurações, o usuário deve digitar o número a ser convertido e o programa imprime o valor na base escolhida.

def binário_decimal(binário):
    return int(binário, 2)

def octal_decimal(octal):
    return int(octal, 8)

def hexadecimal_decimal(hexadecimal):
    return int(hexadecimal, 16)

# ------ #

def decimal_binário(decimal):
    return bin(decimal)[2:]

def decimal_octal(decimal):
    return oct(decimal)[2:]

def decimal_hexadecimal(decimal):
    return hex(decimal)[2:]

print("Programa de Conversão")
def base():
    while True:
        print('''Base de origem:
        [1] Binário
        [2] Octal
        [3] Hexadecimal
        [4] Decimal''')
        opção_user = input("Digite a opcão: ")

        print('''Base para conversão:
        [1] Binário
        [2] Octal
        [3] Hexadecimal
        [4] Decimal''')
        opção = input("Digite a opcão: ")
        num = input("Número a ser convertido: ")

        if opção_user == "1":
            if all(bit == '0' or bit == '1' for bit in num):
                decimal = binário_decimal(num)
            else:
                print("Número binário inválido, tente novamente.")
                continue

        elif opção_user == "2":
            if all("0"<= digito <= "7" for digito in num):
                decimal = octal_decimal(num)
            else:
                print("Número octal inválido, tente novamente.")
                continue

        elif opção_user == "3":
            if all(digito in "0123456789abcdefABCDEF" for digito in num):
                decimal = hexadecimal_decimal(num)
            else:
                print("Número hexadecimal inválido, tente novamente.")
                continue

        elif opção_user == "4":
            if num.digito():
                decimal = int(num)
            else:
                print("Número decimal inválido, tente novamente.")
                continue

        else:
            print("Por favor escolha uma opção válida!")
            continue

        if opção == "1":
            resultado = decimal_binário(decimal)
        elif opção == "2":
            resultado = decimal_octal(decimal)
        elif opção == "3":
            resultado = decimal
        elif opção == "4":
            resultado = decimal_hexadecimal(decimal)
        else:
            print("Por favor escolha uma opção válida!")
            continue
        
        print("O número {} na base {} equivale a {} na base {}." .format(num, opção_user, resultado, opção))
        break

base()