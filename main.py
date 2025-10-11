from templats import *


#*******************************************************
#Crinado Janelas
janela = Tk()
janela.title('')
janela.geometry('850x620')
janela.configure(background= co5)
janela.resizable(FALSE,FALSE)
largura_root = 850
altura_root = 620
#obter tamanho da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
janela.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")













janela.mainloop()