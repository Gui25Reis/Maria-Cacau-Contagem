# Graph Report - Maria-Cacau-App  (2026-06-25)

## Corpus Check
- 175 files · ~18,333 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 863 nodes · 1422 edges · 39 communities detected
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 368 edges (avg confidence: 0.77)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]

## God Nodes (most connected - your core abstractions)
1. `DataSourceError` - 20 edges
2. `connect()` - 20 edges
3. `SheetsController` - 19 edges
4. `DSChart` - 15 edges
5. `call()` - 14 edges
6. `from_response()` - 14 edges
7. `SummaryView` - 14 edges
8. `DeliveryView` - 13 edges
9. `StatusBarController` - 12 edges
10. `unexpected_error()` - 11 edges

## Surprising Connections (you probably didn't know these)
- `HTTPResponse` --uses--> `Contrato que qualquer client precisa cumprir.`  [INFERRED]
  /Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/core/network/_response.py → core/network/_client.py
- `HTTPResponse` --uses--> `Roteia requests para o backend local (in-process).     Nenhuma rede envolvida —`  [INFERRED]
  /Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/core/network/_response.py → core/network/_client.py
- `HTTPRequest` --uses--> `Contrato que qualquer client precisa cumprir.`  [INFERRED]
  /Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/core/network/_request.py → core/network/_client.py
- `HTTPRequest` --uses--> `Roteia requests para o backend local (in-process).     Nenhuma rede envolvida —`  [INFERRED]
  /Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/core/network/_request.py → core/network/_client.py
- `FeatureEvents` --uses--> `SheetsController`  [INFERRED]
  /Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/features/cpf_validation/domain/events.py → features/sheets/presentation/controller.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.03
Nodes (59): GoogleSheetsDataSource, Implementação de DataSourceProtocol para Google Sheets via gspread., _fix_prod4(), normalize(), Normaliza headers inconsistentes da planilha para os valores canônicos dos enums, Traduz headers reais da planilha para os nomes canônicos definidos nos enums., _rename_at(), _rename_keys() (+51 more)

