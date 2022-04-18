"""
    Nome: Alexandre Kovaleski Rocha
    Curso: Tecnologia em Big Data e Inteligência Analítica
"""

import random

print("GAME ZOMBIE DICE")
print("Seja bem vindo ao Jogo Zombie Dice")

# Informar o nº de jogadores (pelo menos 2 jogadores), guarda na vareiável numJogadores

numJogadores = 0
while numJogadores < 2:
    numJogadores = int(input("Informe o nº de jogadores: "))

    if numJogadores < 2:
        print("AVISO: Voce precisa de pelo menos 2 jogadores\n")

    # Onde guardará os nomes dos jogadores em uma lista, na variável listaJogadores

    listaJogadores = []
    for i in range(numJogadores):
        nome = input("Qual o nome do jogador " + str(i + 1) + ": ")

        listaJogadores.append(nome)  # Salva os nomes dos jogdores na variavel listaJogadores

    dadoVerde = "CPCTPC"
    dadoAmarelo = "TPCTPC"
    dadoVermelho = "TPTCPT"

    listaDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
                  dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
                  dadoVermelho, dadoVermelho, dadoVermelho]

    print("QUE COMECEM OS JOGOS!", "\n")  # Onde irá começar o jogo

    jogadorAtual = 0
    dadosSorteados = []
    tiros = 0
    cerebros = 0
    passos = 0
    resultadoJogo = []

    # Começará a sortear os dados para o primeiro jogador e também os seus pontos

    while True:

        print("Turno do jogador: " + listaJogadores[jogadorAtual], "\n")

        for i in range(3):
            numSorteado = random.choice(listaDados)
            dadoSorteado = numSorteado

            if dadoSorteado == dadoVerde:
                corDado = 'VERDE'
            elif dadoSorteado == dadoAmarelo:
                corDado = 'AMARELO'
            else:
                corDado = 'VERMELHO'

        print("Dado sorteado: ", corDado)
        print("As faces sorteadas do dado foram: ", dadoSorteado, "\n")

        # Estrutura condicional (if, elif e else), para somar os pontos de cada jogador

        if corDado == "VERDE":
            ladoDado = random.choice("CPCTPC")
            if ladoDado == 'C':
                print("VOCÊ TIROU: CÉREBRO - você comeu um cérebro!")
                cerebros = cerebros + 1

            elif ladoDado == "T":
                print("VOCÊ TIROU: TIRO - levou um tiro!")
                tiros = tiros + 1
            else:
                print("VOCÊ TIROU: PASSOS - uma vítima escapou")
                passos = passos + 1

            if corDado == "VERDE":
                listaDados.remove(dadoVerde)
                print("1 dado verde retirado")

        if corDado == "AMARELO":
            ladoDado = random.choice("TPCTPC")
            if ladoDado == "C":
                print("VOCÊ TIROU: CÉREBRO - você comeu um cérebro!")
                cerebros = cerebros + 1
            elif ladoDado == "T":
                print("VOCÊ TIROU: TIRO - levou um tiro!")
                tiros = tiros + 1
            else:
                print("VOCÊ TIROU: PASSOS - uma vítima escapou")
                passos = passos + 1

            if corDado == "AMARELO":
                listaDados.remove(dadoAmarelo)
                print("1 dado amarelo retirado")

        if corDado == "VERMELHO":
            ladoDado = random.choice("TPTCPT")
            if ladoDado == "C":
                print("VOCÊ TIROU: CÉREBRO - você comeu um cérebro!")
                cerebros = cerebros + 1

            elif ladoDado == "T":
                print("VOCÊ TIROU: TIRO - levou um tiro!")
                tiros = tiros + 1

            else:
                print("VOCÊ TIROU: PASSOS - uma vítima escapou")
                passos = passos + 1

            if corDado == "VERMELHO":
                listaDados.remove(dadoVermelho)
                print("1 dado vermelho retirado")

        print("SCORE ATUAL: ")
        print("CÉREBROS: ", cerebros)
        print("TIROS: ", tiros)
        print("PASSOS: ", passos, "\n")
        print(listaDados)

        # Perguntará se o primeiro jogador quer continuar a rodada

        print("AVISO: Voce deseja continuar jogando dados? (S=sim / N=não)")
        continuarTurno = input()

        if continuarTurno == "N":
            resultadoJogo.append(cerebros)
            resultadoJogo.append(tiros)
            resultadoJogo.append(passos)

            jogadorAtual = jogadorAtual + 1
            dadosSorteados = []
            tiros = 0
            cerebros = 0
            passos = 0

            # Renova listaDados pela litaDados2

            listaDados2 = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
                           dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
                           dadoVermelho, dadoVermelho, dadoVermelho]

            listaDados.clear()
            listaDados.extend(listaDados2)

            print("Os dados foram renovados" "\n")
            print(listaDados2, "\n")

        if jogadorAtual == numJogadores:
            print("Fim de jogo")


            print("O jogador vencedor é: ", resultadoJogo)
            break

        else:
            print("Iniciando outra rodada para turno atual")
            dadosSorteados = []