from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkinter import messagebox
from conexion_db.consultas_db import *

class VistaArl_espe(ttk.Frame):
   def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)

       self.Label_title = Label(self,text="Especie arbol  ",font=("Arial Black",15)).place(x=300, y=10)
       #self.Label_title = Label(self,text="--------------------------------------------------------------------------------------------------------------------",font=("Arial ",15)).place(x=10, y=40)
       
       self.miImafen=PhotoImage(file="img/logo.png").subsample(3)
       self.label_im= Label(self,image=self.miImafen).place(x=700,y=10)

       #LABELS IZQUIERDA 
       self.CODESPE=StringVar()
       Label(self,text = "Codigo especie :",font=("Arial ",13)).place(x=30,y=70)
       self.entry_ESP = Entry (self,state="readonly",textvariable=self.CODESPE)
       self.entry_ESP.place(x=200,y=70)
       
       self.NOMAR=StringVar()
       Label(self,text = "Nombre arbol :",font=("Arial ",13)).place(x=30,y=110)
       self.entry_NOM_ARBOL = Entry (self,state="readonly",textvariable=self.NOMAR)
       self.entry_NOM_ARBOL.place(x=200,y=110)
       
       self.HIGH=StringVar()
       Label(self,text = "Altura arbol :",font=("Arial ",13)).place(x=30,y=150)
       self.entry_ALTURA = Entry (self,state="readonly",textvariable=self.HIGH)
       self.entry_ALTURA.place(x=200,y=150)
       
       self.CODRAIZ=StringVar()
       Label(self,text = "Codigo raiz :",font=("Arial ",13)).place(x=30,y=190)
       self.entry_RAIZ = Entry (self,state="readonly",textvariable=self.CODRAIZ)
       self.entry_RAIZ.place(x=200,y=190)
       
       self.CODRAMAS=StringVar()
       Label(self,text = "Codigo ramas :",font=("Arial ",13)).place(x=30,y=230)
       self.entry_RAMAS = Entry (self,state="readonly",textvariable=self.CODRAMAS)
       self.entry_RAMAS.place(x=200,y=230)
       
       self.CODHOJAS=StringVar()
       Label(self,text = "Codigo hojas :",font=("Arial ",13)).place(x=30,y=270)
       self.entry_HOJAS = Entry (self,state="readonly",textvariable=self.CODHOJAS)
       self.entry_HOJAS.place(x=200,y=270)
       #--------------TABLA------------------------
       self.tabla=ttk.Treeview(self,columns=('','','','','',''))
       #self.tabla.columns(width=80)
       self.tabla.place(x=5,y=300)
       self.tabla.heading('#0',text="CODIGO")
       self.tabla.heading('#1',text="ALTURA")
       self.tabla.heading('#2',text="CODIGO RAIZ")
       self.tabla.heading('#3',text="CODGIO RAMAS")
       self.tabla.heading('#4',text="CODGIO HOJAS")
       self.tabla.heading('#5',text="NOMBRE ARBOLES")

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
           cursor.execute('SELECT * FROM ARL_ESPE')
           registros = cursor.fetchall()

           for ARL_ESPE in registros:
               self.tabla.insert('',0,text=ARL_ESPE[0],value=(ARL_ESPE[1],ARL_ESPE[2],ARL_ESPE[3],ARL_ESPE[4],ARL_ESPE[5]))

       def BotonGuardar():
           if self.entry_ESP.get() == '':
               print(messagebox.askretrycancel(message="Falta llenar campos,desea reintentar?", title="Título"))
           else:
               cursor = db_conn.cursor()

               codespe =self.CODESPE.get()
               nomar = self.NOMAR.get()
               high =self.HIGH.get()
               codraiz =self.CODRAIZ.get()
               codramas=self.CODRAMAS.get()
               codhojas=self.CODRAIZ.get()

               cursor.execute("INSERT INTO CONSULTA_ARBOL VALUES ('TREE{}','{}','{}','{}','{}','{}')".format(codespe,nomar,high,codraiz,codramas,codhojas))
           #
               MessageBox.showinfo("EXITO","DATOS GUARDADOS CON EXITO") 
               BotonMostar()
               db_conn.commit()
           
       def BotonAgregar():

           self.entry_ESP.config(state="normal")
           self.entry_NOM_ARBOL.config(state="normal")
           self.entry_ALTURA.config(state="normal")
           self.entry_RAIZ.config(state="normal")
           self.entry_RAMAS.config(state="normal")
           self.entry_HOJAS.config(state="normal")

           Button(self,text="GUARDAR",command =BotonGuardar,font=("Arial Black",9)).place(x=500, y=80)

           BotonGuardar()
           BotonMostar()
       def BotonBorrar():

           self.entry_ESP.config(state="readonly")
           self.entry_NOM_ARBOL.config(state="readonly")
           self.entry_ALTURA.config(state="readonly")
           self.entry_RAIZ.config(state="readonly")
           self.entry_RAMAS.config(state="readonly")
           self.entry_HOJAS.config(state="readonly")

           codigo = self.tabla.item(self.tabla.selection())['text']
           query = 'DELETE FROM ARL_ESPE WHERE ARLPE_ID =?'

           conn = Conectar_db()
           conn.run_db(query,(codigo,))

           BotonMostar()
      

     #  def selected(event):
      #    if var.get() == 'ARBOLES':

       #   if var.get() == 'SUELOS':
       #       print("3")

       #var = StringVar()
       #var.set('CODIGOS')
       #opciones = ['ARBOLES','SUELOS','HOJAS','PLAGAS']
       #opcion =  OptionMenu(self,var,*opciones,command =selected)
       #opcion.place(x=500, y=80) 
       def BotonActualizar(codigo_n,codigo_a,cod_arl_n,cod_arl_a,tot_n,tot_a,cod_clim_n,cod_clim_a,cod_cui_n,cod_cuid_a,cod_ramas_n,cod_ramas_a):
           query= 'UPDATE ARL_ESPE SET ARLPE_ID = ?,ARLPE_NAME = ?,ARLPE_ALTURA = ?,ARLPE_RAIZ_ID =?, ARLPE_RAMAS_ID=? ,ARLPE_HOJAS_ID=? WHERE ARLPE_ID = ? AND ARLPE_NAME = ? AND ARLPE_ALTURA = ? AND ARLPE_RAIZ_ID =? AND ARLPE_RAMAS_ID=? AND ARLPE_HOJAS_ID=?'
           parametros = (codigo_n,cod_arl_n,tot_n,cod_clim_n,cod_cui_n,cod_ramas_n,codigo_a,cod_arl_a,tot_a,cod_clim_a,cod_cuid_a,cod_ramas_a)
           
           conn= Conectar_db()
           conn.run_db(query,parametros)
           
           self.ventana_editar.destroy()
           BotonMostar()    
       def BotonEditar():
            
            codigo_especie = self.tabla.item(self.tabla.selection())['text']
            arbol_name_anti = self.tabla.item((self.tabla.selection())['value'][1])
            altura_anti = self.tabla.item((self.tabla.selection())['values'][2])
            codigo_raiz_anti = self.tabla.item((self.tabla.selection())['value'][3])
            codigo_ramas_anti= self.tabla.item((self.tabla.selection())['value'][4])
            codigo_hojas_anti= self.tabla.item((self.tabla.selection())['value'][4])

            #VENTANA EXTRA
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar especie arbol ")
            self.ventana_editar.geometry("300x450")
            self.ventana_editar.resizable(width=0, height=0)
            

            #campo de CODIGO arl_espe
            self.label_codigo_especie = Label(self.ventana_editar,text="Codigo especie:")
            self.label_codigo_especie.grid(row=0,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_especie = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = codigo_especie ),state='readonly')
            self.entry_codigo_especie.grid(row=0,column = 1,pady=10,padx=10)

             #campo de nombre arbol_ANTIGUO
            self.label_arbol_name_antiguo  =Label(self.ventana_editar,text="Cod arbol antiguo:")
            self.label_arbol_name_antiguo.grid(row=1,column = 0, pady = 10 ,padx = 10)
            self.entry_arbol_name_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = arbol_name_anti),state='readonly')
            self.entry_arbol_name_antiguo.grid(row=1,column = 1,pady=10,padx=10)

            #campo de nombre_arbol_NUEVO 
            self.label_arbol_name_nuevo = Label(self.ventana_editar,text="Cod arbol nuevo:")
            self.label_arbol_name_nuevo.grid(row=2,column = 0, pady = 10 ,padx = 10)
            self.entry_arbol_name_nuevo = Entry(self.ventana_editar)
            self.entry_arbol_name_nuevo.grid(row=2,column = 1,pady=10,padx=10)
            
            #CODIGO altura_ANTIGUO
            self.label_altura_antiguo  =Label(self.ventana_editar,text="Cod altura antiguo:")
            self.label_altura_antiguo.grid(row=3,column = 0, pady = 10 ,padx = 10)
            self.entry_altura_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = altura_anti),state='readonly')
            self.entry_altura_antiguo.grid(row=3,column = 1,pady=10,padx=10)
            
            #CODIGO altura_NUEVO
            self.label_altura_nuevo = Label(self.ventana_editar,text="Cod altura nuevo:")
            self.label_altura_nuevo.grid(row=4,column = 0, pady = 10 ,padx = 10)
            self.entry_altura_nuevo = Entry(self.ventana_editar)
            self.entry_altura_nuevo.grid(row=4,column = 1,pady=10,padx=10) 
            
            #CODIGO codigo_raiz_anti
            self.label_codigo_raiz_antiguo  =Label(self.ventana_editar,text="Cod raiz antiguo:")
            self.label_codigo_raiz_antiguo.grid(row=5,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_raiz_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = codigo_clima_anti),state='readonly')
            self.entry_codigo_raiz_antiguo.grid(row=5,column = 1,pady=10,padx=10)
            #CODIGO codigo_raiz_NUEVO 
            self.label_codigo_raiz_nuevo = Label(self.ventana_editar,text="Cod raiz nuevo:")
            self.label_codigo_raiz_nuevo.grid(row=6,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_raiz_nuevo = Entry(self.ventana_editar)
            self.entry_codigo_raiz_nuevo.grid(row=6,column = 1,pady=10,padx=10)
            
            #CODIGO codigo_ramas_ANTIGUO
            self.label_codigo_ramas_antiguo  =Label(self.ventana_editar,text="Cod ramas antiguo:")
            self.label_codigo_ramas_antiguo.grid(row=7,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_ramas_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = codigo_ramas_anti),state='readonly')
            self.entry_codigo_ramas_antiguo.grid(row=7,column = 1,pady=10,padx=10)
            #CODIGO codigo ramas_NUEVO
            self.label_codigo_ramas_nuevo = Label(self.ventana_editar,text="Cod ramas nuevo:")
            self.label_codigo_ramas_nuevo.grid(row=8,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_ramas_nuevo = Entry(self.ventana_editar)
            self.entry_codigo_ramas_nuevo.grid(row=8,column = 1,pady=10,padx=10)

            #CODIGO codigo_hojas_ANTIGUO
            self.label_codigo_hojas_antiguo  =Label(self.ventana_editar,text="Cod hojas antiguo:")
            self.label_codigo_hojas_antiguo.grid(row=7,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_hojas_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = codigo_hojas_anti),state='readonly')
            self.entry_codigo_hojas_antiguo.grid(row=7,column = 1,pady=10,padx=10)
            #CODIGO codgio hojas_NUEVO
            self.label_codigo_hojas_nuevo = Label(self.ventana_editar,text="Cod hojas nuevo:")
            self.label_codigo_hojas_nuevo.grid(row=8,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_hojas_nuevo = Entry(self.ventana_editar)
            self.entry_codigo_hojas_nuevo.grid(row=8,column = 1,pady=10,padx=10)

            #Boton Actualizar 
            self.boton_act = Button(self.ventana_editar, text = "ACTUALIZAR ", command=lambda:BotonActualizar(codigo_especie,codigo_especie,
            self.entry_arbol_name_nuevo.get(),arbol_name_anti,self.entry_altura_nuevo.get(),altura_anti,self.entry_codigo_raiz_nuevo.get(),
            codigo_raiz_anti,self.entry_codigo_ramas_nuevo.get(),codigo_ramas_anti,self.entry_codigo_hojas_nuevo.get(),codigo_hojas_anti))
            self.boton_act.grid(row = 9, column = 0,pady = 10, padx = 10)

            

       Button(self,text="Mostar",command =BotonMostar,font=("Arial Black",9)).place(x=500, y=80)
       Button(self,text="Editar",command =BotonEditar,font=("Arial Black",9)).place(x=500, y=120) 
       Button(self,text="Agregar",command =BotonAgregar,font=("Arial Black",9)).place(x=500, y=160) 
       Button(self,text="Borrar",command =BotonBorrar,font=("Arial Black",9)).place(x=500, y=200) 
       
      # self.tabla.heading('#3',text="Codigo CUIDADOS")