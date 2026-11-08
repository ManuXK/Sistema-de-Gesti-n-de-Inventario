from tkinter import *
from PIL import ImageTk, Image, ImageWin #py -m pip install pillow
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
conexion=mysql.connector.connect(host="localhost",port=3306,user="root",password="")
conex=conexion.cursor()
conex.execute("CREATE DATABASE IF NOT EXISTS sistemaventas")
conex.close()
conexion=mysql.connector.connect(host="localhost",port=3306,database="sistemaventas",user="root",password="")
conex=conexion.cursor()
conex.execute("CREATE TABLE IF NOT EXISTS inventario(codigo VARCHAR(50)PRIMARY KEY,producto VARCHAR(50),precio VARCHAR(50),cantidad INT(20))")
#conex.execute("INSERT INTO inventario (codigo,producto,precio,cantidad)values('789','Leche Condensada','400','5')")
conexion.commit()
conex.close()
conexion=mysql.connector.connect(host="localhost",port=3306,database="sistemaventas",user="root",password="")
conex=conexion.cursor() 
#conex.execute("CREATE TABLE IF NOT EXISTS clientes(cedula VARCHAR(50)PRIMARY KEY,nombre VARCHAR(50),sexo VARCHAR(50),estado VARCHAR(20),provincia VARCHAR(20),canton VARCHAR(20),distrito VARCHAR(20),ocupacion VARCHAR(20),correo VARCHAR(20),telefono INT(20))")
conex.close()
def inventa():
    inven=Tk()
    inven.title("Pantalla de Inventario")
    inven.geometry("600x450")
    inven.config(bg="purple")
    codigo=Label(inven,text="Codigo",font=("Arial",20,"bold")).place(x=20,y=10)
    txt_codigo=Entry(inven,font=("Arial",20,"bold"),bd=2,width=10)
    txt_codigo.place(x=130,y=10)

    producto=Label(inven,text="Producto",font=("Arial",20,"bold")).place(x=20,y=70)
    txt_producto=Entry(inven,font=("Arial",20,"bold"),bd=2,width=34)
    txt_producto.place(x=160,y=70)
    
    precio=Label(inven,text="Precio",font=("Arial",20,"bold")).place(x=20,y=120)
    txt_precio=Entry(inven,font=("Arial",20,"bold"),bd=2,width=10)
    txt_precio.place(x=140,y=120)
    
    cantidad=Label(inven,text="Cantidad",font=("Arial",20,"bold")).place(x=350,y=120)
    txt_cantidad=Entry(inven,font=("Arial",20,"bold"),bd=2,width=7)
    txt_cantidad.place(x=480,y=120)
    txt_codigo.bind("<Return>",lambda event:consultar_datos())
    def consultar_datos():
        conex=conexion.cursor()
        conex.execute("select * from inventario where codigo='{}'".format(txt_codigo.get()))
        datos=conex.fetchall()
        conex.close()
        for columna in datos:
             if(txt_codigo.get()==columna[0]):
                txt_producto.insert(0,columna[1])
                txt_precio.insert(0,columna[2])
                txt_cantidad.insert(0,columna[3])
                txt_codigo.focus()
                break
                
    btn_consultar=Button(inven,text="Consultar",font=("Agency Fb",18,"bold"),command=consultar_datos)
    btn_consultar.place(x=300,y=8)
    
    def agregar_datos():
        conex=conexion.cursor()
        conex.execute("insert into inventario(codigo,producto,precio,cantidad)values('{}','{}','{}','{}')".format(txt_codigo.get(),txt_producto.get(),txt_precio.get(),txt_cantidad.get()))
        conexion.commit()
        conex.close()
        messagebox.showinfo(message="El producto se agregó en forma exitosa",title="Nuevo Producto")
        txt_codigo.delete(0,END)
        txt_producto.delete(0,END)
        txt_precio.delete(0,END)
        txt_cantidad.delete(0,END)
        txt_codigo.focus()
    btn_agregar=Button(inven,text="Agregar",font=("Agency Fb",18,"bold"),command=agregar_datos)
    btn_agregar.place(x=10,y=180)

    def modificar_producto():    
        conex=conexion.cursor()
        sistemaventas=txt_producto.get(),txt_precio.get(),txt_cantidad.get(),txt_codigo.get()
        conex.execute("update inventario set producto=%s,precio=%s,cantidad=%s where codigo=%s",sistemaventas)
        conexion.commit()
        conex.close()
        messagebox.showinfo(message="El producto se modificó en forma exitosa",title="Modificando Producto")
        txt_codigo.delete(0,END)
        txt_producto.delete(0,END)    
        txt_precio.delete(0,END)
        txt_cantidad.delete(0,END)
        txt_codigo.focus()
    btn_modificar=Button(inven,text="Modificar",font=("Agency Fb",18,"bold"),command=modificar_producto)
    btn_modificar.place(x=200,y=180)

    def eliminar_producto():
        conex=conexion.cursor()
        conex.execute("delete from inventario where codigo='{}'".format(txt_codigo.get()))
        conexion.commit()
        conex.close()
        messagebox.showinfo(message="El producto se eliminó en forma exitosa",title="Eliminando Producto")
        txt_codigo.delete(0,END)
        txt_producto.delete(0,END)
        txt_precio.delete(0,END)
        txt_cantidad.delete(0,END)
        txt_codigo.focus()
    btn_eliminar=Button(inven,text="Eliminar",font=("Agency Fb",18,"bold"),command=eliminar_producto)
    btn_eliminar.place(x=400,y=180)
    
    
                    

        
