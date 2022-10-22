#Eis aqui um programa que utiliza uma tupla preenchida com algumas palavras.
#O objetivo do programa é mostrar quais são as vogais de cada palavra.
palavras = ('vara','azul','Deus','sorvete','carro')
for c in palavras:
    print(f"Para a palavra '{c}', temos as vogais: ", end=(""))
    for letras in c:
        if letras.upper() in "AEIOU":
            print(f"{letras}", end=(" - "))
    print()
print("FIM!")
