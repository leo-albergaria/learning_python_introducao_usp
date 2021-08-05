xQtde_Comp = 0
xQtde_User = 0
xQtde_Rodadas = 0

def computador_escolhe_jogada(n, m):
    global xQtde_Comp
    if n < m:
       print("O computador tirou %s peça." % n)
       n = 0
    else:
       n = n - m
       print("O computador tirou %s peça.---" % m)
       
    if n == 0:
       xQtde_Comp += 1
       print ("Fim do jogo! O computador ganhou!\n")
    else:
       print("Agora restam %s peças no tabuleiro." % n)
       
    return n

def usuario_escolhe_jogada(n, m):
    global xQtde_User
    xQtde_Escolha = m
    while xQtde_Escolha <= m:
       xQtde_Escolha = int(input("\nQuantas peças você vai tirar? "))
       if xQtde_Escolha > m and xQtde_Escolha > n: 
          print("\nOops! Jogada inválida! Tente de novo.")
          xQtde_Escolha = 1
       else:
          n = n - xQtde_Escolha          
          print("\nVoce tirou %s peças." % xQtde_Escolha)
          if n == 0:
             xQtde_User += 1
             print ("Fim do jogo! Você ganhou!\n")
          else:
             print("Agora restam apenas %s peças no tabuleiro." % n, "\n")
          break
    return n

def partida():
    global xQtde_Comp
    global xQtde_User
    global xQtde_Rodadas

    for i in range(1, xQtde_Rodadas+1):
       print("**** Rodada %s ****" % i, "\n")
       n = int(input("Quantas peças? "))
       m = int(input("Limite de peças por jogada? "))
       if (((n )%(m + 1)) == 0):
          print("\nVoce começa!")
          while (n > 0):
             if n != 0:
                n = usuario_escolhe_jogada(n,m)
             if n != 0:
                n = computador_escolhe_jogada(n,m)
       else:
          print("\nComputador Começa!!\n")
          while( n > 0):
             if n != 0:
                n = computador_escolhe_jogada(n,m)
             if n != 0:
                n = usuario_escolhe_jogada(n,m)

while True:
   try:
        print("\nBem-vindo ao jogo do NIM! Escolha:\n")
        print("1 - para jogar uma partida isolada")
        tipo_jogo = int(input("2 - para jogar um campeonato "))
        if ( tipo_jogo == 1 ):
            print("\nVoce escolheu partida isolada!\n")
            xQtde_Rodadas = 1    
            partida()
            print("**** Final do campeonato! ****")
            break
        elif ( tipo_jogo == 2):
            print("\nVoce escolheu um campeonato!\n")
            xQtde_Rodadas = 3
            partida()
            print("**** Final do campeonato! ****\n")
            print("Placar: Você %s " % xQtde_User, "x %s Computador" % xQtde_Comp)
            break
   except ValueError:
          print("\nAcabou!!! Até a próxima.")
          break


