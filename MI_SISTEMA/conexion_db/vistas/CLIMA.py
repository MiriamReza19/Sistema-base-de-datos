from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkinter import messagebox
from conexion_db.consultas_db import *


class VistaClima(ttk.Frame):
   def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       
       self.Label_title = Label(self,text="CLIMA ",font=("Arial Black",15)).place(x=350, y=10)
       #self.Label_title = Label(self,text="---------------------------------------------------------------------------------------------------------------",font=("Arial ",15)).place(x=10, y=40)

       self.miImafen=PhotoImage(file="img/logo.png").subsample(3)
       self.label_im= Label(self,image=self.miImafen).place(x=700,y=10)

      #LABELS IZQUIERDA 
       self.CODCLIMA=StringVar()
       Label(self,text = "Codigo clima :",font=("Arial ",13)).place(x=30,y=70)
       self.entry_COD = Entry (self,state="readonly",textvariable=self.CODCLIMA)
       self.entry_COD.place(x=200,y=70)
       
       self.NAMECLIMA=StringVar()
       Label(self,text = "Nombre clima:",font=("Arial ",13)).place(x=30,y=110)
       self.entry_NAME = Entry (self,state="readonly",textvariable=self.NAMECLIMA)
       self.entry_NAME.place(x=200,y=110)
       
       self.CODZGEO=StringVar()
       Label(self,text = "Codigo zona geo :",font=("Arial ",13)).place(x=30,y=150)
       self.entry_CLIM_Z= Entry (self,state="readonly",textvariable=self.CODZGEO)
       self.entry_CLIM_Z.place(x=200,y=150)
       
       self.TEMP=StringVar()
       Label(self,text = "TEMP:",font=("Arial ",13)).place(x=30,y=190)
       self.entry_TEMP = Entry (self,state="readonly",textvariable=self.TEMP)
       self.entry_TEMP.place(x=200,y=190)
       
       self.ALTITUD=StringVar()
       Label(self,text = "ALTITUD :",font=("Arial ",13)).place(x=360,y=70)
       self.entry_ALTI = Entry (self,state="readonly",textvariable=self.ALTITUD)
       self.entry_ALTI.place(x=500,y=70)

       self.LATITU=StringVar()
       Label(self,text = "LATITUD :",font=("Arial ",13)).place(x=360,y=110)
       self.entry_LATI = Entry (self,state="readonly",textvariable=self.LATITU)
       self.entry_LATI.place(x=500,y=110)

       self.CODSUELO=StringVar()
       Label(self,text = "Codigo suelo :",font=("Arial ",13)).place(x=360,y=150)
       self.entry_SUELO = Entry (self,state="readonly",textvariable=self.CODSUELO)
       self.entry_SUELO.place(x=500,y=150)

       self.tabla=ttk.Treeview(self,columns=('','','','','','',''),height=10)
       self.tabla.place(x=5,y=280)
       self.tabla.heading('#0',text="CODIGO CLIMA",anchor=CENTER)
       self.tabla.heading('#1',text="NOMBRE CLIMA",anchor=CENTER)
       self.tabla.heading('#2',text="CODIGO ZONA_GEO",anchor=CENTER)
       self.tabla.heading('#3',text="TEMPERATURA",anchor=CENTER)
       self.tabla.heading('#4',text="ALTITUD",anchor=CENTER)
       self.tabla.heading('#4',text="LATITUD",anchor=CENTER)
       self.tabla.heading('#4',text="CODIGO SUELO",anchor=CENTER)

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
           #LIMPIAR DATOS
           recorrer_tabla =self.tabla.get_children()
           for elementos in recorrer_tabla:
               self.tabla.delete(elementos)

           cursor = db_conn.cursor()
           cursor.execute('SELECT * FROM CLIMA')
           registros = cursor.fetchall()

           for CLIMA in registros:
               self.tabla.insert('',0,text=CLIMA[0],value=(CLIMA[1],CLIMA[2],CLIMA[3],CLIMA[4],CLIMA[5],CLIMA[6]))  
       
       def BotonGuardar():
         if (self.entry_COD == ""): #or self.entry_ID == ""):
           MessageBox.showerror("ERROR","INSERTE DATOS") 
         else:
           cursor = db_conn.cursor()

           codigo=self.varCod.get()
           codar =self.varABONO.get()
           codtotal=self.varPLAGAS.get()
          
         #q  datos = (self.varCODCLIM.get(),self.varCODCUI().get(),self.varCODAR.get(),self.varTOTAL().get()) 
          
           cursor.execute("INSERT INTO CLIMA VALUES ('CLIMA{}','{}','{}')".format(codigo,codar,codtotal))
           
           MessageBox.showinfo("EXITO","DATOS GUARDADOS CON EXITO") 
           BotonMostar()
           db_conn.commit()
           
       def BotonAgregar():
           self.entry_COD.config(state="normal")
           self.entry_NAME.config(state="normal")
           self.entry_CLIM_Z.config(state="normal")
           self.entry_TEMP.config(state="normal")
           self.entry_ALTI.config(state="normal")
           self.entry_LATI.config(state="normal")
           self.entry_SUELO.config(state="normal")

           Button(self,text="GUARDAR",command =BotonGuardar,font=("Arial Black",9)).place(x=500, y=80)

           BotonGuardar()
           BotonMostar()
       def BotonBorrar():

           confirm= MessageBox.askyesnocancel(message="¿ESta seguro de eliminarlo?", title="Confirmacion")
           print(confirm)
           if (confirm == TRUE):
               cursor =db_conn.cursor()
            
               codigo =self.tabla.item(self.tabla.selection())['text']
               query ="DELETE FROM CUIDADOS WHERE CLIMA_ID ='%s'"%codigo
            
               cursor.execute(query)
            
               db_conn.commit() 

               MessageBox.showinfo("BORRAR","Informacion eliminada con exito ")
               BotonMostar()
       


       def BotonActualizar():
           query= 'UPDATE CLIMA SET CLIMA_ID = ?,CLIMA_NAME = ?,CLIMA_Z_GEO_ID = ?,CLIMA_TEMP =?, CLIMA_ALTI=? ,CLIMA_LATI=?,CLIMA_SUELO_ID WHERE CLIMA_ID = ? AND CLIMA_NAME = ? AND CLIMA_Z_GEO_ID = ? AND CLIMA_TEMP =? AND CLIMA_ALTI=? AND CLIMA_LATI=? AND CLIMA_SUELO_ID '
           parametros = (codigo_n,name_n,clim_zg_n,temp_n,alti_n,lati_n,suelo_n,codigo_a,name_a,climzg_a,temp_a,alti_a,lati_a,suelo_a)
           
           conn= Conectar_db()
           conn.run_db(query,parametros)
           
           self.ventana_editar.destroy()
           BotonMostar()    
       def BotonEditar():
            
            codigo_clima = self.tabla.item(self.tabla.selection())
            nombre_clima_anti = self.tabla.item(self.tabla.selection())
            clima_zona_anti = self.tabla.item(self.tabla.selection())
            temp_anti = self.tabla.item(self.tabla.selection())
            alti_anti= self.tabla.item(self.tabla.selection())
            lati_anti= self.tabla.item(self.tabla.selection())
            clim_sue_anti= self.tabla.item(self.tabla.selection())

            #VENTANA EXTRA
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("Editar consulta arbol ")
            self.ventana_editar.geometry("300x450")
            self.ventana_editar.resizable(width=0, height=0)
            

            #campo de CODIGO 
            self.label_codigo_clima = Label(self.ventana_editar,text="Codigo suelo:")
            self.label_codigo_clima.grid(row=0,column = 0, pady = 10 ,padx = 10)
            self.entry_codigo_clima = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = codigo_clima ),state='readonly')
            self.entry_codigo_clima.grid(row=0,column = 1,pady=10,padx=10)

             #campo de nombre clima antiguo
            self.label_nombre_clima_antiguo  =Label(self.ventana_editar,text="Cod clima antiguo:")
            self.label_nombre_clima_antiguo.grid(row=1,column = 0, pady = 10 ,padx = 10)
            self.entry_nombre_clima_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = nombre_clima_anti),state='readonly')
            self.entry_nombre_clima_antiguo.grid(row=1,column = 1,pady=10,padx=10)

            #campo de nombre clima nuevo 
            self.label_nombre_clima_nuevo = Label(self.ventana_editar,text="Cod clima nuevo:")
            self.label_nombre_clima_nuevo.grid(row=2,column = 0, pady = 10 ,padx = 10)
            self.entry_nombre_clima_nuevo = Entry(self.ventana_editar)
            self.entry_nombre_clima_nuevo.grid(row=2,column = 1,pady=10,padx=10)
            
            # CODIGO_zona geo ANTIGUO
            self.label_clim_zona_geo_antiguo  =Label(self.ventana_editar,text="Cod zona geo antiguo:")
            self.label_clim_zona_geo_antiguo.grid(row=3,column = 0, pady = 10 ,padx = 10)
            self.entry_clim_zona_geo_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = clima_zona_anti),state='readonly')
            self.entry_clim_zona_geo_antiguo.grid(row=3,column = 1,pady=10,padx=10)
            
            #CODIGO_zona geo_NUEVO
            self.label_clim_zona_geo_nuevo = Label(self.ventana_editar,text="Cod zona geo nuevo:")
            self.label_clim_zona_geo_nuevo.grid(row=4,column = 0, pady = 10 ,padx = 10)
            self.entry_clim_zona_geo_nuevo = Entry(self.ventana_editar)
            self.entry_clim_zona_geo_nuevo.grid(row=4,column = 1,pady=10,padx=10) 
            
            #TEMPERRATURA ANTIGUO
            self.label_clima_temp_antiguo  =Label(self.ventana_editar,text="Temperatura antiguo:")
            self.label_clima_tem_antiguo.grid(row=5,column = 0, pady = 10 ,padx = 10)
            self.entry_clima_tem_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = temp_anti),state='readonly')
            self.entry_clima_tem_antiguo.grid(row=5,column = 1,pady=10,padx=10)
            #TEMPERATURA NUEVO
            self.label_clima_tem_nuevo = Label(self.ventana_editar,text="Temperatura nuevo:")
            self.label_clima_tem_nuevo.grid(row=6,column = 0, pady = 10 ,padx = 10)
            self.entry_clima_tem_nuevo = Entry(self.ventana_editar)
            self.entry_clima_tem_nuevo.grid(row=6,column = 1,pady=10,padx=10)
            
            #CODIGO altitud_ANTIGUO
            self.label_altitud_antiguo  =Label(self.ventana_editar,text="Altitud antiguo:")
            self.label_altitud_antiguo.grid(row=7,column = 0, pady = 10 ,padx = 10)
            self.entry_altitud_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = alti_anti),state='readonly')
            self.entry_altitud_antiguo.grid(row=7,column = 1,pady=10,padx=10)
            #CODIGO altitud_NUEVO
            self.label_altitud_nuevo = Label(self.ventana_editar,text="Altitud nuevo:")
            self.label_altitud_nuevo.grid(row=8,column = 0, pady = 10 ,padx = 10)
            self.entry_altitud_nuevo = Entry(self.ventana_editar)
            self.entry_altitud_nuevo.grid(row=8,column = 1,pady=10,padx=10)

             # latitud_ANTIGUO
            self.label_latitud_antiguo  =Label(self.ventana_editar,text="Latitud antiguo:")
            self.label_latitud_antiguo.grid(row=9,column = 0, pady = 10 ,padx = 10)
            self.entry_latitud_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = lati_anti),state='readonly')
            self.entry_latitud_antiguo.grid(row=9,column = 1,pady=10,padx=10)
            #latitud_NUEVO
            self.label_latitud_nuevo = Label(self.ventana_editar,text="Latitud nuevo:")
            self.label_latitud_nuevo.grid(row=10,column = 0, pady = 10 ,padx = 10)
            self.entry_latitud_nuevo = Entry(self.ventana_editar)
            self.entry_latitud_nuevo.grid(row=10,column = 1,pady=10,padx=10)

             # cod suelo_ANTIGUO
            self.label_cod_suelo_antiguo  =Label(self.ventana_editar,text="Latitud antiguo:")
            self.label_cod_suelo_antiguo.grid(row=11,column = 0, pady = 10 ,padx = 10)
            self.entry_cod_suelo_antiguo = Entry(self.ventana_editar,textvariable=StringVar(self.ventana_editar,value = clim_sue_anti),state='readonly')
            self.entry_cod_suelo_antiguo.grid(row=11,column = 1,pady=10,padx=10)
            # cod suelo _NUEVO
            self.label_cod_suelonuevo = Label(self.ventana_editar,text="Latitud nuevo:")
            self.label_cod_suelo_nuevo.grid(row=12,column = 0, pady = 10 ,padx = 10)
            self.entry_cod_suelo_nuevo = Entry(self.ventana_editar)
            self.entry_cod_suelo_nuevo.grid(row=12,column = 1,pady=10,padx=10)

            #Boton Actualizar 
            self.boton_act = Button(self.ventana_editar, text = "ACTUALIZAR ", command=BotonActualizar)
            self.boton_act.grid(row = 9, column = 0,pady = 10, padx = 10)

       Button(self,text="Mostar",command =BotonMostar,font=("Arial Black",9)).place(x=30, y=230)
       Button(self,text="Editar",command =BotonEditar,font=("Arial Black",9)).place(x=130, y=230) 
       Button(self,text="Agregar",command =BotonAgregar,font=("Arial Black",9)).place(x=230, y=230) 
       Button(self,text="Borrar",command =BotonBorrar,font=("Arial Black",9)).place(x=330, y=230) 
       
         
       #def codigos():
          
           
       #Button(self,text="Codigos",command =codigos,font=("Arial Black",11)).place(x=650, y=180)
      