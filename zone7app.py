from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()
root.config(width=400, height=600)
root.title("Zone7")
root.iconbitmap(r"C:\Users\Tomi PC\Desktop\Tomi\Python\zone 7 app\zon.ico")


#frame
frame = Frame(width=400, height=190)
frame.grid(columnspan=3)


#logo
imagen = PhotoImage(file=r"C:\Users\Tomi PC\Desktop\Tomi\Python\zone 7 app\maxresdefault.png")
Label(root, image=imagen, bg='black').grid(row=0, column=1, rowspan=3)

#colores
    #tema oscuro
zone_gris = '#151411' # bg widget
verde_hack = '#00FF00' # fg widget
    #tema chillón
pastel = '#FBE2E1' # bg
verde_agua = '#25F5A7' # fg variable
rosa_fucsia = '#FF7DF5' # fg variable
    #default


#funciones
def crearConexion():
    conexion=sqlite3.connect("BBDD7")
        
    cursor=conexion.cursor()
    
    try: 
        cursor.execute('''
            CREATE TABLE DATOS_EVENTOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            EVENTO VARCHAR(70),
            FECHA VARCHAR(70),
            UBICACION VARCHAR(70),
            CONTACTO VARCHAR(70),
            COMENTARIOS VARCHAR(160))
            ''')
        messagebox.showinfo("BBDD", "Base de datos creada con exito.")
    except:
        messagebox.showinfo("BBDD", "Conexión exitosa!")

def salirPrograma():

    valor=messagebox.askquestion("Salir", "Deseas salir de la aplicación?")

    if valor == "yes":
        root.destroy()

def limpiarCampos():
    texto_id.set("")
    texto_evento.set("")
    texto_fecha.set("")
    texto_ubicacion.set("")
    texto_contacto.set("")
    campo_comentarios.delete(1.0, END)

def limpiarEventos():
    notas.delete(0, END)

def limpiarTodos():
    texto_id.set("")
    texto_evento.set("")
    texto_fecha.set("")
    texto_ubicacion.set("")
    texto_contacto.set("")
    campo_comentarios.delete(1.0, END)
    notas.delete(0, END)

def agregar():
    crearcon=sqlite3.connect("BBDD7")
    crearcursor=crearcon.cursor()
    
    datos = texto_evento.get(), texto_fecha.get(), texto_ubicacion.get(), texto_contacto.get(), campo_comentarios.get(1.0, END)
    
    if datos == ('', '', '', '', '\n'):
        messagebox.showerror("BBDD", "Todos los campos deben estar completos.")       
    else:
        try:
            crearcursor.execute("INSERT INTO DATOS_EVENTOS VALUES(NULL, ?, ?, ?, ?, ?)", (datos))
            crearcon.commit()

            messagebox.showinfo("BBDD", "Registro insertado con exito")

            datos_notas = "" + texto_evento.get() + ", "  + texto_fecha.get() + ", " + texto_ubicacion.get() + ", " + texto_contacto.get() +", "+ campo_comentarios.get(1.0, END) + ""
            notas.insert(0, datos_notas)
        except:
            messagebox.showerror("BBDD", "No hay ninguna base de datos creada")
       
def eliminar():
    crearcon=sqlite3.connect("BBDD7")
    crearcursor=crearcon.cursor()
    try:
        crearcursor.execute("DELETE FROM DATOS_EVENTOS WHERE ID=" + texto_id.get())
        crearcursor.execute("DELETE FROM sqlite_sequence WHERE name='DATOS_EVENTOS'")
        crearcon.commit()

        messagebox.showinfo("BBDD", "Registro eliminado con exito")
    except:
        messagebox.showerror("BBDD", "Debes ingresar un ID.")

def editar():
    crearcon=sqlite3.connect("BBDD7")
    crearcursor=crearcon.cursor()
    try:
        crearcursor.execute("UPDATE DATOS_EVENTOS SET EVENTO='" + texto_evento.get() + 
        "', FECHA='" + texto_fecha.get() +
        "', UBICACION='" + texto_ubicacion.get() +
        "', CONTACTO='" + texto_contacto.get() +
        "', COMENTARIOS='" + campo_comentarios.get("1.0", END) +
        "' WHERE ID="+ texto_id.get())
        crearcon.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con exito")
    except:
        messagebox.showerror("BBDD", "Debes ingresar un ID.")

def lectura():
    crearcon=sqlite3.connect("BBDD7")
    crearcursor=crearcon.cursor()
    try:    
        crearcursor.execute("SELECT * FROM DATOS_EVENTOS WHERE ID=" + texto_id.get())

        impresion=crearcursor.fetchall()
        try:
            for i in impresion:
                a = [i[0]]
                b = [i[1]]
                c = [i[2]]
                d = [i[3]]
                e = [i[4]]
                f = [i[5]]

                texto_id.set(str(i[0]))
                texto_evento.set(i[1])
                texto_fecha.set(i[2])
                texto_ubicacion.set(i[3])
                texto_contacto.set(i[4])
                campo_comentarios.insert(1.0, i[5])

            string1 = "" + str(a[0]) + ". " + b[0] + ", "  + c[0] + ", " + d[0] + ", " + e[0] + ", " + f[0] + "."

            notas.insert(0, string1)
            crearcon.commit()
        except:
            messagebox.showerror("BBDD", "No existe fecha con ese ID.")
    except:
        messagebox.showerror("BBDD", "Debes ingresar un ID.")

