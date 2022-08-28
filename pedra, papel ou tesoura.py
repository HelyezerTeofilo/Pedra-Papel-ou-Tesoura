import random
def jogo():
    qtd_vitorias = 0
    #qtd_derrotas = 0
    #qtd_empates = 0
    cont = 0
    escolha = input("\nDeseja jogar? s ou n: ")
    while escolha.upper() == "S":
        cont+=1
        usuario = input("\nEscolha uma jogada! 'r' para pedra, 'p' para papel e 't' para tesoura: ")
        computador = random.choice(['r','p','t'])
        print("\nO computador escolheu",computador)
        if usuario == computador:
            print("Empate!")
            #qtd_derrotas +=1
        elif vencedor(usuario, computador):
            print("Você ganhou!")
            #qtd_vitorias +=1
        else:
            print("Você perdeu!")
            #qtd_empates +=1
        escolha = input("\nDeseja jogar? s ou n: ")
    return "Partidas jogadas: "+ str(cont) + " Você ganhou " + str(qtd_vitorias) +" vez(es)!"
    
# r > t; t > p; p > r
def vencedor(jogador, oponente):
    if (jogador == 'r' and oponente == 't') or (jogador == 't' and oponente == 'p') \
        or (jogador == 'p' and oponente == 'r'):
        return True


print(jogo())
