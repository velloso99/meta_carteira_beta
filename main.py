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
        adicionar_clientes()
    #voltar de clientes
    if i =='voltar cadastro':
        for widget in frame_cima.winfo_children():
            widget.destroy()
        for widget in frame_meio.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        #chamar a função
        cadastro()
    








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
def adicionar_clientes():

    def cad_clientes():

        matricula= e_matricula.get()
        razaosocial = e_raz_social.get()
        nomefantasia = e_fantasia.get()
        endereco = e_endereco.get()
        bairro = e_bairro.get()
        atendete = e_atendente.get()

        lista=[matricula,razaosocial,nomefantasia,endereco,bairro,atendete]
        #verificando se os valores estão vazios
        for i in lista:
            if i == "":
                messagebox.showerror('Erro', "Preencha todosos campos!")
                return
        #inserir dados
        cadastrar_clientes(lista)
        #mostrando menssagem de sucesso
        messagebox.showinfo('Sucesso', "Os dados inseridos com sucesso!")

        e_matricula.delete(0,END)
        e_raz_social.delete(0,END)
        e_fantasia.delete(0,END)
        e_endereco.delete(0,END)
        e_bairro.delete(0,END)
        e_atendente.delete(0,END)

        #mostrando valores na tabela
        mostrar_clientes()

    def del_clientes():
        try:
            tree_itens = tree_clientes.focus()
            tree_dicionario = tree_clientes.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]
            #deletar dados no banco de dadsos
            deletar_clientes([valor_id])

            #mostrando menssagem
            messagebox.showinfo('Sucesso', "Dados deletados com sucesso!")

            #mostrando os valores na tabela
            ver_clientes()
        except IndexError:
            messagebox.showerror('Erro', "Selecione os dados para serem exluidos!")

    def update_login():
        try:
            tree_item = tree_clientes.focus()
            tree_dicionario = tree_clientes.item(tree_item)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_matricula.delete(0,END)
            e_raz_social.delete(0,END)
            e_fantasia.delete(0,END)
            e_endereco.delete(0,END)
            e_bairro.delete(0,END)
            e_atendente.delete(0,END)



    
    t_titulo= Label(frame_cima, text=("Cadastro Clientes"), font=('Ivy 20 bold'), bg=co9, fg=co11)
    t_titulo.place(x=425, y=23, anchor=CENTER)

    bt_salvar= Button(frame_meio,command=cad_clientes, text="Salvar", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
    bt_salvar.grid(row=0, column=0)

    bt_atualizar= Button(frame_meio, text="Atualizar", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
    bt_atualizar.grid(row=0, column=1)

    bt_clientes= Button(frame_meio,command=del_clientes ,text="Excluir", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
    bt_clientes.grid(row=0, column=2) 

    bt_voltar= Button(frame_meio,command=lambda:control('voltar cadastro'), text="voltar", bd=3, bg=co9, fg=co11, font=('verdana 10 bold'))
    bt_voltar.grid(row=0, column=3) 

    #########################################################################################################
    

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

    l_atendente= Label(frame_baixo, text="Atendente:", font=('Ivy 10 bold'), bg=co9, fg=co11)
    l_atendente.place(x=10, y=210)
    e_atendente= Entry(frame_baixo, width=35, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_atendente.place(x=95, y=210)


    #Tabela Alunos
    def mostrar_clientes():
    
        app_nome = Label(frame_tabela, text="Registros de Clientes", height=1, pady=0, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co11, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")  # Agora correto
        
        #CREATING A TREEVIEW WITH DUAL SCROLLBARS
        list_header = ['id', 'Matricula', 'Razão Social', 'Nome Fantasia', 'Endereço', 'Bairro', 'Atendente']
        # Define the atualizar_clientes function
        def atualizar_clientes(lista):
            # Placeholder implementation for updating data
            # Replace this with actual database update logic
            print(f"Updating record with data: {lista}")
        
        df_list = ver_clientes()
        
        global tree_clientes
        
        tree_clientes = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")
        
        #VERTICAL SCROLLBAR
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_clientes.yview)
        #HORIZONTAL SCROLLBAR
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_clientes.yview)
        
        tree_clientes.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_clientes.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0,weight=12)
        
        hd=["center","center","nw","nw","nw","center","center"]  
        h = [40, 100, 100, 150, 50, 160, 160]
        n=0
        
        for col in list_header:
            tree_clientes.heading(col, text=col.title(), anchor=NW)
            #ADJUST THE COLUMN'S WIDTH TO THE HEADER STRING
            tree_clientes.column(col, width=h[n], anchor=hd[n])
            
            n+=1
            
            for item in df_list:
                tree_clientes.insert("", "end", values=item)
    mostrar_clientes()



janela.mainloop()