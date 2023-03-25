from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from global_color import *

import sys
sys.path.insert(0, './src/infra/database')
import register_user, find_user, update_user, delete_user

# CONTAINER
window = Tk()
window.title('')
window.geometry('1043x473')
window.configure(background=blue_100)
window.resizable(width=FALSE, height=FALSE)

# GRID
top_left = Frame(window, width=310, height=50, bg=stone_700, relief='flat')
top_left.grid(row=0, column=0)

button_left = Frame(window, width=310, height=420, bg=blue_400, relief='flat')
button_left.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

right = Frame(window, width=898, height=420, bg=blue_400, relief='flat')
right.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# LABEL TITLE
title = Label(top_left, text='Formulário de Consultoria', anchor=NW,
              font=('Ivy 13 bold'), bg=stone_700, fg=zinc_300, relief='flat')
title.place(x=10, y=20)


def insertUser():
    name = name_input.get()
    email = email_input.get()
    phone = phone_input.get()
    date_at = calendar_input.get()
    state = state_input.get()
    observations = observations_input.get()

    completeList = [name, email, phone, date_at, state, observations]

    if name == '':
        messagebox.showerror('Error', 'O nome não pode ser vazio')
    else:
        register_user.registerUser(completeList)
        messagebox.showinfo('Successfully registered',
                            'Os dados foram inseridos com sucesso')

        name_input.delete(0, 'end')
        email_input.delete(0, 'end')
        phone_input.delete(0, 'end')
        calendar_input.delete(0, 'end')
        state_input.delete(0, 'end')
        observations_input.delete(0, 'end')

    for widget in right.winfo_children():
        widget.destroy()

    checkUser()

global tree

def updateUser():
    try:
        treePreviewData = tree.focus()
        treePreviewDisc = tree.item(treePreviewData)
        treePreviewList = treePreviewDisc['values']

        userId = treePreviewList[0]

        name_input.delete(0, 'end')
        email_input.delete(0, 'end')
        phone_input.delete(0, 'end')
        calendar_input.delete(0, 'end')
        state_input.delete(0, 'end')
        observations_input.delete(0, 'end')

        name_input.insert(0, treePreviewList[1])
        email_input.insert(0, treePreviewList[2])
        phone_input.insert(0, treePreviewList[3])
        calendar_input.insert(0, treePreviewList[4])
        state_input.insert(0, treePreviewList[5])
        observations_input.insert(0, treePreviewList[6])

        def updateUserData():
            name = name_input.get()
            email = email_input.get()
            phone = phone_input.get()
            date_at = calendar_input.get()
            state = state_input.get()
            observations = observations_input.get()

            completeList = [name, email, phone,
                            date_at, state, observations, userId]

            if name == '':
                messagebox.showerror('Error', 'O nome não pode ser vazio')
            else:
                update_user.updateUserDb(completeList)
                messagebox.showinfo('Successfully registered',
                                    'Os dados foram atualizados com sucesso')

                name_input.delete(0, 'end')
                email_input.delete(0, 'end')
                phone_input.delete(0, 'end')
                calendar_input.delete(0, 'end')
                state_input.delete(0, 'end')
                observations_input.delete(0, 'end')

            for widget in right.winfo_children():
                widget.destroy()

            checkUser()

        updateConfirm = Button(button_left, command=updateUserData, text='Confirmar', width=10, fg=zinc_300,
                               font=('Ivy 7 bold'), bg=orange_500, overrelief='ridge',
                               relief='raised'
                               )
        updateConfirm.place(x=110, y=370)

    except IndexError:
        messagebox.showerror('Error', 'Selecione um dos dados na tabela!')

def deleteUser():
    try:
        treePreviewData = tree.focus()
        treePreviewDisc = tree.item(treePreviewData)
        treePreviewList = treePreviewDisc['values']

        userId = treePreviewList[0]

        delete_user.deleteUserDb(userId)
        messagebox.showinfo('Successfully registered',
                            'Os dados foram deletados com sucesso')
        
        for widget in right.winfo_children():
                widget.destroy()

        checkUser()
    except IndexError:
        messagebox.showerror('Error', 'Selecione um dos dados na tabela!')

# LABELS AND INPUTS
# Name
name_label = Label(button_left, text='Nome', anchor=NW,
                   font=('Ivy 10 bold'), bg=blue_400, fg=zinc_300, relief='flat')
name_label.place(x=10, y=10)
name_input = Entry(button_left, width=30, relief='solid', justify='left')
name_input.place(x=15, y=40)

# Email
email_label = Label(button_left, text='Email', anchor=NW,
                    font=('Ivy 10 bold'), bg=blue_400, fg=zinc_300, relief='flat')
email_label.place(x=10, y=70)
email_input = Entry(button_left, width=30, relief='solid', justify='left')
email_input.place(x=15, y=100)

# Phone number
phone_label = Label(button_left, text='Telefone', anchor=NW,
                    font=('Ivy 10 bold'), bg=blue_400, fg=zinc_300, relief='flat')
phone_label.place(x=10, y=130)
phone_input = Entry(button_left, width=30, relief='solid', justify='left')
phone_input.place(x=15, y=160)

# Date
calendar_label = Label(button_left, text='Data da consulta', anchor=NW,
                       font=('Ivy 8 bold'), bg=blue_400, fg=zinc_300,
                       relief='flat')
calendar_label.place(x=10, y=190)
calendar_input = DateEntry(button_left, width=13, background='dark',
                           foreground='white', borderwidth=2, year=2023)
calendar_input.place(x=15, y=220)

# State
state_label = Label(button_left, text='Estado da consulta', anchor=NW,
                    font=('Ivy 8 bold'), bg=blue_400, fg=zinc_300, relief='flat'
                    )
state_label.place(x=160, y=190)
state_input = Entry(button_left, width=14, relief='solid', justify='left')
state_input.place(x=160, y=220)

# Observations
observations_label = Label(
    button_left, text='Observações', anchor=NW, font=('Ivy 10 bold'),
    bg=blue_400, fg=zinc_300, relief='flat'
)
observations_label.place(x=15, y=260)
observations_input = Entry(
    button_left, width=30, relief='solid', justify='left'
)
observations_input.place(x=15, y=290)

# BUTTONS
insert = Button(button_left, command=insertUser, text='Enviar', width=10,
                fg=zinc_300, font=('Ivy 7 bold'), bg=green_600,
                overrelief='ridge', relief='raised'
                )
insert.place(x=15, y=340)

update = Button(button_left, command=updateUser, text='Atualizar', width=10, fg=zinc_300,
                font=('Ivy 7 bold'), bg=orange_500, overrelief='ridge',
                relief='raised'
                )
update.place(x=110, y=340)

delete = Button(button_left, command=deleteUser, text='Deletar', width=10, fg=zinc_300,
                font=('Ivy 7 bold'), bg=red_500, overrelief='ridge',
                relief='raised')
delete.place(x=205, y=340)


def checkUser():
    global tree

    list_data: list = find_user.findUsers()
    print(list_data)
    list_header = ['ID', 'name', 'email',
                   'telefone', 'data', 'estado', 'sobre']

    tree = ttk.Treeview(right, selectmode='extended',
                        columns=list_header, show='headings')

    vsb = ttk.Scrollbar(right, orient='vertical', command=tree.yview)

    hsb = ttk.Scrollbar(right, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    right.grid_rowconfigure(0, weight=12)

    hd = ['center', 'nw', 'nw', 'nw', 'nw', 'center', 'center']
    h = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for items in list_data:
        tree.insert('', 'end', values=items)


def StartProgram():
    checkUser()
    window.mainloop()
