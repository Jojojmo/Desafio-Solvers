# Sobre o projeto
<p>Este repositório é destinado ao Desafio de Código para o processo seletivo de estagiários da PWC. Explicações sobre funcionamento, navegação dentro dos arquivos e outras informações pertinentes serão aprofundadas neste README.</p>

## Linguagem escolhida
<p>A linguagem para criação deste repositório foi o Python, para tomar esta escolha, foi considerado a familiaridade com a linguagem, pelo uso em meu dia a dia e nas monitorias de algoritmo que aplico, ter várias ferramentas para manipulação de Strings já integras, ser uma linguagem de alto nível fácil de compreender.  </p>

## Arquivos
Dentro deste repositório temos:
- Pasta “imgs”
	- Contém as imagens das tarefas a serem cumpridas;
- Pasta “Tarefas”
	- Possui a existência do arquivo __init__.py para o diretório ser compreendido como um pacote pelo Python;
	- Contém 5 arquivos .py respectivos a cada tarefa, vale ressaltar que cada arquivo pode ser iniciado de maneira independente, tendo os próprios exemplos contidos neles, contudo, se certifique de estar utilizando uma IDE para rodar ele ou outra ferramenta que não feche o terminal de comandos assim que finalizado;
- .gitattributes & .gitignore
	- São arquivos próprios do Github para a criação desse repositório;
- logo.txt
	- imagem feita com texto utilizando ASCII;
- objetivos.md
	- Arquivo do tipo Markdown para organização e check de To-do list;
- main.py
	- Arquivo principal, reúne todas as tarefas e dispõe de um menu de opções interno, para que você escolha qual desafio vai utilizar.

## Tarefas do Desafio
<small>Obs: Todos os arquivos desta pasta possuem a linha de código <code>if __name__ == "__main__":</code> Realizando os casos passados dentro desafio, esta condicional só é acionada quando você executa o arquivo separadamente, para que não ocorra sobreposições durante o uso no arquivo main.py</small>

### Tarefa 1
<p>Esta tarefa é responsável pela inversão de palavras dadas pelo usuário, foi criado uma função onde se cria uma lista temporária com o comando <code>.split()</code>, já para retornar a frase como String novamente, se utiliza da função <code>.join()</code> e do fatiamento de strings <code>[::-1]</code>, o qual inverte a String ou lista. No mesmo exemplo, caso não seja passado uma String para a função, ou ela tenha tamanho zero, é retornado o aviso “A string está vazia!”.</p>

```
def inversor_str(string:str) -> str:
    assert isinstance(string, str), "O parâmetro deve ser uma string!"
    if len(string) == 0:
        return 'A string está vazia!'
    saco_de_palavras = string.split()
    return str(' '.join(saco_de_palavras[::-1]))  


if __name__ == "__main__":
    input = "Hello, World! OpenAI is amazing"

    print(inversor_str(input))
```

### Tarefa 2
<p>Consiste na criação da função <code>exclui_char_repetido()</code>, que ao se passar o parâmetro de uma String, vai retornar apenas os caracteres não repetido, para que isto ocorra, é feito um laço com o comando <code>for</code> onde se percorre toda a String, em cada interação, é feita uma verificação se o caractere já está contido na lista interna da função, caso não esteja, é feita a sua inserção. Após o loop acabar, é retornado uma String utilizando a função <code>.join()</code> com o parâmetro sendo esta lista que foi formada.</p>

```
def exclui_char_repetido(string: str) -> str:
    assert isinstance(string, str), "O parâmetro deve ser uma string!"
    lista_char_unico = []
    for i in string:
        if i not in lista_char_unico:
            lista_char_unico.append(i)
    return(str(''.join(lista_char_unico)))


if __name__ == "__main__":
    input = "Hello, World!"

    print(exclui_char_repetido(input))

```

### Tarefa 3 
<p>Na tarefa 3, era preciso localizar a maior sub_string que é um palíndromo de uma string passada como parâmetro, para que isso ocorra, é feito um tratamento que deixa todas as letras em maiúsculas e retira os espaços entre os caracteres. Ao fazer este tratamento, é gerado uma cópia invertida da string, esta variável tem como nome <code>sub_string.</code></p>
<p>Ao se fazer o laço <code>for</code> com a quantidade de interações igual ao tamanho da String, é sempre verificado se as variáveis são iguais, caso isso não aconteça, ainda na mesma interação, é feito o fatiamento da <code>sub_string</code>, removendo seu primeiro caractere e a remoção do último caractere da variável <code>string</code>, assim localizando a maior <code>sub_string</code> palíndromo da original.</p>