def tema_default():
    root.config(bg='SystemButtonFace')
    frame.config(bg='SystemButtonFace')
    frame_notas.config(bg='SystemButtonFace')
    frame3.config(bg='SystemButtonFace')
    frame_botones.config(bg='SystemButtonFace')
    
    label_comentarios.config(bg='SystemButtonFace', fg='black')
    label_contacto.config(bg='SystemButtonFace', fg='black')
    label_evento.config(bg='SystemButtonFace', fg='black')
    label_fecha.config(bg='SystemButtonFace', fg='black')
    label_id.config(bg='SystemButtonFace', fg='black')
    label_ubicacion.config(bg='SystemButtonFace', fg='black')

    entry_evento.config(bg='white', fg='black')
    entry_contacto.config(bg='white', fg='black')
    entry_fecha.config(bg='white', fg='black')
    entry_id.config(bg='white', fg='black')
    entry_ubicacion.config(bg='white', fg='black')
    campo_comentarios.config(bg='white', fg='black')
    notas.config(bg='white', fg='black')
    
    boton_agg.config(bg='SystemButtonFace', fg='black')
    boton_editar.config(bg='SystemButtonFace', fg='black')
    boton_leer.config(bg='SystemButtonFace', fg='black')
    boton_eliminar.config(bg='SystemButtonFace', fg='black')

def tema_claro():
    root.config(bg=pastel)
    frame.config(bg=pastel)
    frame_notas.config(bg=pastel)
    frame3.config(bg=pastel)
    frame_botones.config(bg=pastel)
    
    label_comentarios.config(bg=pastel, fg=rosa_fucsia)
    label_contacto.config(bg=pastel, fg=rosa_fucsia)
    label_evento.config(bg=pastel, fg=rosa_fucsia)
    label_fecha.config(bg=pastel, fg=rosa_fucsia)
    label_id.config(bg=pastel, fg=rosa_fucsia)
    label_ubicacion.config(bg=pastel, fg=rosa_fucsia)

    entry_evento.config(bg=verde_agua, fg=rosa_fucsia)
    entry_contacto.config(bg=verde_agua, fg=rosa_fucsia)
    entry_fecha.config(bg=verde_agua, fg=rosa_fucsia)
    entry_id.config(bg=verde_agua, fg=rosa_fucsia)
    entry_ubicacion.config(bg=verde_agua, fg=rosa_fucsia)
    campo_comentarios.config(bg=verde_agua, fg=rosa_fucsia)
    notas.config(bg=verde_agua, fg=rosa_fucsia)
    
    boton_agg.config(bg=verde_agua, fg=rosa_fucsia)
    boton_editar.config(bg=verde_agua, fg=rosa_fucsia)
    boton_leer.config(bg=verde_agua, fg=rosa_fucsia)
    boton_eliminar.config(bg=verde_agua, fg=rosa_fucsia)
    
def tema_oscuro():
    root.config(bg='black')
    frame.config(bg='black')
    frame_notas.config(bg='black')
    frame3.config(bg='black')
    frame_botones.config(bg='black')

    label_comentarios.config(bg='black', fg=verde_hack)
    label_contacto.config(bg='black', fg=verde_hack)
    label_evento.config(bg='black', fg=verde_hack)
    label_fecha.config(bg='black', fg=verde_hack)
    label_id.config(bg='black', fg=verde_hack)
    label_ubicacion.config(bg='black', fg=verde_hack)

    entry_evento.config(bg=zone_gris, fg=verde_hack)
    entry_contacto.config(bg=zone_gris, fg=verde_hack)
    entry_fecha.config(bg=zone_gris, fg=verde_hack)
    entry_id.config(bg=zone_gris, fg=verde_hack)
    entry_ubicacion.config(bg=zone_gris, fg=verde_hack)
    campo_comentarios.config(bg=zone_gris, fg=verde_hack)
    notas.config(bg=zone_gris, fg=verde_hack)
    
    boton_agg.config(bg=zone_gris, fg=verde_hack)
    boton_editar.config(bg=zone_gris, fg=verde_hack)
    boton_leer.config(bg=zone_gris, fg=verde_hack)
    boton_eliminar.config(bg=zone_gris, fg=verde_hack)

def elim_selec():
    eleccion = notas.curselection()

    for i in eleccion:
        notas.delete(i)

def ver_todos():
    crearcon=sqlite3.connect("BBDD7")
    crearcursor=crearcon.cursor()

    crearcursor.execute("SELECT * FROM DATOS_EVENTOS")
    impresion=crearcursor.fetchall()
    crearcon.commit()
    
    if impresion != []:

        for i in impresion:
            notas.insert(0, i)
    else:
        messagebox.showerror("BBDD", "La base de datos esta vacía.")

