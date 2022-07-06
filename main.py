import tkinter as tk

#Funções#
def NovoArquivo():
    print("Criar novo arquivo")

def SalvarArquivo():
    print("Salvar Arquivo")

def SalvarComoArquivo():
    print("Salvar Como Arquivo")


#Tela e Dimenção da tela
window = tk.Tk()
window.title("Bloco De Notas")
window.geometry("1280x720")

text_area = tk.Text(window, font="Arial 18 bold", width=1280, heigh=780)
text_area.pack()


#Parte Menu
main_menu = tk.Menu(window)


arquivo_menu = tk.Menu(main_menu, tearoff=0)
arquivo_menu.add_command(label="Novo", command = NovoArquivo)
arquivo_menu.add_command(label="Salvar", command = SalvarArquivo)
arquivo_menu.add_command(label="Salvar Como...", command = SalvarComoArquivo)
arquivo_menu.add_command(label="Sair", command = window.quit)

#Cascata dos Menus
main_menu.add_cascade(label="Arquivos", menu =arquivo_menu)
main_menu.add_cascade(label="Fonte")
window.config(menu=main_menu)

tk.mainloop()