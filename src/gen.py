import json
import random
from tokenize import Name
from venv import create
import adder
from datetime import datetime
from simple_term_menu import TerminalMenu
from fpdf import FPDF

class PDF(FPDF):
    """Classe relativa ao tipo PDF"""
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")

    ## Definição da capa dos pdfs
    def header(self):
        if self.page_no()==1:

            ## Seccao de informacao do aluno
            self.set_y(45)
            self.set_font('Times', 'B', 13)
            self.cell(190, 15, 'Numero:_________ Nome:__________________________________________ Data:'+self.current_time, 1, 0, 'C')
            self.ln()
            
            ## Nota Geral
            self.set_font('Times', size=15)
            self.multi_cell(190,10,'\nNota:\n Os testes gerados nao apresentam qualquer formato oficial.\n'
                         +'As perguntas são geradas com base nos ficheiros JSON da pasta .\'data\'*.json e podem estar sujeitos a erros.\n'
                         +'Os ficheiros de solução nao passam de sugestoes de resolucao dos problemas propostos.\n'
                         +'Sugere-se para testar as respostas um exemplo no final de cada pergunta.',0,0,'L')
            self.ln()

            ## Info sobre o repo
            self.set_y(-50)
            self.multi_cell(190, 10, 'Para mais informações sobre este projeto pode visitar o repositório em:\nhttps://github.com/RicAlvesO/Generador-de-Testes',1,0,'C')
    
    ## Definicao dos footers dos pdfs
    def footer(self):
        if self.page_no()>1:
            self.set_font('Times','I', 8)

            ## Data
            self.set_y(-15)
            self.cell(0, 10, self.current_time, 0, 0, 'L')
            self.ln()

            ## Autor do Projeto
            self.set_y(-15)
            self.cell(0, 10, 'By Ricardo O.', 0, 0, 'C')
            self.ln()

            ## Pagina
            self.set_y(-15)
            self.cell(0, 10, 'Page %s' % ((self.page_no())-1), 0, 0, 'R')

def wait():
    """Funcao de Stall"""
    input("\nPressione Enter para continuar...\n")

def gera_test(questoes, title, current_time):
    """Gera um pdf para o teste com as perguntas e titulo fornecido."""
    pdf = PDF()   

    ## Capa
    pdf.add_page()
    pdf.set_y(15)
    pdf.set_font("Times", size = 30)
    pdf.cell(190, 30, title, 1, 0, 'C')

    ## Paginas de Pergunta
    pdf.set_font("Times", size = 15)
    for x in questoes:
        pdf.add_page()
        pdf.multi_cell(190, 10, x, 1, 'L')
        pdf.multi_cell(190, 10, '\tResposta:', 0, 'L')

    ## Criação de Documento
    nome = ''.join(("output/testes/teste_", current_time, ".pdf"))
    pdf.output(nome) 
    print('Teste gerado com sucesso em:\n'+nome)

def gera_res(resps, title, current_time):
    """Gera um pdf para a resolucao com as respostas e titulo fornecido."""
    pdf = PDF()   

    ## Capa
    pdf.add_page()
    pdf.set_y(15)
    pdf.set_font("Times", size=20)
    pdf.cell(190, 30, (title+" (Resolucao)"), 1, 0, 'C')

    ## Paginas com Resolucao de Exercicios
    pdf.set_font("Times", size = 10)
    for x in resps:
        pdf.add_page()
        pdf.multi_cell(190, 5, x, 1, 'L')

    ## Criacão do Documento
    nome=''.join(("output/resolucoes/resolucao_teste_",current_time,".pdf"))
    pdf.output(nome) 
    print('Sugestao de resolucao de teste gerado com sucesso em:\n'+nome)

def get_q(file, amount, title):
    """Gera um com n perguntas e respostas aleatórias."""

    ## Parsing do JSON de perguntas e respostas
    with open(file, "r") as read_file:
        data = json.load(read_file)

    ## Escolha aleatória de n perguntas
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

    ## Criação dos PDFS
    gera_test(quest, title, current_time)
    gera_res(resp, title, current_time)
    wait()

def test_menu():
    """Menu Criação de Testes"""

    create=True
    ## Parsing dos dados guardados
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
    
    ## Menu Tamanho
    while True:
      try:
        amount = int(input("Numero desejado de perguntas: "))
        break
      except ValueError:
          print("Por favor introduza um número válido...")
          continue
    
    ## Verificacoes de Tamanho
    if (amount<=0):
        quit()
    elif (amount>dbsize[menu_entry_index]):
        print("Questoes insuficientes para gerar teste!!!\nMaximo atual para esta linguagem: "
              +str(dbsize[menu_entry_index])+" questoes!\nExprimente adicionar mais questoes e tentar novamente.")
        wait() 
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
    wait()

def menu():
    """Menu Principal"""
    while True:
        options = ["[n] Novo Teste", "[p] Adicionar Perguntas", "[l] Adicionar Linguagens", "[i] Informacoes", "[s] Sair"]
        terminal_menu = TerminalMenu(options, title="Menu")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index == 0):
            test_menu()
        elif (menu_entry_index == 1):
            adder.menu_p()
        elif (menu_entry_index == 2):
            adder.menu_l()
        elif (menu_entry_index == 3):
            info()
        elif (menu_entry_index == 4):
            quit()

        ## Clear screen
        print('\033c')  


def main():
    """Função de inicio"""
    print('\033c')  
    menu()

if __name__ == "__main__":
    main()
