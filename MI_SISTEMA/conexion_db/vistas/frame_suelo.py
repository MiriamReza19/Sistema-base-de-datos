from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox

class VistaSuelo(ttk.Frame):

   def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       
       self.Label_title = Label(self,text="Registrar nuevo tipo de suelo ",font=("Arial Black",15)).place(x=300, y=10) 
       
       Label(self,text="ID:",font=("Arial ",13)).place(x=100,y=100)
       self.VarID =StringVar()
       self.entry_ID = Entry (self,textvariable=self.VarID,state="readonly")
       self.entry_ID.place(x=250,y=100)

       Label(self,text = "Tipo de suelo :",font=("Arial ",13)).place(x=450,y=100)
       self. VarNombre=StringVar()
       self.entry_suelo = Entry (self,textvariable=self.VarNombre,state="readonly")
       self.entry_suelo.place(x=550,y=100)

    
       self.tabla=ttk.Treeview(self,columns=('',''))
       self.tabla.place(x=100,y=200)
       self.tabla.heading('#0',text="CODIGO")
       self.tabla.heading('#1',text="NOMBRE SUELO")
             
       scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.tabla.yview)
       scrollbar.place(x=690,y=200)
       self.tabla.configure(yscrollcommand=scrollbar.set)
       #---------------------CONEXION-------------
       import cx_Oracle
       conn_str='USR_CONSUL_TREE/PassConsul@localhost:1521/xepdbtree'
       db_conn = cx_Oracle.connect(conn_str)
       cursor = db_conn.cursor()
       #--------------------------------------

       #BOTONES
       def BotonMostar():

           self.entry_suelo.config(state="readonly")
           self.entry_ID.config(state="readonly")
           #LIMPIAR DATOS
           recorrer_tabla =self.tabla.get_children()
           for elementos in recorrer_tabla:
               self.tabla.delete(elementos)

           cursor = db_conn.cursor()
           cursor.execute('SELECT * FROM SUELO')
           registros = cursor.fetchall()
           
           for SUELO in registros:
              self.tabla.insert('',0,text=SUELO[0],value=(SUELO[1],))
           #print(registros)
          
           db_conn.commit()

       def EliminarDatos():
            self.entry_suelo.delete(0,END)
            self.entry_ID.delete(0,END)

       def BotonGuardar():
         if (self.entry_suelo == ""): #or self.entry_ID == ""):
           MessageBox.showerror("ERROR","INSERTE DATOS") 
         else:
           try:  
               cursor = db_conn.cursor()
               suelo=self.VarNombre.get()
                # print(suelo)
               ident=self.VarID.get()
               #print(ident)
          
               query=("INSERT INTO SUELO VALUES ('SUELO{}','{}')".format(ident,suelo))
               cursor.execute(query,)

               MessageBox.showinfo("EXITO","DATOS GUARDADOS CON EXITO") 
               BotonMostar()
               db_conn.commit()
           except:
               MessageBox.showerror("ERROR","VERIFIQUE QUE LOS DATOS NO SE REPITAN ") 

       def BotonAgregar():
           EliminarDatos()
           self.entry_suelo.config(state="normal")
           self.entry_ID.config(state="normal")

           Button(self,text="GUARDAR",command =BotonGuardar,font=("Arial Black",9)).place(x=600, y=500)
           
           
       def BotonBorrar():
              
       #dentro de boton guardar
            confirm= MessageBox.askyesnocancel(message="¿Esta seguro de eliminarlo?", title="Confirmacion")
            #print(confirm)
            if (confirm == TRUE):
               cursor =db_conn.cursor()
            
               codigo =self.tabla.item(self.tabla.selection())['text']
               query =("DELETE FROM SUELO WHERE SUELO_ID ='{}'".format(codigo))
               cursor.execute(query)
            
               db_conn.commit() 

               MessageBox.showinfo("BORRAR","Informacion eliminada con exito ")
               BotonMostar()
           

        
       def BotonActualizar():
           cursor =db_conn.cursor()
          
           
           datos=self.VARnombre_nuevo.get()
           
           cursor.execute("UPDATE SUELO SET SUELO_NAME ='"+ self.VARnombre_nuevo.get() +"' WHERE SUELO_ID=" + self.entry_suelo.get())
            
           db_conn.commit() 
           
           self.ventana_editar.destroy()
           BotonMostar()

       def BotonEditar():

            codigo = self.tabla.item(self.tabla.selection())['text']
            nombre_antiguo = self.tabla.item(self.tabla.selection())['values']

            #VENTANA EXTRA
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar suelo")
            self.ventana_editar.geometry("300x200")
            self.ventana_editar.resizable(width=0, height=0)
            

            #campo de codigo
            
            self.label_codigo = Label(self.ventana_editar,text="Codigo suelo:")
            self.label_codigo.grid(row=0,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = codigo),state='readonly')
            self.entry_codigo.grid(row=0,column = 1,pady=10,padx=10)
            #print(self.entry_codigo)
             #campo de NOMBRE_antiguo
            self.label_nombre_antiguo  =Label(self.ventana_editar,text="Nombre antiguo:")
            self.label_nombre_antiguo.grid(row=1,column = 0, pady = 10 ,padx = 10)
            self.entry_nombre_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = nombre_antiguo),state='readonly')
            self.entry_nombre_antiguo.grid(row=1,column = 1,pady=10,padx=10)

            #campo de NOMBRE_nuevo

            self.label_nombre_nuevo = Label(self.ventana_editar,text="Nombre nuevo:")
            self.label_nombre_nuevo.grid(row=2,column = 0, pady = 10 ,padx = 10)
            self.VARnombre_nuevo =StringVar()
            self.entry_nombre_nuevo = Entry(self.ventana_editar)
            self.entry_nombre_nuevo.grid(row=2,column = 1,pady=10,padx=10)

            #Boton Actualizar 
            self.boton_act = Button(self.ventana_editar, text = "ACTUALIZAR ", command=BotonActualizar)
            self.boton_act.grid(row = 5, column = 0,pady = 10, padx = 10)

            BotonActualizar()
       
       def BotonBuscar():
           

            #VENTANA EXTRA
            self.ventana_ed = Toplevel()
            self.ventana_ed.title("Editar suelo")
            self.ventana_ed.geometry("300x200")
            self.ventana_ed.resizable(width=0, height=0)

            self.label_codigo = Label(self.ventana_ed,text="Codigo suelo:")
            self.label_codigo.grid(row=0,column = 0, pady = 10 ,padx = 10)
            self.identi =StringVar()
            self.entry_codigo = Entry(self.ventana_ed,textvariable=self.identi,state='normal')
            self.entry_codigo.grid(row=0,column = 1,pady=10,padx=10)

            self.label_nombre = Label(self.ventana_ed,text="Nombre nuevo:")
            self.label_nombre.grid(row=2,column = 0, pady = 10 ,padx = 10)
            self.VARnombre =StringVar()
            self.entry_nombre = Entry(self.ventana_ed,state="readonly",textvariable=self.VARnombre)
            self.entry_nombre.grid(row=2,column = 1,pady=10,padx=10)

            self.boton_act = Button(self.ventana_ed, text = "OKAY ", command= OKay)
            self.boton_act.grid(row = 5, column = 0,pady = 10, padx = 10)

            self.boton_cerrar = Button(self.ventana_ed, text = "CERRAR ", command= cerrar)
            self.boton_cerrar.grid(row = 5, column = 1,pady = 10, padx = 10)
       def cerrar():
           self.ventana_ed.destroy()
       def OKay():
             
            iden=self.identi.get()
            nom=self.VARnombre.get()
            
            print(iden)
            print(nom)
            cursor = db_conn.cursor()
           # cursor.execute("SELECT * FROM SUELO WHERE SUELO_ID="+ iden)
            cursor.execute("SELECT * FROM SUELO WHERE SUELO_ID='{}'" .format(iden))
            registros = cursor.fetchall()
            print(registros)
            for ident in registros:
               self.identi.set(ident[0])
               self.VARnombre.set(ident[1])


            db_conn.commit()
            

       Button(self,text="Mostar",command = BotonMostar,font=("Arial Black",9)).place(x=100, y=150)
       Button(self,text="Agregar",command = BotonAgregar,font=("Arial Black",9)).place(x=200, y=150) 
       Button(self,text="Borrar",command = BotonBorrar,font=("Arial Black",9)).place(x=300, y=150) 
       Button(self,text="Editar",command = BotonEditar,font=("Arial Black",9)).place(x=400, y=150) 
       Button(self,text="Buscar",command = BotonBuscar,font=("Arial Black",9)).place(x=500, y=150)