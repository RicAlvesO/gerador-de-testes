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

def update_json(file,amount,id):
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
        amount=int(x)-1
    amount+=1

    while amount:
        print('\033c')  
        print('Pergunta: ')
        q=get_multiline()
        print('Resposta: ')
        a=get_multiline()
        print('Exemplo\nInput: ')
        i=get_multiline()
        print('Output: ')
        o=get_multiline()
        data["Questoes"].append({"Pergunta":q,"Resposta":a,"Exemplo":{"Input":i,"Output":o}})
        data["Total"]+=1
        amount-=1

    ## Guardar nova versão do JSON
    jsonFile = open(file, "w+")
    jsonFile.write(json.dumps(data, indent=2))
    jsonFile.close()

    ## Update de informação global 
    with open("data/data.json", "r") as read_file:
        gdata = json.load(read_file)
    ((gdata["Languages"])[id])["Total"]=data["Total"];
    jsongdata = open("data/data.json", "w+")
    jsongdata.write(json.dumps(gdata, indent=2))
    jsongdata.close()

def menu():
    """Menu Principal"""

    ## Parsing de dados locais
    with open("data/data.json", "r") as read_file:
        data = json.load(read_file)
    options = []
    flist = []
    for l in data["Languages"]:
        options.append("["+l["Alias"]+"] "+l["Name"])
        flist.append(l["Path"])

    while True:
        
        ## Menu Linguagens
        terminal_menu = TerminalMenu(options, title="Linguagem")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index==3):
            quit()
        
        ## Menu Tamanho 
        amount = ["[a] 1 Questao", "[b] Varias", "[s] Sair"]
        amount_menu = TerminalMenu(amount, title="Quantidade")
        amount_entry_index = amount_menu.show()
        if (amount_entry_index==2):
            quit()
       
        ## Update Used JSON
        update_json(flist[menu_entry_index], amount_entry_index, menu_entry_index)

        ## Clear screen
        print('\033c')  

def main():
    """Função de inicio"""
    print('\033c')  #cls
    menu()

if __name__ == "__main__":
    main()
