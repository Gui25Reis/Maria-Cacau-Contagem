@echo off
REM Uso: scripts\release\prepareNewRelease.bat major|minor|patch
REM
REM Orquestra o fluxo completo de preparo de uma release:
REM   checkDependency (gh) -> newRelease -> build -> package -> uploadRelease
REM Merge do PR e publicacao da release ficam manuais (o texto e definido a mao).

cd /d "%~dp0\..\.."

set BUMP=%1
if "%BUMP%"=="" (
    echo Uso: scripts\release\prepareNewRelease.bat major, minor ou patch
    exit /b 1
)

call scripts\checkDependency.bat gh
if errorlevel 1 exit /b 1

call scripts\release\newRelease.bat %BUMP%
if errorlevel 1 exit /b 1

call scripts\build.bat
if errorlevel 1 exit /b 1

call scripts\release\package.bat
if errorlevel 1 exit /b 1

call scripts\release\uploadRelease.bat
if errorlevel 1 exit /b 1

echo.
echo ==========================================================
echo Release preparada. 
echo ==========================================================
