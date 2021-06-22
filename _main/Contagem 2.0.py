#   Gui Reis      -       gui.sreis25@gmail.com  

# Esse programa tem como objetivo fazer uma análise e filtrar dados vindo da planilha auxiliar.

#---------------------------------------------------------------------------------------------------
## BIBLIOTECAS:
import pandas as pd, openpyxl as op

print(''' \n\t\t|\/| /\ /? | /\   ( /\ ( /\ |_| ''')
print('\n\nLendo a planíliha...')


#---------------------------------------------------------------------------------------------------
## ARQUIVOS:
local_arq = 'G:/OneDrive/Gui/GuiTestes/Python/Maria Cacau/Contagem/Arquivos/Arq MC c.xlsx'
# local_arq = 'Arquivos/Arq MC.xlsx' 
arq = pd.read_excel(local_arq, decimal='.')

local_txt = 'G:/OneDrive/Gui/GuiTestes/Python/Maria Cacau/Contagem/Arquivos/Resumo pedidos.txt'
# local_txt = 'Arquivos/Resumo pedidos.txt'   
arq_peds = open(local_txt,'w')

# local_txt = 'Arquivos/Resumo produtos.txt'   
local_txt = 'G:/OneDrive/Gui/GuiTestes/Python/Maria Cacau/Contagem/Arquivos/Resumo produtos.txt'
arq_prods = open(local_txt,'w')




#---------------------------------------------------------------------------------------------------
## COLUNAS:

# Cria uma lista com todas as colunas dp excel
arq_cols = list(arq.columns)

# Colunas usadas nos resumos dos produtos
cols_ped = ['PEDIDO','DATA ENTREGA','Modal','TEL','Q1','Prod1','Q2','Prod2','Q3','Prod3','Q4','Prod4','Q5','Prod5','Q6','Prod6','Q7','Prod7','Outro\nEspec.',]

# Colunas iniciais (Notas-SAGE e Pedido)
cols = ['PEDIDO']
[cols.append(x) for x in arq_cols[73:85]]

# Coluna da exeção de entregas (Notas-SAGE e Envio Direto)
modal_nota = ['MOTOBOY', 'GUARITA', 'FEIRA', 'FABRICA', 'ENTREGA']


# Colunas necessarias pra (Notas-SAGE):
cols_NS = ['PEDIDO','Modal','NOME COMPRADOR','CPF','EMAIL','CEP','Rua','Compl.','Bairro','Cidade-UF','$FRETE','TOTAL','TEL','NEGOCIAÇÃO','Evento']


# Colunas necessarias pra (Melhor Envio):
cols_ME = ['PEDIDO','Modal','NOME COMPRADOR','TEL','EMAIL','CEP','Rua','Compl.','Bairro','Cidade-UF','CPF']




#---------------------------------------------------------------------------------------------------
## TABELAS:

# Cria uma tabela ordenada pela data de entrega:
arq_ord = pd.DataFrame(arq.sort_values(["DATA ENTREGA"]) [cols_ped]) .reset_index() .drop(columns=['index'])




#---------------------------------------------------------------------------------------------------
## FUNÇÕES:


dia_OK = lambda d: '{0[0]}/{0[1]}/{0[2]}' .format(d.split('-')[::-1])       # Função (aux): arruma a data 


def pedidos(dia_):                                                          # Função: escreve no arquivo "Resumo pedidos"
    # Cria uma tabela, filtrando a data e com as culunas necessárias
    filt = arq.loc[(arq['DATA ENTREGA'] == '{} 00:00:00' .format(dia_))] [cols] .reset_index() .drop(columns=['index'])

    quant = filt['Modal'].value_counts()            # Conta quantas aparições 
    tipo = quant.index.tolist()                     # Pega as aparições

    entregas = ''                                   # Str para colocar as entregas
    for x in range (len(quant)):
        entregas += f'\n{tipo[x]} = {quant[x]}'

    pag = filt[cols[1]]                             # Pega a coluna do "falta pagar"

    dev = ''                                        # Str para colocar quem precisa pagar
    for x in range(len(pag)):
        if pag[x] < 0 and filt[cols[3]][x] != 'FABRICA':                                                        # Pega quem está devendo e não vai retirar na fábrica(vai pagar na hora) 
            dev += '\n' + '{} -> {} | {} | {} | $: {} \n' .format(                                              # Puxa os dados necessários para cobrança
            filt[cols[0]][x], filt[cols[4]][x], filt[cols[3]][x], filt[cols[-3]][x], filt[cols[1]][x])

    return f'Para o dia {dia_OK(dia_)} temos: {sum(quant)} pedidos \n{entregas} \n\nFalta(m) pagar: \n{dev}\n\n\n\n\n'    # Retorna o rexto pronto
    

