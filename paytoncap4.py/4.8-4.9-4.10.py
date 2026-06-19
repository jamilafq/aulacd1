#4.7 categoria x preço ,  usando elefe

# categoria = int (input('Digite a categoria do produto:'))
# if categoria ==1:
#     preço= 10
# elif categoria ==2:
#     preço = 18
# elif categoria ==3:
#     preço = 23
# elif categoria ==4:
#     preço = 26
# elif categoria ==5:
#     preço = 31

# else: 
#     print("Categoria inválida,  digite um valor entre 1 e 5!")
#     preço= 0
# print(f"O preço do produto é R$ {preço:6.2f}" )   
# 
# 
# 4.8 leia 2 numeros/ Qual operação vece deseja realiza?
# soma
# subtraçao 
# multiplicaçao e divisao/ exiba o resultado da opreçao solicitada 

# numero1= float(input ('Escolha um numero: ')) 
# numero2= float (input("Escolha outro numero"))
# calculo= int (input("escolha um calculo: 1 soma , 2 subtraçao 3 multiplicaçao , 4 divisao  "))

# if calculo ==1:
#     soma = numero1 +numero2
#     print (f'resultado da {soma}')
# elif calculo ==2:
#     subtraçao = numero1 - numero2
#     print (f'resuldado da subritraça {subtraçao}')
# elif calculo == 3:
#      multiplicaçao = numero1 * numero2
#      print (f'resuldado da subritraça {multiplicaçao}')
        
# elif calculo == 4:
#      divisao  = numero1 / numero2
#      print (f'resuldado da subritraça {divisao }')

# else :
#      print ("opçao invalida  didite para calculo ate o 5")                

# aprovar um emprestimo bancario/qual o valor da compra?/o salario ?/ quantia a ser paga?/ O valor da prestação mensal nao pode ser superior a 30%.  Calcule o valor da prestação como sendo o valor da casa a comprar didido pelo numero de meses a pagar.


# valorCompra= int (input (" Qual o valor da compra"))
# valorSalario = int (input("Qual o valor  do salario "))
# valorPagar = int(input('Qual o valor da prestaçao'))

# if valorPagar > valorSalario :
#     print (f" valor exede o salrio ")
# elif valorPagar >= valorSalario*0.30:
#     print(f"prestação acima do valor permitido ")

# else :
#     valorPagar= valorPagar /12
#     print(F"Valor da prestaçao é de {valorPagar /12}")


#Pergunte a quaqntidade de kwh consumida?/ Tipo de instação ?/ R para residencia;  I indutria/ C comercio. / Calcule o preço a pagar 

# consumo = int(input("Qual a quantidade de kwh consumido"))
# tipoInstalaçao = tipoInstalacao = input("Qual o tipo de instalação (R, I ou C): ").upper()
# if  tipoInstalaçao== "R":
#     valor = consumo * 0.65
#     print(f"Valor a pagar: R$ {valor:.2f}")

# elif tipoInstalaçao == "C":
#     valor = consumo * 0.60
#     print(f"Valor a pagar: R$ {valor:.2f}")

# elif tipoInstalaçao == "I":
#     valor = consumo * 0.55
#     print(f"Valor a pagar: R$ {valor:.2f}")

# else:
#     print("Tipo de instalação inválido!")
