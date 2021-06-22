######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS

# -*- coding: utf-8 -*-

## Classe responsável pela criação da área de consulta de frete

#    Essa classe é responsável pela interface gráfica + toda
# a parte lógica.  


## Bibliotecas necessárias:
# Arquivo local:
from auxWidgets import AuxWidgets

# GUI:
from auxWidgets import QWidget


class Gui_ConsFrete(AuxWidgets):
    ## Construtor: define a super classe e também o grupo
    def __init__(self, wid_:QWidget) -> None:                                 
        super(Gui_ConsFrete, self).__init__()

        self.root = self.gBox("Consulta Frete", 990, 450, 360, 210, wid_)               # Cria o Group Box
        self.root.setEnabled(False)                                                     # v5.0: Deixa inativo

        self.gui_Ui()                                                                   # Chama o método de construção da GUI (Interface Gráfica)
        

    ## Destruidor: desaloca os atributos declarados
    def __del__(self) -> None:
        del self.root                                                                   # Deleta os atributos
        del self.btVeri, self.btCopi, self.resp,self.tOrigem, self.tDestino
    

    ## Método: cria e configura a janela
    def gui_Ui(self) -> None:
        self.tOrigem = self.lblBt("Origem:", 10, 80, self.root)                         # Cria a label e a entrada de texto 

        self.tDestino = self.lblBt("Destino:", 195, 260, self.root)                     # Cria a label e a entrada de texto 

        self.resp = self.txtView(10, 60, 340, 100, self.root)                           # Cria área de vizualização de texto

        self.btVeri = self.bts("Verificar", 140, 173, 100, 23, self.root)               # Cria o botão "Verificar"

        self.btCopi = self.bts("Copiar", 250, 173, 100, 23, self.root)                  # Cria o botão "Copiar"