'''
Nota para frequência. Existem algumas diferenças entre as escolas latina e anglo-saxônica
de música. A mais conhecida é a diferença no nome das notas musicais. Na escola latina
temos Dó, Ré, Mi, Fá, Sol, Lá e Si. Os nomes correspondentes na escola anglo-saxônica são
C, D, E, F, G, A e B (do dó ao si, respectivamente. Além disso, a tecnologia MIDI incorporou
um número ao nome de cada nota indicando em qual oitava ela pertence. Por exemplo, o dó
central do piano é chamado de C4, o dó mais agudo, uma oitava acima é chamado de C5, e o
dó uma oitava abaixo (mais grave) é chamado de C3.
A tabela abaixo exibe as frequências de cada nota da oitava central do piano (cada nota
musical tem uma frequência específica em hertz).


Comece escrevendo um programa Python que recebe do usuário o nome de uma nota e exibe
a frequência correspondente. Seu programa deve aceitar todas as notas da tabela acima. 


Uma vez que seu programa esteja funcionando, você deve modificá-lo para suportar todas as notas
de C0 a C8. Embora isso possa ser feito incluindo um monte de condições de ifs, elifs e else,
mas isso é extremamente "tosco" e deselegante, e portanto inaceitável como solução deste
exercício. Ao invés disso, você pode explorar as relações entre notas em oitavas adjacentes
(por exemplo relação da nota G4 com a nota G5, são duas notas sol, em oitavas diferentes).
Em particular, 

a frequência de uma nota em uma oitava é metade do valor da frequência damesma nota uma oitava acima.
Por exemplo: se A4 tem 440.00Hz, a nota A5 tem 880.00Hz de frequência e a nota A3 tem 220.00Hz.

Tendo em mente estas relações, você consegue
resolver o problema para todas as notas musicais adicionais sem incluir novos casos nos seus
comandos condicionais.
'''

nome_nota = input("Insira o nome da nota: ").lower()
letra = nome_nota[0]
numero = int(nome_nota[1])

if letra == "a":
    frequencia = 440.00/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')

elif letra == "b":
    frequencia = 493.88/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')

elif letra == "c":
    frequencia = 261.63/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')

elif letra == "d":
    frequencia = 293.66/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')

elif letra == "e":
    frequencia = 329.63/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')

elif letra == "g":
    frequencia = 392.00/2**(4-numero)
    print(f'A frequencia da nota {nome_nota} é de: {frequencia}Hz')
else:
    print("Não foi possivel encontrar a nota musical escolhida.")