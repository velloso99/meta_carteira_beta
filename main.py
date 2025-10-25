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

frame_baixo= Frame(janela, width=850, height=260, bg=co9)
frame_baixo.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=5, columnspan=1, ipadx=680 )

frame_tabela= Frame(janela, width=850, height=260, bg=co9)
frame_tabela.grid(row=6, column=0, pady=0, padx=0, sticky=NSEW)
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

    bt_clientes= Button(frame_meio, text="Cadastro ", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
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

    l_endereco = Label(frame_baixo, text="Endereço:", font=('Ivy 10 bold'), bg=co9, fg=co11)
    l_endereco.place(x=10, y=130)
    e_endereco= Entry(frame_baixo, width=35, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_endereco.place(x=95, y=130)

    l_bairro = Label(frame_baixo, text="Bairro:", font=('Ivy 10 bold'), bg=co9, fg=co11)
    l_bairro.place(x=10, y=170)
    e_bairro= Entry(frame_baixo, width=35, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_bairro.place(x=115, y=170)

    l_ = Label(frame_baixo, text="Atendente:", font=('Ivy 10 bold'), bg=co9, fg=co11)
    l_.place(x=10, y=210)
    e_= Entry(frame_baixo, width=35, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_.place(x=95, y=210)


    #Tabela Alunos
    def mostrar_lucro():
    
        app_nome = Label(frame_tabela, text="Registros de Rotas", height=1, pady=0, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co11, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")  # Agora correto
        
        #CREATING A TREEVIEW WITH DUAL SCROLLBARS
        list_header = ['id', 'Matricula', 'Razão Social', 'Nome Fnatsia', 'Endereço', 'Bairro', 'Atendente']
        # Define the atualizar_lucro function
        def atualizar_lucro(lista):
            # Placeholder implementation for updating data
            # Replace this with actual database update logic
            print(f"Updating record with data: {lista}")
        
        df_list = ver_clientes()
        
        global tree_lucro
        
        tree_lucro = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")
        
        #VERTICAL SCROLLBAR
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_lucro.yview)
        #HORIZONTAL SCROLLBAR
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_lucro.yview)
        
        tree_lucro.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_lucro.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0,weight=12)
        
        hd=["center","center","nw","nw","nw","center","center"]  
        h = [40, 100, 100, 130, 50, 160, 160]
        n=0
        
        for col in list_header:
            tree_lucro.heading(col, text=col.title(), anchor=NW)
            #ADJUST THE COLUMN'S WIDTH TO THE HEADER STRING
            tree_lucro.column(col, width=h[n], anchor=hd[n])
            
            n+=1
            
            for item in df_list:
                tree_lucro.insert("", "end", values=item)
    mostrar_lucro()



janela.mainloop()