def compl (coluna_):                                                        # Função (aux): padroniza o complemento
    compl = []                                                                  
    for y in list(coluna_):                                                     # Pega os complementos da coluna
        try:                                                                    # Tentativa:
            if  'complemento:' in y.lower() or 'compl.' in y.lower():               # se tiver auma dessas palvras, tira ela
                compl.append(y.split(':')[1])
            else:                                                                   # já está ok
                compl.append(y) 
        except:                                                                 # Exeção:
                compl.append(y)                                                     # Só add, mesmo tendo alguma escrita
    return compl                                                                # Retorno: lista padronizada


def nota_SAGE (dia_):                                                       # Função: puxa os dados necessários para a nota fiscal
    dia_ = '2020-07-03'
 ## Verificando se tem belga:
    cols = [arq_cols[x] for x in range(15,43,4)]                            # Lista com as colunas que tem os produtos
    
    # Cria uma tabela só com os produtos, com a filtragens que vai ser usada;
    prods = arq.loc[(arq['DATA ENTREGA'] == '{} 00:00:00' .format(dia_)) & (arq['Modal'] != 'MOTOBOY') & (arq['Evento'] != 'Amostras')] [cols] .reset_index() .drop(columns=['index'])

    veri = lambda x: 'Sim' if 'BELGA' in str(set(prods.loc[x])) else 'Não'  # Verifica se no produto tem a palavra "BELGA"
    belga = list(map(veri, range(len(prods))))                              # Cria uma lista, com o Sim e Não
    

 ## Criando a tabela final:

   # Cria a tabela com os filtros que vão ser utilizados:
    filt = arq.loc[(arq['DATA ENTREGA'] == '{} 00:00:00' .format(dia_)) & (arq['Modal'] != 'MOTOBOY') & (arq['Evento'] != 'Amostras')] [cols_NS] 
    filt['Belga?'] = belga          # Adiciona a coluna belga
    filt = filt.reset_index() .drop(columns=['index'])             # Re-ordena a tabela


   # Cálculo do total (tira o frete embutido)
    tot = list(filt[cols_NS[11]])                                     # Pega todos os totais
    fret = list(filt[cols_NS[10]])                                    # Pega todos os fretes
    total = [str(round(tot[x] - fret[x])) for x in range(len(tot))]     # Subtrai o frete
    
    
   # Cria a 1ª coluna, coluna das legendas (principal):
    colunas = list(filt.columns)    # Pega as colunas da tabela criada
    colunas.insert(12,'Belga?')     # Acrescenta a coluna "Belga"
    colunas.insert(10,'')           # Add Pula linha (1º)
    colunas.insert(14,'')           # Add Pula linha (2º)


 ## Escrevendo na planílha:
    num_coluna = 2                                                                                          # Coloca os dados na coluna seguinte da legenda
    for col in range(len(filt)):
        if filt.iloc[col][1] not in modal_nota:                                                             # Se for um pedido que faz a nota fiscal
            for lin in range(len(colunas)-1):                                                               # Começa a colocar os dados na tabela
                if lin == 7:                                                                                # Linha do complemento:
                    plan.cell(row=lin+1, column=num_coluna, value=str(compl(filt[cols_NS[7]])[col]))          # Coloca o complemento personalizado
                elif lin == 11:                                                                             # Linha do frete:
                    plan.cell(row=lin+1, column=num_coluna, value=str(fret[col]))                               # Pega da lista q juntou os fretes
                elif lin == 12:                                                                             # Linha do total:
                    plan.cell(row=lin+1, column=num_coluna, value=str(total[col]))                              # Coloca ototal sem o frete
                elif lin not in [10,14] and lin not in [7,11,12]:                                           # Coloca as dados normais
                    plan.cell(row=lin+1, column=num_coluna, value=str(filt[colunas[lin]] [col]))        
            num_coluna += 4                                                                                 # Avança 4 colunas de distância


