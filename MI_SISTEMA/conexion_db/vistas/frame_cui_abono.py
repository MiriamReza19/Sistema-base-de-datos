from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox


class VistaAbono(ttk.Frame):

   def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)

       self.Label_title = Label(self,text="Registrar nuevo tipo de abono ",font=("Arial Black",15)).place(x=300, y=10) 
       
       Label(self,text="ID:",font=("Arial ",13)).place(x=100,y=100)
       self.VarID =StringVar()
       self.entry_ID = Entry (self,textvariable=self.VarID,state="readonly")
       self.entry_ID.place(x=250,y=100)

       Label(self,text = "Tipo abono:",font=("Arial ",13)).place(x=450,y=100)
       self. VarNombre=StringVar()
       self.entry_suelo = Entry (self,textvariable=self.VarNombre,state="readonly")
       self.entry_suelo.place(x=550,y=100)

       self.tabla=ttk.Treeview(self,columns=('',''))
       self.tabla.place(x=100,y=200)
       self.tabla.heading('#0',text="CODIGO")
       self.tabla.heading('#1',text="NOMBRE ABONO ")
             
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
           cursor.execute('SELECT * FROM CUIDADOS_ABONO')
           registros = cursor.fetchall()
           
           for ABONO in registros:
              self.tabla.insert('',0,text=ABONO[0],value=(ABONO[1],))
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
             abono=self.VarNombre.get()
             # print(suelo)
             ident=self.VarID.get()
             #print(ident)
          
             query=("INSERT INTO CUIDADOS_ABONO VALUES ('ABONO{}','{}')".format(ident,abono))
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
               query ="DELETE FROM CUIDADO_ABONO WHERE ABONO_ID ='%s'"%codigo
            
               cursor.execute(query)
            
               db_conn.commit() 

               MessageBox.showinfo("BORRAR","Informacion eliminada con exito ")
               BotonMostar()
           



       Button(self,text="Mostar",command =BotonMostar,font=("Arial Black",9)).place(x=100, y=150)
       Button(self,text="Agregar",command =BotonAgregar,font=("Arial Black",9)).place(x=200, y=150) 
       Button(self,text="Borrar",command =BotonBorrar,font=("Arial Black",9)).place(x=300, y=150) 

    