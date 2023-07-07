
 ##############################################################
#                                                              #
#   888888                                 888b     d888       #
#     "88b          88888888               8888b   d8888       #
#      888                                 88888b.d88888       #
#      888  .d88b.   8888b.   .d88b.       888Y88888P888       #
#      888 d88""88b     "88b d88""88b      888 Y888P 888       #
#      888 888  888 .d888888 888  888      888  Y8P  888       #
#      88P Y88..88P 888  888 Y88..88P      888   "   888 d8b   #
#      888  "Y88P"  "Y888888  "Y88P"       888       888 Y8P   #
#    .d88P                                                     #
#  .d88P"                                                      #
# 888P"                                                        #
#                                                             #
 ############################################################




from time import sleep

from tarefas import tarefa_1, tarefa_2, tarefa_3, tarefa_4, tarefa_5


dicionario_funcoes =  { '1':{'função':tarefa_1.inversor_str,'texto': 'Digite a String para inverter as palavras'},
                        '2':{'função':tarefa_2.exclui_char_repetido,'texto': 'Digite a String que terá seus caracteres repetidos excluidos'},
                        '3':{'função':tarefa_3.verifica_palindromo,'texto':'Digite uma String, será vereficado sua substring mais longa'},
                        '4':{'função':tarefa_4.cap_frases,'texto':'Escreva uma string, será colocado letras maiúsculas no início das frases'},
                        '5':{'função':tarefa_5.anagrama_result_formatado,'texto':'Escreva uma string, será verificado a existência de anagramas palindromos'}}

def entrada_opcoes():
    entrada = input("R: ")
    if entrada not in ['1', '2', '3', '4', '5', '6', '7']:
        print("A opção está incorreta ou não existe, por favor, digite novamente")
        print("Ps: Digite o número correspondente")
        return entrada_opcoes()
    else:
        return entrada


with open("logo.txt","r") as logo:
    solvers = logo.read()

print(solvers)
sleep(2)


while True:
    print("""O que você pretende utilizar:
[1] Inversor de palavras nas Strings
[2] Excluir caracteres repetidos
[3] Verificar palindromo
[4] Letras maiúsculas no início das frases
[5] Verificar anagrama palindromo
[6] Contato
[7] Sair
Ps: Digite o número correspodente""")
    entrada = entrada_opcoes()
    if entrada in ['1','2','3','4','5']:
        print('=-='*25)
        print(dicionario_funcoes[entrada]['texto'])
        print('=-='*25)
        input_funcao = str(input("R: "))
        print('=-='*25)
        print(dicionario_funcoes[entrada]['função'](input_funcao))
        print('=-='*25)
        sleep(1)
    if entrada == "6":
        print('=-='*25)
        print("Linkedin:\nhttps://www.linkedin.com/in/joão-matheus-oliveira-107b98179/")
        print("Github\nhttps://github.com/jojojmo")
        print('=-='*25)
        sleep(2)
    if entrada == "7":
        break

        