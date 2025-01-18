:: 
:: Date of Creation: 2023-10-05
:: Author: Rahul Ghosh
:: Description: This batch file checks for administrative privileges and runs the PowerShell script to install ChromeDriver.
:: Version: 1.0.0
:: License: MIT License
::

@echo off
:: Check for admin privileges
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c %~f0' -Verb RunAs"
    exit /b
)

:: Run the PowerShell script
powershell -ExecutionPolicy Bypass -File "%~dp0ExecuteChromeDriverInstaller.ps1"
