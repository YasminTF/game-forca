import os

def limparTela():
    os.system("cls")

def criarBaseDados():
    try:
        arquivo = open("banco_dados.txt","r")
        arquivo.close()    
    except:
        arquivo = open("banco_dados.txt","w")
        arquivo.close()


def convertcaps(texto):
    return texto .upper()


def mudarCor():
    os.system("color  A")



def boneco():
  boneco = [
        """
            ____
           |    |
           |    O
           |
           |
           |
        """,
        """
            ____
           |    |
           |    O
           |    |
           |
           |
        """,
        """
            ____
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
            ____
           |    |
           |    O
           |   /|\
           |
           |
        """,
        """
            ____
           |    |
           |    O
           |   /|\
           |   /
           |
        """,
        """
            ____
           |    |
           |    O
           |   /|\
           |   / \
           |
        """
    ]

   



