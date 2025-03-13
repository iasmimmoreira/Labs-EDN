def is_palindromo (texto):
    #remove espaços e converte para minúsculas
    texto_limpo = ''.join(char.lower()
                          for char in texto
                          if char.isalnum())
    #compara o texto com sua versão invertida
    return texto_limpo == texto_limpo[::-1]

#exemplo de uso    
frase = "A cara rajada da jararaca"
resultado = is_palindromo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{frase}' é um palindromo? {resposta}")