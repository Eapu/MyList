# load a Tkinter listbox with data lines from a file,
# sort data lines, select a data line, display the data line,
# edit the data line, update listbox with the edited data line
# add/delete a data line, save the updated listbox to a data file
# used a more modern import to give Tkinter items a namespace
# tested with Python24       vegaseat       16nov2006
import Tkinter as tk
import ttk
import tkMessageBox
import io
root = tk.Tk()


# create the listbox (note that size is in characters)
listbox1 = tk.Listbox(root, width=50, height=20)
listbox1.grid(row=0, column=0)
listbox2 = tk.Listbox(root, width=50, height=20)
listbox2.grid(row=0, column=2)

def add_item():
    """
    add the text in the Entry widget to the end of the listbox
    """
    listbox1.insert(tk.END, enter1.get())
def delete_item():
    """
    delete a selected line from the listbox
    """
    try:
        # get selected line index
        index = listbox1.curselection()[0]
        listbox1.delete(index)
    except IndexError:
        pass
 
def get_list(event):
    """
    function to read the listbox selection
    and put the result in an entry widget
    """
    # get selected line index
    index = listbox1.curselection()[0]
    # get the line's text
    seltext = listbox1.get(index)
    # delete previous text in enter1
    enter1.delete(0, 50)
    # now display the selected text
    enter1.insert(0, seltext)
def set_list(event):
    """
    insert an edited line from the entry widget
    back into the listbox
    """
    try:
        index = listbox1.curselection()[0]
        # delete old listbox line
        listbox1.delete(index)
    except IndexError:
        index = ttk.END
    # insert edited item back into listbox1 at index
    listbox1.insert(index, enter1.get())
def sort_list():
    """
    function to sort listbox items case insensitive
    """
    temp_list = list(listbox2.get(0, tk.END))
    temp_list.sort(key=str.lower)
    # delete contents of present listbox
    listbox2.delete(0, tk.END)
    # load listbox with sorted data
    for item in temp_list:
        listbox2.insert(ttk.END, item)
def save_list():
    """
    save the current listbox contents to a file
    """
    # get a list of listbox lines
    temp_list = list(listbox1.get(0, tk.END))
    # add a trailing newline char to each line
    temp_list = [lista + '\n' for lista in temp_list]
    # give the file a different name
    fout = open("lista.txt", "w")
    fout.writelines(temp_list)
    fout.close()

# def listbox2
def moveDown():

    move_text = listbox1.selection_get()
    curindex = int(listbox1.curselection()[0])
   
    listbox2.insert(tk.END, move_text)

def save_list2():
    """
    save the current listbox contents to a file
    """
    # get a list of listbox lines
    temp_list2 = list(listbox2.get(0, tk.END))
    # add a trailing newline char to each line
    temp_list2 = [comprar + '\n' for comprar in temp_list2]
    # give the file a different name
    fout2 = open("comprar.txt","w")
    fout2.writelines(temp_list2)
    fout2.close()

def delete_item2():
    """
    delete a selected line from the listbox
    """
    try:
        # get selected line index
        index2 = listbox2.curselection()[0]
        listbox2.delete(index2)
    except IndexError:
        pass

def combine2():

    delete_item2()
    save_list2()

def mail():
    execfile("mail2.py") 
    tkMessageBox.showinfo(":)", "Correo enviado")




var = tk.StringVar(root) # initial value
choices = ['1','2','3','4','5','6','7','8','9']
option = tk.OptionMenu(root, var, *choices)
var.set('1')
option.grid(row = 1, column =1)

def moveDown_and_select():
   
   
    move_text = listbox1.selection_get()
    curindex = int(listbox1.curselection()[0])
    sf = "value is %s" % var.get()

    var4 = '%s %s' % (move_text, var.get())

    listbox2.insert(tk.END, var4)

def combine():
    moveDown_and_select()
    save_list2()


 