def melhor_Envio (dia_):                                                    # Função: puxa os dados necessários para o Melhor Envio
    # Cria a tabela com os filtros que vão ser utilizados:
    filt = arq.loc[(arq['DATA ENTREGA'] == '{} 00:00:00' .format(dia_)) & (arq['Modal'] != 'MOTOBOY') & (arq['Evento'] != 'Amostras')] [cols_ME] .reset_index() .drop(columns=['index'])

    # Cria as colunas para os dados
    colunas = list(filt.columns)    # Pega as colunas da tabela criada
    colunas.insert(2,'')            # Add Pula linha
    
    # Escrevendo na plamílha
    num_coluna = 2                                                                                          # Coloca os dados na coluna seguinte da legenda 
    for col in range(len(filt)):
        if filt.iloc[col][1] not in modal_nota:                                                             # Se for um pedido que faz o Melhor Envio
            for lin in range(len(colunas)):                                                                 # Começa a colocar os dados na tabela
                if lin == 8:                                                                                # Linha do complemento:
                    plan2.cell(row=lin+1, column=num_coluna, value=str(compl(filt[cols_ME[7]])[col]))      # Coloca o complemento personalizado
                elif lin not in [2,8]:                                                                      # Coloca as dados normais
                    plan2.cell(row=lin+1, column=num_coluna, value=str(filt[colunas[lin]] [col]))
            num_coluna += 4                                                                                 # Avança 4 colunas de distância


def junta_pedidos():                                                        # Função: Cria tabelas dos pedidos individuais
    for ped in range(len(arq_ord)):                             # Loop: pega todos os pedidos (um por um)
        quant, prod = [], []                                    # Cria uma lista para colocar os produtos e as quantidades
        for x in range(4,17,2):                                 # Pego as colunas de produtos e quantidades (da tabela excel)
            q = arq_ord.loc[ped][cols_ped[x]]                   # Coloca cada uma em lista (junta produtos e junta quantidades)
            p = arq_ord.loc[ped][cols_ped[x+1]]
            if q != 0:                                          # Se tiver um produto cadastrado (se a quant for != 0)
                quant.append(q)                                 # Adiciona a quantidade
                prod.append(p)                                  # Adiciona o produto
    
        if str(arq_ord.loc[ped][cols_ped[-1]]) != '-':          # Se tiver algum produto em outros
            quant.append(0)                                     # Adiciona a quantidade (como 0, pois a quantidade esta com o produto)
            prod.append(x)                                      # Adiciona o produto
    
        ped_individuais.append(soma_pedidos(quant, prod))       # Cria uma tabela (dataframe) com todos os produtos (sem repetição, somados)


def soma_pedidos(listaQ_,listaP_):                                          # Função: junta os produtos iguais
        df_temp = pd.DataFrame({"Quant":listaQ_, "Produtos":listaP_})       # Cria uma tabela com as quantidades e produtos

        prod_dif = list(pd.DataFrame(listaP_) [0].unique())                 # Acha quais os produtos diferentes q tem
        prod_dif.sort()                                                     # Ordena

        quant_OK, prod_OK = [],[]

        for x in prod_dif:                                                  # Pega o produto
            aux = df_temp.loc[(df_temp["Produtos"] == x)]                   # Filtra a tabela com apenas esse produto
            quant_OK.append(sum(list(aux['Quant'])))                        # Soma todas as quantidades que aparecem daquele produto (junta os produtos duplicados)
            prod_OK.append(x)                                                   

        return pd.DataFrame({"Quant":quant_OK, "Produtos":prod_OK})         # Cria uma tabela atualizada sem repetição de produtos


def concatena (lista_, rang_):                                              # Função: junta tabelas (dataframes)
    df_aux = pd.concat([lista_[x] for x in rang_])                              # Junta as tabelas, uma embaixo da outra
    return soma_pedidos(list(df_aux['Quant']), list(df_aux['Produtos']))        # Junta as repetições


def prod_escrita (ped_, ind_, esc_):                                        # Função (aux): cria a escrita dos produtos
    q = list(ped_[ind_]['Quant'])                                               # Lista com as quantidades
    p = list(ped_[ind_]['Produtos'])                                            # Lista com os produtos     

    for y in range(len(q)):                                                     
        if q[y] < 10:                                                           # Printa de acordo com o número de dígitos do número
            esc_ += f'\n   {q[y]} -> {p[y]} '
        elif q[y] < 100:
            esc_ += f'\n  {q[y]} -> {p[y]} '
        elif q[y] < 1000:
            esc_ += f'\n {q[y]} -> {p[y]} '
        else:
            esc_ += f'\n{q[y]} -> {p[y]} '

    esc_ += '\n\n'                                                              # Pula algumas linhas
    arq_prods.write(esc_)                                                       # Escreve no arquivo


