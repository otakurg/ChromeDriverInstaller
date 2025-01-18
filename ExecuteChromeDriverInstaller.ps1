# 
# Date of Creation: 2023-10-05
# Author: Rahul Ghosh
# Description: This PowerShell script checks for administrative privileges and runs the Python script to install ChromeDriver.
# Version: 1.0.0
# License: MIT License
#

# Check for admin privileges
$principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    # Relaunch the script with admin privileges
    Start-Process powershell "-File `"$PSCommandPath`"" -Verb RunAs
    exit
}

# Your existing PowerShell script content goes here

# Run the Python script
python "$PSScriptRoot\ChromeDriverInstaller.py"
