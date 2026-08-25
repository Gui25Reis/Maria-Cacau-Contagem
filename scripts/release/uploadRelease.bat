@echo off
REM Uso: scripts\release\uploadRelease.bat
REM
REM Sobe o .exe gerado em dist\ pelo scripts\release\package.bat como asset
REM da release em draft correspondente a versao atual do pyproject.toml.
REM
REM Estrutura em goto/labels de proposito: blocos if/else com parenteses
REM aninhados no cmd.exe quebram de forma imprevisivel quando o texto de um
REM echo tem caracteres como (, ), <, >, | - mesmo escapados com ^. goto evita
REM essa classe de problema porque cada linha e interpretada isoladamente.

cd /d "%~dp0\..\.."

if not exist "venv\Scripts\activate.bat" goto no_venv
call venv\Scripts\activate.bat
goto after_venv
:no_venv
echo AVISO: venv nao encontrado. Execute scripts\build.bat primeiro.
:after_venv

for /f "delims=" %%i in ('python -c "import maria_cacau; print(maria_cacau.__app_name__)"') do set APP_NAME=%%i
for /f "delims=" %%i in ('python -c "import maria_cacau; print(maria_cacau.__version__)"') do set VERSION=%%i

set EXE_PATH=dist\%APP_NAME%.exe
if exist "%EXE_PATH%" goto exe_ok
echo ERRO: %EXE_PATH% nao encontrado. Rode scripts\release\package.bat primeiro.
exit /b 1

:exe_ok
gh release view "%VERSION%" >nul 2>&1
if errorlevel 1 goto create_release
echo Release v%VERSION% ja existe, reaproveitando...
goto after_release
:create_release
echo Release v%VERSION% nao encontrada. Criando em draft...
gh release create "%VERSION%" --draft --title "v%VERSION%" --notes ""
if errorlevel 1 exit /b 1
:after_release

echo Subindo %EXE_PATH% na release v%VERSION%...
gh release upload "%VERSION%" "%EXE_PATH%" --clobber
if errorlevel 1 goto upload_failed
goto done

:upload_failed
echo ERRO: falha ao subir o asset. A release v%VERSION% existe e esta em draft?
exit /b 1

:done
echo.
echo Asset enviado para a release v%VERSION%.
