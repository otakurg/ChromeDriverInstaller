# ChromeDriver Installation Guide

## Introduction
ChromeDriver is a standalone server that implements WebDriver's wire protocol for Chromium. It is used for automated testing of web applications in the Chrome browser.

## Prerequisites
- Ensure you have Python installed on your computer.
- You may need administrative privileges to install ChromeDriver.

## Installation Steps
1. **Download the Installer Script**:
   - Clone or download the repository containing the `ChromeDriverInstaller.py` script.

2. **Execute the Installer**:
   - You can run the installation using either of the following methods:
   - **Using Batch File**:
     - Right-click on `ExecuteChromeDriverInstaller.bat` and select "Run as administrator" to start the installation.
   - **Using Python Script**:
     - Open an elevated terminal (run as administrator) and execute the following command:
       ```
       <Folder where the script is>\python ChromeDriverInstaller.py
       ```

3. **Follow Prompts**:
   - Follow any prompts that appear during the installation process.

## Conclusion
Once the installation is complete, you can start using ChromeDriver for your automated testing needs. For more information, refer to the [ChromeDriver documentation](https://chromedriver.chromium.org/).

## Additional Resources
- You can directly download ChromeDriver from this URL: [ChromeDriver Download](https://googlechromelabs.github.io/chrome-for-testing/)

## Author
- Rahul Ghosh

## ChromeDriverInstaller.py Functionality
The `ChromeDriverInstaller.py` script performs the following functions:
- **Purpose**: Installs ChromeDriver, manages its version, and provides options to add it to the Start Menu and Desktop.
- **Key Features**:
  - **Directory Setup**: Creates a directory for ChromeDriver if it doesn't exist.
  - **Process Management**: Stops any running ChromeDriver processes before installation.
  - **Version Management**: Fetches the latest version of ChromeDriver from a JSON endpoint.
  - **Download**: Downloads the ChromeDriver binary from a constructed URL based on the latest version.
  - **Backup**: Offers an option to create a backup of the existing ChromeDriver installation.
  - **User Interface**: Uses a simple Tkinter GUI to ask the user if they want to add shortcuts to the Start Menu and Desktop.
  - **Shortcut Creation**: Creates shortcuts for ChromeDriver on the Desktop and in the Start Menu if the user opts for it.

## ChromeDriver JSON Endpoints Utilization
The script utilizes the following JSON endpoint to fetch the latest stable version of ChromeDriver:

- **Endpoint**: `https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE`

### How It Works
1. **Fetch Latest Version**: The script sends a GET request to the JSON endpoint to retrieve the latest stable version of ChromeDriver.
2. **Construct Download URL**: It constructs the download URL for the ChromeDriver binary based on the fetched version.
3. **Download ChromeDriver**: The script downloads the ChromeDriver binary from the constructed URL and saves it to the specified directory.
4. **Unzip and Cleanup**: After downloading, the script unzips the downloaded file and removes the zip file.

## Git Repository
- [ChromeDriverInstaller Repository](https://github.com/otakurg/ChromeDriverInstaller.git)
