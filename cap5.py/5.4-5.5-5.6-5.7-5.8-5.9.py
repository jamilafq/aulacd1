# 5.4 Modifique o programa anterior para imprimir de 1 ate o numero digitado pelo usuario,  mas dessa vez apenas numeros pares 
# fim = int(input("Digite o ultimo numero a ser contado: "))

# x = 1

# while x <= fim:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1

#5.5 reescreva o programa anterior para escrever os 10 primeiros multiplo de tres 


# x = 1
# cont=0

# while cont <= 10:
#     if x % 3 == 0:
#         print(x)
#         cont= cont +1
#     x = x + 1


#5.6 altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada :2*4 =1

# x = 2
# cont= 1
# while cont <= 10:
#     print(x,"x ",cont,"=", x* cont)
#     cont = cont+1


# 5.7 modifique o program anterior de forma que o usauário também digite o inicio e fo fim da tabuada .

a = int(input("Digite o primeiro  numero a ser contado: "))
b =int(input("Digite o ultimo numero a ser contado: "))
x = a
while x <= b:
    cont= 1
while cont <= 10:
     print(x,"x ",cont,"=", x* cont)
     cont = cont+1
print("-----------")
x= x+1