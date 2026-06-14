conda create -n pyside6n -c conda-forge -c defaults pyside6 qttools
 where /r "%CONDA_PREFIX%" designer.exe
C:\Users\<계정명>\miniconda3\envs\pyside6n\Library\lib\qt6\bin\designer.exe
where /r "%CONDA_PREFIX%" qt6.conf
C:\Users\<계정명>\miniconda3\envs\pyside6n\qt6.conf
C:\Users\<계정명>\miniconda3\envs\pyside6n\Library\bin\qt6.conf
copy C:\Users\<계정명>\miniconda3\envs\pyside_latest\Library\bin\qt6.conf C:\Users\<계정명>\miniconda3\envs\pyside_latest\Library\lib\qt6\bin\
%CONDA_PREFIX%\Library\lib\qt6\bin\designer.exe
(
echo [Paths]
echo Prefix=..
) > "%CONDA_PREFIX%\Library\lib\qt6\bin\qt.conf"
cd %CONDA_PREFIX%\etc\conda\activate.d
@echo off

rem Save original PATH only once
if not defined _OLD_CONDA_QT_PATH (
    set "_OLD_CONDA_QT_PATH=%PATH%"
)

rem Prepend Qt6 tool paths
set "PATH=%CONDA_PREFIX%\Library\lib\qt6\bin;%CONDA_PREFIX%\Library\bin;%PATH%"
@echo off

if defined _OLD_CONDA_QT_PATH (
    set "PATH=%_OLD_CONDA_QT_PATH%"
    set _OLD_CONDA_QT_PATH=
)
