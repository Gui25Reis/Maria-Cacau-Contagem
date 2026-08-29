# Gerar executável

Compilação do projeto em um binário standalone via [Nuitka](https://nuitka.net) — automatizada
pelo workflow `app-distribution`, que roda em [`Maria-Cacau-Actions`](https://github.com/Maria-Cacau/Maria-Cacau-Actions).
Não é mais necessário gerar o `.exe` localmente.

## Como funciona

1. O PR de release (workflow `pr-release`) bumpa a versão em `pyproject.toml` e é mergeado na `main`
2. O push na `main` com mudança em `pyproject.toml` dispara `app-distribution`
3. A action `build` roda o `scripts/build.bat` do próprio repo (grupo de extras `build`, que inclui
   `nuitka`) num runner Windows
4. A action `nuitka` lê os metadados do app direto do módulo (`__app_name__`, `__version__`,
   `__copyright__`, `__company__`, `__icon_win__`) e chama `python -m nuitka` com as flags de
   empacotamento
5. O `.exe` gerado é anexado como asset na release publicada automaticamente

## Rodar localmente (debug)

```bat
REM Windows — instala o grupo "build" (inclui nuitka) em vez do "dev" padrão
scripts\build.bat build
python -m nuitka ...  REM ver actions/nuitka/action.yml em Maria-Cacau-Actions pras flags exatas
```

Gerar o `.exe` só funciona numa máquina Windows.

## Saída

| Plataforma | Arquivo gerado |
|---|---|
| Windows | `dist/MC Consultas.exe` |

## Metadados do executável

Os metadados (nome, versão, copyright, empresa, ícone) são lidos automaticamente do `__init__.py`,
que por sua vez os lê do `pyproject.toml`. A versão é atualizada pelo workflow `pr-release`, não
manualmente.

## Dependência de build

O Nuitka está declarado como dependência opcional de build no `pyproject.toml`:

```toml
[project.optional-dependencies]
build = ["nuitka", "zstandard"]
```

Isso é convencional — ferramentas de empacotamento não devem entrar nas dependências normais do
projeto. `scripts/build.bat`/`build.sh` instalam esse grupo quando chamados com `build` como
argumento (`scripts\build.bat build`); sem argumento, instalam o grupo `dev` (padrão de
desenvolvimento local).