### Tarefa 4
<p>Dentro da Tarefa 4 existem duas funções, sendo elas: <code>esp_frases()</code> que verifica se existe espaços entre caracteres específicos e <code>cap_frases()</code> que deixa A primeira letra maiúscula de cada frase. </p>
<p>Na função <code>esp_frases()</code>, existe a seguinte lista: <code>['.', '?', '!', ':', ",", ";"]</code>, por regras gramaticais, todos estes caracteres precisam de um espaço depois deles, ou seja, o próximo caractere dos itens desta lista precisam ser o espaço. Em seguida é criado a variável <code>nova_string</code>, que por hora está vazia e a variável <code>string</code>, que foi passada como parâmetro, sofre um tratamento com a função <code>.strip()</code>.</p>
<p>No próximo bloco de código, é feito um laço <code>for</code> com a mesma quantidade de interações  ao tamanho da string, em cada interação, é adicionado um caractere na variável <code>nova_string</code>. Na mesma interação, é feito um comando <code>if</code> com dois operadores <code>and</code>, ou seja, para que ocorra, é necessário que os três testes lógicos sejam verdade, são eles: 1° o caractere da string desta interação tem que estar contido na lista chamada <code>espaço_char</code>, 2° a variável i da interação mais o valor de 1 (i+1) não pode ser maior que o tamanho da string, para que não ocorre o erro de <code>“the index is out of range”</code>, causado por um incide que não existe na estrutura original e não consegue ser encontrado pelo Python, 3° o índice seguinte (i+1) é diferente do caractere de espaço. Em caso do <code>if</code> ser atendido, é inserido um espaço dentro da <code>nova_string</code>, por fim é retornado esta variável ao final da função.</p>
<p>Dentro da função <code>cap_frases()</code> existe a lista denominada separadores, que são caracteres que gramaticalmente seguem a regra da palavra posterior começar com a letra maiúscula, em seguida, é gerada a variável <code>nova_string</code> desta função, que utiliza a <code>esp_frases()</code>. Dentro do seu laço for, é utilizado uma logica parecida com a função <code>esp_frases()</code>, já que é verificado se o caractere corresponde a um valor interno da lista, contudo, a formatação ocorre de maneira diferente, fazendo um fatiamento da <code>nova_string</code> que monta uma nova no final com os caracteres do início de cada frase em maiúsculo. </p> 

```
def esp_frases(string: str) -> str:
    assert isinstance(string, str), "O parâmetro deve ser uma string!"
    espaco_char = ['.', '?', '!', ':', ",", ";"]
    nova_string = ""
    string = string.strip()
    for i in range(len(string)):
        nova_string += string[i]
        if string[i] in espaco_char and i + 1 < len(string) and string[i+1] != ' ':
            nova_string += ' '
    return nova_string



def cap_frases(string) -> str:
    assert isinstance(string, str), "O parâmetro deve ser uma string!"
    separadores = ['.', '?', '!', ':']
    nova_string = esp_frases(string)
    nova_string = nova_string[0].upper() + nova_string[1:]
    for char in range(len(nova_string) - 1):
        if nova_string[char] in separadores:
            nova_string = nova_string[:char + 2] + nova_string[char + 2].upper() + nova_string[char +3:]
    return nova_string

if __name__ == "__main__":
    input = "hello. how are you? i'm fine, thank you."

    print(cap_frases(input))
```
### Tarefa 5
<p>Neste arquivo, existem duas funções contidas nele, sendo elas: <code>anagrama_palindromo()</code> e anagrama_result_formatado(), tendo como dependência e <code>import</code> necessário a <code>biblioteca itertools</code>.</p>
<p>É importante ressaltar que a  função <code>anagrama_palindromo()</code>  se baseia em se baseia em permutação simples, tendo um crescimento de ordem fatorial, o qual exige um grande poder de processamento e tempo conforme maior for o tamanho da String, para que isto não ocorra, foi imposto um limite interno de 8 para a largura da string, sendo o desafio propôs uma string de tamanho 7. Lembrando que para outros exemplos com strings de tamanho maior, é recomendável encontrar outros métodos de análise combinatória para criação de anagramas.</p>
<p>Ressalvas dadas, o código se utiliza da função <code>permutations()</code> que retorna um objeto contendo listas de todos os anagramas possíveis, como eles estão contidos e em um formato diferente do desejado, é utilizado um laço <code>for</code> para fazer a interação de item a item do objeto, além de armazenar os valores não repetidos em uma variável chamada de <code>lista_anagrama</code>. Com esta nova lista criada, é feito a interação para encontrar anagramas palíndromos, ao achar um, o dicionário <code>dict_anagrama</code> recebe os valores  de +1 na chave <code>“count”</code>, <code>True</code> dentro de <code>“resultados”</code> e armazena o palíndromo em uma lista também contido no dicionário. Ao terminar o laço, é impressa o resultado caso o parâmetro <code>print_resul</code> seja verdadeiro.</p>
<p>Na execução <code>anagrama_result_formatado()</code>, será utilizado a função recém explicada, imprimindo a resposta se existe um anagrama palíndromo e quais são. Lembrando que ambas as funções são limitadas e tem uma mensagem caso o tamanho string a ser passada seja maior que 8.</p>

