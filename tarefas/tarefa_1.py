def inversor_str(string):
    if len(string) == 0:
        return 'A string está vazia!'
    saco_de_palavras = string.split()
    return str(' '.join(saco_de_palavras[::-1]))  


input = "Hello, World! OpenAI is amazing"

print(inversor_str(input))