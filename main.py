# 1 - import/ biblioteca

# 2 - classe

# 3 - metodos e funções
# def = definição

def print_hi(name):
    print(f'Oi, {name}')

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_quadrado(lado):
    return lado ** 2
def contagem_progressiva(fim):
    for numero in range(fim):#repetir o bloco de zero ate o fim
        print(numero)

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        # contador = numero + 1
        # print(f'{contador} - {nome}')
        if numero < 9:
            print(f'00{numero + 1} - {nome}')

        elif numero < 99:
            print(f'0{numero + 1} - {nome}')

        else:
            print(numero +1, '-', nome)




# estrutura de identificação/ execução de script
if __name__ == '__main__':
    print_hi('Gustavo')
    # chamar a função de calculo da area do retangulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'A área do retangulo é de {resultado} m')

    # chamar a função de calculo area do quadrado
    resultado = calcular_area_quadrado(5)
    print(f'A área do quadrado e de: {resultado} mts')

    # executar uma contagem progressiva
    contagem_progressiva(10)

    apoiar_candidato('fake', 100)