def produto ():                                                             # Função: escreve no arquivo "Resumo produtos"
   # Escrevendo os produtos semanais 
    esc = f'\n\nPerido: {dia_OK(data[0])} - {dia_OK(data[-1])} - {len(arq_ord)} pedidos'            # Texto de introdução
    [prod_escrita(ped_periodo, x, esc) for x in range(len(ped_periodo))]                            # Escrevendo no arquivo
    arq_prods.write(f'\n\n{pula_linha}\n\n')                                                        # Pula a linha

   # Escrevendo os produtos diários
    [prod_escrita(ped_diario, x, f'\n\nDia: {dia_OK(data[x])} - {len(q_ped_diarios(data[x]))} pedidos') for x in range(len(ped_diario))]
    arq_prods.write(f'\n\n{pula_linha}\n\n')                                                        # Pula linha

   # Escrevendo os produtos individuais
    for dia in data:                                                                                # Pega de dia em dia
        arq_prods.write(f' \n\nDia {dia_OK(dia)} - {len(q_ped_diarios(dia))} pedidos')              # Escreve a introdução    
        for x in q_ped_diarios(dia):                                                                # loop: escreve pedido por pedido
            esc = f'\n\nPedido: {arq_ord.loc[x][0]} | {arq_ord.loc[x][2]} | {arq_ord.loc[x][3]}'    # Dados iniciais do pedido
            prod_escrita(ped_individuais, x, esc)                                                   # Produtos        

    arq_peds.close()




#---------------------------------------------------------------------------------------------------
## ALGUMAS CONFIGURAÇÕES E LISTAS:

# Pega as datas diferentes que tem na planilha e ordena
data = [str(x)[0:10] for x in list(arq_ord["DATA ENTREGA"].unique())]

# Cria as listas para guardar os produtos em cada periodo
ped_periodo, ped_individuais, ped_diario = [], [], []
junta_pedidos()

# Pega os índices equivalentes ao dia e junta os pedidos (pedidos diário):
q_ped_diarios = lambda x: list(arq_ord.loc[(arq_ord["DATA ENTREGA"] == f"{x} 00:00:00")] .index)
[ped_diario.append(concatena(ped_individuais, q_ped_diarios(dia))) for dia in data]

# Pega todos os dias e junta:
ped_periodo.append(concatena(ped_diario, range(len(data))) )

pula_linha = '-'*80     # separa os grupos no arquivo "Resumo produtos"




#---------------------------------------------------------------------------------------------------
## MAIN:
while True:
   # Fazendo a escrita nos arquivos txt 
    [arq_peds.write(pedidos(dia)) for dia in data]  # Resumo das entregas
    produto()                                       # Resumo dos pedidos

   # Mostra as datas encontradas 
    print('\n\nDatas encontradas: \n')

    [print(f'0{d+1} -> {dia_OK(data[d])}' if d < 9 else f'{d+1} -> {dia_OK(data[d])}') for d in range(len(data))]
    print("\n00 -> Sair do programa")

    print('\n\nEscolha uma data para configurar a Nota-SAGE e o Melhor Envio')
    opc = input('Opção: ')

   # Valida a entrada: 
    vali = str(list(range(len(data)+1)))
    while opc not in vali:
        print(f'\nEntrada inválida. \nDigite entre {int(vali[0])+1} - {int(vali[-1])} ')
        opc = input("\nOpção: ")
    opc = int(opc)

    if opc == 0:
        break
    
  #---------------------------------------------------------------------------------------------------
  ## ARQUIVOS:
    arq_2 = op.load_workbook(local_arq)
    plan = arq_2['Nota - SAGE']
    plan2 = arq_2['Melhor Envio']

  # Ecrevendo no excel: Nota-SAGE
    nota_SAGE(data[opc-1])              # Faz a escrita
    arq_2.save(local_arq)               # Salva as mudanças

  # Ecrevendo no excel: Melhor-Envio
    melhor_Envio(data[opc-1])           # Faz a escrita
    arq_2.save(local_arq)               # Salva as mudanças
    
    arq_2.close()                       # Fecha o arquivo

    print('\nPronto!!')
    break

# Fecha o programa
input('\n\n PRESSIONE ENTER PARA FECHAR O PROGRAMA')