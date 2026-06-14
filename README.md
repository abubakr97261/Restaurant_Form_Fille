Restaurant Form Filler Automation
<p align="center">
  <img src="ICON_PIC.png" alt="Restaurant Form Filler Logo" width="160" />
</p>
A Python-based browser automation project that uses Selenium to open scheduled restaurant operations forms, authenticate through the web login flow, fill configured checklist fields, sign the form, submit it, and write local execution logs.
> **Important:** This project should only be used with authorised accounts, authorised environments, and accurate operational data. Do not use this script to falsify HACCP, food safety, travel path, or compliance records. If the repository is public, never commit real credentials, logs, or generated executables.
---
Table of Contents
Project Overview
Main Features
Technology Stack
Project Structure
How the Application Works
Requirements
Installation
Configuration
Running the Script
Building a Windows EXE
GitHub Upload Checklist
Recommended .gitignore
Troubleshooting
Security Notes
Known Limitations
Future Improvements
License
---
Project Overview
Restaurant Form Filler Automation is a desktop automation script for repetitive restaurant web-form workflows. It reads login details, restaurant information, manager name, and form schedule times from a local YAML configuration file. It then runs daily scheduled jobs that open the browser, log in, navigate to the required form, complete the selected fields, apply a signature, submit the form, and close the browser session.
The current script targets several restaurant operation forms, including:
HACCP Log A — Opening
HACCP Log B
HACCP Log C
HACCP Log D — Closing
Daily Travel Path — Brand Standard AM pre-rush
Daily Travel Path — Brand Standard PM pre-rush
The application is intended as a browser automation example and should be adapted carefully before real-world use.
---
Main Features
Selenium-based browser automation using Google Chrome.
YAML-based local configuration for credentials and schedule times.
Daily scheduling through the Python `schedule` package.
Automated navigation to multiple restaurant operation forms.
Local logging to `log.txt` for debugging and execution tracking.
Optional conversion into a standalone Windows executable using PyInstaller.
Uses Selenium Manager when a ChromeDriver binary is not manually supplied.
---
Technology Stack
Tool / Library	Purpose
Python	Main programming language
Selenium	Browser automation
Requests	HTTP request to retrieve SSO/company information
PyYAML	Reading the local YAML configuration file
schedule	Running jobs at configured daily times
PyInstaller	Optional packaging into a Windows `.exe` file
Google Chrome	Browser used by Selenium
---
Project Structure
Recommended clean repository structure:
```text
Restaurant-Form-Filler/
│
├── Restaurant_Form_Filler.py      # Main automation script
├── requirements.txt               # Python dependencies
├── requirements.bat               # Optional Windows install helper
├── py to exe.txt                  # PyInstaller command reference
├── ICON_PIC.png                   # Application icon/logo
├── credentials.example.yml        # Safe example config file; no real credentials
├── README.md                      # Project documentation
└── .gitignore                     # Files that should not be uploaded
```
Files that should not be committed to GitHub:
```text
credentials.yml
log.txt
*.exe
chromedriver.exe
old app/
build/
dist/
__pycache__/
*.spec
```
---
How the Application Works
The script starts from `main()`.
`main()` calls `task()`.
`task()` loads values from `credentials.yml`.
The script creates scheduled daily jobs using the configured form times.
When a job time is reached, the related form function runs.
The function requests company/SSO information from the web endpoint.
Selenium opens Chrome and navigates to the generated login URL.
The script enters the configured username and password.
After login, it opens the selected form.
It fills configured text fields, numeric fields, yes/no buttons, and signature fields.
It submits the form and closes the browser.
The `while True` loop keeps the scheduler alive and repeatedly checks pending jobs.
---
Requirements
Before running the project, make sure you have:
Windows 10 or Windows 11.
Python 3.9+ installed.
Google Chrome installed.
Internet access.
An authorised account for the target web system.
Permission to automate the selected forms.
---
Installation
1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/Restaurant-Form-Filler.git
cd Restaurant-Form-Filler
```
2. Create a virtual environment
```bash
python -m venv .venv
```
3. Activate the virtual environment
For Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```
For Windows Command Prompt:
```cmd
.venv\Scripts\activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
The dependency file currently includes:
```text
selenium==4.6.0
requests==2.27.1
schedule
pyyaml==6.0
```
---
Configuration
Create a local file named `credentials.yml` in the project root.
Use this structure, but replace all placeholder values with your own authorised test or production values:
```yaml
Zenput credentials:
  userName: "YOUR_USERNAME"
  Password: "YOUR_PASSWORD"
  email: "YOUR_LOGIN_EMAIL"
  restaurant_name: "YOUR_RESTAURANT_NUMBER"
  HACCP LOG A form filling time: "09:15"
  HACCP LOG B form filling time: "13:15"
  HACCP LOG C form filling time: "17:15"
  HACCP LOG D form filling time: "20:15"
  Daily Travel Path - Brand Standard (AM pre-rush) time: "11:15"
  Daily Travel Path - Brand Standard (PM pre-rush) time: "16:15"
  Manager name: "YOUR_MANAGER_NAME"
