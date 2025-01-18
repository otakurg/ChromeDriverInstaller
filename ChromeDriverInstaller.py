""" 
Date of Creation: 2023-10-05 
Author: Rahul Ghosh 
Description: This script installs ChromeDriver, manages its version, and provides options to add it to the Start Menu and Desktop. 
Version: 1.0.0 
License: MIT License 
"""

import requests  # For making HTTP requests to download ChromeDriver
import os  # For interacting with the operating system
import shutil  # For file operations like copying and removing files
import subprocess  # For executing system commands
from datetime import datetime  # For timestamping backups
import zipfile  # For handling zip files
import tkinter as tk  # For creating the GUI
from tkinter import filedialog  # For file dialog operations
import win32com  # For Windows COM support
from win32com.client import Dispatch  # For creating Windows shortcuts

# Define constants
CHROME_DRIVER_DIR = "C:\\Program Files\\ChromeDriver"
CHROME_DRIVER_ZIP = "chromedriver-win64.zip"
CHROME_DRIVER_EXE = "chromedriver.exe"

# Create the folder if it does not exist
if not os.path.exists(CHROME_DRIVER_DIR):
    os.makedirs(CHROME_DRIVER_DIR)

# Function to stop any running ChromeDriver processes
def stop_chromedriver():
    """Stops any running ChromeDriver processes."""
    try:
        subprocess.call(["taskkill", "/F", "/IM", CHROME_DRIVER_EXE])
    except Exception as e:
        print(f"Error stopping ChromeDriver: {e}")

# Define the JSON endpoint URL
json_url = "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE"

# Fetch data from the JSON endpoint
response = requests.get(json_url)
latest_version = response.text.strip()

# Construct the download URL for the ChromeDriver binary
download_url = f"https://storage.googleapis.com/chrome-for-testing-public/{latest_version}/win64/{CHROME_DRIVER_ZIP}"

# Stop any running ChromeDriver processes
stop_chromedriver()

# Create the main window
root = tk.Tk()
root.title("ChromeDriver Installer")

# Add the ChromeDriver executable to the start menu (optional)
def add_to_start_menu():
    """Adds the ChromeDriver executable to the Windows Start Menu."""
    start_menu_dir = os.path.join(os.environ["USERPROFILE"], "AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs")
    if not os.path.exists(start_menu_dir):
        os.makedirs(start_menu_dir)
    shutil.copy(os.path.join(CHROME_DRIVER_DIR, "chromedriver-win64", CHROME_DRIVER_EXE), start_menu_dir)

# Add the ChromeDriver executable to the desktop (optional)
def add_to_desktop():
    """Creates a shortcut for the ChromeDriver executable on the Desktop."""
    desktop_dir = os.path.join(os.environ["USERPROFILE"], "OneDrive", "Desktop")
    if not os.path.exists(desktop_dir):
        desktop_dir = os.path.join(os.environ["USERPROFILE"], "Desktop")
    if not os.path.exists(desktop_dir):
        os.makedirs(desktop_dir)
    shortcut_path = os.path.join(desktop_dir, "ChromeDriver.lnk")
    target_path = os.path.join(CHROME_DRIVER_DIR, "chromedriver-win64", CHROME_DRIVER_EXE)
    icon_path = os.path.join(os.path.dirname(__file__), "chromedriver.ico")
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.IconLocation = icon_path
    shortcut.Description = "ChromeDriver"
    shortcut.Save()

# Ask the user if they want to add the ChromeDriver executable to the start menu
add_to_start_menu_checkbox = tk.BooleanVar()
add_to_start_menu_checkbox.set(False)

# Ask the user if they want to create a backup
create_backup_checkbox = tk.BooleanVar()
create_backup_checkbox.set(True)

# Ask the user if they want to add the ChromeDriver executable to the desktop
add_to_desktop_checkbox = tk.BooleanVar()
add_to_desktop_checkbox.set(False)

# Function to download the ChromeDriver binary
def download_chromedriver():
    """Downloads the ChromeDriver binary and manages backups."""
    
    # Create a backup if requested
    if create_backup_checkbox.get():
        if os.path.exists(os.path.join(CHROME_DRIVER_DIR, "chromedriver-win64")):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_dir = os.path.join(CHROME_DRIVER_DIR, f"chromedriver-win64_{timestamp}")
            os.makedirs(backup_dir, exist_ok=True)
            shutil.copytree(os.path.join(CHROME_DRIVER_DIR, "chromedriver-win64"), os.path.join(backup_dir, "chromedriver-win64"))
    
    # Download the ChromeDriver binary
    response = requests.get(download_url)

    # Save the binary to a file
    with open(os.path.join(CHROME_DRIVER_DIR, CHROME_DRIVER_ZIP), "wb") as file:
        file.write(response.content)

    print("ChromeDriver downloaded successfully!")

    # Unzip the downloaded file
    with zipfile.ZipFile(os.path.join(CHROME_DRIVER_DIR, CHROME_DRIVER_ZIP), 'r') as zip_ref:
        zip_ref.extractall(CHROME_DRIVER_DIR)

    # Delete the zip file
    os.remove(os.path.join(CHROME_DRIVER_DIR, CHROME_DRIVER_ZIP))


def ask_user():
    """Prompts the user with options for installation preferences."""
    global add_to_start_menu_checkbox, create_backup_checkbox, add_to_desktop_checkbox
    label = tk.Label(root, text="Do you want to add the ChromeDriver executable to the start menu?")
    label.pack()
    checkbox = tk.Checkbutton(root, text="Yes", variable=add_to_start_menu_checkbox)
    checkbox.pack()
    label = tk.Label(root, text="Do you want to create a backup?")
    label.pack()
    checkbox = tk.Checkbutton(root, text="Yes", variable=create_backup_checkbox)
    checkbox.pack()
    label = tk.Label(root, text="Do you want to add the ChromeDriver executable to the desktop?")
    label.pack()
    checkbox = tk.Checkbutton(root, text="Yes", variable=add_to_desktop_checkbox)
    checkbox.pack()
    button = tk.Button(root, text="OK", command=lambda: [root.destroy(), download_chromedriver()])
    button.pack()
    root.mainloop()
    if add_to_start_menu_checkbox.get():
        add_to_start_menu()
    if add_to_desktop_checkbox.get():
        add_to_desktop()

ask_user()
