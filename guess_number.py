""" * Jogo de adivinhação numérica 
    * Usando o módulo random
    * Lendo documentação -random- Generate pseudo random numbers.


 """
import random

print("Seja muito bem vindo ao Guess Number Game!")
choice_number = input("Digite o número teto do desafio: ")     # Número dentro do "input" se torna uma string (Texto), para que isso não aconteça, utilizar o "int".

if choice_number.isdigit():    # ".isdigt" verifica se é um número, se sim retornará True, se não retornará False.
    choice_number = int(choice_number)
else:
    print("Erro: valor informado não é númerico. Favor execute novamente e informe um número!")
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0 

while True:          # "while"= (enquanto): Enquanto for verdadeiro, continue.
    answer_user = input("Adivinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
       print("Erro: valor informado não é um númerico. Favor informe um número: ")
       continue
    
    n_choices = n_choices + 1

    if answer_user == random_number:
        print("Acertou!")
        break   # Quebra o loop!
    elif answer_user > random_number:
        print("Chutou alto, o número randomico é menor que isso... ")
    else:
        print("Chutou baixo, o número randomico é maior que isso... ")

print("Número de tentativas: " + str(n_choices))
