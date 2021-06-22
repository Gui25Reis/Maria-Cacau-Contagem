######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS

# -*- coding: utf-8 -*-

## Classe responsável pela criação das planilhas

#    Nessa classe é feita APENAS criação das planilha já com as filtragens necessessárias
# que serão usadas, mas não pe feita nenhuma anáise. Além disso é feito os tratamento de 
# erros, sendo cada erro identificado com um código.

## Bibliotecas necessárias:

# Arquivo da análise da planilha
from pandas.core.frame import DataFrame
from pandas import read_excel

# Arquivo local:
from gui_PopUp import Gui_popup

class Analise:
    def __init__(self) -> None:
        super(Analise, self).__init__()

        self.arq:DataFrame = None                                                                       # Atributo: Guarda a tabela com todas as colunas que VÃO SER USADAS apenas.
        self.arqUsados:dict = {}                                                                        # Atributo: Guarda os Dataframes que já foram filtrados usados!

        self.dtsPed:dict = {}                                                                           # Atributo: Guarda as datas e a quantidade de pedidos

        self.colsFiltro:dict = {                                                                        # Atributo: Guarda as colunas que vão ser usadas no geral
            "Sage":['PEDIDO','Modal','Destinatário','CPF','EMAIL','CEP','Rua','Compl.','Bairro','Cidade-UF','$FRETE','TOTAL','TEL','Evento'],
            "Envio":['PEDIDO','Modal','NOME COMPRADOR','TEL','EMAIL','CEP','Rua','Compl.','Bairro','Cidade-UF','CPF','Evento'],
            "Pula Modal":['MOTOBOY', 'GUARITA', 'FEIRA', 'FABRICA', 'ENTREGA'],
            "Entrega":['PEDIDO','Destinatário','Modal','TEL','Quanto\nfalta\npagar?','DATA ENTREGA'],
            "Produtos":['PEDIDO','DATA ENTREGA','Modal','TEL','Q1','Prod1','Q2','Prod2','Q3','Prod3','Q4','Prod4','Q5','Prod5','Q6','Prod6','Q7','Prod7','Outro\nEspec.'],
            "Belga":['Prod1','Prod2','Prod3','Prod4','Prod5','Prod6','Prod7','Outro\nEspec.','Modal','Evento'],
            "gSage":['Destinatário','CPF','EMAIL','CEP','Rua','Compl.','Bairro','Cidade-UF','$FRETE','TOTAL','Belga','PEDIDO','Modal','TEL'],
            "gLbl":["NOME", "CPF", "EMAIL", "CEP", "RUA", "COMPL", "BAIRRO", "CIDADE", "FRETE", "TOTAL", "BELGA?", "PEDIDO", "ENTREGA","TEL"]
        }
        self.allColsFiltro:list = list(set(self.colsFiltro["Sage"] + self.colsFiltro["Envio"] + self.colsFiltro["Entrega"] + self.colsFiltro["Produtos"]))

        ## Obejto intanciado de da classe local
        self.popUp:Gui_popup = Gui_popup()                                                              # Atributo: Cria os popUp

    ## Destruidor: Deleta os atributos
    def __del__(self) -> None:
        del self.dtsPed, self.colsFiltro, self.allColsFiltro                                            # Deletas os atributos
        del self.arq, self.arqUsados, self.popUp

    ## Método especial: Pega as colunas já filtradas
    def getCol(self, k_:str) -> list: return self.colsFiltro[k_]                                        # Retorna as colunas

    ## Método especial: Pega as colunas já filtradas
    def getDts(self) -> dict: return self.dtsPed                                                        # Retorna as datas ordenadas

    ## Método especial: Faz a leitura do arquivo
    def setArq(self, local_:str) -> bool: 
        if (local_ == ""): return False
        if ((local_[-5:] != ".xlsx")): 
            txts = ["Erro na leitura do arquivo",'Arquivo não é ".xlsx"',
            f'O arquivo escolhido não é compatível com o programa. Procure um arquivo Excel do tipo ".xlsx" \n\nCódigo do erro: A001']
            self.popUp.show_PopUp(txts)                                                                 # ERRO A001
            return False

        try:
            arq = read_excel(local_)                                                                    # Faz a leitura do arquivo
            self.arq = arq[arq[arq.columns[0]].isnull() == False][self.allColsFiltro]                   # Tira as linhas em branco (no meio e no final)
        except:
            txts = ["Erro na leitura do arquivo",'Colunas não encontradas',
            f'O arquivo escolhido não é compatível com o programa. Procure o arquivo padrão. \n\nCódigo do erro: A002']
            self.popUp.show_PopUp(txts)                                                                 # ERRO A002
            return False

        try:
            qDts = self.arq["DATA ENTREGA"].value_counts()                                              # Pega a quantidade de datas que tem
            dts = qDts.index.tolist()
            self.dtsPed = {str(dts[x])[:10]:int(qDts[x]) for x in range(len(dts))}
        except:
            txts = ["Erro na leitura do arquivo",'Coluna incompatível',
            f'Houve um problema ao ler a coluna "DATA ENTREGA". Verifique os dados da coluna e tente novamente. \n\nCódigo do erro: A003']
            self.popUp.show_PopUp(txts)                                                                 # ERRO A003
            return False

        qLinhas = len(self.arq.index)
        if (qLinhas == 0): 
            txts = ["Erro na leitura do arquivo",'Arquivo vazio',
            f'O arquivo está vazio, não tem nenhuma linha para ser lida. \n\nCódigo do erro: A004']
            self.popUp.show_PopUp(txts)                                                                 # ERRO A004
            return False
        
        txts = ["Concluído",'Planilha lida com sucesso', f'Foi encontrada(s) {qLinhas} linhas.']
        self.popUp.show_PopUp(txts, "I")                                                                # Mostra quantas linhas foram lidas

        del arq, dts, qDts, txts, qLinhas                                                               # Deleta as variáveis locais
        return True
        
    ## Método especial: Devolve a planilha filtrada
    def getArq(self, l_:list, d_:str) -> DataFrame: 
        if (d_ in self.arqUsados.keys()): return self.arqUsados[d_][l_]                                 # Memoization: verifica se essa tabela já foi filtrada
        self.arqUsados[d_] = self.arq.loc[(self.arq['DATA ENTREGA'] == f"{d_} 00:00:00")].reset_index() .drop(columns=['index'])
        return self.arqUsados[d_][l_]                                                                   # Retorna a planilha com as colunas pedidas
    
    ## Método especial: Devolve a planilha filtrada com exceções a mais
    def getArqDados(self, l_:list, d_:str) -> DataFrame:
        arq = self.getArq(l_, d_)
        return arq.loc[(arq['Modal'] != 'MOTOBOY') & (arq['Evento'] != 'Amostras')].reset_index() .drop(columns=['index','Evento'])