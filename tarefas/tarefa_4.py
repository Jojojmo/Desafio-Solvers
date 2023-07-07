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

