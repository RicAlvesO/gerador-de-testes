import json
import random
import adder
import gpdf
import utils
from datetime import datetime
from simple_term_menu import TerminalMenu

def get_q(file, amount, title):
    """Gera um com n perguntas e respostas aleatórias."""

    ## Parsing do JSON de perguntas e respostas
    with open(file, "r") as read_file:
        data = json.load(read_file)

    ## Escolha aleatória de n perguntas
    indexs = random.sample(range(0, data["Total"]), amount)
    i=1
    quest=[]
    resp=[]

    ## Distribuição de pontos pelo teste
    total=0.0
    for ind in indexs:
        total += (data["Questoes"][ind])["Dificuldade"]
    total=float(20/total)

    for ind in indexs:
        quest.append(''.join(("Questão ", str(i), ":"," (%.1f" % ((data["Questoes"][ind])["Dificuldade"]*total),
                     " Valores)\n",((data["Questoes"][ind])["Pergunta"]), 
                     '\n\nExemplo\nInput: ', (((data["Questoes"][ind])["Exemplo"])["Input"]), 
                     '\nOutput: ', (((data["Questoes"][ind])["Exemplo"])["Output"]))))
        resp.append(''.join(("Resposta ",str(i),":\n",((data["Questoes"][ind])["Resposta"]))))
        i+=1

    now = datetime.now()
    current_time = now.strftime("%Y%m%d_%H%M%S")

    ## Criação dos PDFS
    gpdf.gera_test(quest, title, current_time)
    gpdf.gera_res(resp, title, current_time)
    utils.wait()

def test_menu():
    """Menu Criação de Testes"""
    create=True

    ## Parsing dos dados globais guardados no json 
    with open("data/data.json", "r") as read_file:
        data = json.load(read_file)
    options = []
    flist = []
    dbsize = []

    for l in data["Languages"]:
        options.append("["+l["Alias"]+"] "+l["Name"])
        flist.append(l["Path"])
        dbsize.append(l["Total"])
    options.append("[s] Sair")

    ## Menu Linguagens
    terminal_menu = TerminalMenu(options, title="Linguagem")
    menu_entry_index = terminal_menu.show()
    if (menu_entry_index==data["Total"]):
        return
    
    amount = utils.get_int("Numero desejado de perguntas: ")

    ## Verificacoes de Tamanho
    while (amount <= 0): # Número de questões não é positivo
        print("Impossivel gerar teste com "+str(amount)+" questoes!!"
              +"\nExprimente colocar um número positivo e tente novamente.")
        utils.wait()
        amount = utils.get_int("Numero desejado de perguntas: ")

    if (amount>dbsize[menu_entry_index]): # Número de questões superior ao máximo
        print("Questoes insuficientes para gerar teste!!!\nMaximo atual para esta linguagem: "
              +str(dbsize[menu_entry_index])+" questoes!\nExprimente adicionar mais questoes e tentar novamente.")
        utils.wait() 
        create=False
    
    ## Criação do Teste
    if create:
        title = ' '.join(("Teste de",(options[menu_entry_index][4:]),":",str(amount),"perguntas"))
        get_q(flist[menu_entry_index], amount, title)

def info():
    """Pagina de informacao sobre o projeto"""

    print('Perguntas disponiveis atualmente:\n'
        +str(json.load(open("data/c.json", "r"))["Total"])+' Questoes de C\n'
        +str(json.load(open("data/haskell.json", "r"))["Total"])+' Questoes de Haskell\n'
        +str(json.load(open("data/java.json", "r"))["Total"])+' Questoes de Java\n\n'
        +'Este projeto foi desenvolvido por:\n-> Ricardo Oliveira (https://github.com/RicAlvesO)\n'
        +'O repositorio do projeto pode ser visitado em:\nhttps://github.com/RicAlvesO/Generador-de-Testes')
    
    utils.wait()

def menu():
    """Menu Principal"""

    while True:
        options = ["[n] Novo Teste", "[p] Adicionar Perguntas", "[l] Adicionar Linguagens", "[i] Informacoes", "[s] Sair"]
        terminal_menu = TerminalMenu(options, title="Menu")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index == 0):
            test_menu()                 # Criar Teste
        elif (menu_entry_index == 1):
            adder.menu_p()              # Adicionar Pergunta
        elif (menu_entry_index == 2):
            adder.menu_l()              # Adicionar Linguagem
        elif (menu_entry_index == 3):
            info()                      # Mostrar Informação
        elif (menu_entry_index == 4):
            quit()                      # Sair

        ## Clear screen
        print('\033c')  


def main():
    """Função de inicio"""
    print('\033c')  
    menu()

if __name__ == "__main__":
    main()
