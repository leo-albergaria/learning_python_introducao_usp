def xRodadas():
    xUsuario = 0
    xComputador = 0
    for i in range(1, 4):
       print("\n**** Rodada %s ****\n" % i)
       xVencedor = partida()
       if xVencedor == "Usuario":
          xUsuario = xUsuario + 1
       elif xVencedor == "Computador":
          xComputador = xComputador + 1
    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você %s " % xUsuario, " x %s Computador" % xComputador)

def partida():
    n = m = 0
  #  while n <= m:
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
   #    if ( n <= m):
    #      print("\nOops! Jogada inválida! Tente de novo.")     
    
    xQuem_Comeca = "C"
    if n % (m+1) == 0: 
        xQuem_Comeca = "U"
        print("\nVocê começa!")
    else:
        print("\nComputador começa!")
    while n > 0:
       if xQuem_Comeca == "C":
          xQtde_Tirar = computador_escolhe_jogada(n, m)
          if (xQtde_Tirar == 1):
             print("\nO computador tirou uma peça.")
          else:
             print("\nO computador tirou %s peças." % xQtde_Tirar)
          xQuem_Comeca = "U"
       else:
          xQtde_Tirar = usuario_escolhe_jogada(n, m)
          if (xQtde_Tirar == 1):
             print("\nVocê tirou uma peça.")
          else:
             print("\nVocê tirou %s peças." % xQtde_Tirar)
          xQuem_Comeca = "C"
       n = n - xQtde_Tirar
       if (n == 1):
          print("Agora resta apenas uma peça no tabuleiro.")
       elif (n > 1):
          print("Agora restam %s peças no tabuleiro." % n)

    if xQuem_Comeca == "C":
        print("Fim do jogo! Você ganhou!")
        return "Usuario"
    else:
        print("Fim do jogo! O computador ganhou!")
        return "Computador"

def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        xQtde_Tirar = n % (m+1)
        if xQtde_Tirar > 0:
            return xQtde_Tirar
    return m

def usuario_escolhe_jogada(n, m):
    xQtde_Tirar = 0
    while xQtde_Tirar == 0:
        xQtde_Tirar = int(input("\nQuantas peças você vai tirar? "))
        if (xQtde_Tirar > n) or (xQtde_Tirar > m) or (xQtde_Tirar < 1):
            print("\nOops! Jogada inválida! Tente de novo.")
            xQtde_Tirar = 0
    return xQtde_Tirar

while True:
   try:
        print("\nBem-vindo ao jogo do NIM! Escolha:\n")
        print("1 - para jogar uma partida isolada")
        tipo_jogo = int(input("2 - para jogar um campeonato "))
        if ( tipo_jogo == 1 ):
            print("\nVoce escolheu partida isolada!")
            partida()
            break
        elif ( tipo_jogo == 2):
            print("\nVoce escolheu um campeonato!")
            xRodadas()
            break
   except ValueError:
          print("\nAcabou!!! Até a próxima.")
          break  
