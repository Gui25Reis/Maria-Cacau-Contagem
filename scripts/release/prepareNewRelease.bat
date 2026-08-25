@echo off
REM Uso: scripts\release\prepareNewRelease.bat major|minor|patch
REM
REM Orquestra o fluxo completo de preparo de uma release: checkDependency gh,
REM depois newRelease, build, package e uploadRelease, nessa ordem.
REM Merge do PR e publicacao da release ficam manuais (o texto e definido a mao).

cd /d "%~dp0\..\.."

set BUMP=%1
if not "%BUMP%"=="" goto bump_ok
echo Uso: scripts\release\prepareNewRelease.bat major, minor ou patch
exit /b 1

:bump_ok
echo ==========================================================
echo [1/5] Checando dependencia: gh
echo ==========================================================
call scripts\checkDependency.bat gh
if errorlevel 1 goto step_failed_checkdep

echo.
echo ==========================================================
echo [2/5] Branch de release + PR + release em draft
echo ==========================================================
call scripts\release\newRelease.bat %BUMP%
if errorlevel 1 goto step_failed_newrelease

echo.
echo ==========================================================
echo [3/5] Setup do ambiente (scripts\build.bat)
echo ==========================================================
call scripts\build.bat
if errorlevel 1 goto step_failed_build

echo.
echo ==========================================================
echo [4/5] Gerando o .exe - PULADO (package.bat comentado para teste)
echo ==========================================================
REM TEMP: package.bat comentado para validar o resto do fluxo reaproveitando
REM o .exe ja gerado em dist\, build da 5.1.0. Descomentar antes de usar pra
REM valer - sem isso, o .exe enviado nao corresponde a nova versao.
REM call scripts\release\package.bat
REM if errorlevel 1 goto step_failed_package

echo.
echo ==========================================================
echo [5/5] Subindo o .exe na release em draft
echo ==========================================================
call scripts\release\uploadRelease.bat
if errorlevel 1 goto step_failed_upload

echo.
echo ==========================================================
echo Release preparada com sucesso.
echo ==========================================================
exit /b 0

:step_failed_checkdep
echo.
echo ERRO no passo [1/5]: falha ao checar/instalar a dependencia gh. Abortando.
exit /b 1

:step_failed_newrelease
echo.
echo ERRO no passo [2/5]: falha ao criar a branch/PR/draft da release. Abortando.
exit /b 1

:step_failed_build
echo.
echo ERRO no passo [3/5]: falha no setup do ambiente (scripts\build.bat). Abortando.
exit /b 1

:step_failed_package
echo.
echo ERRO no passo [4/5]: falha ao gerar o .exe (scripts\release\package.bat). Abortando.
exit /b 1

:step_failed_upload
echo.
echo ERRO no passo [5/5]: falha ao subir o .exe na release em draft. Abortando.
exit /b 1
