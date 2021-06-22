######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS

# -*- coding: utf-8 -*-

## Classe responsável pela criação da janela PopUp

#    Nessa classe é criada a janela Pop-Up quando faz alguma alteração e essa 
# não é salva. Aqui é gerado e feito toda a configuração dela.


## Bibliotecas necessárias:
# Arquivo local:


# GUI:
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QFont


class Gui_popup(QMessageBox):
    ## Construtor: Cria a gui e o necessário para futuras configurações
    def __init__(self) -> None:
        super(Gui_popup, self).__init__()

        self.gui_Ui()                                                       # Configura a gui

    ## Destruidor: Deleta os atributos
    def __del__(self) -> None:
        del self.btEsq

    ## Método: Configura a interface (GUI)
    def gui_Ui(self) -> None:
        self.setWindowIcon(QIcon('images/logo-icone.png'))                  # Define o icone da janela (geral)
        self.setStyleSheet("QLabel{max-width: 400px;};")                    # Define o tamanho máximo do espaço interno
        self.setIcon(self.Critical)                                         # Define o ícone que mostra ao lado da mensagemm
        self.setStandardButtons(self.Save)                                  # Add os botões
        self.setDefaultButton(self.Save)                                    # Botão padrão: "salvar"

        self.btEsq = self.button(self.Save)                                 # Atributo: guarda o botão "Cancel"/Sair
        self.btEsq.setFont(QFont('Arial', 10))                              # Definindo a fonte dos botões
        self.btEsq.setText("OK")                                            # Definindo o texto

    ## Método: Mostra a janela.
    def show_PopUp(self, lMsg_:list, icon_:str = "C") -> int: 
        self.setTxts(lMsg_)                                                 # Define as mensagens
        if (icon_ == "I"): self.setIcon(self.Information)                   # Define o ícone de onformação
        return self.exec()                                                  # Executa/Mostra a janela    

    ## Método: Define o texto de saída
    def setTxts(self, lTxts_:list) -> None:
        self.setWindowTitle(lTxts_[0])                                      # Título da janela
        self.setText(lTxts_[1])                                             # Tìtulo da mensagem
        self.setInformativeText(lTxts_[2])                                  # Mensagem (pergunta)