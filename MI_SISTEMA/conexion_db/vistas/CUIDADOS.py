from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkinter import messagebox

class VistaCuidados(ttk.Frame):
   def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       
       self.Label_title = Label(self,text="CUIDADOS ",font=("Arial Black",15)).place(x=350, y=10)
       #self.Label_title = Label(self,text="---------------------------------------------------------------------------------------------------------------",font=("Arial ",15)).place(x=10, y=40)

       self.miImafen=PhotoImage(file="img/logo.png").subsample(3)
       self.label_im= Label(self,image=self.miImafen).place(x=700,y=10)

       #LABELS IZQUIERDA 
       self.varCod=StringVar()
       Label(self,text = "Codigo consulta :",font=("Arial ",13)).place(x=30,y=70)
       self.entry_COD = Entry (self,textvariable=self.varCod,state="readonly")
       self.entry_COD.place(x=200,y=70)
       
       self.varABONO=StringVar()
       Label(self,text = "Codigo Abonos :",font=("Arial ",13)).place(x=30,y=110)
       self.entry_CODAR = Entry (self,textvariable=self.varABONO,state="readonly")
       self.entry_CODAR.place(x=200,y=110)
       
       self. varPLAGAS=StringVar()
       Label(self,text = "Codigos Plagas :",font=("Arial ",13)).place(x=30,y=150)
       self.entry_TOTAL = Entry (self,textvariable=self.varPLAGAS,state="readonly")
       self.entry_TOTAL.place(x=200,y=150)

       self.tabla=ttk.Treeview(self,columns=('','',''))
       self.tabla.place(x=5,y=300)
       self.tabla.heading('#0',text="CODIGO")
       self.tabla.heading('#1',text="CODIGO ABONO")
       self.tabla.heading('#2',text="CODIGO PLAGA")

       scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.tabla.yview)
       scrollbar.place(x=860,y=300)
       scrollbar1 = ttk.Scrollbar(self, orient=HORIZONTAL, command=self.tabla.xview)
       scrollbar1.place(x=100,y=520)
       self.tabla.configure(xscrollcommand=scrollbar1.set,yscrollcommand=scrollbar.set)
       
       #---------------------CONEXION-------------
       import cx_Oracle
       conn_str='USR_CONSUL_TREE/PassConsul@localhost:1521/xepdbtree'
       db_conn = cx_Oracle.connect(conn_str)
       cursor = db_conn.cursor()
      
      #-------------------------------------------------------------------------

      #BOTONES

       def BotonMostar():
           #LIMPIAR DATOS
           recorrer_tabla =self.tabla.get_children()
           for elementos in recorrer_tabla:
               self.tabla.delete(elementos)

           cursor = db_conn.cursor()
           cursor.execute('SELECT * FROM CUIDADOS')
           registros = cursor.fetchall()

           for CUIDADOS in registros:
               self.tabla.insert('',0,text=CUIDADOS[0],value=(CUIDADOS[1],CUIDADOS[2]))
       
       def BotonBorrar():
           self.entry_COD.config(state="readonly")
           self.entry_CODAR.config(state="readonly")
           self.entry_TOTAL.config(state="readonly")
           

           confirm= MessageBox.askyesnocancel(message="¿Esta seguro de eliminarlo?", title="Confirmacion")
            #print(confirm)
           if (confirm == TRUE):
               cursor =db_conn.cursor()
            
               codigo =self.tabla.item(self.tabla.selection())['text']
               query ="DELETE FROM CUIDADOS WHERE CUIDADOS_ID ='%s'"%codigo
            
               cursor.execute(query)
               db_conn.commit() 

               MessageBox.showinfo("BORRAR","Informacion eliminada con exito ")
               BotonMostar()

       def EliminarDatos():
           self.entry_COD.delete(0,END)
           self.entry_CODAR.delete(0,END)
           self.entry_TOTAL.delete(0,END)
            
       def BotonGuardar():

         if (self.entry_COD == ""): #or self.entry_ID == ""):
           MessageBox.showerror("ERROR","INSERTE DATOS") 
         else:
           try:
              cursor = db_conn.cursor()

              codigo=self.varCod.get()
              codar =self.varABONO.get()
              codtotal=self.varPLAGAS.get()
          
              cursor.execute("INSERT INTO CUIDADOS VALUES ('CUID{}','{}','{}')".format(codigo,codar,codtotal))
           
              MessageBox.showinfo("EXITO","DATOS GUARDADOS CON EXITO") 
              BotonMostar()
              db_conn.commit()
           except:
               MessageBox.showerror("ERROR","VERIFIQUE QUE LOS DATOS NO SE REPITAN ") 

       def BotonAgregar():
           EliminarDatos()
           self.entry_COD.config(state="normal")
           self.entry_CODAR.config(state="normal")
           self.entry_TOTAL.config(state="normal")

           Button(self,text="GUARDAR",command =BotonGuardar,font=("Arial Black",9)).place(x=650, y=200)
        
       Button(self,text="Mostar",command =BotonMostar,font=("Arial Black",9)).place(x=500, y=80)
       #Button(self,text="Editar",command =BotonEditar,font=("Arial Black",9)).place(x=500, y=120) 
       Button(self,text="Agregar",command =BotonAgregar,font=("Arial Black",9)).place(x=500, y=160) 
       Button(self,text="Borrar",command =BotonBorrar,font=("Arial Black",9)).place(x=500, y=200) 