```
Important configuration notes
Use 24-hour time format: `HH:MM`.
Keep the YAML structure consistent with the script.
Do not commit `credentials.yml` to GitHub.
Create `credentials.example.yml` for GitHub instead, using only placeholder values.
The current script reads YAML values by position after converting the YAML object to a string. This is fragile. A future improvement should read fields by key name instead.
---
Running the Script
Start the automation with:
```bash
python Restaurant_Form_Filler.py
```
The script will keep running because it uses a scheduler loop. Keep the terminal window open while the automation is active.
To stop it, press:
```text
CTRL + C
```
---
Building a Windows EXE
Install PyInstaller:
```bash
pip install pyinstaller
```
Build the executable:
```bash
pyinstaller --onefile --icon=ICON_PIC.png Restaurant_Form_Filler.py
```
After the build finishes, the executable will be created inside the `dist/` folder.
Do not upload generated `.exe` files directly to the main GitHub repository. If you want to share compiled builds, use the Releases section of GitHub instead.
---
GitHub Upload Checklist
Before uploading the project to GitHub, do this:
Delete or exclude real `credentials.yml`.
Delete or exclude `log.txt`.
Delete or exclude `Restaurant_Form_Filler.exe`.
Delete or exclude `chromedriver.exe` unless there is a strong reason to include it.
Add a safe `credentials.example.yml` file.
Add a `.gitignore` file.
Replace any hardcoded private values with placeholders.
Check the full Git history before making the repository public.
If real credentials were ever committed, rotate/reset those credentials immediately.
---
Recommended .gitignore
Create a `.gitignore` file in the project root:
```gitignore
# Secrets and local config
credentials.yml
*.env
.env

# Logs
log.txt
*.log

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
.venv/
venv/
env/

# Build outputs
build/
dist/
*.spec
*.exe

# Local drivers and old files
chromedriver.exe
old app/

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
```
---
Troubleshooting
1. `credentials.yml` not found
Make sure `credentials.yml` exists in the same folder as `Restaurant_Form_Filler.py`.
2. Chrome opens but login fails
Check:
username
password
email/login hint
account permissions
whether multi-factor authentication is required
whether the login page structure has changed
3. Selenium cannot find an element
This usually means the website layout, form name, field ID, button ID, or XPath changed. Update the relevant selector in `Restaurant_Form_Filler.py`.
4. ChromeDriver or browser version problem
Selenium 4.6.0 can use Selenium Manager to locate or download a compatible driver. If driver issues continue, update Google Chrome, update Selenium, or manually install a matching ChromeDriver.
5. Script runs but forms do not submit
Check:
internet connection
login session status
form availability
form names
field IDs
page load timing
whether the site has added CAPTCHA, MFA, or anti-automation checks
---
Security Notes
Never upload real usernames, passwords, restaurant IDs, private login URLs, tokens, or logs to GitHub.
The local log file may contain sensitive browser session details or login URLs.
If credentials have already been uploaded to a public repository, assume they are compromised and rotate them immediately.
For production-grade use, replace `credentials.yml` with environment variables, a secrets manager, or encrypted local storage.
Avoid storing passwords in plain text.
Review the target website's terms of service and internal compliance rules before using automation.
---
Known Limitations
The script uses hardcoded XPaths and field IDs.
The script uses `time.sleep()` instead of Selenium explicit waits.
YAML parsing is fragile because values are extracted by string position.
There is limited exception handling around browser actions.
The script uses generated and hardcoded numeric entries in several form fields. These must be replaced with verified, accurate values before any legitimate operational use.
The scheduler runs indefinitely until manually stopped.
Any website UI change can break the automation.
---
Future Improvements
Recommended improvements before professional or production use:
Use `WebDriverWait` instead of fixed `time.sleep()` calls.
Read YAML values by key name instead of positional string splitting.
Move credentials to environment variables or a secure vault.
Add better exception handling and retry logic.
Add screenshots on failure for easier debugging.
Add command-line arguments for running one form manually.
Add a dry-run mode for testing without submitting forms.
Separate form data from code using JSON/YAML form templates.
Add unit tests for configuration loading and scheduling logic.
Replace generated numeric values with validated data inputs.
Add clear audit logging without exposing secrets.
---
License
No license has been selected yet. Add a license before making the repository public.
Common choices:
MIT License for open-source use.
Private/internal license for company-only automation.
No license if you do not want others to reuse the code.
---
Disclaimer
This project is provided for educational and authorised automation purposes only. The maintainer is responsible for ensuring that the script is used lawfully, ethically, and in line with workplace, food safety, and platform rules.
