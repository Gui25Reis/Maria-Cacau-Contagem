@echo off
REM Checa se uma dependencia externa esta instalada e a instala se nao estiver.
REM Uso: scripts\checkDependency.bat nome
REM Exit code 0 (+ "true" no stdout) se a dependencia esta disponivel ao final,
REM exit code 1 (+ "false" no stdout) caso contrario.
REM
REM Para adicionar uma nova dependencia, criar um label ":dep_nome" seguindo
REM o padrao do bloco "gh" abaixo (checar, instalar, checar de novo) e um
REM "if" apontando pra ele, igual ao de baixo.
REM
REM Estrutura em goto/labels de proposito: blocos if/else com parenteses
REM aninhados no cmd.exe quebram de forma imprevisivel quando o texto de um
REM echo tem caracteres como (, ), <, >, | - mesmo escapados com ^. goto evita
REM essa classe de problema porque cada linha e interpretada isoladamente.

set DEP=%1

if "%DEP%"=="" goto usage
if "%DEP%"=="gh" goto dep_gh

echo Dependencia desconhecida: %DEP%
echo false
exit /b 1

:usage
echo Uso: checkDependency.bat nome
echo false
exit /b 1

:dep_gh
where gh >nul 2>&1
if errorlevel 1 goto install_gh
echo true
exit /b 0

:install_gh
echo gh CLI nao encontrado. Instalando via winget...
winget install --id GitHub.cli -e --accept-source-agreements --accept-package-agreements

where gh >nul 2>&1
if errorlevel 1 goto install_gh_failed

gh auth status >nul 2>&1
if errorlevel 1 gh auth login

echo true
exit /b 0

:install_gh_failed
echo ERRO: instalacao do gh via winget falhou. Instale manualmente em https://cli.github.com/
echo false
exit /b 1
