def palindromo(word):
    word = word.lower.replace(' ',' ')
    if word == word[::-1]:
        return f'{word} es palindromo'
    else:
        return f'{word} no es palindromo'

es_palindromo = lambda word:'si es' if word.lower().replace(' ',' ') == word.lower().replace(' ',' ')[::-1] else 'no es ' 
print(es_palindromo('La tele letal'))