def vaciar_bbdd():
    advertencia = messagebox.askquestion("BBDD", "Esto eliminará todos los eventos y registros\n                 de la base de datos.\n\n                   Desea continuar?")

    if advertencia == 'yes':
        
        crearcon=sqlite3.connect("BBDD7")
        crearcursor=crearcon.cursor()

        crearcursor.execute('DELETE FROM DATOS_EVENTOS')
        crearcon.commit()
    

#botones
frame_botones = Frame(width=400, height=100)
frame_botones.grid(columnspan=3)

boton_agg = Button(frame_botones, text='Agregar', width=6, cursor='hand2', command=agregar)
boton_agg.grid(row=0, column=0, padx=20, pady=3)

boton_editar = Button(frame_botones, text='Editar', cursor='hand2', width=6, command=editar)
boton_editar.grid(row=0, column=2, padx=20, pady=3)

boton_leer = Button(frame_botones, text='Leer', width=6, cursor='hand2', command=lectura)
boton_leer.grid(row=0, column=1, padx=20, pady=3)

boton_eliminar = Button(frame_botones, text='Eliminar', width=6, cursor='hand2', command=eliminar)
boton_eliminar.grid(row=0, column=3, padx=20, pady=3)


#campos
frame3 = Frame(width=400, height=200)
frame3.grid(columnspan=3, rowspan=10)

texto_id = StringVar()
texto_evento = StringVar()
texto_fecha = StringVar()
texto_ubicacion = StringVar()
texto_contacto = StringVar()

label_id = Label(frame3, text='ID:', font=('Agency FB', 20))
label_id.grid(row=0)
entry_id = Entry(frame3, textvariable=texto_id)
entry_id.grid(row=0, column=1, pady=20, padx=3, sticky='w')   

label_evento = Label(frame3, text='Evento:', font=('Agency FB', 20))
label_evento.grid(row=1)
entry_evento = Entry(frame3, textvariable=texto_evento)
entry_evento.grid(row=1, column=1, pady=20, padx=3, sticky='w')   

label_fecha = Label(frame3, text='Fecha:', font=('Agency FB', 20))
label_fecha.grid(row=2)
entry_fecha = Entry(frame3, textvariable=texto_fecha)
entry_fecha.grid(row=2, column=1, pady=20, padx=3, sticky='w')   

label_ubicacion = Label(frame3, text='Ubicacion:', font=('Agency FB', 20))
label_ubicacion.grid(row=3)
entry_ubicacion = Entry(frame3, textvariable=texto_ubicacion)
entry_ubicacion.grid(row=3, column=1, pady=20, padx=3, sticky='w')  

label_contacto = Label(frame3, text='Contacto:', font=('Agency FB', 20))
label_contacto.grid(row=4)
entry_contacto = Entry(frame3, textvariable=texto_contacto)
entry_contacto.grid(row=4, column=1, pady=20, padx=3, sticky='w')  

campo_comentarios = Text(frame3, height=5, width=16)
campo_comentarios.grid(row=5, column=1, pady=20, padx=3, sticky='e')
label_comentarios = Label(frame3, text="Comentarios:", font=('Agency FB', 20))
label_comentarios.grid(row=5)


#menus
barraMenu = Menu(root)
root.config(menu=barraMenu)

menu_bbdd = Menu(barraMenu,tearoff=0)
menu_bbdd.add_command(label='Conectar', command=crearConexion)
menu_bbdd.add_command(label='Formatear', command=vaciar_bbdd)
menu_bbdd.add_command(label='Salir', command=salirPrograma)

menu_limpiar = Menu(barraMenu, tearoff=0)
menu_limpiar.add_command(label='Limpiar campos', command=limpiarCampos)
menu_limpiar.add_command(label='Limpiar eventos', command=limpiarEventos)
menu_limpiar.add_command(label='Limpiar todo', command=limpiarTodos)
menu_limpiar.add_command(label='Elim. Selec.', command=elim_selec)

menu_tema = Menu(barraMenu, tearoff=0)
menu_tema.add_command(label='Por defecto', command=tema_default)
menu_tema.add_command(label='Chillón', command=tema_claro)
menu_tema.add_command(label='Hacker', command=tema_oscuro)


menu_crud = Menu(barraMenu, tearoff=0)
menu_crud.add_command(label='Agregar', command=agregar)
menu_crud.add_command(label='Leer', command=lectura)
menu_crud.add_command(label='Editar', command=editar)
menu_crud.add_command(label='Eliminar', command=eliminar)
menu_crud.add_command(label='Ver todo', command=ver_todos)

barraMenu.add_cascade(label='Base de Datos', menu=menu_bbdd)
barraMenu.add_cascade(label='CRUD', menu=menu_crud)
barraMenu.add_cascade(label='Limpiar', menu=menu_limpiar)
barraMenu.add_cascade(label='Temas', menu=menu_tema)



#notas
frame_notas = Frame(root, width=400, height=400)
frame_notas.grid(columnspan=4)

notas = Listbox(frame_notas, width=40, font=("Consolas", 12))
notas.grid(row=5, column=0, columnspan=2, pady=20)




root.mainloop()