### Community 1 - "Community 1"
Cohesion: 0.04
Nodes (37): OrdersSummaryAPI, DeliveriesMapper, ErrorMapper, from_response(), OrdersSummaryMapper, PaymentsMapper, Mappers de HTTPResponse para domain models e de HTTPResponseError para ErrorMode, SummaryRepository (+29 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (25): API, ConnectAuthAPI, DeliveriesAPI, DisconnectAuthAPI, path(), PaymentsPendentAPI, Endpoints do backend consumidos pela feature Auth., RemoveSheetAPI (+17 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (12): MenuHandler, connect(), SheetsUseCase, Erro genérico para exceções não tratadas., unexpected_error(), AuthController, SheetsController, AuthView (+4 more)

### Community 4 - "Community 4"
Cohesion: 0.05
Nodes (39): ABC, API, entity(), Comunicação alto nivel para chamadas de api, HTTPClientContract, LocalClient, Realiza as request de fato, Contrato que qualquer client precisa cumprir. (+31 more)

### Community 5 - "Community 5"
Cohesion: 0.06
Nodes (11): DSDialog, DSDialogIcon, DSDialogModel, DSComboBox, DeliveryController, Inicia a consulta: trava a view, dispara o ViewModel e registra o timestamp para, Recebe o resultado do ViewModel, atualiza a view e loga a duração da consulta., SummaryController (+3 more)

### Community 6 - "Community 6"
Cohesion: 0.05
Nodes (30): BackendServer, handle_backend_error(), handle_data_source_error(), handle_unexpected_error(), DeliveriesSummary, DeliveryTypeCount, Models de domínio da feature de entregas., DeliveriesRepository (+22 more)

### Community 7 - "Community 7"
Cohesion: 0.07
Nodes (16): _EventBus, CpfValidationResult, Models utilizados no módulo, AuthSignals, CpfValidationSignals, DeliverySignals, Canal de comunicação entre o ViewModel e o Controller., SheetsSignals (+8 more)

### Community 8 - "Community 8"
Cohesion: 0.07
Nodes (12): DSButton, DSGroupBox, DSLoadingHandler, DSLoadingHandler, Deve ser chamado no __init__ do componente, após o super().__init__()., Implementar no componente: o que fazer com cada frame do spinner., Mixin que adiciona comportamento de loading animado a qualquer componente QObjec, DeliveryView (+4 more)

### Community 9 - "Community 9"
Cohesion: 0.06
Nodes (15): Rotas de autenticação, AuthService, Service de autenticação — gerencia o estado de conexão do DataSource., DataSourceProtocol, Autentica com o dict da service account e guarda o client em memória., Remove o client autenticado da memória. Mantém o sheet_id., Remove a planilha ativa da memória. Mantém as credenciais., Define a planilha ativa e dispara prewarm em background. (+7 more)

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (25): asset(), Metadados centralizados do pacote maria-cacau., Resolve um path relativo à pasta assets, funciona em dev e no .exe compilado., _customer(), _customization(), _delivery(), _financial(), OrderMapper (+17 more)

### Community 11 - "Community 11"
Cohesion: 0.1
Nodes (6): StatusBarState, DSLabel, StatusBarController, StatusBarView, QLabel, QStatusBar

### Community 12 - "Community 12"
Cohesion: 0.1
Nodes (9): AppCoordinator, MainWindow, main(), Entry point da aplicação. Execute com: python -m maria_cacau, QMainWindow, QWidget, HomeController, HomeFeaturesModel (+1 more)

### Community 13 - "Community 13"
Cohesion: 0.13
Nodes (11): DSButtonState, AppEvent, _Observability, Observabilidade centralizada do app., Services, FeatureEvents, Eventos de observabilidade da feature CPF Validation., Enum (+3 more)

### Community 14 - "Community 14"
Cohesion: 0.14
Nodes (13): Retorna pedidos no intervalo de datas informado (DD/MM/YYYY)., _cast_numeric(), OrdersSummaryRepository, Repositório de pedidos por período — busca e prepara dados da planilha para o Or, Acessa o data source e entrega um DataFrame tipado para o OrdersService.      Ún, Retorna todos os pedidos de um período com colunas numéricas convertidas para fl, _to_dataframe(), OrdersMapper (+5 more)

### Community 15 - "Community 15"
Cohesion: 0.12
Nodes (6): DSDateInput, DSTextInput, QDateEdit, QDialog, QLineEdit, SheetCreateView

### Community 16 - "Community 16"
Cohesion: 0.21
Nodes (4): DSChartType, DSChart, Widget de gráfico reutilizável (barras ou pizza) usando seaborn + matplotlib., _short_label()

### Community 17 - "Community 17"
Cohesion: 0.17
Nodes (12): AppError, certificado_limpo(), certificado_ok(), planilha_conectada(), planilha_ok(), Códigos de erro da aplicação com estrutura AppError., Confirmação de certificado configurado com sucesso., Confirmação de credenciais removidas com sucesso. (+4 more)

### Community 18 - "Community 18"
Cohesion: 0.15
Nodes (11): _cast_numeric(), PaymentsRepository, Repositório de pagamentos — busca e prepara dados da planilha para o PaymentsSer, Acessa o data source e entrega um DataFrame tipado para o PaymentsService., Retorna todos os pedidos de uma data com colunas numéricas convertidas para floa, _to_dataframe(), PaymentsMapper, PaymentsService (+3 more)

### Community 19 - "Community 19"
Cohesion: 0.31
Nodes (2): Backend de armazenamento seguro via arquivo protegido no diretório do usuário., SecurityStorage

### Community 20 - "Community 20"
Cohesion: 0.5
Nodes (1): AppSession

### Community 21 - "Community 21"
Cohesion: 0.5
Nodes (3): normalize_decimal(), Utilitários de formatação numérica., Converte número no formato brasileiro para o formato inglês.      Remove o separ

### Community 22 - "Community 22"
Cohesion: 1.0
Nodes (1): r"""Indica se a resposta foi bem sucedida (status code 2xx).

### Community 23 - "Community 23"
Cohesion: 1.0
Nodes (1): O tipo precisa aceitar **kwargs (dataclass ou similar).

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (1): Lê o JSON do backend; cai em http_error genérico se o corpo não for JSON válido.

### Community 45 - "Community 45"
Cohesion: 1.0
Nodes (1): Renomeia a coluna que segue prod3 para prod4, independente do header atual.

### Community 46 - "Community 46"
Cohesion: 1.0
Nodes (1): Busca pedidos por datas usando dois passes para minimizar chamadas à API.

### Community 48 - "Community 48"
Cohesion: 1.0
Nodes (1): Monta um Order completo a partir de uma linha do DataFrame.

### Community 50 - "Community 50"
Cohesion: 1.0
Nodes (1): Converte list[dict] em DataFrame com cast numérico de todas as colunas de valor.

### Community 51 - "Community 51"
Cohesion: 1.0
Nodes (1): Faz cast numérico de uma coluna se ela existir no DataFrame.

### Community 53 - "Community 53"
Cohesion: 1.0
Nodes (1): Converte list[dict] em DataFrame com cast numérico de todas as colunas de valor.

### Community 54 - "Community 54"
Cohesion: 1.0
Nodes (1): Faz cast numérico de uma coluna se ela existir no DataFrame.

### Community 58 - "Community 58"
Cohesion: 1.0
Nodes (1): Normaliza uma data para DD/MM/YYYY aceitando os formatos DD/MM/YY e DD/MM/YYYY.

### Community 59 - "Community 59"
Cohesion: 1.0
Nodes (1): Converte linhas da planilha em lista de dicts usando o cabeçalho como chaves (lo

### Community 60 - "Community 60"
Cohesion: 1.0
Nodes (1): Agrupa números de linha consecutivos em ranges A1 notation e divide em batches d

### Community 61 - "Community 61"
Cohesion: 1.0
Nodes (1): Retorna o conjunto de todas as datas (DD/MM/YYYY) entre start e end, inclusive.

### Community 62 - "Community 62"
Cohesion: 1.0
Nodes (1): Serializa o resultado do OrdersService para dict JSON-ready.

### Community 63 - "Community 63"
Cohesion: 1.0
Nodes (1): Busca e monta os pedidos de um período.

### Community 64 - "Community 64"
Cohesion: 1.0
Nodes (1): Retorna todos os pedidos do período informado.

## Knowledge Gaps
- **116 isolated node(s):** `Metadados centralizados do pacote maria-cacau.`, `Resolve um path relativo à pasta assets, funciona em dev e no .exe compilado.`, `Entry point da aplicação. Execute com: python -m maria_cacau`, `Observabilidade centralizada do app.`, `Erros mapeados usados no módulo` (+111 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 19`** (9 nodes): `Backend de armazenamento seguro via arquivo protegido no diretório do usuário.`, `SecurityStorage`, `.clean_all()`, `.delete()`, `.__init__()`, `._path()`, `.retrieve()`, `.save()`, `security.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (4 nodes): `AppSession`, `.__init__()`, `__init__.py`, `session.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (1 nodes): `r"""Indica se a resposta foi bem sucedida (status code 2xx).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (1 nodes): `O tipo precisa aceitar **kwargs (dataclass ou similar).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (1 nodes): `Lê o JSON do backend; cai em http_error genérico se o corpo não for JSON válido.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (1 nodes): `Renomeia a coluna que segue prod3 para prod4, independente do header atual.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (1 nodes): `Busca pedidos por datas usando dois passes para minimizar chamadas à API.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (1 nodes): `Monta um Order completo a partir de uma linha do DataFrame.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (1 nodes): `Converte list[dict] em DataFrame com cast numérico de todas as colunas de valor.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `Faz cast numérico de uma coluna se ela existir no DataFrame.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (1 nodes): `Converte list[dict] em DataFrame com cast numérico de todas as colunas de valor.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (1 nodes): `Faz cast numérico de uma coluna se ela existir no DataFrame.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (1 nodes): `Normaliza uma data para DD/MM/YYYY aceitando os formatos DD/MM/YY e DD/MM/YYYY.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 59`** (1 nodes): `Converte linhas da planilha em lista de dicts usando o cabeçalho como chaves (lo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (1 nodes): `Agrupa números de linha consecutivos em ranges A1 notation e divide em batches d`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (1 nodes): `Retorna o conjunto de todas as datas (DD/MM/YYYY) entre start e end, inclusive.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 62`** (1 nodes): `Serializa o resultado do OrdersService para dict JSON-ready.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (1 nodes): `Busca e monta os pedidos de um período.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 64`** (1 nodes): `Retorna todos os pedidos do período informado.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `connect()` connect `Community 3` to `Community 5`, `Community 7`, `Community 8`, `Community 9`, `Community 11`, `Community 12`, `Community 15`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Why does `SheetsController` connect `Community 3` to `Community 2`, `Community 5`, `Community 7`, `Community 9`, `Community 13`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Why does `from_response()` connect `Community 1` to `Community 10`, `Community 2`, `Community 4`, `Community 6`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `connect()` (e.g. with `.__init__()` and `._create_features_menu()`) actually correct?**
  _`connect()` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `SheetsController` (e.g. with `FeatureEvents` and `SheetModel`) actually correct?**
  _`SheetsController` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `DSChart` (e.g. with `._setup_components()` and `._setup_components()`) actually correct?**
  _`DSChart` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Metadados centralizados do pacote maria-cacau.`, `Resolve um path relativo à pasta assets, funciona em dev e no .exe compilado.`, `Entry point da aplicação. Execute com: python -m maria_cacau` to the rest of the system?**
  _116 weakly-connected nodes found - possible documentation gaps or missing edges._