@echo off
REM Uso: scripts\release\newRelease.bat major|minor|patch
REM
REM Cria a branch de release a partir da branch atual (a que estiver com
REM checkout feito no momento, normalmente a develop - atualizada antes),
REM faz o bump de versao no pyproject.toml (commit so na branch de release,
REM nunca na branch base), abre o PR release/x.y.z para main (corpo vazio) e
REM cria a release em draft (vazia). Merge do PR e publicacao da release
REM ficam manuais.
REM
REM Estrutura em goto/labels de proposito: blocos if/else com parenteses
REM aninhados no cmd.exe quebram de forma imprevisivel quando o texto de um
REM echo tem caracteres como (, ), <, >, | - mesmo escapados com ^. goto evita
REM essa classe de problema porque cada linha e interpretada isoladamente.

cd /d "%~dp0\..\.."

set BUMP=%1
if "%BUMP%"=="major" goto bump_ok
if "%BUMP%"=="minor" goto bump_ok
if "%BUMP%"=="patch" goto bump_ok
echo ERRO: parametro invalido. Uso: scripts\release\newRelease.bat major, minor ou patch
exit /b 1

:bump_ok
if not exist "venv\Scripts\activate.bat" goto no_venv
call venv\Scripts\activate.bat
goto after_venv
:no_venv
echo AVISO: venv nao encontrado. Execute scripts\build.bat primeiro.
:after_venv

for /f "delims=" %%i in ('git rev-parse --abbrev-ref HEAD') do set BASE_BRANCH=%%i

echo Atualizando a branch atual: %BASE_BRANCH%
git fetch origin
if errorlevel 1 exit /b 1

git pull origin "%BASE_BRANCH%"
if errorlevel 1 goto pull_failed
goto after_pull
:pull_failed
echo ERRO: falha ao atualizar %BASE_BRANCH%.
exit /b 1
:after_pull

for /f "delims=" %%i in ('python scripts\release\bump_version.py %BUMP% --dry-run') do set NEW_VERSION=%%i
if not "%NEW_VERSION%"=="" goto version_ok
echo ERRO: falha ao calcular a nova versao.
exit /b 1
:version_ok

set BRANCH=release/%NEW_VERSION%
set BRANCH_EXISTS=0

git rev-parse --verify "%BRANCH%" >nul 2>&1
if errorlevel 1 goto check_remote_branch
echo Branch local ja existe, reaproveitando: %BRANCH%
git checkout "%BRANCH%"
if errorlevel 1 exit /b 1
set BRANCH_EXISTS=1
goto branch_ready

:check_remote_branch
git ls-remote --exit-code --heads origin "%BRANCH%" >nul 2>&1
if errorlevel 1 goto create_branch
echo Branch remota ja existe, reaproveitando: %BRANCH%
git checkout -b "%BRANCH%" "origin/%BRANCH%"
if errorlevel 1 exit /b 1
set BRANCH_EXISTS=1
goto branch_ready

:create_branch
echo Criando branch: %BRANCH%
git checkout -b "%BRANCH%"
if errorlevel 1 exit /b 1

:branch_ready
if "%BRANCH_EXISTS%"=="1" goto skip_bump

echo Aplicando bump de versao %BUMP%: %NEW_VERSION%
python scripts\release\bump_version.py %BUMP%
if errorlevel 1 exit /b 1

git add pyproject.toml
git commit -m "chore: bump version to %NEW_VERSION%"
if errorlevel 1 exit /b 1
goto after_bump

:skip_bump
echo Branch reaproveitada: assumindo que o bump de versao ja foi commitado nela.
:after_bump

git push -u origin "%BRANCH%"
if errorlevel 1 exit /b 1

gh pr view "%BRANCH%" >nul 2>&1
if errorlevel 1 goto create_pr

for /f "delims=" %%i in ('gh pr view "%BRANCH%" --json state --jq .state') do set PR_STATE=%%i

if "%PR_STATE%"=="OPEN" goto pr_open
if "%PR_STATE%"=="CLOSED" goto pr_reopen
if "%PR_STATE%"=="MERGED" goto pr_merged

echo AVISO: PR para %BRANCH% em estado desconhecido: %PR_STATE%. Pulando.
goto after_pr

:pr_open
echo PR para %BRANCH% ja existe e esta aberto, pulando criacao.
goto after_pr

:pr_reopen
echo PR para %BRANCH% existe mas esta fechado. Reabrindo...
gh pr reopen "%BRANCH%"
if errorlevel 1 exit /b 1
goto after_pr

:pr_merged
echo AVISO: PR para %BRANCH% ja foi mergeado anteriormente. Nada a fazer aqui.
goto after_pr

:create_pr
echo Criando PR de %BRANCH% para main...
gh pr create --base main --head "%BRANCH%" --title "Release %NEW_VERSION%" --body ""
if errorlevel 1 exit /b 1
:after_pr

gh release view "%NEW_VERSION%" >nul 2>&1
if errorlevel 1 goto create_release
echo Release v%NEW_VERSION% ja existe, pulando criacao.
goto after_release
:create_release
echo Criando release em draft: v%NEW_VERSION%
gh release create "%NEW_VERSION%" --draft --title "v%NEW_VERSION%" --notes ""
if errorlevel 1 exit /b 1
:after_release

echo.
echo Release %NEW_VERSION% preparada. Branch: %BRANCH%
echo Falta preencher o texto do PR e da release antes de mergear/publicar.
exit /b 0
