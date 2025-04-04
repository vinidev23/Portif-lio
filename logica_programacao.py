#Imprimir Tipos de Variáveis
# Crie variáveis de diferentes tipos (inteiro, float, string, booleano) e imprima seus tipos usando a função type()
idade = 18
print(type(idade))

velocidade = 80.5
print(type(velocidade))

nome = "vinicius"
print(type(nome))

verdade = True
mentira = False
print(type(verdade))


# Conversão de Tipos
# Escreva um programa que converta uma string para um número inteiro e um número float para uma string.

string_para_int = "123"
numero_inteiro = int(string_para_int)
print(numero_inteiro)

float_para_string = 47.34
numero_flutuante = str(float_para_string)
print("String do número float:", numero_flutuante)


#Operações com Inteiros e Floats
#Crie um programa que peça dois números ao usuário e imprima a soma, subtração,multiplicação e divisão desses número

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

# Soma
soma = numero1+numero2
print("A soma é: ", soma)

# Subtração
subtracao = numero1-numero2
print("A subtração é: ", subtracao)

# Divisão
divisao = numero1/numero2
print("A divisão é: ", divisao)

# Multiplicação
multiplicacao = numero1*numero2
print("A multiplicação é: ", multiplicacao)

# Módulo
resultado = numero1 % numero2
print(resultado)

# Manipulação de Strings
# Peça ao usuário para inserir uma frase e imprima a frase em maiúsculas, minúsculas e com a primeira letra de cada palavra em maiúscula.
frase = input("Digite uma frase: ")
print("MAIÚSCULAS", frase.upper())
print("MINÚSCULAS", frase.lower())
print("TÍTULO", frase.title())


# Booleanos e Operadores Lógicos
#Escreva um programa que verifique se dois números inseridos pelo usuário são ambos positivos.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
if num1 > 0 and num2 > 0:
 print("Os dois números são Positivos")
elif num1 > 0 and num2 < 0:
 print("Somente o primeiro número é Positivo")
elif num1 < 0 and num2 > 0:
 print("Somente o segundo número é Positivo")
else:
 print("Ambos números são negativos")

# Entrada de Dados
# Crie um programa que peça ao usuário para inserir seu nome e idade
# Depois, imprima uma mensagem com essas informações

nome = input("Inserir nome: ")
idade_inserir = int(input("Inserir idade: "))
print("Nome: ", nome)
print("Idade: ", idade_inserir)

#Operações com Strings
#Peça ao usuário para inserir uma palavra e imprima o número de caracteres dessa palavra.

palavra = input("Digite uma palavra: ")
print(f"A palavra '{palavra} contém {len(palavra)} caractéres")


# Formatação de Strings
# Escreva um programa que peça ao usuário para inserir seu nome e idade
# Depois,imprima uma mensagem formatada usando f-strings

nome_x = input("Inserir nome: ")
idade_inserir_x = int(input("Inserir idade: "))
print(f"Olá {nome_x}, sua idade é de {idade_inserir_x} anos")

#Listas Básicas
#Crie uma lista com cinco frutas e imprima cada fruta

frutas = ["banana", "maçã", "uva", "abacate", "morango"]
print(frutas)

#Manipulação de Listas
#Adicione e remova elementos de uma lista e imprima a lista resultante

# Criando uma lista inicial
minhaLista = ["Maçã", "Morango", "Abacaxi"]
print("Sua lista de frutas é: ", minhaLista)

# Adicionando elementos à lista
minhaLista.append("Melancia")
print("Depois de adicionar melancia", minhaLista)
minhaLista.insert(1, "Uva")
print("Depois de adicionar Uva na posição 1", minhaLista)

# Removendo elementos da lista
minhaLista.remove("Morango")
print("Depois de remover morango da sua lista: ", minhaLista)
removido = minhaLista.pop(2)
print(f"Depois de remover o elemento na posição 2 ('{removido}')", minhaLista)

# Imprimindo a lista resultante
print("Sua lista resultante é: ", minhaLista)


# Tuplas
#Crie uma tupla com cinco elementos e imprima cada elemento.
cores = ("Preto", "Branco", "Azul", "Bege", "Vermelho")
for cor in cores:
 print(cor)


# Dicionário
# Crie um dicionário com três pares de chave-valor (por exemplo, nome e idade) e imprima cada chave e valor
alunos = {
 "Vini": 18,
 "Julia": 16,
 "Mariana": 8
}
for nome, idade in alunos.items():
 print(f"Nome: {nome}, Idade: {idade}")


# Sets
# Crie um set com cinco elementos e imprima cada elemento
valores = {13, 34, 56, 76, 45}
print(valores)


# Operações com Dicionários
# Adicione e remova elementos de um dicionário e imprima o dicionário resultante
jogadores = {
    "Neymar":33,
    "Messi":37,
    "Cristiano":40
}
for jogador, anos in jogadores.items():
    print(f"Nome : {jogador}, Idade:  {anos}")

jogadores["Champions"] = 9
print(jogadores)

del jogadores["Messi"]
print(jogadores)


# Operações com Sets
# Adicione e remova elementos de um set e imprima o set resultante
profissoes = {"engenheiro", "dev", "médico"}
print(profissoes)
profissoes.add("eletricista")
print(profissoes)
profissoes.remove("engenheiro")
print(profissoes)


# Operadores de Comparação
# Escreva um programa que compare dois números e imprima se eles são iguais, diferentes, maior ou menor.
valor1 = input("Digite um número: ")
valor2 = input("Digite outro número: ")
if valor1 == valor2:
    print("Os dois valores são iguais")
else:
    print("Os dois valores são diferentes")
if valor1 > valor2:
    print("O primeiro número é maior")
if valor2 > valor1:
    print("O segundo número é maior")

# Operadores de Atribuição
# Escreva um programa que utilize operadores de atribuição para modificar o valor de uma variável.
vaLor = 10
vaLor += 5
vaLor -= 7
vaLor *= 5
vaLor /= 8
vaLor %= 4
print("O valor final da varíavel é: ", vaLor)


# Operadores de Identidade
# Crie um programa que verifique se duas variáveis apontam para o mesmo objeto na memória
a = [1, 2, 3]
b = a

c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)

print("Endereço de memória a: ", id(a))
print("Endereço de memória b: ", id(b))
print("Endereço de memória c:", id(c))

# Operadores de Associação
# Escreva um programa que verifique se um elemento está presente em uma lista.
listen = ["program", "variable", "print"]
elemento = "variable"

if elemento in listen:
    print(f"O elemento {elemento} está presente na lista")
else:
    print(f"O elemento {elemento} não está presente na lista")

# Verificar se não está na lista
lista = ["Banana", "Uva", "Morango"]
element = "Abacaxi"

if element not in lista:
   print(f"O elemento {element} não está presente na lista")
else:
    print(f"O elemento {element} está presente na lista")


# Chute o número
import random
valorAleatorio = random.randint(1, 100)

acertou = False

while acertou == False:
 chute = int(input("Chute um número de 1 a 100: "))
 if chute > valorAleatorio:
     print("Você chutou muito alto! Chute mais baixo")
 elif chute < valorAleatorio:
     print("Você chutou muito baixo! Chute mais alto")
 elif chute == valorAleatorio:
     acertou = True
     print("Parabéns! Você acertou.")
