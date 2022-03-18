import json
import random
from datetime import datetime
from simple_term_menu import TerminalMenu
from fpdf import FPDF

def gera_test(questoes, title):
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
    now = datetime.now()
    current_time = now.strftime("%Y%m%d_%H%M%S")
    pdf.output(''.join(("output/testes/teste_",current_time,".pdf"))) 

def gera_res(resps, title):
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
    now = datetime.now()
    current_time = now.strftime("%Y%m%d_%H%M%S")
    pdf.output(''.join(("output/resolucoes/resolucao_teste_",current_time,".pdf"))) 

def get_q(file, amount, title):
    """Gera um com n perguntas e respostas aleatórias."""

    #Parsing do JSON de perguntas e respostas
    with open(file, "r") as read_file:
        data = json.load(read_file)
    
    #Escolha aleatória de n perguntas
    indexs = random.sample(range(0, data["Total"]), amount)
    i=1;
    quest=[]
    resp=[]
    for ind in indexs:
        quest.append(' '.join((str(i),") ",((data["Questoes"][ind])["Pergunta"]))))
        resp.append(' '.join(("Resposta ",str(i),":\n",((data["Questoes"][ind])["Resposta"]))))
        i+=1

    #Criação dos PDFS
    gera_test(quest, title)
    gera_res(resp, title)

def menu():
    """Menu Principal"""
    while True:
        
        #Menu Linguagens
        options = ["[h] HASKELL", "[c] C", "[j] JAVA", "[q] QUIT"]
        terminal_menu = TerminalMenu(options, title="Linguagem")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index==3):
            quit()
        
        #Menu Tamanho 
        amount = ["[a] 2 Questoes", "[b] 4 Questoes", "[c] 6 Questoes", "[d] 8 Questoes", "[e] 10 Questoes", "[q] QUIT"]
        amount_menu = TerminalMenu(amount, title="Quantidade")
        amount_entry_index = amount_menu.show()
        if (amount_entry_index==5):
            quit()
        
        #Criação do Teste
        title = ' '.join(("Teste de",(options[menu_entry_index][4:]),":",str((amount_entry_index+1)*2),"perguntas"))
        data = ["data/haskell.json","data/c.json","data/java.json"]
        get_q(data[menu_entry_index], (amount_entry_index+1)*2, title)

        #Clear screen
        print('\033c')  

def main():
    """Função de inicio"""
    print('\033c')  #cls
    menu()

if __name__ == "__main__":
    main()
