from tkinter import *
from tkinter import ttk
from vistas.ARBOL import *
from vistas.ARL_ESPE import *
from vistas.frame_cui_abono import *
from vistas.frame_hojas import *
from vistas.frame_plagas import *
from vistas.frame_raiz import*
from vistas.frame_ramas import *
from vistas.frame_suelo import *
from vistas.frame_zona_geo import*
from vistas.CLIMA import *
from vistas.CUIDADOS import *
from vistas.REPORTES import *


class aplicacion(ttk.Frame):
    def __init__ (self, ventana):
        super().__init__(ventana)
        
        self.mi_ventana = ventana
        self.mi_ventana.title("Consulta de arboles")
        self.mi_ventana.iconbitmap("img/logo-ipn.ico")
        self.navegador = ttk.Notebook(self.mi_ventana)
        self.navegador.config(width="880",height="620")
       
        #PANEL ARBOL
        self.reg_arbol= VistaTREE(self.navegador)
        self.navegador.add(self.reg_arbol,text="ARBOL")

        #panel ARL_espe
        self.reg_arl_espe = VistaArl_espe(self.navegador)
        self.navegador.add(self.reg_arl_espe,text="ESPECIE")

        #panel CLIMA
        self. reg_clima = VistaClima(self.navegador)
        self.navegador.add(self.reg_clima,text="CLIMA")

        #panel CUIDADOS
        self. reg_CUIDADOS= VistaCuidados(self.navegador)
        self.navegador.add(self.reg_CUIDADOS,text="CUIDADOS")

        #panel REPORTES
        self.miImagen=PhotoImage(file="img/report.png").subsample(32)
        self. reg_REPOR= VistaReports(self.navegador)
        self.navegador.add(self.reg_REPOR,text="REPORTES",image=self.miImagen,compound=LEFT)
       #------------------------------------------------
        self.miImafen=PhotoImage(file="img/ID.png").subsample(32)
       #panel Suelo 
        self.reg_suelo= VistaSuelo(self.navegador)
        self.navegador.add(self.reg_suelo ,text="SUELO",image=self.miImafen,compound=LEFT)
       #panel abono 
        self.reg_abono = VistaAbono(self.navegador)
        self.navegador.add(self.reg_abono,text="ABONO",image=self.miImafen,compound=LEFT)
        #panel hojas
        self.reg_hojas = VistaHojas(self.navegador)
        self.navegador.add(self.reg_hojas,text="HOJAS",image=self.miImafen,compound=LEFT)
        #panel plagas
        self.reg_PLAGAS = VistaPlagas(self.navegador)
        self.navegador.add(self.reg_PLAGAS,text="PLAGAS",image=self.miImafen,compound=LEFT)
        #panel ramas
        self.reg_RAMAS = VistaRamas(self.navegador)
        self.navegador.add(self.reg_RAMAS,text="RAMAS",image=self.miImafen,compound=LEFT)
        #panel zpna_geo 
        self.reg_ZONA = VistaClimaZona(self.navegador)
        self.navegador.add(self.reg_ZONA,text="ZONA GEO",image=self.miImafen,compound=LEFT)
        #panel raiz 
        self.reg_raiz = VistaRaiz(self.navegador)
        self.navegador.add(self.reg_raiz,text="RAIZ",image=self.miImafen,compound=LEFT)

       
        self.navegador.pack()
        self.pack()