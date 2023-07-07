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

