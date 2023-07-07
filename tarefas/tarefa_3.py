
def verifica_palindromo(string:str) -> str:
    assert isinstance(string, str), "O parâmetro deve ser uma string!"
    string = string.lower().replace(" ","")
    sub_string = string[::-1]
    for i in range(len(string)):
        if string == sub_string:
            return sub_string
        else:
            sub_string = sub_string[1:]
            string = string[:-1]

if __name__ == "__main__":
    input = 'babad'

    print(verifica_palindromo(input))