# create the sample data file
str1 = """
Aceite de oliva 0,4-Ybarra-5L-Lata
Caja-Aceite girasol-Happyday-1L-Cajar
Aceite refinado girasol-Diplo-25L-Garrafa
Aceite de oliva extra virgen-Vivo-5L-Botella
Aceituna manzanilla s/hueso-Escamilla-1,900g-Bote
Alcaparras-Luxeappers-1kg-Bote
Arroz grano largo-Rocio-1kg-Caja
Azucar-Amogoldi-1kg-Paquete
Atun lata mediana-Lata
Bacon ahumado-Granjaflor-2,40kg
Caldo de pescado-Knorr-1kg-Bote
Caldo de pollo Knorr-1kg-Bote
Canela en rama-La Barraca-250g-Bote
Canela molida-Diplo-720g-Bote",
Champignon laminado lata-Diamante-355g-Lata
Comino molido-La Barraca-670g
Espaguetis Nr.2-La Islena-Caja
Guindillas Rama-La Barraca-180g-Botes
Jamon cocido Fiambre-El Pozo-4kg-Barra
Ketchup-Diplo-1,900g-Bote
Laurel hoja-La Barraca-60g-Bote
Leche-Rio/Gallega-6cartones-Caja 
Mantequilla-Harmony-5kg-Barra
Mayonesa-Ybarra-1,8L-Cubo 
Mayonesa-Ybarra-2,5L-Cubos
Mostaza-Diamante-1,900g-1Bote
Nata liquida-Krona-1L-Carton
Nata spray-Krona-500ml-Botes
Oregano-La Barraca-200g-Bote
Pimenton dulce-La Barraca-810g-Bote
Pimenton picante-La Barraca-810g-Bote
Pimienta negra molida-La Barraca-750g-Bote
Pimienta blanca molida-La Barraca-810g-Bote
Pimienta verde bote-Diamante-65g-Bote
Pina-El pilar-340g-Lata
Queso-GranjaFlor-3,5kg-Barra
Rabo de buey-Knorr-700g-Bote 
Salsa-HP sauce-2L-1Bote
Salsa Perrys-Lea & Perrins-150ml-Bote 
Salsa Tabasco-60ml-Bote
Tomate frito carton-Orlando-2,65kg-Carton
Tomate triturado-Orlando-2,5kg-Lata
Vinagre de vino-Diplo-5L
Vino blanco-Cruzares-1L-Carton
Botellitas de aceite y vinagre de cristal

             ----------Productos postres----------

Bizcocho soletilla-Paquete
Chocolate blanco-Tirma-150g
Chocolate con leche-Tirma-150g 
Chocolate negro-Tirma-150g
Chocolate para fundir-Tirma-150g 
Galletas-Maria Oro-Paquete
Sirope caramelo-Carta DOr-875ml-Bote
Sirope chocolate-Carta DOr-875ml-Bote
Sirope fresa-Carta DOr-875ml-Bote"
Cuajada sobres-Paquete


        ----------Productos limpieza y varios---------

Desengrasante-Kidel-10kg 
Detergente liquido-Calgonit finish Prof.
kh-7-Bote grande
Fregona algodon industrial
Guantes plancha    Talla M 
Jabon liquido banos
Lavavajillas mano (garrafa)-Fairy-5L
Lejia-Conejo-4L 
Lejia-marca blanca-4L
Papel termico(rollos de 6cm)
Palillos enfundados         
Pinchos brocheta 

       --------------Bebidas-----------------

Akuavit
Amaretto
Anis Chinchon
Anis Sambuca
Baileys
Brandy 103
Brandy Carlos I
Brandy Carlos III
Brandy cocina barato
Brandy Magno
Brandy Veterano
Cerveza Coronita
Cerveza S.Miguel
Cordon negro Freixenet
Cordon negro Freixenet mini
Cynar
Drambuie
Fernet Branca
Frangelico
Ginebra barata
Ginebra Beefeater
Ginebra Gordons 
Granadina
Jaergermeister
Licor de Lima
Licor de Platano
Martini blanco 
Martini dry
Martini rosso
Orujo Aguardiente
Orujo Hierbas
Pacharan
Pampelmuse
Ramazotti
Ron Bacardi
Ron Blanco Arehucas
Ron miel Cayest-Caja
Ron Oro Arehucas
Ron Santa Teresa 
Ron Santiago de Cuba
San Miguel
Tia Maria
Triple Seco
Vino fino Tio Pepe
Vino Protos
Vino tinto RVA. Marques del Riscal
Vodka Caramelo 
Vodka Moskoskaya
Vodka Smirnoff
Whisky 100 pp
Whisky barato
Whisky E.N.
Whisky E.R.
Whisky J.B.
Whisky J.H.
"""
fout = open("lista.txt", "w")
fout.write(str1)
fout.close()
 
# read the data file into a list
fin = open("lista.txt", "r")
temp_list3 = fin.readlines()
fin.close()
# strip the trailing newline char
temp_list3 = [lista.rstrip() for lista in temp_list3]
 




 

# use entry widget to display/edit selection
enter1 = tk.Entry(root, width=50, bg='yellow')
enter1.insert(0, '')
enter1.grid(row=1, column=0)
# pressing the return key will update edited line
enter1.bind('<Return>', set_list)
# or double click left mouse button to update line
enter1.bind('<Double-1>', set_list)
# button to sort listbox
#button1 = ttk.Button(root, text='Orden alfabetico', command=sort_list)
#button1.grid(row=2, column=3, sticky=tk.E)
# button to save the listbox's data lines to a file
button2 = ttk.Button(root, text='Guardar lista', command=save_list)
button2.grid(row=3, column=0, sticky=tk.W)
# button to add a line to the listbox
button3 = ttk.Button(root, text='Insertar producto', command=add_item)
button3.grid(row=2, column=0, sticky=tk.E)
# button to delete a line from listbox
button4 = ttk.Button(root, text='Borrar producto     ', command=delete_item)
button4.grid(row=3, column=0, sticky=tk.E)

#button of listbox2
button5 = ttk.Button(root, text="Comprar", command=combine)
button5.grid(row=2, column=1, sticky=tk.E)
button6 = ttk.Button(root, text="Borrar", command=combine2)
button6.grid(row=2, column=2, sticky=tk.W)

button7 = ttk.Button(root, text="Correo", command=mail)
button7.grid(row=2, column=2, sticky=tk.E)





# load the listbox with data
for item in temp_list3:
    listbox1.insert(tk.END, item)
 
# left mouse click on a list item to display selection





root.mainloop()


