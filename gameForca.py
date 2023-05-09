from funcoes import limparTela, criarBaseDados,  convertcaps, mudarCor
criarBaseDados()
mudarCor()

limparTela()
print("//////////////////////////////////////////")
print ("     Pressione enter para começar!")
print (input("//////////////////////////////////////////"))
limparTela()
arquivo = open("banco_dados.txt", "r")
dados = arquivo.read()
print(dados)
print (input("//////////////////////////////////////////"))
limparTela()
jogador1 = convertcaps(input("Insira o nome do Desafiante:"))
limparTela()
jogador2 = convertcaps(input("Insira o nome do Competidor:"))
limparTela()
listadeDicas=[]

print("Atenção," , jogador1, "!!!!") 
palavrachave =convertcaps( input("Escolha sabiamente uma palavra:")) 
print("------------------------------------")
listadeDicas.append(input("insira a primeira dica:"))
print("------------------------------------")
listadeDicas.append(input("insira a segunda dica:"))
print("------------------------------------")
listadeDicas.append(input("insira a terceira dica:"))
limparTela()

boneco = [
        """
            ____
           |    |
           |    O
           |
           |
           |▲▲▲▲▲▲▲▲▲
        """,
        """
            ____
           |    |
           |    O
           |    |
           |
           |▲▲▲▲▲▲▲▲▲
        """,
        """
            ____
           |    |
           |    O
           |   /|
           |
           |▲▲▲▲▲▲▲▲▲
        """,
        """
            ____
           |    |
           |    O
           |   /|\\
           |
           |▲▲▲▲▲▲▲▲▲
        """,
        """
            ____
           |    |
           |    O
           |   /|\\
           |   /
           |▴▲▲▲▲▲▲▲▲▲
        """,
        """
            ____
           |    |
           |    O
           |   /|\\
           |   / \\
           |▲▲▲▲▲▲▲▲▲
        """
    ]


soma=0
chances = 5 
tentativas = 0
errou = 0
acertoupalavra = []

letrasescolhidas = []
letrasforca = ["X"] * len(palavrachave) 
print (letrasforca)

while chances> tentativas:
      try:
        comeco = int(input("Para jogar digite (1)." "Para solicitar dica digite (0):"))

        if comeco ==0:
            soma=soma+1
            if soma==1:
               print("A primeira dica é:",listadeDicas[0])
            if soma==2:
                print("A segunda dica é:",listadeDicas[1])
            if soma==3:
                print("A terceira dica é",listadeDicas[2])
            if soma >3: 
                print("Acabaram suas dicas Jedi, mero Padawan... BOA SORTE!") 
            continue   
        
        if comeco ==1:
           print(boneco[errou])
           print("Atenção," , jogador2 , "!!!!")
           letra =convertcaps( input("Escolha uma letra:"))
           letrasescolhidas.append(letra)
           
          
        if letra in palavrachave: 
            #completar
            print ("Letra correta")
            for item in range(len(palavrachave)):
                if letra == palavrachave[item]:
                    letrasforca [item] = letra  
                    acertoupalavra.append(letra *item)
            if len(palavrachave) == len(acertoupalavra):
                    print("PARABÉNS" , jogador2 , "VOCÊ ACERTOU A PALAVRA!!!!!!" ) 

                    arquivo = open("banco_dados.txt","a")
                    arquivo.write("\n" "O vencedor foi:" +jogador2+ "\n" "O perdedor foi:"   +jogador1 + "\n" "Com a palavra:" +palavrachave )
                    arquivo.close()
                    break

        else:
            print("Letra não existente na palavra! Tente novamente:")
            tentativas = tentativas + 1  
            errou=errou+ 1
            if errou==1:
              print(boneco[1])  
            if errou==2:
                print(boneco[2])               
            if errou==3:
                print(boneco[3])
            if errou==4:
                print(boneco[4])             
            if errou==5:
                print(boneco[5])                
            if errou==6:
                print(boneco[6])
          
        print("Status da partida:",letrasforca)
        print ("Tentativas restantes:" , chances-tentativas)  
        print ("Letras que já tentou:" , letrasescolhidas)
        if tentativas ==5:
            arquivo = open("banco_dados.txt","a")
            arquivo.write("\n" "O vencedor foi:" +jogador1+ "\n" "O perdedor foi:"   +jogador2 + "\n" "Com a palavra:" +palavrachave )
            arquivo.close()
            break
      except:
          print ("Escolha 0 ou 1")
         


