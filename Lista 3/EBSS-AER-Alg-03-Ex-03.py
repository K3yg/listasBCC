'''
Vogal ou consoante. Escreva um programa Python que peça para o usuário uma letra do
alfabeto. Se o usuário entrar com as letras a, e, i, o ou u, o programa deve exibir uma
mensagem dizendo que a letra é uma vogal. Caso contrário, o programa deve exibir a
mensagem informando que a letra é uma consoante.
'''

letra = str(input('Insira uma letra: '))

if letra == 'a' or 'e' or 'i' or 'o' or 'u':
    print(f'{letra} é uma vogal!')
else:
    print(f'{letra} é uma consoante!')