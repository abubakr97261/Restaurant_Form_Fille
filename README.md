Restaurant Form Filler Automation
<p align="center">
  <img src="ICON_PIC.png" alt="Restaurant Form Filler Logo" width="160" />
</p>


A Python-based browser automation tool for filling scheduled restaurant operational forms through the Zenput web platform. The project uses Selenium WebDriver to log in through the restaurant SSO flow, open assigned forms, populate required fields, complete checklist items, add signatures, submit the forms, and record activity in a local log file.

> **Important:** This project should only be used by authorised users for legitimate restaurant operations. Do not use this tool to submit false, random, or unverified compliance data. HACCP and operational logs are business-critical records and may be audited.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Main Features](#main-features)
* [Technology Stack](#technology-stack)
* [Project Structure](#project-structure)
* [How the Automation Works](#how-the-automation-works)
* [Forms Automated](#forms-automated)
* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)
* [Running the Project](#running-the-project)
* [Building the EXE File](#building-the-exe-file)
* [Logging](#logging)
* [Security Notes](#security-notes)
* [GitHub Upload Guide](#github-upload-guide)
* [Recommended `.gitignore`](#recommended-gitignore)
* [Known Limitations](#known-limitations)
* [Future Improvements](#future-improvements)
* [Disclaimer](#disclaimer)

---

## Project Overview

Restaurant Form Filler is a desktop automation project designed to reduce repetitive manual work involved in completing daily restaurant forms.

The script opens the Zenput web platform, performs the login process, selects specific restaurant forms, enters configured information, fills operational fields, completes checklist buttons, signs the form, and submits it.

The automation is built mainly for restaurant management workflows where repeated daily forms need to be completed at specific times.

---

## Main Features

* Automates login to the Zenput web platform.
* Uses restaurant credentials stored in a local YAML configuration file.
* Opens specific restaurant forms by name.
* Fills HACCP-related temperature fields.
* Completes yes/no checklist items.
* Adds manager name where required.
* Creates a simple signature using Selenium action chains.
* Submits forms automatically.
* Supports scheduled execution using the `schedule` package.
* Writes detailed runtime logs to `log.txt`.
* Can be packaged into a Windows `.exe` file using PyInstaller.

---

## Technology Stack

The project uses the following technologies:

| Technology       | Purpose                                                         |
| ---------------- | --------------------------------------------------------------- |
| Python           | Main programming language                                       |
| Selenium         | Browser automation                                              |
| Chrome WebDriver | Controls Google Chrome                                          |
| Requests         | Sends HTTP request to retrieve SSO company information          |
| PyYAML           | Reads login and scheduling configuration from `credentials.yml` |
| Schedule         | Runs form-filling jobs at defined times                         |
| Logging          | Tracks execution details in `log.txt`                           |
| PyInstaller      | Converts the Python script into a Windows executable            |

---

## Project Structure

Recommended project structure:

```text
Restaurant-Form-Filler/
│
├── Restaurant_Form_Filler.py
├── requirements.txt
├── requirements.bat
├── README.md
├── ICON_PIC.png
├── py to exe.txt
│
├── credentials.example.yml
└── .gitignore
```

Local-only files that should not be uploaded to GitHub:

```text
credentials.yml
log.txt
chromedriver.exe
Restaurant_Form_Filler.exe
__pycache__/
build/
dist/
*.spec
```

---

## How the Automation Works

The automation follows this general workflow:

1. Opens the local `credentials.yml` file.
2. Loads user login details, restaurant details, manager name, and scheduled form times.
3. Sends a request to Zenput to get SSO company information.
4. Builds the SSO authentication URL.
5. Opens Google Chrome using Selenium WebDriver.
6. Enters the username and password into the Okta login screen.
7. Waits for the dashboard to load.
8. Opens the required form from the task list.
9. Clicks the form submit/start button.
10. Fills required input fields.
11. Selects required checklist buttons.
12. Draws a signature using Selenium `ActionChains`.
13. Submits the form.
14. Closes the browser.
15. Writes execution status to `log.txt`.

---

## Forms Automated

The current script includes automation for the following forms:

### HACCP Forms

* HACCP Log A Opening
* HACCP Log B
* HACCP Log C
* HACCP Log D Closing

### Daily Travel Path Forms

* Daily Travel Path - Brand Standard AM Pre-Rush
* Daily Travel Path - Brand Standard PM Pre-Rush

Each form has its own function inside the main script. The script uses Selenium XPath selectors to locate fields, buttons, text areas, signature fields, and submit buttons.

---

## Requirements

Before running the project, install the following:

* Windows operating system
* Python 3.8 or later
* Google Chrome browser
* Internet connection
* Valid authorised Zenput/restaurant account
* Access to the required forms in Zenput
* Python dependencies listed in `requirements.txt`

The project dependencies are:

```text
selenium==4.6.0
requests==2.27.1
schedule
pyyaml==6.0
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Restaurant-Form-Filler.git
cd Restaurant-Form-Filler
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows Command Prompt:

```bash
venv\Scripts\activate
```

For PowerShell:

```bash
venv\Scripts\Activate.ps1
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Configuration

The project requires a local `credentials.yml` file.

Do not upload the real `credentials.yml` file to GitHub.

Instead, create a safe example file named:

```text
credentials.example.yml
```

Example structure:

```yml
credentials:
  user: "YOUR_USERNAME"
  password: "YOUR_PASSWORD"
  login_hint: "YOUR_EMAIL_OR_LOGIN_HINT"
  restaurant_name: "YOUR_RESTAURANT_NUMBER"

schedule:
  haccp_a_time: "10:00"
  haccp_b_time: "12:00"
  haccp_c_time: "15:00"
  haccp_d_time: "22:00"
  daily_travel_path_am_time: "09:00"
  daily_travel_path_pm_time: "17:00"

manager:
  name: "MANAGER_NAME"
```

Then create your real local file:

```text
credentials.yml
```

Use your actual values only in the local `credentials.yml` file.

---

## Running the Project

After installing dependencies and creating `credentials.yml`, run:

```bash
python Restaurant_Form_Filler.py
```

The script will start the scheduler and run the configured form-filling tasks at the times defined in the credentials/configuration file.

---

## Building the EXE File

This project can be converted into a Windows executable using PyInstaller.

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --icon=ICON_PIC.png Restaurant_Form_Filler.py
```

After the build completes, the executable file will be available inside the `dist` folder:

```text
dist/Restaurant_Form_Filler.exe
```

You can then run the executable directly on a Windows machine.

---

## Logging

The script creates a local log file:

```text
log.txt
```

The log file stores runtime activity such as:

* Credential file opened
* Credentials loaded
* Form job started
* Browser driver status
* Web requests
* Form opened
* Form submitted
* Errors or exceptions

Example log messages:

```text
credential file opened...
All credentials loaded...
form_377033_LOGA opened
form_377033_LOGA submitted
```

The log file is useful for debugging, but it must not be uploaded to GitHub because it may contain sensitive runtime details.

---

## Security Notes

This project handles sensitive information.

Do not upload the following files to GitHub:

```text
credentials.yml
log.txt
Restaurant_Form_Filler.exe
chromedriver.exe
```

The `credentials.yml` file may contain usernames, passwords, restaurant details, and login hints.

The `log.txt` file may expose login flow details, form names, URLs, browser session information, and other sensitive operational information.

If real credentials were ever committed to GitHub, you should immediately:

1. Delete them from the repository.
2. Remove them from Git history.
3. Change the exposed password.
4. Regenerate any affected credentials.
5. Review account activity.

---

## GitHub Upload Guide

Before uploading to GitHub, your repository should include:

```text
Restaurant_Form_Filler.py
requirements.txt
requirements.bat
README.md
ICON_PIC.png
py to exe.txt
credentials.example.yml
.gitignore
```

Your repository should not include:

```text
credentials.yml
log.txt
Restaurant_Form_Filler.exe
chromedriver.exe
old app/
build/
dist/
*.spec
```

Recommended upload steps:

```bash
git init
git add Restaurant_Form_Filler.py requirements.txt requirements.bat README.md ICON_PIC.png "py to exe.txt" credentials.example.yml .gitignore
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/Restaurant-Form-Filler.git
git push -u origin main
```

---

## Recommended `.gitignore`

Create a `.gitignore` file and add:

```gitignore
# Sensitive files
credentials.yml
log.txt

# Executables and drivers
*.exe
chromedriver.exe

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environments
venv/
env/
.venv/

# PyInstaller output
build/
dist/
*.spec

# IDE files
.idea/
.vscode/

# OS files
.DS_Store
Thumbs.db

# Logs
*.log
```

---

## Known Limitations

This project works, but it has several important limitations.

### 1. Hardcoded XPaths

The script depends heavily on hardcoded XPath selectors. If Zenput changes its page structure, form layout, field IDs, or button labels, the automation may break.

### 2. Fixed Sleep Times

The script uses `time.sleep()` for waiting. This works, but it is not ideal. If the internet connection is slow or the page takes longer than expected, the script may fail.

A better approach would be to use Selenium explicit waits.

### 3. Randomised Form Values

Some fields are filled using random values within a range. This is risky for compliance records. HACCP forms should only contain accurate and verified readings.

Do not use random values for real compliance submissions unless the values are approved, verified, and legally acceptable for your workplace.

### 4. Browser Must Be Available

The script requires Google Chrome to be installed and working correctly.

### 5. Login Flow May Change

The script depends on the current Zenput/Auth0/Okta login flow. If the authentication process changes, the script may need updates.

### 6. No Graphical User Interface

The current version runs as a script or executable. It does not include a user-friendly GUI for editing schedules or credentials.

---

## Future Improvements

Possible future improvements include:

* Add a graphical user interface.
* Replace `time.sleep()` with Selenium explicit waits.
* Store credentials more securely using environment variables.
* Add better exception handling.
* Add email or desktop notifications after successful form submission.
* Add screenshot capture on failure.
* Add configuration validation before running.
* Add support for multiple restaurants.
* Add form status reporting.
* Add unit tests for configuration loading.
* Add structured logging with log rotation.
* Replace hardcoded XPath selectors with more stable selectors where possible.

---

## Disclaimer

This project is intended for educational and authorised operational automation purposes only.

The developer is not responsible for incorrect submissions, false compliance records, account misuse, platform policy violations, or business consequences caused by improper use of this tool.

Users are responsible for making sure that all submitted form data is accurate, authorised, and compliant with their organisation’s policies.
