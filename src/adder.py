import json
from simple_term_menu import TerminalMenu

def get_multiline():
    """Get multi line string input"""
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return '\n'.join(lines)

def update_json(file,amount):
    """Função responsável por atualizar ficheiros JSON com novas perguntas"""
    
    ## Parsing do JSON
    jsonFile = open(file, "r") 
    data = json.load(jsonFile) 
    jsonFile.close()

    ## Adicionar novas perguntas
    if amount:
        x='a'
        while x.isnumeric()==False:
            print('\033c')  
            x=input("Numero desejado de perguntas a adicionar: ")
        amount=x-1
    amount+=1

    while amount:
        print('\033c')  
        print('Pergunta: ')
        q=get_multiline()
        print('Resposta: ')
        a=get_multiline()
        data["Questoes"].append({"Pergunta":q,"Resposta":a})
        data["Total"]+=1
        amount-=1

    ## Guardar nova versão do JSON
    jsonFile = open(file, "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

def menu():
    """Menu Principal"""
    while True:
        
        ## Menu Linguagens
        options = ["[h] HASKELL", "[c] C", "[j] JAVA", "[q] QUIT"]
        terminal_menu = TerminalMenu(options, title="Linguagem")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index==3):
            quit()
        
        ## Menu Tamanho 
        amount = ["[a] 1 Questao", "[b] Varias", "[q] QUIT"]
        amount_menu = TerminalMenu(amount, title="Quantidade")
        amount_entry_index = amount_menu.show()
        if (amount_entry_index==2):
            quit()
       
        ## Update Used JSON
        files = ["data/haskell.json","data/c.json","data/java.json"]
        update_json(files[menu_entry_index], amount_entry_index)

        ## Clear screen
        print('\033c')  

def main():
    """Função de inicio"""
    print('\033c')  #cls
    menu()

if __name__ == "__main__":
    main()
