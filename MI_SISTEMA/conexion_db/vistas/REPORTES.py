from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkinter import messagebox
from vistas.reports import *

class VistaReports(ttk.Frame):
   def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)
       
       self.Label_title = Label(self,text="REPORTES ",font=("Arial Black",15)).place(x=350, y=10)
       #self.Label_title = Label(self,text="---------------------------------------------------------------------------------------------------------------",font=("Arial ",15)).place(x=10, y=40)

       self.miImafen=PhotoImage(file="img/logo.png").subsample(3)
       self.label_im= Label(self,image=self.miImafen).place(x=700,y=10)
       
       #BOTONES 
       self.Label_title = Label(self,text="ABONOS Y PLAGAS ",font=("Arial Black",17)).place(x=50, y=80)
       def REPORT1():
           
           rep1=advanced_example_using_database()

       Button(self,text="REPORTE",command =REPORT1,font=("Arial Black",12)).place(x=500, y=100)


       self.Label_title = Label(self,text="TOTAL ARBOLES POR NOMBRE ",font=("Arial Black",17)).place(x=50, y=200)
       def REPORT2():
           pass
       Button(self,text="REPORTE",command =REPORT2,font=("Arial Black",12)).place(x=500, y=180)


       self.Label_title = Label(self,text="TIPO CLIMA POR ZONA GEO  ",font=("Arial Black",17)).place(x=50, y=300)
       def REPORT3():
           pass
       Button(self,text="REPORTE",command =REPORT3,font=("Arial Black",12)).place(x=500, y=280)