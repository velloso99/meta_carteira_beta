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

frame_cima= Frame(janela, width=850, height=50, bg=co9)
frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680 )

frame_meio= Frame(janela, width=850, height=50, bg=co9)
frame_meio.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680 )

frame_baixo= Frame(janela, width=850, height=285, bg=co9)
frame_baixo.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)
#*******************************************************************************************************
#Função de Controle
def control(i):
    #Cadastro 
    if i =='cadastro':
        for widget in frame_cima.winfo_children():
            widget.destroy()
        for widget in frame_meio.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        #chamar a função
        cadastro()
    #Cadastro de clientes
    if i =='cadastro clientes':
        for widget in frame_cima.winfo_children():
            widget.destroy()
        for widget in frame_meio.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        #chamar a função
        cadastro_clientes()









#*******************************************************************************************************
#Titulo

t_titulo= Label(frame_cima, text=("Painel"), font=('Ivy 20 bold'), bg=co9, fg=co11)
t_titulo.place(x=425, y=23, anchor=CENTER)






#********************************************************************************************************
#Botões

bt_Cadastro= Button(frame_meio,command=lambda:control('cadastro'), text="Cadastro", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
bt_Cadastro.grid(row=0, column=0)

bt_atualizar= Button(frame_meio, text="Atualizar", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
bt_atualizar.grid(row=0, column=1)

bt_clientes= Button(frame_meio, text="Clientes", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
bt_clientes.grid(row=0, column=2)



#******************************************************************************************************
#Cadastro
def cadastro():

    t_titulo= Label(frame_cima, text=("Cadastro em Geral"), font=('Ivy 20 bold'), bg=co9, fg=co11)
    t_titulo.place(x=425, y=23, anchor=CENTER)

    
    bt_Cadastro= Button(frame_meio, command=lambda:control('cadastro clientes'), text="Cadastro Clientes", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
    bt_Cadastro.grid(row=0, column=0)

    bt_atualizar= Button(frame_meio, text="Cadastro Meta", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
    bt_atualizar.grid(row=0, column=1)

    bt_clientes= Button(frame_meio, text="Cadstro ", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
    bt_clientes.grid(row=0, column=2)

#******************************************************************************************************
# Cadastrar Clientes
def cadastro_clientes():

    t_titulo= Label(frame_cima, text=("Cadastro Clientes"), font=('Ivy 20 bold'), bg=co9, fg=co11)
    t_titulo.place(x=425, y=23, anchor=CENTER)

    bt_Cadastro= Button(frame_meio, text="Salvar", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
    bt_Cadastro.grid(row=0, column=0)

    bt_atualizar= Button(frame_meio, text="Atualizar", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
    bt_atualizar.grid(row=0, column=1)

    bt_clientes= Button(frame_meio, text="Excluir", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
    bt_clientes.grid(row=0, column=2) 

    l_matricula = Label(frame_baixo, text="Matricula:", font=('Ivy 10 bold'), bg=co9, fg=co11)
    l_matricula.place(x=10, y=10)
    e_matricula= Entry(frame_baixo, width=15, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_matricula.place(x=95, y=10)

    l_raz_social = Label(frame_baixo, text="Razão Social:", font=('Ivy 10 bold'), bg=co9, fg=co11)
    l_raz_social.place(x=10, y=50)
    e_raz_social= Entry(frame_baixo, width=35, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_raz_social.place(x=105, y=50)

    l_fantasia = Label(frame_baixo, text="Nome Fantasia:", font=('Ivy 10 bold'), bg=co9, fg=co11)
    l_fantasia.place(x=10, y=90)
    e_fantasia= Entry(frame_baixo, width=35, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_fantasia.place(x=115, y=90)







janela.mainloop()