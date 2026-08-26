# Graph Report - Maria-Cacau-App  (2026-08-26)

## Corpus Check
- 213 files · ~22,103 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2086 nodes · 3487 edges · 198 communities (151 shown, 47 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 320 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `858e64bd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Maria-Cacau-Contagem/maria_cacau/backend/data_source/errors/_errors.py
- .log
- from_response
- Enum
- SheetsRepository
- AuthController
- Maria-Cacau-Contagem/maria_cacau/core/network/api.py
- Maria-Cacau-Contagem/maria_cacau/backend/features/orders/subfeatures/deliveries/service.py
- Maria-Cacau-Contagem/maria_cacau/backend/features/orders/shared/models.py
- DataSourceProtocol
- Maria-Cacau-Contagem/maria_cacau/core/error/errors.py
- connect
- StatusBarController
- SheetCreateView
- .get_by_period
- ._configure_app
- DSChart
- SecurityStorage
- DSComboBox
- AppSession
- Maria-Cacau-Contagem/maria_cacau/backend/utils/numbers.py
- r"""Indica se a resposta foi bem sucedida (status code 2xx).
- O tipo precisa aceitar **kwargs (dataclass ou similar).
- HTTPResponse
- maria_cacau/features/home/sub_features/delivery/data/repository.py
- Lê o JSON do backend; cai em http_error genérico se o corpo não for JSON válido.
- maria_cacau/features/cpf_validation/presentation/controller.py
- properties
- Renomeia a coluna que segue prod3 para prod4, independente do header atual.
- Busca pedidos por datas usando dois passes para minimizar chamadas à API.
- Converte list[dict] em DataFrame com cast numérico de todas as colunas de valor.
- Faz cast numérico de uma coluna se ela existir no DataFrame.
- Converte list[dict] em DataFrame com cast numérico de todas as colunas de valor.
- Faz cast numérico de uma coluna se ela existir no DataFrame.
- maria_cacau/backend/data_source/errors/_errors.py
- Converte uma linha do DataFrame (vinda do SheetsRepository) em um Order.
- Monta um Order completo a partir de uma linha do DataFrame.
- Normaliza uma data para DD/MM/YYYY aceitando os formatos DD/MM/YY e DD/MM/YYYY.
- Converte linhas da planilha em lista de dicts usando o cabeçalho como chaves (lo
- Agrupa números de linha consecutivos em ranges A1 notation e divide em batches d
- Retorna o conjunto de todas as datas (DD/MM/YYYY) entre start e end, inclusive.
- Serializa o resultado do OrdersService para dict JSON-ready.
- Busca e monta os pedidos de um período.
- Retorna todos os pedidos do período informado.
- CacheStorage
- tokens/__init__.py
- deliveries/response/schema.json
- properties
- maria_cacau/backend/features/orders/subfeatures/deliveries/service.py
- ErrorModel
- DSButton
- _utils.py
- SheetsRepository
- maria_cacau/backend/data_source/__init__.py
- coordinator.py
- summary/service.py
- DSChart
- .to_model
- properties
- SummaryController
- call
- DSButton
- Maria-Cacau-Contagem/maria_cacau/backend/data_source/sheet_mapper.py
- GoogleSheetsDataSource
- DataSourceProtocol
- $defs
- properties
- maria_cacau/backend/_server.py
- v6/components/__init__.py
- .pre_login
- OrderMapper
- maria_cacau/features/home/sub_features/summary/data/repository.py
- maria_cacau/features/home/sub_features/summary/presentation/view.py
- AuthRepository
- maria_cacau/features/home/sub_features/summary/presentation/viewmodel.py
- SheetsController
- SummaryView
- strings.py
- Customer
- payments/response/schema.json
- maria_cacau/design_system/components/__init__.py
- DSBadgeStyle
- HomeController
- Maria-Cacau-Contagem/maria_cacau/features/cpf_validation/domain/use_case.py
- DeliveryView
- properties
- PaymentsRepository
- OrdersSummaryRepository
- DSContainer
- _SheetsViewModel
- Maria-Cacau-Contagem/maria_cacau/backend/data_source/_normalizer.py
- Maria-Cacau-Contagem/maria_cacau/features/home/sub_features/delivery/domain/models.py
- _SheetsGuard
- DSButton
- SheetCreateView
- DeliveryView
- SummaryView
- StatusBarView
- StatusBarController
- Maria-Cacau-Contagem/maria_cacau/core/network/_errors.py
- BackendError
- .get_by_date
- SheetsUseCase
- properties
- properties
- unexpected_error
- maria_cacau/features/auth/presentation/viewmodel.py
- Maria-Cacau-Contagem/maria_cacau/backend/features/orders/subfeatures/payments/service.py
- DSDialog
- maria_cacau/backend/features/auth/route.py
- maria_cacau/backend/features/sheet/route.py
- sheets/presentation/controller.py
- DSLoadingHandler
- Maria-Cacau-Contagem/maria_cacau/features/home/sub_features/summary/data/repository.py
- properties
- maria_cacau/features/auth/presentation/controller.py
- AuthController
- SheetsMenuView
- Maria-Cacau-Contagem/maria_cacau/core/network/_config.py
- Maria-Cacau-Contagem/maria_cacau/features/home/sub_features/summary/presentation/controller.py
- Maria-Cacau-Contagem/maria_cacau/core/network/_observability.py
- GoogleSheetsDataSource
- required
- SheetModel
- Maria-Cacau-Contagem/maria_cacau/backend/features/orders/subfeatures/payments/repository.py
- Maria-Cacau-Contagem/maria_cacau/core/storage/handler.py
- to_response
- Maria-Cacau-Contagem/maria_cacau/features/cpf_validation/domain/signals.py
- unexpected_error
- maria_cacau/backend/features/orders/subfeatures/payments/route.py
- Backend
- SummaryViewModel
- DeliveryViewModel
- DSDateInput
- ConnectAuthAPI
- AuthView
- CacheStorage
- .json
- _SheetsViewModel
- Maria-Cacau-Contagem/maria_cacau/features/cpf_validation/presentation/controller.py
- AuthUseCase
- _shadows.py
- CPF Validation
- Delivery
- SummaryViewModel
- Summary
- DSTextView
- Maria Cacau — App
- Maria-Cacau-Contagem/maria_cacau/design_system/components/chart/chart_widget.py
- Maria-Cacau-Contagem/maria_cacau/features/auth/data/repository.py
- DSTextInput
- deliveries/response/example.json
- DSTextView
- payments/response/example.json
- maria_cacau/features/home/sub_features/summary/domain/signals.py
- _Palette
- HomeFeaturesModel
- maria-cacau
- QFrame
- Mapeamento de uma linha do DataFrame para o model Order.
- Service e Mapper de resumo de pedidos por período.

## God Nodes (most connected - your core abstractions)
1. `SheetModel` - 26 edges
2. `ErrorModel` - 25 edges
3. `DataSourceError` - 24 edges
4. `OrderMapper` - 24 edges
5. `HTTPResponse` - 23 edges
6. `API` - 21 edges
7. `SheetsController` - 21 edges
8. `DSChart` - 20 edges
9. `DataSourceError` - 20 edges
10. `unexpected_error()` - 17 edges

## Surprising Connections (you probably didn't know these)
- `from_response()` --calls--> `DeliveryCount`  [INFERRED]
  /Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/features/home/sub_features/summary/data/mapper.py → /Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/features/home/sub_features/delivery/domain/models.py
- `AppCoordinator` --uses--> `MainWindow`  [INFERRED]
  maria_cacau/app/coordinator.py → maria_cacau/app/window.py
- `SheetNormalizer` --uses--> `PaymentCols`  [INFERRED]
  maria_cacau/backend/data_source/_normalizer.py → maria_cacau/backend/data_source/sheet_mapper.py
- `SheetNormalizer` --uses--> `ProductCols`  [INFERRED]
  maria_cacau/backend/data_source/_normalizer.py → maria_cacau/backend/data_source/sheet_mapper.py
- `_SheetsViewModel` --uses--> `SheetCols`  [INFERRED]
  maria_cacau/backend/data_source/_viewmodel.py → maria_cacau/backend/data_source/sheet_mapper.py

## Import Cycles
- 3-file cycle: `/Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/backend/data_source/__init__.py -> /Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/backend/data_source/_google_sheets.py -> /Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/backend/data_source/_viewmodel.py -> /Users/kings/Documents/GitHub/Maria-Cacau-Contagem/maria_cacau/backend/data_source/__init__.py`
- 3-file cycle: `maria_cacau/backend/data_source/__init__.py -> maria_cacau/backend/data_source/_google_sheets.py -> maria_cacau/backend/data_source/_viewmodel.py -> maria_cacau/backend/data_source/__init__.py`

## Communities (198 total, 47 thin omitted)

### Community 0 - "Maria-Cacau-Contagem/maria_cacau/backend/data_source/errors/_errors.py"
Cohesion: 0.10
Nodes (19): ApiQuotaExceededError, ApiUnexpectedResponseError, CredentialsFileCorruptedError, CredentialsFileNotFoundError, CredentialsFormatError, CredentialsSaveError, DataSourceError, DataSourceNotReadyError (+11 more)

### Community 1 - ".log"
Cohesion: 0.14
Nodes (4): DeliveryController, Inicia a consulta: trava a view, dispara o ViewModel e registra o timestamp para, Recebe o resultado do ViewModel, atualiza a view e loga a duração da consulta., SummaryController

### Community 2 - "from_response"
Cohesion: 0.14
Nodes (15): DeliveriesMapper, ErrorMapper, from_response(), OrdersSummaryMapper, PaymentsMapper, Mappers de HTTPResponse para domain models e de HTTPResponseError para ErrorMode, DaySummary, OrderDetail (+7 more)

### Community 3 - "Enum"
Cohesion: 0.20
Nodes (7): DSDialogIcon, DSDialogModel, DSButtonState, Services, FeatureEvents, Eventos de observabilidade da feature CPF Validation., Enum

### Community 4 - "SheetsRepository"
Cohesion: 0.21
Nodes (6): RemoveSheetAPI, SelectSheetAPI, _extract_sheet_id(), Retorna o sheet_id da última planilha salva em cache, sem HTTP., SheetsRepository, SheetModel

### Community 5 - "AuthController"
Cohesion: 0.17
Nodes (4): AuthController, AuthView, AuthViewModel, QMenu

### Community 6 - "Maria-Cacau-Contagem/maria_cacau/core/network/api.py"
Cohesion: 0.21
Nodes (5): API, Comunicação alto nivel para chamadas de api, HTTP métodos disponíveis para uso, HTTPRequest, Dados e parâmetros de uma request

### Community 7 - "Maria-Cacau-Contagem/maria_cacau/backend/features/orders/subfeatures/deliveries/service.py"
Cohesion: 0.20
Nodes (9): DeliveriesSummary, DeliveryTypeCount, Models de domínio da feature de entregas., DeliveriesMapper, DeliveriesService, Service e Mapper de entregas — agrupa pedidos do dia por tipo de entrega., Serializa DeliveriesSummary para dict JSON-ready., Aplica regra de negócio sobre os pedidos do dia e retorna o resumo de entregas. (+1 more)

### Community 8 - "Maria-Cacau-Contagem/maria_cacau/backend/features/orders/shared/models.py"
Cohesion: 0.17
Nodes (10): Address, Customer, Customization, Delivery, Event, Financial, Order, PaymentItem (+2 more)

### Community 9 - "DataSourceProtocol"
Cohesion: 0.07
Nodes (15): Rotas de autenticação, AuthService, Service de autenticação — gerencia o estado de conexão do DataSource., DataSourceProtocol, Autentica com o dict da service account e guarda o client em memória., Remove o client autenticado da memória. Mantém o sheet_id., Remove a planilha ativa da memória. Mantém as credenciais., Define a planilha ativa e dispara prewarm em background. (+7 more)

### Community 10 - "Maria-Cacau-Contagem/maria_cacau/core/error/errors.py"
Cohesion: 0.17
Nodes (12): AppError, certificado_limpo(), certificado_ok(), planilha_conectada(), planilha_ok(), Códigos de erro da aplicação com estrutura AppError., Confirmação de certificado configurado com sucesso., Confirmação de credenciais removidas com sucesso. (+4 more)

### Community 11 - "connect"
Cohesion: 0.22
Nodes (3): connect(), CpfValidationController, CpfValidationView

### Community 12 - "StatusBarController"
Cohesion: 0.08
Nodes (8): MainWindow, StatusBarState, DSLabel, StatusBarController, StatusBarView, QLabel, QMainWindow, QStatusBar

### Community 14 - ".get_by_period"
Cohesion: 0.24
Nodes (7): Retorna pedidos no intervalo de datas informado (DD/MM/YYYY)., _cast_numeric(), OrdersSummaryRepository, Repositório de pedidos por período — busca e prepara dados da planilha para o Or, Acessa o data source e entrega um DataFrame tipado para o OrdersService.      Ún, Retorna todos os pedidos de um período com colunas numéricas convertidas para fl, _to_dataframe()

### Community 15 - "._configure_app"
Cohesion: 0.38
Nodes (3): main(), Entry point da aplicação. Execute com: python -m maria_cacau, QApplication

### Community 18 - "DSComboBox"
Cohesion: 0.25
Nodes (3): DSComboBox, DSComboBox, QComboBox

### Community 20 - "Maria-Cacau-Contagem/maria_cacau/backend/utils/numbers.py"
Cohesion: 0.50
Nodes (3): normalize_decimal(), Utilitários de formatação numérica., Converte número no formato brasileiro para o formato inglês.      Remove o separ

### Community 27 - "HTTPResponse"
Cohesion: 0.05
Nodes (48): EntityT, API, ABC, Comunicação alto nivel para chamadas de api, O tipo precisa aceitar **kwargs (dataclass ou similar)., HTTPClientContract, LocalClient, Protocol (+40 more)

### Community 28 - "maria_cacau/features/home/sub_features/delivery/data/repository.py"
Cohesion: 0.05
Nodes (32): DeliveriesAPI, PaymentsPendentAPI, DeliveriesMapper, ErrorMapper, PaymentsMapper, DeliveriesSummary, Mappers de HTTPResponse para domain models e de HTTPResponseError para…, OrdersRepository (+24 more)

### Community 35 - "maria_cacau/features/cpf_validation/presentation/controller.py"
Cohesion: 0.08
Nodes (19): FeatureEvents, Enum, Eventos de observabilidade da feature CPF Validation., CpfValidationResult, Models utilizados no módulo, CpfValidationSignals, QObject, Canal de comunicação entre o ViewModel e o Controller. (+11 more)

### Community 44 - "properties"
Cohesion: 0.05
Nodes (41): $ref, $ref, $ref, $ref, $ref, type, items, minItems (+33 more)

### Community 58 - "maria_cacau/backend/data_source/errors/_errors.py"
Cohesion: 0.12
Nodes (16): before_request, ApiQuotaExceededError, ApiUnexpectedResponseError, CredentialsFileCorruptedError, CredentialsFormatError, DataSourceError, DataSourceNotReadyError, InvalidCredentialsError (+8 more)

### Community 68 - "CacheStorage"
Cohesion: 0.10
Nodes (11): Any, CacheStorage, Path, Backend de cache em arquivo JSON no diretório do usuário., ABC, T, Contrato base para todos os backends de armazenamento., StorageHandler (+3 more)

### Community 69 - "tokens/__init__.py"
Cohesion: 0.13
Nodes (21): IntEnum, ColorTokens, Tokens semânticos como QColor. Único ponto de acesso a cores no app.…, FontFamily, FontFamilyToken, load_fonts(), Enum, Registra as fontes customizadas do DS na aplicação. Chamar uma vez no boot. (+13 more)

### Community 70 - "deliveries/response/schema.json"
Cohesion: 0.07
Nodes (28): minimum, type, items, type, properties, required, type, total (+20 more)

### Community 71 - "properties"
Cohesion: 0.08
Nodes (26): description, properties, required, type, type, type, Address, type (+18 more)

### Community 72 - "maria_cacau/backend/features/orders/subfeatures/deliveries/service.py"
Cohesion: 0.12
Nodes (18): DeliveriesSummary, DeliveryTypeCount, Models de domínio da feature de entregas., DeliveriesRepository, DataFrame, Repositório de entregas — busca e prepara dados da planilha para o…, Retorna todos os pedidos de uma data como DataFrame bruto., Acessa o data source e entrega um DataFrame para o DeliveriesService. Não faz… (+10 more)

### Community 73 - "ErrorModel"
Cohesion: 0.13
Nodes (16): AppError, certificado_limpo(), certificado_ok(), http_error(), planilha_conectada(), planilha_ok(), Códigos de erro da aplicação com estrutura AppError., Confirmação de certificado configurado com sucesso. (+8 more)

### Community 74 - "DSButton"
Cohesion: 0.13
Nodes (10): _ButtonPalette, DSButton, DSButtonState, QPushButton, # TODO: paleta default ainda não definida, Reaplica o QSS — chamar após mudar `color`/`text_color` manualmente., DSButtonState, Enum (+2 more)

### Community 75 - "_utils.py"
Cohesion: 0.13
Nodes (16): InvalidDateRangeError, handle_api(), _is_valid_date(), date_range(), DateFormat, normalize_date(), datetime, Enum (+8 more)

### Community 76 - "SheetsRepository"
Cohesion: 0.16
Nodes (5): AppSession, SelectSheetAPI, _extract_sheet_id(), Retorna o sheet_id da última planilha salva em cache, sem HTTP., SheetsRepository

### Community 77 - "maria_cacau/backend/data_source/__init__.py"
Cohesion: 0.18
Nodes (13): Normaliza headers inconsistentes da planilha para os valores canônicos dos…, PaymentCols, ProductCols, StrEnum, Mapeamento de colunas e tabs da planílha., Colunas fixas da aba Cadastro, agrupadas por domínio., Colunas dos slots de produto (1–7). Usar com .slot(n)., Colunas das parcelas de pagamento (1–6). Usar com .slot(n). (+5 more)

### Community 78 - "coordinator.py"
Cohesion: 0.15
Nodes (9): AppCoordinator, BackendServer, configure(), Configura o client ativo., AppEvent, _Observability, Enum, Observabilidade centralizada do app. (+1 more)

### Community 79 - "summary/service.py"
Cohesion: 0.15
Nodes (14): get_orders(), get, Rota de pedidos — GET /orders., OrdersMapper, Service e Mapper de resumo de pedidos por período., Serializa o resultado do OrdersService para dict JSON-ready., DateFormat, datetime (+6 more)

### Community 80 - "DSChart"
Cohesion: 0.21
Nodes (6): DSChartType, Enum, DSChart, QWidget, Widget de gráfico reutilizável (barras ou pizza) usando seaborn + matplotlib., _short_label()

### Community 81 - ".to_model"
Cohesion: 0.16
Nodes (10): Customer, Customization, Delivery, Financial, Monta um Order completo a partir de uma linha do DataFrame., Soma à lista os itens de "Outro Espec.", casando por nome sem diferenciar…, PaymentItem, ProductItem (+2 more)

### Community 82 - "properties"
Cohesion: 0.11
Nodes (19): $ref, description, type, Event, properties, description, properties, type (+11 more)

### Community 83 - "SummaryController"
Cohesion: 0.14
Nodes (6): FeatureEvents, Enum, Eventos relacionados ao resumo de produtos por período., ProductsViewData, Controller da feature Summary: conecta signals da view ao ViewModel e trata…, SummaryController

### Community 84 - "call"
Cohesion: 0.16
Nodes (8): API, DeliveriesAPI, DisconnectAuthAPI, PaymentsPendentAPI, OrdersRepository, Repository da feature Auth: gerencia storage seguro e chamadas ao backend., Remove credenciais do storage e desautentica o backend., call()

### Community 85 - "DSButton"
Cohesion: 0.13
Nodes (7): DSButton, DSLoadingHandler, DSLoadingHandler, Deve ser chamado no __init__ do componente, após o super().__init__()., Implementar no componente: o que fazer com cada frame do spinner., Mixin que adiciona comportamento de loading animado a qualquer componente QObjec, QPushButton

### Community 86 - "Maria-Cacau-Contagem/maria_cacau/backend/data_source/sheet_mapper.py"
Cohesion: 0.14
Nodes (11): PaymentCols, ProductCols, Mapeamento de colunas e tabs da planílha., Colunas fixas da aba Cadastro, agrupadas por domínio., Colunas dos slots de produto (1–7). Usar com .slot(n)., Colunas das parcelas de pagamento (1–6). Usar com .slot(n)., SheetCols, SheetTabs (+3 more)

### Community 87 - "GoogleSheetsDataSource"
Cohesion: 0.16
Nodes (5): GoogleSheetsDataSource, Implementação de DataSourceProtocol para Google Sheets via gspread., Renomeia a coluna que segue prod3 para prod4, independente do header atual.…, Traduz headers reais da planilha para os nomes canônicos definidos nos enums.…, SheetNormalizer

### Community 88 - "DataSourceProtocol"
Cohesion: 0.11
Nodes (10): DataSourceProtocol, Protocol, Autentica com o dict da service account e guarda o client em memória., Remove o client autenticado da memória. Mantém o sheet_id., Remove a planilha ativa da memória. Mantém as credenciais., Define a planilha ativa e dispara prewarm em background., Retorna pedidos da data informada (DD/MM/YYYY)., Retorna pedidos no intervalo de datas informado (DD/MM/YYYY). (+2 more)

### Community 89 - "$defs"
Cohesion: 0.12
Nodes (17): $defs, Delivery, Financial, ProductItem, description, type, description, required (+9 more)

### Community 90 - "properties"
Cohesion: 0.11
Nodes (18): description, type, type, properties, $ref, type, items, type (+10 more)

### Community 91 - "maria_cacau/backend/_server.py"
Cohesion: 0.23
Nodes (10): errorhandler, BackendError, Exception, generic_mapper(), Exception, translate(), handle_backend_error(), handle_data_source_error() (+2 more)

### Community 92 - "v6/components/__init__.py"
Cohesion: 0.17
Nodes (6): AlignmentFlag, DSLabel, QLabel, QResizeEvent, QSize, setter

### Community 93 - ".pre_login"
Cohesion: 0.17
Nodes (6): ConnectAuthAPI, AuthRepository, Lê o JSON do caminho, envia ao backend e persiste apenas se der sucesso., Reenvia credenciais ao backend com o sheet_id atual., Lê credenciais do storage sem fazer chamada HTTP., AppInitUseCase

### Community 94 - "OrderMapper"
Cohesion: 0.39
Nodes (13): OrderMapper, Mapeamento de uma linha do DataFrame para o model Order., Converte uma linha do DataFrame (vinda do SheetsRepository) em um Order., Address, Customer, Customization, Delivery, Event (+5 more)

### Community 95 - "maria_cacau/features/home/sub_features/summary/data/repository.py"
Cohesion: 0.21
Nodes (8): Enum, Services, OrdersSummaryAPI, ErrorMapper, OrdersSummaryMapper, Mappers de HTTPResponse para domain models e de HTTPResponseError para…, Repository da feature Summary: chama a API e converte erros HTTP em ErrorModel., SummaryRepository

### Community 96 - "maria_cacau/features/home/sub_features/summary/presentation/view.py"
Cohesion: 0.16
Nodes (5): DSGroupBox, DSLabel, QLabel, View da feature Summary: resumo de produtos por período., QFont

### Community 97 - "AuthRepository"
Cohesion: 0.17
Nodes (7): AuthRepository, Repository da feature Auth: gerencia storage seguro e chamadas ao backend., Reenvia credenciais ao backend com o sheet_id atual., Lê credenciais do storage sem fazer chamada HTTP., Remove credenciais do storage e desautentica o backend., NoCachedCredentialsError, Caso de uso: gerencia credenciais da service account.

### Community 98 - "maria_cacau/features/home/sub_features/summary/presentation/viewmodel.py"
Cohesion: 0.29
Nodes (10): DaySummary, OrderDetail, ProductCount, ProductsSummary, Models utilizados no módulo de resumo de produtos., Caso de uso: agrega pedidos do período em resumo de produtos por dia e global., SummaryUseCase, _to_sorted_counts() (+2 more)

### Community 100 - "SummaryView"
Cohesion: 0.20
Nodes (3): DSGroupBox, SummaryView, QGroupBox

### Community 101 - "strings.py"
Cohesion: 0.27
Nodes (5): MenuHandler, QMenu, MainWindow, QMenuBar, QRect

### Community 102 - "Customer"
Cohesion: 0.13
Nodes (15): description, required, type, Customer, Receiver, $ref, description, type (+7 more)

### Community 103 - "payments/response/schema.json"
Cohesion: 0.13
Nodes (14): $ref, total, items, type, properties, orders, total, required (+6 more)

### Community 104 - "maria_cacau/design_system/components/__init__.py"
Cohesion: 0.24
Nodes (7): DSDialog, DSDialogIcon, DSDialogModel, Enum, asset(), Metadados centralizados do pacote maria-cacau., Resolve um path relativo à pasta assets, funciona em dev e no .exe compilado.

### Community 105 - "DSBadgeStyle"
Cohesion: 0.25
Nodes (6): DSBadge, QFrame, DSBadgeStyle, DSStatusType, Enum, QColor

### Community 106 - "HomeController"
Cohesion: 0.27
Nodes (4): HomeController, HomeFeaturesModel, HomeView, QWidget

### Community 107 - "Maria-Cacau-Contagem/maria_cacau/features/cpf_validation/domain/use_case.py"
Cohesion: 0.19
Nodes (7): CpfValidationResult, CpfValidationUseCase, _is_valid_cpf(), Regra de negócios: validação matemática de CPF., Valida um CPF pela regra dos dois dígitos verificadores (algoritmo da Receita Fe, CpfValidationViewModel, ViewModel da feature CPF Validation: executa o UseCase e emite resultado via sig

### Community 108 - "DeliveryView"
Cohesion: 0.23
Nodes (4): DSDateInput, DeliveryView, QDateEdit, QWidget

### Community 109 - "properties"
Cohesion: 0.14
Nodes (14): type, description, minimum, type, properties, name, price, quantity (+6 more)

### Community 110 - "PaymentsRepository"
Cohesion: 0.20
Nodes (9): PaymentsRepository, DataFrame, Acessa o data source e entrega um DataFrame tipado para o PaymentsService.…, Retorna todos os pedidos de uma data com colunas numéricas convertidas para…, Converte list[dict] em DataFrame com cast numérico de todas as colunas de valor., Faz cast numérico de uma coluna se ela existir no DataFrame., PaymentsService, Filtra pedidos com pagamento pendente e monta os objetos de domínio. (+1 more)

### Community 111 - "OrdersSummaryRepository"
Cohesion: 0.20
Nodes (9): OrdersSummaryRepository, DataFrame, Acessa o data source e entrega um DataFrame tipado para o OrdersService. Único…, Retorna todos os pedidos de um período com colunas numéricas convertidas para…, Converte list[dict] em DataFrame com cast numérico de todas as colunas de valor., Faz cast numérico de uma coluna se ela existir no DataFrame., OrdersService, Busca e monta os pedidos de um período. (+1 more)

### Community 112 - "DSContainer"
Cohesion: 0.24
Nodes (6): DSContainer, QFrame, QResizeEvent, DSContainerStyle, Enum, QColor

### Community 113 - "_SheetsViewModel"
Cohesion: 0.19
Nodes (7): Client, UnexpectedSheetStructureError, Encapsula o acesso à planilha: schema cacheado, prewarm e fetch., Carrega cabeçalho e índice da coluna DATA na primeira chamada; no-op nas…, Busca pedidos por datas usando dois passes para minimizar chamadas à API. Passo…, _SheetsViewModel, Worksheet

### Community 114 - "Maria-Cacau-Contagem/maria_cacau/backend/data_source/_normalizer.py"
Cohesion: 0.21
Nodes (9): _fix_prod4(), normalize(), Normaliza headers inconsistentes da planilha para os valores canônicos dos enums, Traduz headers reais da planilha para os nomes canônicos definidos nos enums., _rename_at(), _rename_keys(), SheetNormalizer, fetch() (+1 more)

### Community 115 - "Maria-Cacau-Contagem/maria_cacau/features/home/sub_features/delivery/domain/models.py"
Cohesion: 0.19
Nodes (5): DeliveriesSummary, DeliveryCount, DeliveryModel, DeliveryUseCase, Busca deliveries e payments em paralelo e retorna o modelo consolidado.

### Community 116 - "_SheetsGuard"
Cohesion: 0.15
Nodes (5): CredentialsFileNotFoundError, CredentialsSaveError, InvalidDateFormatError, SheetIdInvalidError, _SheetsGuard

### Community 117 - "DSButton"
Cohesion: 0.24
Nodes (6): DSButton, DSButtonState, QPushButton, DSButtonState, Enum, View da feature Delivery: resumo diário de entregas e pagamentos pendentes.

### Community 118 - "SheetCreateView"
Cohesion: 0.21
Nodes (3): QDialog, SheetCreateView, QLineEdit

### Community 121 - "StatusBarView"
Cohesion: 0.28
Nodes (3): Enum, StatusBarState, StatusBarView

### Community 123 - "Maria-Cacau-Contagem/maria_cacau/core/network/_errors.py"
Cohesion: 0.22
Nodes (9): HTTPRequestError, HTTPResponseError, NetworkError, NetworkNotConfiguredError, Erros mapeados usados no módulo, r"""Erro base da camada de network., configure() não foi chamado antes de usar a lib., Erro antes de receber resposta (conectividade, timeout, URL inválida). (+1 more)

### Community 124 - "BackendError"
Cohesion: 0.29
Nodes (7): handle_backend_error(), handle_data_source_error(), handle_unexpected_error(), BackendError, generic_mapper(), translate(), str

### Community 125 - ".get_by_date"
Cohesion: 0.17
Nodes (7): Retorna pedidos da data informada (DD/MM/YYYY)., DeliveriesRepository, Repositório de entregas — busca e prepara dados da planilha para o DeliveriesSer, Retorna todos os pedidos de uma data como DataFrame bruto., Acessa o data source e entrega um DataFrame para o DeliveriesService.      Não f, ErrorModel, Exception

### Community 127 - "properties"
Cohesion: 0.17
Nodes (12): minimum, type, type, PaymentItem, minimum, type, description, properties (+4 more)

### Community 128 - "properties"
Cohesion: 0.17
Nodes (12): type, type, description, properties, type, Customization, type, type (+4 more)

### Community 129 - "unexpected_error"
Cohesion: 0.23
Nodes (4): Exception, Erro genérico para exceções não tratadas., unexpected_error(), SheetsViewModel

### Community 130 - "maria_cacau/features/auth/presentation/viewmodel.py"
Cohesion: 0.18
Nodes (5): AuthUseCase, Lê o arquivo JSON, salva em storage seguro e autentica o backend., Remove credenciais do storage e desautentica o backend., AuthViewModel, ViewModel da feature Auth: executa o UseCase em background e emite resultados…

### Community 131 - "Maria-Cacau-Contagem/maria_cacau/backend/features/orders/subfeatures/payments/service.py"
Cohesion: 0.18
Nodes (8): get_payments_pendent(), Rota de pagamentos — GET /orders/payments-pendent., PaymentsMapper, PaymentsService, Service e Mapper de pagamentos pendentes., Serializa o resultado do PaymentsService para dict JSON-ready., Filtra pedidos com pagamento pendente e monta os objetos de domínio., Retorna pedidos com amount_pendent > 0 para a data informada.

### Community 133 - "maria_cacau/backend/features/auth/route.py"
Cohesion: 0.20
Nodes (7): connect(), disconnect(), delete, Rotas de autenticação, AuthService, Service de autenticação — gerencia o estado de conexão do DataSource., post

### Community 134 - "maria_cacau/backend/features/sheet/route.py"
Cohesion: 0.20
Nodes (6): delete, remove_sheet(), select_sheet(), Service de planilha — gerencia a planilha ativa no DataSource., SheetService, put

### Community 135 - "sheets/presentation/controller.py"
Cohesion: 0.22
Nodes (6): _EventBus, QObject, FeatureEvents, Enum, QObject, SheetsSignals

### Community 136 - "DSLoadingHandler"
Cohesion: 0.22
Nodes (4): DSLoadingHandler, Deve ser chamado no __init__ do componente, após o super().__init__()., Implementar no componente: o que fazer com cada frame do spinner., Mixin que adiciona comportamento de loading animado a qualquer componente…

### Community 137 - "Maria-Cacau-Contagem/maria_cacau/features/home/sub_features/summary/data/repository.py"
Cohesion: 0.27
Nodes (4): OrdersSummaryAPI, path(), Endpoints do backend consumidos pela feature Auth., SummaryRepository

### Community 138 - "properties"
Cohesion: 0.20
Nodes (10): type, properties, type, type, cpf, email, phone, relationship (+2 more)

### Community 139 - "maria_cacau/features/auth/presentation/controller.py"
Cohesion: 0.24
Nodes (7): FeatureEvents, Enum, Eventos observáveis da feature Auth., AuthSignals, QObject, Canal de comunicação entre o ViewModel (background thread) e o Controller (main…, Controller da feature Auth: conecta signals da view ao ViewModel e atualiza…

### Community 142 - "Maria-Cacau-Contagem/maria_cacau/core/network/_config.py"
Cohesion: 0.20
Nodes (9): clear_override(), configure(), get_client(), override(), Configurações globais para uso do módulo, Configura o client ativo., Substitui o client — útil para testes ou WireMock., Remove o override. Volta ao client padrão. (+1 more)

### Community 143 - "Maria-Cacau-Contagem/maria_cacau/features/home/sub_features/summary/presentation/controller.py"
Cohesion: 0.27
Nodes (3): Controller da feature CPF Validation: conecta signals da view ao ViewModel e tra, View da feature CPF Validation: dialog para validação de CPF., view_title()

### Community 144 - "Maria-Cacau-Contagem/maria_cacau/core/network/_observability.py"
Cohesion: 0.22
Nodes (6): AppEvent, _Observability, Observabilidade centralizada do app., NetworkEvent, Observabilidade da camada de network., track()

### Community 146 - "required"
Cohesion: 0.28
Nodes (9): required, required, type, required, amount, confirmed, date, installment (+1 more)

### Community 148 - "Maria-Cacau-Contagem/maria_cacau/backend/features/orders/subfeatures/payments/repository.py"
Cohesion: 0.28
Nodes (6): _cast_numeric(), PaymentsRepository, Repositório de pagamentos — busca e prepara dados da planilha para o PaymentsSer, Acessa o data source e entrega um DataFrame tipado para o PaymentsService., Retorna todos os pedidos de uma data com colunas numéricas convertidas para floa, _to_dataframe()

### Community 149 - "Maria-Cacau-Contagem/maria_cacau/core/storage/handler.py"
Cohesion: 0.29
Nodes (3): ABC, Contrato base para todos os backends de armazenamento., StorageHandler

### Community 150 - "to_response"
Cohesion: 0.29
Nodes (5): get_deliveries(), Rota de entregas — GET /orders/deliveries., to_response(), get_orders(), Rota de pedidos — GET /orders.

### Community 151 - "Maria-Cacau-Contagem/maria_cacau/features/cpf_validation/domain/signals.py"
Cohesion: 0.32
Nodes (5): CpfValidationSignals, DeliverySignals, Canal de comunicação entre o ViewModel e o Controller., SummarySignals, QObject

### Community 152 - "unexpected_error"
Cohesion: 0.36
Nodes (3): Erro genérico para exceções não tratadas., unexpected_error(), SheetsViewModel

### Community 153 - "maria_cacau/backend/features/orders/subfeatures/payments/route.py"
Cohesion: 0.29
Nodes (5): get_payments_pendent(), get, Rota de pagamentos — GET /orders/payments-pendent., PaymentsMapper, Serializa o resultado do PaymentsService para dict JSON-ready.

### Community 154 - "Backend"
Cohesion: 0.25
Nodes (7): Auth — `/auth`, Backend, Como funciona, Erros, Orders — `/orders`, Rotas disponíveis, Sheet — `/sheet`

### Community 156 - "DeliveryViewModel"
Cohesion: 0.43
Nodes (3): DeliveryViewData, DeliveryViewModel, Roda o UseCase, monta o ViewData e emite sucesso ou erro — sempre via signal par

### Community 157 - "DSDateInput"
Cohesion: 0.38
Nodes (3): DSDateInput, DSTextInput, QDate

### Community 159 - "AuthView"
Cohesion: 0.33
Nodes (3): AuthView, QMenu, View da feature Auth: menu Segurança com ações de certificado.

### Community 161 - ".json"
Cohesion: 0.33
Nodes (4): BackendServer, entity(), HTTPResponse, r"""Decodifica o body para um objeto.

### Community 162 - "_SheetsViewModel"
Cohesion: 0.40
Nodes (3): Encapsula o acesso à planilha: schema cacheado, prewarm e fetch., Carrega cabeçalho e índice da coluna DATA na primeira chamada; no-op nas seguint, _SheetsViewModel

### Community 164 - "AuthUseCase"
Cohesion: 0.33
Nodes (3): AuthUseCase, Lê o arquivo JSON, salva em storage seguro e autentica o backend., Remove credenciais do storage e desautentica o backend.

### Community 165 - "_shadows.py"
Cohesion: 0.33
Nodes (4): QWidget, Cria uma instância fresca do effect — Qt não permite compartilhar um…, ShadowConfig, Shadows

### Community 166 - "CPF Validation"
Cohesion: 0.33
Nodes (5): Arquitetura, CPF Validation, Fluxo principal, Observabilidade, Responsabilidade das classes

### Community 167 - "Delivery"
Cohesion: 0.33
Nodes (5): Arquitetura, Delivery, Fluxo de erro, Fluxo principal, Responsabilidade das classes

### Community 169 - "Summary"
Cohesion: 0.33
Nodes (5): Arquitetura, Fluxo de erro, Fluxo principal, Responsabilidade das classes, Summary

### Community 171 - "Maria Cacau — App"
Cohesion: 0.33
Nodes (5): Autor, Como rodar, Gerar executável, Maria Cacau — App, Plataforma e Requisitos

### Community 175 - "deliveries/response/example.json"
Cohesion: 0.40
Nodes (4): deliveries, $schema, total, unique

### Community 177 - "payments/response/example.json"
Cohesion: 0.50
Nodes (3): orders, $schema, total

### Community 178 - "maria_cacau/features/home/sub_features/summary/domain/signals.py"
Cohesion: 0.50
Nodes (3): QObject, Canal de comunicação entre o ViewModel (background thread) e o Controller (main…, SummarySignals

### Community 179 - "_Palette"
Cohesion: 0.67
Nodes (3): _Palette, StrEnum, Hex crus. Uso interno — referenciado apenas por ColorTokens.

## Knowledge Gaps
- **182 isolated node(s):** `$schema`, `description`, `type`, `zip`, `type` (+177 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **47 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `HTTPResponse` connect `HTTPResponse` to `maria_cacau/features/home/sub_features/summary/presentation/viewmodel.py`, `maria_cacau/backend/_server.py`, `maria_cacau/features/home/sub_features/delivery/data/repository.py`, `maria_cacau/features/home/sub_features/summary/data/repository.py`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._
- **Why does `DSDialog` connect `DSDialog` to `SummaryView`, `Enum`, `DeliveryView`, `AuthController`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Why does `call()` connect `call` to `.json`, `SheetsRepository`, `Maria-Cacau-Contagem/maria_cacau/core/network/api.py`, `Maria-Cacau-Contagem/maria_cacau/features/home/sub_features/summary/data/repository.py`, `Maria-Cacau-Contagem/maria_cacau/core/network/_config.py`, `Maria-Cacau-Contagem/maria_cacau/core/network/_errors.py`, `.pre_login`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Are the 10 inferred relationships involving `OrderMapper` (e.g. with `Address` and `Customer`) actually correct?**
  _`OrderMapper` has 10 INFERRED edges - model-reasoned connections that need verification._
- **What connects `$schema`, `description`, `type` to the rest of the system?**
  _182 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Maria-Cacau-Contagem/maria_cacau/backend/data_source/errors/_errors.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10099573257467995 - nodes in this community are weakly interconnected._
- **Should `.log` be split into smaller, more focused modules?**
  _Cohesion score 0.13852813852813853 - nodes in this community are weakly interconnected._