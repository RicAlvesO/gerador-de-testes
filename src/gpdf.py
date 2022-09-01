from datetime import datetime
from fpdf import FPDF

class PDF(FPDF):
    """Classe relativa ao tipo PDF"""
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")

    ## Definição da capa dos pdfs
    def header(self):
        if self.page_no() == 1:

            ## Seccao de informacao do aluno
            self.set_y(45)
            self.set_font('Times', 'B', 13)
            self.cell(190, 15, 'Numero:_________ Nome:__________________________________________ Data:' +
                      self.current_time, 1, 0, 'C')
            self.ln()

            ## Nota Geral
            self.set_font('Times', size=15)
            self.multi_cell(190, 10, '\nNota:\n Os testes gerados nao apresentam qualquer formato oficial.\n'
                            + 'As perguntas são geradas com base nos ficheiros JSON da pasta \'.data/**/*.json\' e podem estar sujeitos a erros.\n'
                            + 'A versão mais atualizada dos mesmos pode ser obtida ao correr o comando \'make sync\'.\n'
                            + 'Os ficheiros de solução nao passam de sugestoes de resolucao dos problemas propostos.\n'
                            + 'Sugere-se para testar as respostas um exemplo no final de cada pergunta.', 0, 0, 'L')
            self.ln()

            ## Info sobre o repo
            self.set_y(-50)
            self.multi_cell(
                190, 10, 'Para mais informações sobre este projeto pode visitar o repositório em:\nhttps://github.com/RicAlvesO/Generador-de-Testes', 1, 0, 'C')

    ## Definicao dos footers dos pdfs
    def footer(self):
        if self.page_no() > 1:
            self.set_font('Times', 'I', 8)

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

def gera_test(questoes, title, current_time):
    """Gera um pdf para o teste com as perguntas e titulo fornecido."""
    pdf = PDF()

    ## Capa
    pdf.add_page()
    pdf.set_y(15)
    pdf.set_font("Times", size=30)
    pdf.cell(190, 30, title, 1, 0, 'C')

    ## Paginas de Pergunta
    pdf.set_font("Times", size=15)
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
    pdf.set_font("Times", size=10)
    for x in resps:
        pdf.add_page()
        pdf.multi_cell(190, 5, x, 1, 'L')

    ## Criacão do Documento
    nome = ''.join(
        ("output/resolucoes/resolucao_teste_", current_time, ".pdf"))
    pdf.output(nome)
    print('Sugestao de resolucao de teste gerado com sucesso em:\n'+nome)