def ventas():
    bro_ventas=Tk()
    bro_ventas.title("Pantalla de Ventas")
    bro_ventas.geometry("1050x600")
    bro_ventas.config(bg="cadetblue")
    eti_codigo=Label(bro_ventas,text="CÓDIGO",bg="cadetblue",font=("calibri",18,"bold"))
    eti_codigo.place(x=20,y=30)
    txt_codigo=Entry(bro_ventas,font=("calibri",18,"bold"),bd=3)
    txt_codigo.place(x=120,y=30)
    lista_productos=ttk.Treeview(bro_ventas,style="mystyle.Treeview",columns=(1,2,3,4,5),height=9,show='headings')
    lista_productos.place(x=20,y=80)
    lista_productos.column(1,width=200,anchor=CENTER)
    lista_productos.heading(1,text='CODIGO',anchor=CENTER)
    lista_productos.column(2,width=200,anchor=CENTER)
    lista_productos.heading(2,text='ARTICULO',anchor=CENTER)
    lista_productos.column(3,width=200,anchor=CENTER)
    lista_productos.heading(3,text='PRECIO',anchor=CENTER)
    lista_productos.column(4,width=200,anchor=CENTER)
    lista_productos.heading(4,text='CANT',anchor=CENTER)
    lista_productos.column(5,width=200,anchor=CENTER)
    lista_productos.heading(5,text='TOTAL',anchor=CENTER)
    barra=ttk.Scrollbar(bro_ventas,orient="vertical")
    barra.place(x=1023,y=80,height=305)
    lista_productos.configure(yscrollcommand=barra.set)
    tema=ttk.Style(lista_productos)
    tema.theme_use("clam")
    tema.configure("Treeview.Heading",background="turquoise",foreground="black",font=("calibri",13,"bold"))
    tema.configure("Treeview",font=("calibri",16,"bold"),rowheight=30)
    eti_subtotal=Label(bro_ventas,text="SubTotal",bg="cadetblue",font=("calibri",24,"bold"))
    eti_subtotal.place(x=700,y=400)
    txt_subtotal=Entry(bro_ventas,font=("calibri",18,"bold"),bd=3,width=15)
    txt_subtotal.place(x=830,y=400)
    eti_efectivo=Label(bro_ventas,text="Paga con",bg="cadetblue",font=("calibri",24,"bold"))
    eti_efectivo.place(x=700,y=450)
    txt_efectivo=Entry(bro_ventas,font=("calibri",18,"bold"),bd=3,width=15)
    txt_efectivo.place(x=830,y=450)
    eti_cambio=Label(bro_ventas,text="Su cambio",bg="cadetblue",font=("calibri",24,"bold"))
    eti_cambio.place(x=690,y=500)
    txt_cambio=Entry(bro_ventas,font=("calibri",18,"bold"),bd=3,width=15)
    txt_cambio.place(x=830,y=500)
    def buscar_codigo():
        conex=conexion.cursor()
        conex.execute("select * from inventario")
        datos=conex.fetchall()
        cod=""
        prod=""
        prec=0
        cant=1
        subtotal=0
        for fila in datos:
            if txt_codigo.get()==fila[0]:
                cod=fila[0]
                prod=fila[1]
                prec=fila[2]
                txt_codigo.delete(0,END)
                txt_codigo.focus()
                break;
        revisar_compras=lista_productos.get_children()
        producto_en_lista_productos=0
        
        for lista in revisar_compras:
            if (lista_productos.item(lista)['values'][0]==int(cod)):
                nueva_cant=lista_productos.item(lista)['values'][3]+int(1)
                calculo=lista_productos.item(lista)['values'][2]*int(nueva_cant)
                lista_productos.item(lista,values=(cod,prod,prec,nueva_cant,calculo))
                #subtotal=subtotal+lista_productos.item(lista)['values'][4]
                txt_subtotal.delete(0,END)
                #txt_subtotal.insert(0,subtotal)
                producto_en_lista_productos=1
                
        if producto_en_lista_productos==0:
            lista_productos.insert("",0,values=(cod,prod,prec,cant,prec))
        revisar_compras=lista_productos.get_children()
        for lista in revisar_compras:
            subtotal=subtotal+lista_productos.item(lista)['values'][4]
        txt_subtotal.delete(0,END)
        txt_subtotal.insert(0,subtotal)
        if (txt_efectivo.get()>"0"):
             vuelto()
    def vuelto():
        cambio=int(txt_efectivo.get())-int(txt_subtotal.get())
        txt_cambio.delete(0,END)
        txt_cambio.insert(0,cambio)
    txt_efectivo.bind("<Return>", lambda event:vuelto())                            
    txt_codigo.bind("<Return>", lambda event:buscar_codigo())
    
