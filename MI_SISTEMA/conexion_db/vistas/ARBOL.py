from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkinter import messagebox

class VistaTREE(ttk.Frame):
   def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       
       self.Label_title = Label(self,text="ARBOL ",font=("Arial Black",15)).place(x=350, y=10)
       #self.Label_title = Label(self,text="---------------------------------------------------------------------------------------------------------------",font=("Arial ",15)).place(x=10, y=40)

       self.miImafen=PhotoImage(file="img/logo.png").subsample(3)
       self.label_im= Label(self,image=self.miImafen).place(x=700,y=10)

      #LABELS IZQUIERDA 
       self.varCod=StringVar()
       Label(self,text = "Codigo consulta :",font=("Arial ",13)).place(x=30,y=70)
       self.entry_COD = Entry (self,textvariable=self.varCod,state="readonly")
       self.entry_COD.place(x=200,y=70)
       
       self.varCODAR=StringVar()
       Label(self,text = "Codigo Arbol :",font=("Arial ",13)).place(x=30,y=110)
       self.entry_CODAR = Entry (self,textvariable=self.varCODAR,state="readonly")
       self.entry_CODAR.place(x=200,y=110)
       
       self. varTOTAL=StringVar()
       Label(self,text = "Total :",font=("Arial ",13)).place(x=30,y=150)
       self.entry_TOTAL = Entry (self,textvariable=self.varTOTAL,state="readonly")
       self.entry_TOTAL.place(x=200,y=150)
       
       self.varCODCLIM=StringVar()
       Label(self,text = "Codigo clima :",font=("Arial ",13)).place(x=30,y=190)
       self.entry_CODCLIM = Entry (self,textvariable=self.varCODCLIM,state="readonly")
       self.entry_CODCLIM.place(x=200,y=190)
       
       self.varCODCUI=StringVar()
       Label(self,text = "Codigo cuidados :",font=("Arial ",13)).place(x=30,y=230)
       self.entry_CODCUI = Entry (self,textvariable=self.varCODCUI,state="readonly")
       self.entry_CODCUI.place(x=200,y=230)

       self.tabla=ttk.Treeview(self,columns=('','','','',''))
       self.tabla.place(x=5,y=300)
       self.tabla.heading('#0',text="CODIGO")
       self.tabla.heading('#1',text="CODIGO CLIMA")
       self.tabla.heading('#2',text="TOTAL")
       self.tabla.heading('#3',text="CODIGO ARBOLES")
       self.tabla.heading('#4',text="CODGIO CUIDADOS")

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
       #--------------------------------------

        #BOTONES

       def BotonMostar():
           self.entry_COD.config(state="readonly")
           self.entry_CODAR.config(state="readonly")
           self.entry_TOTAL.config(state="readonly")
           self.entry_CODCLIM.config(state="readonly")
           self.entry_CODCUI.config(state="readonly")
           #LIMPIAR DATOS
           recorrer_tabla =self.tabla.get_children()
           for elementos in recorrer_tabla:
               self.tabla.delete(elementos)

           cursor = db_conn.cursor()
           cursor.execute('SELECT * FROM CONSULTA_ARBOL')
           registros = cursor.fetchall()

           for CONSULTA_ARBOL in registros:
               self.tabla.insert('',0,text=CONSULTA_ARBOL[0],value=(CONSULTA_ARBOL[1],CONSULTA_ARBOL[2],CONSULTA_ARBOL[3],CONSULTA_ARBOL[4]))
          # print(registros)
           db_conn.commit()

       def BotonBorrar():

           confirm= MessageBox.askyesnocancel(message="¿Eta seguro de eliminarlo?", title="Confirmacion")
           print(confirm)
           if (confirm == TRUE):
               cursor =db_conn.cursor()
            
               codigo =self.tabla.item(self.tabla.selection())['text']
               query ="DELETE FROM CONSULTA_ARBOL WHERE CONSUL_ID ='%s'"%codigo
            
               cursor.execute(query)
            
               db_conn.commit() 

               MessageBox.showinfo("BORRAR","Informacion eliminada con exito ")
               BotonMostar()

       def EliminarDatos():
           self.entry_COD.delete(0,END)
           self.entry_CODAR.delete(0,END)
           self.entry_TOTAL.delete(0,END)
           self.entry_CODCLIM.delete(0,END)
           self.entry_CODCUI.delete(0,END)
            
       def BotonGuardar():

         if (self.entry_COD == ""): #or self.entry_ID == ""):
           MessageBox.showerror("ERROR","INSERTE DATOS") 
         else:
           cursor = db_conn.cursor()

           CODIGO =self.varCod.get()
           CODCLIMA = self.varCODCLIM.get()
           CODCUI =self.varCODCUI.get()
           CODAR =self.varCODAR.get()
           CODTOTAL=self.varTOTAL.get()
          
         #q  datos = (self.varCODCLIM.get(),self.varCODCUI().get(),self.varCODAR.get(),self.varTOTAL().get()) 
          
           #cursor.execute("INSERT INTO CONSULTA_ARBOL (CONSUL_ID,ARL_ARL_ESPE_ID,ARL_TOTAL,ARL_CLIMA_ID,ARL_CUIDADOS_ID)VALUES ('CONSUL{}','{}','{}','{}','{}')".format(CODIGO,CODCLIMA,CODCUI,CODAR,CODTOTAL))
           #
          # cursor.execute("INSERT INTO CONSULTA_ARBOL VALUES (CONSUL_ID='" + CODIGO +
           #      "',ARL_ARL_ESPE_ID='"+CODAR +
           #      "',ARL_TOTAL='"+ CODTOTAL +
           #      "',ARL_CLIMA_ID='"+ CODCLIMA +
           #      "',ARL_CUIDADOS_ID=)'"+CODCUI)

          # cursor.excute(INSERT INTO CONSULTA_ARBOL )
               
           #MessageBox.showinfo("EXITO","DATOS GUARDADOS CON EXITO") 
           #BotonMostar()
           #db_conn.commit()
          
       def BotonAgregar():
           EliminarDatos()
           self.entry_COD.config(state="normal")
           self.entry_CODAR.config(state="normal")
           self.entry_TOTAL.config(state="normal")
           self.entry_CODCLIM.config(state="normal")
           self.entry_CODCUI.config(state="normal")
           

           Button(self,text="GUARDAR",command =BotonGuardar,font=("Arial Black",9)).place(x=650, y=200)

     
       def BotonActualizar():
           #query= 'UPDATE CONSULTA_ARBOL SET CONSUL_ID = ?,ARL_ARL_ESPE_ID = ?,ARL_TOTAL = ?,ARL_CLIMA_ID =?, ARL_CUIDADOS=? WHERE CONSUL_ID=? AND ARL_ARL_ESPE_ID=? AND ARL_TOTAL=? AND ARL_CLIMA_ID=? AND ARL_CUIDADOS_ID=?'
           #parametros = (codigo_n,cod_arl_n,tot_n,cod_clim_n,cod_cui_n,codigo_a,cod_arl_a,tot_a,cod_clim_a,cod_cuid_a)
           
           #conn= Conectar_db()
           #conn.run_db(query,parametros)
           
           #self.ventana_editar.destroy()
           pass
           BotonMostar()    
       def BotonEditar():
            
            codigo_consulta = self.tabla.item(self.tabla.selection())['text']
            codigo_arbol_anti = self.tabla.item(self.tabla.selection())['value'][1]
            num_total_anti = self.tabla.item(self.tabla.selection())
            codigo_clima_anti = self.tabla.item(self.tabla.selection())
            codigo_cuidados_anti= self.tabla.item(self.tabla.selection())

            #VENTANA EXTRA
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar consulta arbol ")
            self.ventana_editar.geometry("300x450")
            self.ventana_editar.resizable(width=0, height=0)
            

            #campo de CODIGO CONSULTA
            self.label_codigo_consulta = Label(self.ventana_editar,text="Codigo suelo:")
            self.label_codigo_consulta.grid(row=0,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_consulta = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = codigo_consulta ),state='readonly')
            self.entry_codigo_consulta.grid(row=0,column = 1,pady=10,padx=10)

             #campo de CODIGO_ARBOL_ANTIGUO
            self.label_codigo_arbol_antiguo  =Label(self.ventana_editar,text="Cod arbol antiguo:")
            self.label_codigo_arbol_antiguo.grid(row=1,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_arbol_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = codigo_arbol_anti),state='readonly')
            self.entry_codigo_arbol_antiguo.grid(row=1,column = 1,pady=10,padx=10)

            #campo de CODIGO_ARBOL_NUEVO 
            self.label_codigo_arbol_nuevo = Label(self.ventana_editar,text="Cod arbol nuevo:")
            self.label_codigo_arbol_nuevo.grid(row=2,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_arbol_nuevo = Entry(self.ventana_editar)
            self.entry_codigo_arbol_nuevo.grid(row=2,column = 1,pady=10,padx=10)
            
            #CODIGO NUM_TOTAL_ANTIGUO
            self.label_num_total_antiguo  =Label(self.ventana_editar,text="Cod total antiguo:")
            self.label_num_total_antiguo.grid(row=3,column = 0, pady = 10 ,padx = 10)
            self.entry_num_total_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = num_total_anti),state='readonly')
            self.entry_num_total_antiguo.grid(row=3,column = 1,pady=10,padx=10)
            
            #CODIGO NUM_TOTAL_NUEVO
            self.label_num_total_nuevo = Label(self.ventana_editar,text="Cod arbol nuevo:")
            self.label_num_total_nuevo.grid(row=4,column = 0, pady = 10 ,padx = 10)
            self.entry_num_total_nuevo = Entry(self.ventana_editar)
            self.entry_num_total_nuevo.grid(row=4,column = 1,pady=10,padx=10) 
            
            #CODIGO CLIMA_ANTIGUO
            self.label_codi_clima_antiguo  =Label(self.ventana_editar,text="Cod clima antiguo:")
            self.label_codi_clima_antiguo.grid(row=5,column = 0, pady = 10 ,padx = 10)
            self.entry_codi_clima_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = codigo_clima_anti),state='readonly')
            self.entry_codi_clima_antiguo.grid(row=5,column = 1,pady=10,padx=10)
            #CODIGO CLIMA_NUEVO 
            self.label_codi_clima_nuevo = Label(self.ventana_editar,text="Cod arbol nuevo:")
            self.label_codi_clima_nuevo.grid(row=6,column = 0, pady = 10 ,padx = 10)
            self.entry_codi_clima_nuevo = Entry(self.ventana_editar)
            self.entry_codi_clima_nuevo.grid(row=6,column = 1,pady=10,padx=10)
            
            #CODIGO CUIDADOS_ANTIGUO
            self.label_codi_cuidados_antiguo  =Label(self.ventana_editar,text="Cod arbol antiguo:")
            self.label_codi_cuidados_antiguo.grid(row=7,column = 0, pady = 10 ,padx = 10)
            self.entry_codi_cuidados_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = codigo_cuidados_anti),state='readonly')
            self.entry_codi_cuidados_antiguo.grid(row=7,column = 1,pady=10,padx=10)
            #CODIGO CUIDADOS_NUEVO
            self.label_codi_cuidados_nuevo = Label(self.ventana_editar,text="Cod arbol nuevo:")
            self.label_codi_cuidados_nuevo.grid(row=8,column = 0, pady = 10 ,padx = 10)
            self.entry_codi_cuidados_nuevo = Entry(self.ventana_editar)
            self.entry_codi_cuidados_nuevo.grid(row=8,column = 1,pady=10,padx=10)

            #Boton Actualizar 
            self.boton_act = Button(self.ventana_editar, text = "ACTUALIZAR ", command=BotonActualizar())
            self.boton_act.grid(row = 9, column = 0,pady = 10, padx = 10)

       Button(self,text="Mostar",command =BotonMostar,font=("Arial Black",9)).place(x=500, y=80)
       Button(self,text="Editar",command =BotonEditar,font=("Arial Black",9)).place(x=500, y=120) 
       Button(self,text="Agregar",command =BotonAgregar,font=("Arial Black",9)).place(x=500, y=160) 
       Button(self,text="Borrar",command =BotonBorrar,font=("Arial Black",9)).place(x=500, y=200) 
       
         
       #def codigos():
       #      pass    
           
       #Button(self,text="Codigos",command =codigos,font=("Arial Black",11)).place(x=650, y=180)
      