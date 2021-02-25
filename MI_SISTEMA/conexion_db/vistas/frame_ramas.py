
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
class VistaRamas(ttk.Frame):

   def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)

       self.Label_title = Label(self,text="Registrar nuevo tipo de ramas ",font=("Arial Black",15)).place(x=300, y=10) 
       
       
       Label(self,text="ID:",font=("Arial ",13)).place(x=100,y=100)
       self.VarID =StringVar()
       self.entry_ID = Entry (self,textvariable=self.VarID,state="readonly")
       self.entry_ID.place(x=250,y=100)

       Label(self,text = "Tipo de ramas :",font=("Arial ",13)).place(x=450,y=100)
       self. VarNombre=StringVar()
       self.entry_suelo = Entry (self,textvariable=self.VarNombre,state="readonly")
       self.entry_suelo.place(x=550,y=100)

       self.tabla=ttk.Treeview(self,columns=('',''))
       self.tabla.place(x=100,y=200)
       self.tabla.heading('#0',text="CODIGO")
       self.tabla.heading('#1',text="NOMBRE RAMAS ")
             
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
           cursor.execute('SELECT * FROM ESPE_RAMAS')
           registros = cursor.fetchall()
           
           for RAMAS in registros:
              self.tabla.insert('',0,text=RAMAS[0],value=(RAMAS[1],))
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
             ramas=self.VarNombre.get()
             # print(suelo)
             ident=self.VarID.get()
             #print(ident)
          
             query=("INSERT INTO ESPE_RAMAS VALUES ('RAMAS{}','{}')".format(ident,ramas))
             cursor.execute(query)

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
           # print(confirm)
            if (confirm == TRUE):
               cursor =db_conn.cursor()
            
               codigo =self.tabla.item(self.tabla.selection())['text']
               query ="DELETE FROM ESPE_RAMAS WHERE ARL_RAMAS_ID ='%s'"%codigo
            
               cursor.execute(query)
            
               db_conn.commit() 

               MessageBox.showinfo("BORRAR","Informacion eliminada con exito ")
               BotonMostar()
       
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
            cursor.execute("SELECT * FROM ESPE_RAMAS WHERE RAMAS_ID='{}'" .format(iden))
            registros = cursor.fetchall()
            print(registros)
            for ident in registros:
               self.identi.set(ident[0])
               self.VARnombre.set(ident[1])


            db_conn.commit()


       Button(self,text="Mostar",command =BotonMostar,font=("Arial Black",9)).place(x=100, y=150)
       Button(self,text="Agregar",command =BotonAgregar,font=("Arial Black",9)).place(x=200, y=150) 
       Button(self,text="Borrar",command =BotonBorrar,font=("Arial Black",9)).place(x=300, y=150) 
       Button(self,text="Buscar",command = BotonBuscar,font=("Arial Black",9)).place(x=500, y=150)
    