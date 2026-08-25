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
call scripts\checkDependency.bat gh
if errorlevel 1 exit /b 1

call scripts\release\newRelease.bat %BUMP%
if errorlevel 1 exit /b 1

call scripts\build.bat
if errorlevel 1 exit /b 1

REM TEMP: package.bat comentado para validar o resto do fluxo reaproveitando
REM o .exe ja gerado em dist\, build da 5.1.0. Descomentar antes de usar pra
REM valer - sem isso, o .exe enviado nao corresponde a nova versao.
REM call scripts\release\package.bat
REM if errorlevel 1 exit /b 1

call scripts\release\uploadRelease.bat
if errorlevel 1 exit /b 1

echo.
echo ==========================================================
echo Release preparada.
echo ==========================================================
