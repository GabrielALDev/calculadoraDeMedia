print('Calculo de notas')

## Vamos fazer a coleta das notas e seus pesos

nota1 = float(input('Qual a nota da sua primeira prova? \n'))
peso1 = float(input('Qual o peso da primeira nota? \n'))

nota2 = float(input('Qual a nota da sua segunda prova? \n'))
peso2 = float(input('Qual o peso da segunda nota? \n'))

nota3 = float(input('Qual a nota do seu trabalho? \n'))
peso3 = float(input('Qual o peso do trabalho? \n'))

## Fazendo a media 

media = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)

## Aqui o programa ja tendo o resultado da média ele vai imprimir a de acordo com o resultado do aluno.

if (media >= 7):
    print(f'Sua média é: {media:.2f} Parabéns você está dentro da média. ^_^\n')
else:
    print(f'Sua média é: {media:.2f} Você não tem notas suficientes para fazer uma média.\n')