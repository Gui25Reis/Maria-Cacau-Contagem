# Gerar executável

Processo para compilar o projeto em um binário standalone usando [Nuitka](https://nuitka.net).

## Pré-requisitos

1. Ter o Python 3.13+ instalado e no PATH
2. Ter rodado o script de setup para criar o venv e instalar as dependências do app

## Ordem dos comandos

### macOS

```bash
# 1. Setup do projeto (cria venv + instala dependências)
./scripts/build.sh

# 2. Gerar o .app
./scripts/release/package.sh
```

### Windows

```bat
REM 1. Setup do projeto (cria venv + instala dependências)
scripts\build.bat

REM 2. Gerar o .exe
scripts\release\package.bat
```

O `package.bat` instala automaticamente as dependências de build (`nuitka`) via `pip install -e ".[build]"` antes de compilar.

## O que cada script faz

### `build.bat` / `build.sh`

- Verifica se Python está no PATH
- Cria o venv em `venv/` (se não existir)
- Ativa o venv
- Instala o pacote e suas dependências: `pip install -e .`

### `package.bat` / `package.sh`

- Ativa o venv
- Instala dependências de build: `pip install -e ".[build]"` (inclui Nuitka)
- Lê os metadados do app direto do módulo (`__app_name__`, `__version__`, `__copyright__`, `__company__`, `__icon_win__`)
- Chama `python -m nuitka` com as flags de empacotamento
- Gera o binário em `dist/`

## Saída

| Plataforma | Arquivo gerado |
|---|---|
| Windows | `dist/MC Consultas.exe` |
| macOS | `dist/MC Consultas.app` |

## Metadados do executável

Os metadados (nome, versão, copyright, empresa, ícone) são lidos automaticamente do `__init__.py`, que por sua vez os lê do `pyproject.toml`. Para atualizar a versão do executável gerado, basta editar:

```toml
# pyproject.toml
[project]
version = "X.Y.Z"   # ex.: 5.0.1 → 5.0.2 (patch), 5.1.0 (minor) ou 6.0.0 (major)

[tool.maria-cacau]
year    = "AAAA"    # ano corrente do release, não um valor fixo do exemplo
company = "KINGS"
```

> `version`, `year` e `company` acima são placeholders — **sempre usar o valor real e atual** no
> momento do release: o ano corrente, e a versão seguinte à publicada (incrementando major, minor
> ou patch conforme o tipo de mudança), nunca copiar os valores de exemplo deste documento.

## Dependência de build

O Nuitka está declarado como dependência opcional de build no `pyproject.toml`:

```toml
[project.optional-dependencies]
build = ["nuitka"]
```

Isso é convencional — ferramentas de empacotamento não devem entrar nas dependências normais do projeto. O `package.bat` e `package.sh` instalam esse grupo automaticamente antes de compilar.
