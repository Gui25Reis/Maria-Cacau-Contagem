######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS

# -*- coding: utf-8 -*-

## Classe responsável pela criação da área Entregas

#    Essa classe é responsável pela interface gráfica + toda
# a parte lógica.  


## Bibliotecas necessárias:
# Arquivo local:
from auxWidgets import AuxWidgets
from gui_PopUp import Gui_popup

# GUI:
from auxWidgets import QWidget

# Outros:
from pandas.core.frame import DataFrame
from pandas.core.series import Series


class Gui_Entregas(AuxWidgets):
    ## Construtor: define a super classe e também o grupo
    def __init__(self, wid_:QWidget) -> None:                                 
        super(Gui_Entregas, self).__init__()

        self.root = self.gBox("Entregas", 480, 10, 870, 290, wid_)              # Cria o Group Box

        self.gui_Ui()                                                           # Chama o método de construção da GUI (Interface Gráfica)
        self.setWidEnable(False)                                                # Deixa 90% desativada

        self.popup:Gui_popup = Gui_popup()                                      # Objeto instanciado pra gerar as janelas 

        self.datas:dict = {}                                                    # Datas que são mostradas pro usuário 
        self.resumos:dict = {}                                                  # MEMOIZATION: os resumos que já feitos são guardados pra não fazer de novo

        self.res:str = ''                                                       # Resumo gerado
        self.col:list = []                                                      # Colunas que vão ser usadas
        
    ## Destruidor: desaloca os atributos declarados
    def __del__(self) -> None:
        del self.col, self.res                                                  # Deleta os atributos 
        del self.popup, self.datas, self.resumos
        del self.txt, self.btAttAtiv, self.btDload, self.btCopiarTxt, self.btOk

    ## Método: cria e configura a janela
    def gui_Ui(self) -> None:
        self.txt = self.txtView(10, 20, 480, 220, self.root)                    # Cria a área de vizualização de texto
        self.setTxt('Nenhuma planilha foi seleciona.')                          # Define o texto inicial

        self.btAttAtiv = self.bts("Ler planilha", 9, 250, 90, 25, self.root)    # Cria o botão (Ler PLanílha | Ativar | Atualizar)

        self.btDload = self.bts("Download", 107, 250, 90, 25, self.root)        # Cria o botão de download do arquivo
        self.btDload.setEnabled(False)                                          # v5.0: inativo

        self.btCopiarTxt = self.bts("Copiar", 205, 250, 90, 25, self.root)      # Cria o botão de copiar o texto
        self.btCopiarTxt.setEnabled(False)                                      # Inicialmente fica inativo
        self.btCopiarTxt.clicked.connect(lambda: self.btCopiar_action(self.txt))

        self.dts = self.cBox(303, 251, 91, 23, self.root)                       # Cria a áreas das datas

        self.btOk = self.bts("OK", 401, 250, 90, 25, self.root)                 # Cria o botão de copiar o texto                         

        gv = self.graphView(510, 20, 350, 260, self.root)                       # Cria a área de vizualização dos gráficos
        
        del self.btDload, gv
        
    
    ## Método: deixa os widgets ativado/desativado
    def setWidEnable(self, b_:bool) -> None:
        self.txt.setEnabled(b_)                                                 # Deixa os botões inativos
        self.dts.setEnabled(b_)
        self.btOk.setEnabled(b_)
        # self.btDload.setEnabled(b_)

    ## Método: ação do botão Ativar (Ler planilha)
    def btAtiv_action(self) -> None:
        # if (self.btAttAtiv.text() == "Ativar"):                               # v5.0: Se o botão estiver na fase "Ativar" | Modo atualizar indisponível
        self.setWidEnable(True)                                                 # Ativa os botões inativos
        self.setTxt('Escolha uma data e pressione "OK" para gerar o resumo das entregas.')          # Mostra o próximo passa pra se fazer
        self.btAttAtiv.setText("Atualizar")                                     # Muda o nome do botão
        self.btAttAtiv.setEnabled(False)                                        # v5.0: Modo atualizar indisponível
    
    ## Método especial: Define o arquivo que vai ser usado
    def getDta(self) -> str: return self.datas[self.dts.currentText()]

    ## Método especial: Define o arquivo que vai ser usado
    def setDta(self, d_:dict) -> None: 
        for x in d_.keys(): self.datas[self.fixDate(str(x)[0:10])] = x          # Add no dicionário: {'dd/MM/aaaa':'aaaa-MM-dd'}
        self.dts.addItems(sorted(self.datas.keys()))                            # Add na área de escolha das datas
        del x

    ## Método especial: define o texto
    def setTxt(self, t_:str) -> None: self.txt.setText(t_)

    ## Método especial: Define as colunas que vão ser usadas
    def setCol(self, c_:list) -> None: self.col = c_

    ## Método: Arruma a data de (aaaa-mm-dd) para (dd/mm/aaaa)
    def fixDate(self, d_:str) -> str: return "/".join(reversed(d_.split("-")))

    ## Método: Cria o resumo pela análise dos dados
    def setResumo(self, d_:str, arq_:DataFrame):
        try:    # Tenta fazer o resumo
            quant:Series = arq_[self.col[2]].value_counts()                     # Conta quantas aparições 
            tipo:list = quant.index.tolist()                                    # Pega as aparições

            entregas:str = ''                                                   # Str para colocar as entregas
            for x in range(len(quant)): entregas += f'\n{tipo[x]} = {quant[x]}'

            pag:Series = arq_[self.col[4]]                                      # Pega a coluna do "falta pagar"

            dev:str = ''                                                        # Str para colocar quem precisa pagar
            for x in range(len(pag)):
                if pag[x] < 0 and arq_[self.col[2]][x] != 'FABRICA':            # Pega quem está devendo e não vai retirar na fábrica (vai pagar na hora) 
                    dev += '\n{} -> {} | {} | {} | $: {}\n' .format(            # Puxa os dados necessários para cobrança
                    arq_[self.col[0]][x], arq_[self.col[1]][x], arq_[self.col[2]][x], arq_[self.col[3]][x], arq_[self.col[4]][x])
                    # Número do pedido  ,         Nome        ,   Tipo de entrega   ,       Telefone      ,  Quanto falta pagar

            self.res = f'Para o dia {self.fixDate(d_)} temos: {sum(quant)} pedido(s)\n{entregas}\n\n'
            if (dev == ''): self.res += "Sem nenhuma pendência!"                # Caso não tenha inadiplência
            else: self.res += f"Falta(m) pagar:\n{dev}"                         # Mostra os inadiplentes

            self.resumos[d_] = self.res                                         # Add no dicionário dos resumos
            del quant, tipo, entregas, pag, dev, x                              # Deleta as variáveis da memória
        
        except:    # Erro em alguma parte do código
            txts = ["Erro inesperado","Erro na leitura do arquivo",
            'Um erro inesperado aconteceu. Contate algúem do suporte técnico.\n\nCódigo do erro: E001']
            self.popup.show_PopUp(txts)                                         # ERRO E001
            del txts