@echo off
REM Uso: scripts\release\newRelease.bat major|minor|patch
REM
REM Cria a branch de release a partir da develop (atualizada), faz o bump de
REM versao no pyproject.toml (commit so na branch de release, nunca na develop),
REM abre o PR release/x.y.z -> main (corpo vazio) e cria a release em draft
REM (vazia). Merge do PR e publicacao da release ficam manuais.

cd /d "%~dp0\..\.."

set BUMP=%1
if not "%BUMP%"=="major" if not "%BUMP%"=="minor" if not "%BUMP%"=="patch" (
    echo ERRO: parametro invalido. Uso: scripts\release\newRelease.bat major^|minor^|patch
    exit /b 1
)

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo AVISO: venv nao encontrado. Execute scripts\build.bat primeiro.
)

echo Atualizando a develop local...
git fetch origin
if errorlevel 1 exit /b 1

git checkout develop
if errorlevel 1 exit /b 1

git pull origin develop
if errorlevel 1 (
    echo ERRO: falha ao atualizar a develop.
    exit /b 1
)

for /f "delims=" %%i in ('python scripts\release\bump_version.py %BUMP% --dry-run') do set NEW_VERSION=%%i
if "%NEW_VERSION%"=="" (
    echo ERRO: falha ao calcular a nova versao.
    exit /b 1
)

set BRANCH=release/%NEW_VERSION%
set BRANCH_EXISTS=0

git rev-parse --verify "%BRANCH%" >nul 2>&1
if not errorlevel 1 (
    echo Branch local '%BRANCH%' ja existe, reaproveitando...
    git checkout "%BRANCH%"
    if errorlevel 1 exit /b 1
    set BRANCH_EXISTS=1
) else (
    git ls-remote --exit-code --heads origin "%BRANCH%" >nul 2>&1
    if not errorlevel 1 (
        echo Branch remota '%BRANCH%' ja existe, reaproveitando...
        git checkout -b "%BRANCH%" "origin/%BRANCH%"
        if errorlevel 1 exit /b 1
        set BRANCH_EXISTS=1
    ) else (
        echo Criando branch %BRANCH%...
        git checkout -b "%BRANCH%"
        if errorlevel 1 exit /b 1
    )
)

if "%BRANCH_EXISTS%"=="1" (
    echo Branch reaproveitada: assumindo que o bump de versao ja foi commitado nela.
) else (
    echo Aplicando bump de versao (%BUMP%) -^> %NEW_VERSION%...
    python scripts\release\bump_version.py %BUMP%
    if errorlevel 1 exit /b 1

    git add pyproject.toml
    git commit -m "chore: bump version to %NEW_VERSION%"
    if errorlevel 1 exit /b 1
)

git push -u origin "%BRANCH%"
if errorlevel 1 exit /b 1

gh pr view "%BRANCH%" >nul 2>&1
if not errorlevel 1 (
    echo PR para %BRANCH% ja existe, pulando criacao.
) else (
    echo Criando PR %BRANCH% -^> main...
    gh pr create --base main --head "%BRANCH%" --title "Release %NEW_VERSION%" --body ""
    if errorlevel 1 exit /b 1
)

gh release view "%NEW_VERSION%" >nul 2>&1
if not errorlevel 1 (
    echo Release v%NEW_VERSION% ja existe, pulando criacao.
) else (
    echo Criando release em draft v%NEW_VERSION%...
    gh release create "%NEW_VERSION%" --draft --title "v%NEW_VERSION%" --notes ""
    if errorlevel 1 exit /b 1
)

echo.
echo Release %NEW_VERSION% preparada (branch %BRANCH%, PR e draft criados).
