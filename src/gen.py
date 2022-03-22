import json
import random
import adder
from datetime import datetime
from simple_term_menu import TerminalMenu
from fpdf import FPDF

def wait():
    input("\nPressione Enter para continuar...\n")

def gera_test(questoes, title, current_time):
    """Gera um pdf para o teste com as perguntas e titulo fornecido."""
    pdf = FPDF()   

    #Capa
    pdf.add_page()
    pdf.set_font("Times", size = 30)
    pdf.cell(0, 200, title, 0, 0, 'C')

    #Paginas de Pergunta
    pdf.set_font("Times", size = 15)
    for x in questoes:
        pdf.add_page()
        pdf.multi_cell(190, 10, x, 1, 'L')
        pdf.multi_cell(190, 10, '\tResposta:', 0, 'L')

    #Criação de Documento
    nome = ''.join(("output/testes/teste_", current_time, ".pdf"))
    pdf.output(nome) 
    print('Teste gerado com sucesso em:\n'+nome)

def gera_res(resps, title, current_time):
    """Gera um pdf para a resolucao com as respostas e titulo fornecido."""
    pdf = FPDF()   

    #Capa
    pdf.add_page()
    pdf.set_font("Times", size = 30)
    pdf.cell(0, 200, (title+" (Resolucao)"), 0, 0, 'C')

    #Paginas com Resolucao de Exercicios
    pdf.set_font("Times", size = 10)
    for x in resps:
        pdf.add_page()
        pdf.multi_cell(190, 5, x, 1, 'L')

    #Criacão do Documento
    nome=''.join(("output/resolucoes/resolucao_teste_",current_time,".pdf"))
    pdf.output(nome) 
    print('Sugestao de resolucao de teste gerado com sucesso em:\n'+nome)

def get_q(file, amount, title):
    """Gera um com n perguntas e respostas aleatórias."""

    #Parsing do JSON de perguntas e respostas
    with open(file, "r") as read_file:
        data = json.load(read_file)
    
    if data["Total"]<amount:
        print('!QUESTOES INSUFICIENTES!')
        wait()
        return

    #Escolha aleatória de n perguntas
    indexs = random.sample(range(0, data["Total"]), amount)
    i=1;
    quest=[]
    resp=[]
    for ind in indexs:
        quest.append(' '.join((str(i),") ",((data["Questoes"][ind])["Pergunta"]),'\n\nExemplo\nInput:',(((data["Questoes"][ind])["Exemplo"])["Input"]),'\nOutput:',(((data["Questoes"][ind])["Exemplo"])["Output"]))))
        resp.append(' '.join(("Resposta ",str(i),":\n",((data["Questoes"][ind])["Resposta"]))))
        i+=1

    now = datetime.now()
    current_time = now.strftime("%Y%m%d_%H%M%S")

    #Criação dos PDFS
    gera_test(quest, title, current_time)
    gera_res(resp, title, current_time)
    wait()

def test_menu():
    """Menu Criação de Testes"""
    #Menu Linguagens
    options = ["[h] HASKELL", "[c] C", "[j] JAVA", "[q] Sair"]
    terminal_menu = TerminalMenu(options, title="Linguagem")
    menu_entry_index = terminal_menu.show()
    if (menu_entry_index==3):
        quit()
    

    #Menu Tamanho
    while True:
      try:
        amount = int(input("Numero desejado de perguntas: "))
        break
      except ValueError:
          print("Por favor introduza um número válido...")
          continue
    if (amount<=0):
        quit()
    
    #Criação do Teste
    title = ' '.join(("Teste de",(options[menu_entry_index][4:]),":",str(amount),"perguntas"))
    data = ["data/haskell.json","data/c.json","data/java.json"]
    get_q(data[menu_entry_index], amount, title)

def info():
    print('Perguntas disponiveis atualmente:\n'
        +str(json.load(open("data/c.json", "r"))["Total"])+' Questoes de C\n'
        +str(json.load(open("data/haskell.json", "r"))["Total"])+' Questoes de Haskell\n'
        +str(json.load(open("data/java.json", "r"))["Total"])+' Questoes de Java\n\n'
        +'Este projeto foi desenvolvido por:\n-> Ricardo Oliveira (https://github.com/RicAlvesO)\n'
        +'O repositorio do projeto pode ser visitado em:\nhttps://github.com/RicAlvesO/Generador-de-Testes')
    wait()

def menu():
    """Menu Principal"""
    while True:
        options = ["[n] Novo Teste", "[a] Adicionar Perguntas", "[i] Informacoes", "[q] Sair"]
        terminal_menu = TerminalMenu(options, title="Menu")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index == 0):
            test_menu()
        elif (menu_entry_index == 1):
            adder.menu()
        elif (menu_entry_index == 2):
            info()
        elif (menu_entry_index == 3):
            quit()

        #Clear screen
        print('\033c')  


def main():
    """Função de inicio"""
    print('\033c')  #cls
    menu()

if __name__ == "__main__":
    main()
