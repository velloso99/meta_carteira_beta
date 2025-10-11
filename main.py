from templats import *


#*******************************************************
#Crinado Janelas
janela = Tk()
janela.title('')
janela.geometry('850x620')
janela.configure(background= co4)
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


#********************************************************************************************************
#Frames

frame_cima= Frame(janela, width=850, height=50, bg=co5)
frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680 )

frame_meio= Frame(janela, width=850, height=570, bg=co5)
frame_meio.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

frame_baixo= Frame(janela, width=850, height=285, bg=co5)
frame_baixo.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

#*******************************************************************************************************
#Titulo

t_titulo= Label(frame_cima, text=("Painel"), font=('Ivy 20 bold'), bg=co5, fg=co11)
t_titulo.place(x=425, y=23, anchor=CENTER)

#********************************************************************************************************
#Botões

bt_Cadastro= Button(frame_meio, text="Cadastro", bd=3, bg=co8, fg=co11, font=('verdana 10 bold'))
bt_Cadastro.place(x=10, y=10)

bt_atualizar= Button(frame_meio, text="Atualizar", bd=3, bg=co8, fg=co11, font=('verdana 10 bold'))
bt_atualizar.place(x=95, y=10)

bt_clientes= Button(frame_meio, text="Clientes", bd=3, bg=co8, fg=co11, font=('verdana 10 bold'))
bt_clientes.place(x=180, y=10)



#******************************************************************************************************
#Cadastro

















janela.mainloop()