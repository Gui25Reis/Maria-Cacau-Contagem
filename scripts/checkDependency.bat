@echo off
REM Checa se uma dependencia externa esta instalada e a instala se nao estiver.
REM Uso: scripts\checkDependency.bat <nome>
REM Exit code 0 (+ "true" no stdout) se a dependencia esta disponivel ao final,
REM exit code 1 (+ "false" no stdout) caso contrario.
REM
REM Para adicionar uma nova dependencia, criar um bloco "if "%DEP%"=="<nome>" ..."
REM seguindo o padrao do bloco "gh" abaixo (checar -> instalar -> checar de novo).

set DEP=%1

if "%DEP%"=="" (
    echo Uso: checkDependency.bat nome
    echo false
    exit /b 1
)

if "%DEP%"=="gh" (
    where gh >nul 2>&1
    if not errorlevel 1 (
        echo true
        exit /b 0
    )

    echo gh CLI nao encontrado. Instalando via winget...
    winget install --id GitHub.cli -e --accept-source-agreements --accept-package-agreements

    where gh >nul 2>&1
    if errorlevel 1 (
        echo ERRO: instalacao do gh via winget falhou. Instale manualmente em https://cli.github.com/
        echo false
        exit /b 1
    )

    gh auth status >nul 2>&1
    if errorlevel 1 (
        echo gh instalado, mas nao autenticado. Rodando 'gh auth login'...
        gh auth login
    )

    echo true
    exit /b 0
)

echo Dependencia desconhecida: %DEP%
echo false
exit /b 1