```
from itertools import permutations

def anagrama_palindromo(string:str,print_result:bool=True) -> dict:
    assert isinstance(string, str), "O parâmetro 'string' deve ser uma string!"
    assert isinstance(print_result, bool), "O parâmetro 'print_result' deve ser True ou False!"

    if len(string) > 8:
        print(f"Este código é baseado em permutação simples!\nStrings grandes possuem crescimento fatorial e um grande processamento")
        return None
    permutacoes = permutations(string)
    lista_anagrama = []
    dict_anagrama = {"count":0,"resultado": False,"palindromos":[]}
    for permutacao in permutacoes:
        junto = "".join(permutacao)
        if junto not in lista_anagrama:
            lista_anagrama.append(junto)

    for anagrama in lista_anagrama:
        if anagrama == anagrama[::-1]:
            dict_anagrama["count"] += 1
            dict_anagrama["resultado"] = True
            dict_anagrama["palindromos"].append(anagrama)
    if print_result == True:
      print(dict_anagrama['resultado'])
    return dict_anagrama

def anagrama_result_formatado(string:str) -> str:
    assert isinstance(string, str), "O parâmetro deve ser uma string!"
    anagramas = anagrama_palindromo(string,False)
    if anagramas == None:
        return 'String longa demais, valor não encontrado'
    if anagramas["resultado"] == False:
        return f"A String {string}, não possui anagramas palindromos"
    else:
        return f"A String '{string}' tem {anagramas['count']} anagramas palindromos, são eles:\n{anagramas['palindromos']}"



if __name__ == "__main__":
  input = "rececar"
  anagrama_palindromo(input)
```
## Main
<p>
    No arquivo <code>main.py</code> há a importação do pacote dos cinco desafios, assim como o uso da biblioteca time e função <code>sleep()</code>.  O dicionário <code>dicionario_funcoes</code> armazena as chaves como opção do menu logo a seguir, tendo seus valores outros dicionários, que possuem a função que o usuário irá escolher, seguidamente pelos textos que aparecem cada vez que é feita a escolha.
    Temos como função recursiva <code>entrada_opcoes()</code>, que é sempre chamada novamente quando o usuário escolhe uma opção não existente e retorna o valor quando estiver correto. Contido no <code>while True</code> ou loop infinito, é mostrado as 7 opções, sendo elas:
</p>

- [1] Inversor de palavras nas Strings
- [2] Excluir caracteres repetidos
- [3] Verificar palindromo
- [4] Letras maiúsculas no início das frases
- [5] Verificar anagrama palindromo
- [6] Contato
- [7] Sair

<p>Os números de 1 até 5 realizam a execução da função correspondente, já a número 6 imprime o Github e Linkedin como contato. Ao digitar o número 7, o loop infinito se quebra, desta maneira, encerrando o código, caso contrário, o loop se reinicia.</p> 

```
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
```

## Contato
jmo.nick@outlook.com <br>
[linkedin](https://www.linkedin.com/in/joão-matheus-oliveira-107b98179/) <br>
[Github](https://github.com/jojojmo)