def contabilidad():
    bro_conta=Tk()
    bro_conta.title("Pantalla de Contabilidad")
    bro_conta.geometry("600x450")
    bro_conta.config(bg="pink")

def ayuda():
    bro_ayuda=Tk()
    bro_ayuda.title("Pantalla de Ayuda")
    bro_ayuda.geometry("600x450")
    bro_ayuda.config(bg="turquoise")
    eti=Label(bro_ayuda,text="Creditos del Autor",bg="turquoise",fg="black",font=("Arial",20,"bold"))
    eti.place(x=20,y=10)
 
def clientes():
    bro_clientes=Tk()
    bro_clientes.title("Pantalla de Contabilidad")
    bro_clientes.geometry("1000x700")
    bro_clientes.config(bg="cadetblue")
    bro_clientes.title("Pantalla de Clientes")
    
    cedula=Label(bro_clientes,text="Cédula",font=("Arial",17,"bold")).place(x=20,y=10)
    txt_cedula=Entry(bro_clientes,font=("Arial",20,"bold"),bd=2,width=10)
    txt_cedula.place(x=115,y=10)

    nombre=Label(bro_clientes,text="Nombre",font=("Arial",17,"bold")).place(x=20,y=70)
    txt_nombre=Entry(bro_clientes,font=("Arial",20,"bold"),bd=2,width=10)
    txt_nombre.place(x=115,y=70)

    sexo=Label(bro_clientes,text="Sexo",font=("Arial",17,"bold")).place(x=20,y=130)
    lista_sexo=ttk.Combobox(bro_clientes,values=["Masculino","Femenino","Prefiero no decir"],width=15,font=("Arial",16,"bold"))
    lista_sexo.place(x=115,y=130)

    estado=Label(bro_clientes,text="Estado Civil",font=("Arial",17,"bold")).place(x=350,y=130)
    lista_estado=ttk.Combobox(bro_clientes,values=["Soltero/a","Casado/a","Divorciado/a","Viudo/a"],width=12,font=("Arial",16,"bold"))
    lista_estado.place(x=500,y=130)

    eti=Label(bro_clientes,text="Dirección",bg="cadetblue",fg="black",font=("Arial",20,"bold"))
    eti.place(x=20,y=175)

    provincia=Label(bro_clientes,text="Provincia",font=("Arial",17,"bold")).place(x=20,y=220)
    lista_provincia=ttk.Combobox(bro_clientes,values=["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"],font=("Arial",13,"bold"),width=10)
    lista_provincia.place(x=140,y=225)

    canton=Label(bro_clientes,text="Cantón",font=("Arial",17,"bold")).place(x=330,y=220)
    lista_canton=ttk.Combobox(bro_clientes,font=("Arial",13,"bold"),width=10)
    lista_canton.place(x=450,y=225)

    distrito=Label(bro_clientes,text="Distrito",font=("Arial",17,"bold")).place(x=630,y=220)
    lista_distrito=ttk.Combobox(bro_clientes,font=("Arial",15,"bold"))
    lista_distrito.place(x=750,y=225)

    ocupacion=Label(bro_clientes,text="Ocupación",font=("Arial",17,"bold")).place(x=20,y=300)
    lista_ocupacion=ttk.Combobox(bro_clientes,values=["Médico","Ingeniero","Abogado","Contador","Informático","Electricista"],width=15,font=("Arial",16,"bold"))
    lista_ocupacion.place(x=160,y=300)

    correo=Label(bro_clientes,text="Correo",font=("Arial",17,"bold")).place(x=20,y=350)
    txt_correo=Entry(bro_clientes,font=("Arial",20,"bold"),bd=2,width=25)
    txt_correo.place(x=115,y=350)

    telefono=Label(bro_clientes,text="Teléfono",font=("Arial",17,"bold")).place(x=515,y=350)
    txt_telefono=Entry(bro_clientes,font=("Arial",20,"bold"),bd=2,width=10)
    txt_telefono.place(x=630,y=350)

    sanjose=["Curridabat","Desamparados","Escazú"]
    alajuela=["Naranjo","Atenas","Grecia"]
    cartago=["Oreamuno","Paraíso","Turrialba"]
    heredia=["Sarapiquí","Barva","San Rafael"]
    guanacaste=["Liberia","Nicoya","Santa Cruz"]
    puntarenas=["Golfito","Esparza","Buenos Aires"]
    limon=["Pococí","Siquirres","Talamanca"]

    def canton(event):
        if(lista_provincia.get()=="San José"):
            lista_canton.delete(0,END)
            lista_distrito.delete(0,END)
            lista_canton.configure(values=())
            lista_canton.configure(values=sanjose)
        elif(lista_provincia.get()=="Alajuela"):
            lista_canton.delete(0,END)
            lista_distrito.delete(0,END)
            lista_canton.configure(values=())
            lista_canton.configure(values=alajuela)
        elif(lista_provincia.get()=="Cartago"):
            lista_canton.delete(0,END)
            lista_distrito.delete(0,END)
            lista_canton.configure(values=())
            lista_canton.configure(values=cartago)
        elif(lista_provincia.get()=="Heredia"):
            lista_canton.delete(0,END)
            lista_distrito.delete(0,END)
            lista_canton.configure(values=())
            lista_canton.configure(values=heredia)
        elif(lista_provincia.get()=="Guanacaste"):
            lista_canton.delete(0,END)
            lista_distrito.delete(0,END)
            lista_canton.configure(values=())
            lista_canton.configure(values=guanacaste)
        elif(lista_provincia.get()=="Puntarenas"):
            lista_canton.delete(0,END)
            lista_distrito.delete(0,END)
            lista_canton.configure(values=())
            lista_canton.configure(values=puntarenas)
        elif(lista_provincia.get()=="Limón"):
            lista_canton.delete(0,END)
            lista_distrito.delete(0,END)
            lista_canton.configure(values=())
            lista_canton.configure(values=limon)
    lista_provincia.bind("<<ComboboxSelected>>",canton)

    #San Jose
    curri=["Sanchéz","Granadilla","Tirrases"]
    desampa=["San Rafael Arriba","San Antonio","Patarrá","Los Guidos"]
    escazu=["Escazú","San Antonio","San Rafael"]
    #Alajuela
    alajuela=["San Antonio","Guácima","San Isidro","Turrúcares","Tambor","Sarapiquí"]
    atenas=["Atenas","Jesús","Mercedes","San Isidro","Concepción","San José","Santa Eulalia","Escobal"]
    grecia=["Grecia","San Isidro","San José","San Roque","Tacares","Puente de Piedra","Bolivar"]
    #Cartago
    cartago=["Oriental","Occidental","Carmen","San Nicolás","Guadalupe","Tierra Blanca","Dulce Nombre","Quebradilla"]
    paraiso=["Paraíso","Santiago","Orosi","Cachí","Santa Lucía"]
    turrialba=["La Suiza","Peralta","Santa Cruz","Santa Teresita","Pavones","Tayutic","Tres Equis","Chirripó"]
    #Heredia
    heredia=["Heredia","San Francisco","Mercedes","Ulloa","Varablanca"]
    barva=["Barva","San Pablo","San Roque","Santa Lucía","San Pedro","San José de la Montaña"]
    sanra=["San Rafael","San Josecito","Santiago","Los Ángeles","Concepción"]
    #Guanacaste
    liberia=["Liberia","Cañas Dulces","Mayorga","Nacascolo","Curubandé"]
    nicoya=["Nicoya","Mansión","San Antonio","Quebrada Honda","Sámara","Nosara","Belén de Nosarita"]
    santacruz=["Santa Cruz","Bolsón","Veintisiete de Abril","Tempate","Cartagena","Cuajiniquil","Diriá","Cabo Velas","Tamarindo"]
    #Puntarenas
    puntarenas=["Paquera","Manzanillo","Barranca","Isla del Coco","Cóbano","Acapulco","El Roble"]
    esparza=["Espírito Santo","San Juan Grande","Macacona","San Rafael","San Jerónimo","Caldera"]
    buenosaire=["Buenos Aires","Volcán","Potrero Grande","Boruca","Pilas","Colinas","Chánguena","Biolley","Brunka"]
    #Limón
    pococi=["Guápiles","Jiménez","La Rita","Roxana","Cariari","Colorado","La Colonia"]
    siquirres=["Siquirres","Pacuario","Florida","Germania","Cairo"]
    talamanca=["Cahuita","Bratsi","Telire","Sixaola"]

    def distrito(event):
        if(lista_canton.get()=="Curridabat"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=curri)
        elif(lista_canton.get()=="Desamparados"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=desampa)
        elif(lista_canton.get()=="Escazú"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=escazu)
        elif(lista_canton.get()=="Alajuela"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=alajuela)
        elif(lista_canton.get()=="Atenas"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=atenas)
        elif(lista_canton.get()=="Grecia"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=grecia)
        elif(lista_canton.get()=="Cartago"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=cartago)
        elif(lista_canton.get()=="Paraíso"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=paraiso)
        elif(lista_canton.get()=="Turrialba"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=turrialba)
        elif(lista_provincia.get()=="Heredia"):
            lista_canton.delete(0,END)
            lista_canton.configure(values=())
            lista_canton.configure(values=heredia)
        elif(lista_provincia.get()=="Barva"):
            lista_canton.delete(0,END)
            lista_canton.configure(values=())
            lista_canton.configure(values=barva)
        elif(lista_provincia.get()=="San Rafael"):
            lista_canton.delete(0,END)
            lista_canton.configure(values=())
            lista_canton.configure(values=sanra)
        elif(lista_canton.get()=="Liberia"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=liberia)
        elif(lista_canton.get()=="Nicoya"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=nicoya)
        elif(lista_canton.get()=="Santa Cruz"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=santacruz)
        elif(lista_canton.get()=="Puntarenas"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=punta)
        elif(lista_canton.get()=="Esparza"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=esparza)
        elif(lista_canton.get()=="Buenos Aires"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=buenosaire)
        elif(lista_canton.get()=="Pococí"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=pococi)
        elif(lista_canton.get()=="Siquirres"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=siquirres)
        elif(lista_canton.get()=="Talamanca"):
            lista_distrito.delete(0,END)
            lista_distrito.configure(values=())
            lista_distrito.configure(values=talamanca)
    lista_canton.bind("<<ComboboxSelected>>",distrito)

    def agregar_cliente():
        conex=conexion.cursor()
        conex.execute("insert into clientes(cedula,nombre,sexo,estado,provincia,canton,distrito,ocupacion,correo,telefono)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(txt_cedula.get(),txt_nombre.get(),lista_sexo.get(),lista_estado.get(),lista_provincia.get(),lista_canton.get(),lista_distrito.get(),lista_ocupacion.get(),txt_correo.get(),txt_telefono.get()))
        conexion.commit()
        conex.close()
        messagebox.showinfo(message="El Cliente se agregó en forma exitosa",title="Nuevo Producto")
        txt_cedula.delete(0,END)
        txt_nombre.delete(0,END)
        lista_sexo.delete(0,END)
        lista_estado.delete(0,END)
        lista_provincia.delete(0,END)
        lista_canton.delete(0,END)
        lista_distrito.delete(0,END)
        lista_ocupacion.delete(0,END)    
        txt_correo.delete(0,END)
        txt_telefono.delete(0,END)
        txt_cedula.focus()


    def modificar_cliente():
        conex=conexion.cursor()
        sistemaventas=txt_nombre.get(),lista_sexo.get(),lista_estado.get(),lista_provincia.get(),lista_canton.get(),lista_distrito.get(),lista_ocupacion.get(),txt_correo.get(),txt_telefono.get(),txt_cedula.get()
        conex.execute("update clientes set nombre=%s,sexo=%s,estado=%s,provincia=%s,canton=%s,distrito=%s,ocupacion=%s,correo=%s,telefono=%s where cedula=%s",sistemaventas)
        conexion.commit()
        conex.close()
        messagebox.showinfo(message="El cliente se modificó en forma exitosa",title="Modificando Cliente")
        txt_cedula.delete(0,END)
        txt_nombre.delete(0,END)
        lista_sexo.delete(0,END)
        lista_estado.delete(0,END)
        lista_provincia.delete(0,END)
        lista_canton.delete(0,END)
        lista_distrito.delete(0,END)
        lista_ocupacion.delete(0,END)    
        txt_correo.delete(0,END)
        txt_telefono.delete(0,END)
        txt_cedula.focus()

    def eliminar_cliente():
        conex=conexion.cursor()
        conex.execute("delete from clientes where cedula='{}'".format(txt_cedula.get()))
        conexion.commit()
        conex.close()
        messagebox.showinfo(message="El cliente se eliminó en forma exitosa",title="Eliminando Cliente")
        txt_cedula.delete(0,END)
        txt_nombre.delete(0,END)
        lista_sexo.delete(0,END)
        lista_estado.delete(0,END)
        lista_provincia.delete(0,END)
        lista_canton.delete(0,END)
        lista_distrito.delete(0,END)
        lista_ocupacion.delete(0,END)    
        txt_correo.delete(0,END)
        txt_telefono.delete(0,END)
        txt_cedula.focus()

    def buscar_datos():
        conex=conexion.cursor()
        conex.execute("select * from clientes where cedula='{}'".format(txt_cedula.get()))
        datos=conex.fetchall()
        conex.close()
        for columna in datos:
             if(txt_cedula.get()==columna[0]):
                txt_nombre.insert(0,columna[1])
                lista_sexo.insert(0,columna[2])
                lista_estado.insert(0,columna[3])
                lista_provincia.insert(0,columna[4])
                lista_canton.insert(0,columna[5])
                lista_distrito.insert(0,columna[6])
                lista_ocupacion.insert(0,columna[7])
                txt_correo.insert(0,columna[8])
                txt_telefono.insert(0,columna[9])
                txt_cedula.focus()
                break
                
    btn_consultar=Button(bro_clientes,text="Consultar",font=("Agency Fb",18,"bold"),command=buscar_datos)
    btn_consultar.place(x=300,y=8)

        
    btn_agregar=Button(bro_clientes,text="Agregar",font=("Agency Fb",18,"bold"),command=agregar_cliente)
    btn_agregar.place(x=100,y=400)

    btn_modificar=Button(bro_clientes,text="Modificar",font=("Agency Fb",18,"bold"),command=modificar_cliente)
    btn_modificar.place(x=350,y=400)


    btn_eliminar=Button(bro_clientes,text="Eliminar",font=("Agency Fb",18,"bold"),command=eliminar_cliente)
    btn_eliminar.place(x=600,y=400)

    
ven=Tk()
ven.title("Pantalla Principal")
ven.state("zoomed")
fondo=Image.open("C:\\Users\\Estudiante\\Pictures\\fondo1.jpg")
traer_imagen=ImageTk.PhotoImage(fondo)
montar_imagen=Label(ven,image=traer_imagen)
montar_imagen.place(x=0,y=0)
barra_menu=Menu(ven)
ven.config(menu=barra_menu)
archivo_menu=Menu(barra_menu, tearoff=0)
#******************* barra de menu archivo
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Inventario", command=inventa, background="#00FFFF")
archivo_menu.add_separator()
archivo_menu.add_command(label="Clientes", command=clientes, background="#8904B1",foreground="white")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ven.destroy, background="red",foreground="white")

#******************* barra de menu sistema
sistema_menu=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Sistema", menu=sistema_menu)
sistema_menu.add_command(label="Registrar Ventas", command=ventas,background="#008000",foreground="white")
sistema_menu.add_separator()
sistema_menu.add_command(label="Contabilidad", command=contabilidad,background="#008080",foreground="white")
#*******************barra de menu ayuda
ayuda_menu=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)
ayuda_menu.add_command(label="Información sobre el sistema", command=ayuda,background="#800080",foreground="white")


