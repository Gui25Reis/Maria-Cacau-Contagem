@echo off
REM Uso: scripts\release\uploadRelease.bat
REM
REM Sobe o .exe gerado em dist\ (por scripts\release\package.bat) como asset
REM da release em draft correspondente a versao atual do pyproject.toml.

cd /d "%~dp0\..\.."

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo AVISO: venv nao encontrado. Execute scripts\build.bat primeiro.
)

for /f "delims=" %%i in ('python -c "import maria_cacau; print(maria_cacau.__app_name__)"') do set APP_NAME=%%i
for /f "delims=" %%i in ('python -c "import maria_cacau; print(maria_cacau.__version__)"') do set VERSION=%%i

set EXE_PATH=dist\%APP_NAME%.exe
if not exist "%EXE_PATH%" (
    echo ERRO: %EXE_PATH% nao encontrado. Rode scripts\release\package.bat primeiro.
    exit /b 1
)

gh release view "%VERSION%" >nul 2>&1
if not errorlevel 1 (
    echo Release v%VERSION% ja existe, reaproveitando...
) else (
    echo Release v%VERSION% nao encontrada. Criando em draft...
    gh release create "%VERSION%" --draft --title "v%VERSION%" --notes ""
    if errorlevel 1 exit /b 1
)

echo Subindo %EXE_PATH% na release v%VERSION%...
gh release upload "%VERSION%" "%EXE_PATH%" --clobber
if errorlevel 1 (
    echo ERRO: falha ao subir o asset. A release v%VERSION% existe e esta em draft?
    exit /b 1
)

echo.
echo Asset enviado para a release v%VERSION%.
