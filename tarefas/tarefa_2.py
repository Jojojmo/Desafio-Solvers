def exclui_char_repetido(string: str) -> str:
    assert isinstance(string, str), "O parâmetro deve ser uma string!"
    lista_char_unico = []
    for i in string:
        if i not in lista_char_unico:
            lista_char_unico.append(i)
    return(str(''.join(lista_char_unico)))

input = "Hello, World!"

print(exclui_char_repetido(input))
