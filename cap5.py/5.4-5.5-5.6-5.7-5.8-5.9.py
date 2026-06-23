# 5.4 Modifique o programa anterior para imprimir de 1 ate o numero digitado pelo usuario,  mas dessa vez apenas numeros pares 
fim = int(input("Digite o ultimo numero a ser contado: "))

x = 1

while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1