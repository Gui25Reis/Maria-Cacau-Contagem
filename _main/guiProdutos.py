######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS

# -*- coding: utf-8 -*-

## Classe responsável pela criação da área Produtos

#    !DESCRIÇÃO DO ARQUIVO!
## Bibliotecas necessárias:
# Arquivo local:
from pandas.core.frame import DataFrame
from auxWidgets import AuxWidgets

# GUI:
from auxWidgets import QWidget, QFont


class Gui_Produtos(AuxWidgets):
    ## Construtor: define a super classe e também o grupo
    def __init__(self, wid_:QWidget) -> None:                                 
        super(Gui_Produtos, self).__init__()

        self.root = self.gBox("Produtos", 10, 10, 450, 650, wid_)               # Atributo: Cria o Group Box

        self.gui_Ui()                                                           # Chama o método de construção da GUI (Interface Gráfica)
        self.setWidEnable(False)                                                # Deixa os botões inativos

        self.arq:DataFrame = None                                               # Atributo: guarda o arquivo

        self.dts:dict = {}                                                      # Atributo: guarda as datas
        self.naValues:list = ['0.0', 'nan', '0', '-']                           # Atributo: strings que identificam produtos/quantidades que não existem (ou que nao tem mais)

        self.pedInd:dict = {}                                                   # Atributo: produtos de um pedido
        self.pedDia:dict = {}                                                   # Atributo: produtos do dia
        self.pedGeral:dict = {}                                                 # Atributo: produtos do período todo

        self.res:str = ''                                                       # Atributo: Texto a ser exibido

        
    ## Destruidor: desaloca os atributos declarados
    def __del__(self) -> None:
        del self.root, self.arq, self.dts, self.naValues
        del self.pedInd, self.pedDia, self.pedGeral, self.res
        del self.txt, self.btAttAtiv, self.btOk


    ## Método: cria e configura a janela
    def gui_Ui(self) -> None:
        ## -----------------------------------------------------------------------------------------------
        ## Vizualização do texto:
        self.txt = self.txtView(10, 20, 430, 220, self.root)
        self.setTxt('Nenhuma planilha foi seleciona.')

        self.btAttAtiv = self.bts("Ler planílha", 10, 250, 100, 25, self.root)

        self.btDload = self.bts("Download", 120, 250, 100, 25, self.root)
        self.btDload.setEnabled(False)
        
        self.btCopiarTxt = self.bts("Copiar", 230, 250, 100, 25, self.root)
        self.btCopiarTxt.setEnabled(False)
        self.btCopiarTxt.clicked.connect(lambda: self.btCopiar_action(self.txt))

        self.btOk = self.bts("OK", 340, 250, 100, 25, self.root)

        ## -----------------------------------------------------------------------------------------------
        ## Gráfico:
        gv = self.graphView(10, 310, 430, 290, self.root)
        btCopiar = self.bts("Copiar", 230, 612, 100, 25, self.root)
        btCopiar.setEnabled(False)

        btSalvar = self.bts("Salvar", 340, 612, 100, 25, self.root)
        btSalvar.setEnabled(False)
        
        ## -----------------------------------------------------------------------------------------------
        ## Copyrights:
        txt = "v5.0 (02/21)\nCOPYRIGHT © 2020 KINGS"
        copyright = self.lbl(txt, 8, 10, 610, 180, 30, self.root)
        copyright.setFont(QFont('Arial', 8, 75))

        del self.btDload, gv, btCopiar, btSalvar, txt, copyright
    

    ## Método: ação do botão Ativar (Ler planilha)
    def btAtiv_action(self):
        # if (self.btAttAtiv.text() == "Ativar"):                               # v5.0: Se o botão estiver na fase "Ativar" | Modo atualizar indisponível
        self.setWidEnable(True)                                                 # Ativa os botões inativos
        self.setTxt('Pressione "OK" para gerar o resumo das entregas.')         # Mostra o próximo passa pra se fazer
        self.btAttAtiv.setText("Atualizar")                                     # Muda o nome do botão
        self.btAttAtiv.setEnabled(False)                                        # v5.0: Modo atualizar indisponível
    
    ## Método: deixa os widgets ativado/desativado
    def setWidEnable(self, b_:bool) -> None:
        self.txt.setEnabled(b_)
        self.btOk.setEnabled(b_)
        # self.btDload.setEnabled(b_)
    
    ## Método especial: define o texto
    def setTxt(self, t_:str) -> None: self.txt.setText(t_)         # Define o texto

    #### ANÁLISE NA PLANILHA ####

    ## Método especial: Define o arquivo que vai ser usado
    def setDta(self, d_:dict) -> None: self.dts = d_

    ## Método especial: Define o arquivo que vai ser usado
    def setArq(self, arq_:DataFrame) -> None: self.arq = arq_
    
    ## Método: Adiciona no dicionário somando os valores que ja existe
    def addDict(self, k_:str, v_:int, d1_:dict) -> None:    
        if (k_ not in d1_.keys()): d1_[k_] = v_
        else: d1_[k_] += v_

    ## Método: Junta as colunas de produtos (e as quantidade deles) em um dicionário
    def juntaColunas(self, l_:list) -> None:
        if str(l_[-1]) not in self.naValues:                                    # Add o produto que está na coluna "Outros"
            self.addDict(l_[-1],1,self.pedInd)                                  # (produto, quant, onde vai salvar)
            self.addDict(l_[-1],1,self.pedDia)
            self.addDict(l_[-1],1,self.pedGeral)    

        for p in range(0,14,2):                                                 # Acessa as colunas
            if str(l_[p]) in self.naValues: break                               # Se não tiver mais produto não tem necessidade de continuar
            self.addDict(l_[p+1],int(l_[p]),self.pedInd)
            self.addDict(l_[p+1],int(l_[p]),self.pedDia)
            self.addDict(l_[p+1],int(l_[p]),self.pedGeral)
        del p

    ## Método: arruma identação do texto
    def tabEscrita(self, n_:int) -> str:
        if n_ < 10: return f'   {n_}'
        elif n_< 100: return f'  {n_}'
        elif n_ < 1000: return f' {n_}'
        else: return f'{n_}'

    # Método: EPga o dicionário e coloca em string ("key -> value")
    def dictTOstr(self, d_:dict, s_:str= '') -> str:
        for x in sorted(d_.keys()): s_ += f"{self.tabEscrita(d_[x])} -> {x}\n"
        del x
        return s_

    ## Método: Cria o resumo de cada pedido
    def pedidosInd(self,i_:int, arq_:DataFrame) -> None: 
        for l in range(i_):
            dia = f"\n\nPedido: {arq_['PEDIDO'][l]} | {arq_['Modal'][l]} | {arq_['TEL'][l]}\n"
            self.juntaColunas(arq_.loc[l][4:19])
            dia += self.dictTOstr(self.pedInd)
            self.pedInd = {}
            self.res += dia
        del l, dia
        
    ## Método: Cria o resumo do dia
    def pedidosDia(self, d_:str, i_:int, arq_:DataFrame) -> None:
        self.res += f"\n\n\n>> Dia {self.fixDate(d_)} - {i_} pedido(s)"
        self.pedidosInd(i_, arq_)
        return self.dictTOstr(self.pedDia)
        
    ## Método: Cria o resumo geral (do perípdo)
    def setResumo(self, dia_:str):
        keys:list = sorted(self.dts.keys())
        pulaLin = "\n\n" + "-"*55

        self.res = f"Entre {self.fixDate(keys[0])} e {self.fixDate(keys[-1])} há {sum(self.dts.values())} pedido(s)\n" + self.dictTOstr(self.pedGeral) + pulaLin + dia_ + pulaLin + self.res 
        self.setTxt(self.res)
        del keys, pulaLin